use std::path::Path;
use tract_hir::prelude::*;

use anyhow::{bail, format_err, Context, Result};
use ffi_convert::{CReprOf, RawBorrow, RawPointerConverter};
use std::cell::RefCell;
use std::ffi::CString;

mod loader;
use loader::load_model;

/// Borrowed from tract-cli with adapted npz type signature
pub fn for_npz(
    npz: &mut ndarray_npy::NpzReader<std::io::Cursor<&[u8]>>,
    name: &str,
) -> Result<Tensor> {
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<f32>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<f64>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<i8>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<i16>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<i32>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<i64>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<u8>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<u16>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<u32>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<u64>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    if let Ok(t) = npz.by_name::<tract_ndarray::OwnedRepr<bool>, tract_ndarray::IxDyn>(name) {
        return Ok(t.into_tensor());
    }
    Err(format_err!("Can not extract tensor from {}", name))
}

fn npz_add_tensor(
    npz: &mut ndarray_npy::NpzWriter<std::io::Cursor<&mut Vec<u8>>>,
    name: String,
    tensor: &Arc<Tensor>,
) -> Result<()> {
    match tensor.datum_type() {
        DatumType::F16 => npz.add_array(name, &tensor.cast_to::<f32>()?.to_array_view::<f32>()?)?,
        DatumType::Bool => npz.add_array(name, &tensor.to_array_view::<bool>()?)?,
        DatumType::U8 => npz.add_array(name, &tensor.to_array_view::<u8>()?)?,
        DatumType::U16 => npz.add_array(name, &tensor.to_array_view::<u16>()?)?,
        DatumType::U32 => npz.add_array(name, &tensor.to_array_view::<u32>()?)?,
        DatumType::U64 => npz.add_array(name, &tensor.to_array_view::<u64>()?)?,
        DatumType::I8 => npz.add_array(name, &tensor.to_array_view::<i8>()?)?,
        DatumType::I16 => npz.add_array(name, &tensor.to_array_view::<i16>()?)?,
        DatumType::I32 => npz.add_array(name, &tensor.to_array_view::<i32>()?)?,
        DatumType::I64 => npz.add_array(name, &tensor.to_array_view::<i64>()?)?,
        DatumType::F32 => npz.add_array(name, &tensor.to_array_view::<f32>()?)?,
        DatumType::F64 => npz.add_array(name, &tensor.to_array_view::<f64>()?)?,
        DatumType::QI8(_) => npz.add_array(name, &tensor.to_array_view::<i8>()?)?,
        DatumType::QU8(_) => npz.add_array(name, &tensor.to_array_view::<u8>()?)?,
        DatumType::QI32(_) => npz.add_array(name, &tensor.to_array_view::<i32>()?)?,
        _ => bail!(format_err!(
            "Not writing {}, {:?}, unsupported type",
            name,
            tensor
        )),
    };
    Ok(())
}

thread_local! {
    pub(crate) static LAST_ERROR: RefCell<Option<String>> = RefCell::new(None);
}
/// Used as a return type of functions that can encounter errors.
/// If the function encountered an error, you can retrieve it using the `tract_get_last_error`
/// function.
#[repr(C)]
#[allow(non_camel_case_types)]
#[derive(Debug, PartialEq, Eq)]
pub enum TractResult {
    /// The function returned successfully
    TRACT_OK = 0,
    /// The function returned an error
    TRACT_KO = 1,
}

#[repr(C)]
#[derive(Debug)]
pub struct CTypedModelPlan(*mut libc::c_void);

fn wrap<F: FnOnce() -> anyhow::Result<()>>(func: F) -> TractResult {
    match func() {
        Ok(_) => TractResult::TRACT_OK,
        Err(e) => {
            let msg = format!("{:#?}", e);
            if std::env::var("TRACT_ERROR_STDERR").is_ok() {
                eprintln!("{}", msg);
            }
            LAST_ERROR.with(|p| *p.borrow_mut() = Some(msg));
            TractResult::TRACT_KO
        }
    }
}

#[no_mangle]
pub extern "C" fn tract_get_last_error(error: *mut *mut ::libc::c_char) -> TractResult {
    wrap(move || {
        LAST_ERROR.with(|msg| {
            let string = msg
                .borrow_mut()
                .take()
                .unwrap_or_else(|| "No error message".to_string());
            let result: *const ::libc::c_char =
                std::ffi::CString::c_repr_of(string)?.into_raw_pointer();
            unsafe { *error = result as _ }
            Ok(())
        })
    })
}

#[no_mangle]
pub extern "C" fn tract_destroy_string(ptr: *mut libc::c_char) -> TractResult {
    {
        unsafe { CString::from_raw(ptr) };
    }
    TractResult::TRACT_OK
}

