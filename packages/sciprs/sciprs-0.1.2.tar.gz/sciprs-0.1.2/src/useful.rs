use nalgebra::{DMatrix, DMatrixSlice, Dynamic, Matrix, SliceStorage};
use nalgebra_py::matrix_to_numpy;
use numpy::{
    ndarray::{Array, ArrayD, ArrayViewD, ArrayViewMutD, Axis},
    IntoPyArray, PyArray1, PyArrayDyn, PyReadonlyArrayDyn,
};
use pyo3::{exceptions::PyValueError, prelude::*, types::PyDict};
use sci_rs::signal::filter::{design::Sos, sosfiltfilt_dyn};

use crate::convert::py_to_nalg;

mod convert;

#[pyclass]
struct Sciprs {}

#[pymethods]
impl Sciprs {
    #[new]
    fn new() -> Self {
        Sciprs {}
    }

    #[args(axis = "-1")]
    fn foobar<'py>(&self, axis: i32) -> PyResult<i32> {
        Ok(axis)
    }
}
// /// nalg_rows(matrix, /)
// /// --
// ///
// /// This function prints a 1D or 2D matrix row by row
// #[pyfn(m)]
// fn nalg_rows(
//     #[pyo3(from_py_with = "py_to_nalg")] matrix: DMatrixSlice<'_, f64, Dynamic, Dynamic>,
// ) -> PyResult<()> {
//     println!("nalgebra matrix {:?}", matrix.shape());
//     for i in 0..matrix.shape().0 {
//         let mut row = vec![];
//         for j in 0..matrix.shape().1 {
//             row.push(matrix[(i, j)]);
//         }
//         println!("{:?}", row);
//     }

//     Ok(())
// }
