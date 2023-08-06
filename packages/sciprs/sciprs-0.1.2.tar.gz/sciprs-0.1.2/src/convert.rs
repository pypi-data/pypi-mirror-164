use std::{marker::PhantomData, mem::transmute};

use nalgebra::{DMatrixSlice, Dynamic};
use nalgebra_py::matrix_slice_from_numpy;
use pyo3::{
    exceptions::{PyTypeError, PyValueError},
    prelude::*,
    types::PyDict,
};

#[allow(unused)]
pub unsafe fn phantom_python<'a>() -> Python<'a> {
    // Pretend we are holding the GIL because we are
    let phantom: PhantomData<()> = PhantomData {};
    // Transumte pretend phantom data into the zero-sized lifetime python token
    let phantom_py: Python<'a> = transmute(phantom);
    phantom_py
}

///
/// For use in a situation where the GIL is held like extracting arugments to a pyfunction
///
#[allow(unused)]
pub fn py_to_nalg<'py>(obj: &'py PyAny) -> PyResult<DMatrixSlice<'_, f64, Dynamic, Dynamic>> {
    unsafe {
        let py = phantom_python();
        matrix_slice_from_numpy(py, obj)
            .map_err(|nae| PyTypeError::new_err(format!("Matrix cast failed: {:?}", nae)))
    }
}

pub(crate) trait Flatten<T> {
    fn flatten(self) -> Option<T>;
}

impl<T> Flatten<T> for Option<Option<T>> {
    fn flatten(self) -> Option<T> {
        match self {
            None => None,
            Some(v) => v,
        }
    }
}

pub fn extract_kwarg_axis(
    kwargs: &Option<&PyDict>,
    key: &'static str,
    axes: usize,
) -> PyResult<usize> {
    let axis_dflt = axes - 1;
    let axis = kwargs
        .map(|kw| kw.get_item(key))
        .flatten()
        .map(|axis| -> PyResult<isize> { axis.extract() })
        .unwrap_or(Ok(axis_dflt as isize))?;
    if axis < 0 && -axis <= axes as isize {
        Ok((axes as isize + axis) as usize)
    } else if axis >= 0 && axis < axes as isize {
        Ok(axis as usize)
    } else {
        Err(PyValueError::new_err(format!(
            "Axis index {} out of range for {} axes",
            axis, axes
        )))
    }
}