macro_rules! create_rust_str_from {
    ($pointer:expr) => {{
        unsafe { ::std::ffi::CStr::raw_borrow($pointer) }?
            .to_str()
            .context("Could not convert pointer to rust str")?
    }};
}
macro_rules! get_typed_model_plan_from {
    ($pointer:expr) => {{
        unsafe {
            TypedRunnableModel::<TypedModel>::raw_borrow(
                CTypedModelPlan::raw_borrow($pointer)?.0 as *mut TypedRunnableModel<TypedModel>,
            )?
        }
    }};
}

/// load simple tract Plan of TypedModel from various serialization:
/// NNEF: folder or tgz
/// ONNX
pub fn call_load_plan_from_path(
    path_string: *const libc::c_char,
    plan_ptr: *mut *const CTypedModelPlan,
) -> Result<()> {
    let path = Path::new(create_rust_str_from!(path_string));
    let typed_model = load_model(path)?;
    let plan: TypedRunnableModel<TypedModel> =
        SimplePlan::new(typed_model.into_decluttered()?.into_optimized()?)?;

    let cplan = CTypedModelPlan(plan.into_raw_pointer() as _);

    unsafe { *plan_ptr = cplan.into_raw_pointer() as _ };

    Ok(())
}

pub fn call_run_typed_model_plan(
    plan_ptr: *mut *const CTypedModelPlan,
    npz_inputs_buffer_ptr: *const libc::c_char,
    npz_input_buffer_length: libc::size_t,
    npz_outputs_buffer_ptr: *mut *mut ::libc::c_char,
    npz_outputs_buffer_length: *mut libc::size_t,
) -> Result<()> {
    let plan = get_typed_model_plan_from!(*plan_ptr);
    unsafe { *plan_ptr = plan.into_raw_pointer() as _ };

    // load npz into ndarray
    let bits: &[u8] = unsafe {
        ::std::slice::from_raw_parts_mut(
            npz_inputs_buffer_ptr as *mut u8,
            npz_input_buffer_length as usize,
        )
    };
    let raw = std::io::Cursor::new(bits);
    let mut input_npz = ndarray_npy::NpzReader::new(raw)?;
    let vectors = input_npz
        .names()?
        .iter()
        .map(|n| {
            let name = n.trim_end_matches(".npy").to_string();
            let node_id = plan.model.node_by_name(name).unwrap().id;
            (node_id, for_npz(&mut input_npz, &n).unwrap())
        })
        .collect::<Vec<(usize, Tensor)>>();

    // ensure model inputs order
    let ordered_vectors = plan
        .model
        .inputs
        .iter()
        .map(|outlet_uid| {
            let (_, tensor) = vectors
                .iter()
                .find(|(node_id, _)| node_id == &outlet_uid.node)
                .unwrap();
            tensor.to_owned()
        })
        .collect::<Vec<_>>();

    let svec = TVec::from_vec(ordered_vectors);
    // run network with npz content
    let results = plan
        .clone()
        .run(svec)?
        .iter()
        .map(|t| t.to_owned().into_arc_tensor())
        .collect::<Vec<Arc<Tensor>>>();

    // write output npz from ndarray
    let mut output_buffer = Vec::<u8>::new();
    {
        // closure to limit borrow buffer using cursor
        let mut output_npz = ndarray_npy::NpzWriter::new(std::io::Cursor::new(&mut output_buffer));
        for (ix, output) in results.iter().enumerate() {
            let name = plan
                .model
                .outlet_label(plan.model.output_outlets()?[ix])
                .map(|name| name.to_string())
                .unwrap_or_else(|| format!("output_{}", ix));
            npz_add_tensor(&mut output_npz, name, output)?;
        }
    }
    let outputs_buffer_len = output_buffer.len();
    unsafe {
        let b = std::ffi::CString::from_vec_unchecked(output_buffer);
        let raw_result: *const ::libc::c_char = b.into_raw_pointer();
        *npz_outputs_buffer_ptr = raw_result as _;
        *npz_outputs_buffer_length = outputs_buffer_len as _;
    }

    Ok(())
}

#[no_mangle]
pub unsafe extern "C" fn load_plan_from_path(
    path_string: *const libc::c_char,
    plan_ptr: *mut *const CTypedModelPlan,
) -> TractResult {
    wrap(|| call_load_plan_from_path(path_string, plan_ptr))
}

#[no_mangle]
pub unsafe extern "C" fn run_typed_model_plan(
    plan_ptr: *mut *const CTypedModelPlan,
    npz_inputs_buffer_ptr: *const libc::c_char,
    npz_input_buffer_length: libc::size_t,
    npz_outputs_buffer_ptr: *mut *mut ::libc::c_char,
    npz_outputs_buffer_length: *mut libc::size_t,
) -> TractResult {
    wrap(|| {
        call_run_typed_model_plan(
            plan_ptr,
            npz_inputs_buffer_ptr,
            npz_input_buffer_length,
            npz_outputs_buffer_ptr,
            npz_outputs_buffer_length,
        )
    })
}
