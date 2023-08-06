use nalgebra::{DMatrix, Dynamic, Matrix, SliceStorage};
use nalgebra_py::{matrix_slice_from_numpy, matrix_to_numpy};
use numpy::{
    ndarray::{Array, ArrayD, ArrayViewD, ArrayViewMutD, Axis},
    IntoPyArray, PyArray1, PyArrayDyn, PyReadonlyArrayDyn,
};
use pyo3::{
    exceptions::{PyTypeError, PyValueError},
    prelude::*,
};
use sci_rs::signal::filter::{design::Sos, sosfiltfilt_dyn};

/// A Python module implemented in Rust.
#[pymodule]
fn sciprs(_py: Python, m: &PyModule) -> PyResult<()> {
    // example using immutable borrows producing a new array
    fn axpy(a: f64, x: ArrayViewD<'_, f64>, y: ArrayViewD<'_, f64>) -> ArrayD<f64> {
        a * &x - &y
    }

    // example using a mutable borrow to modify an array in-place
    fn mult(a: f64, mut x: ArrayViewMutD<'_, f64>) {
        x *= a;
    }

    // wrapper of `axpy`
    #[pyfn(m)]
    #[pyo3(name = "axpy")]
    fn axpy_py<'py>(
        py: Python<'py>,
        a: f64,
        x: PyReadonlyArrayDyn<f64>,
        y: PyReadonlyArrayDyn<f64>,
    ) -> &'py PyArrayDyn<f64> {
        let x = x.as_array();
        let y = y.as_array();
        let z = axpy(a, x, y);
        z.into_pyarray(py)
    }

    // wrapper of `mult`
    #[pyfn(m)]
    #[pyo3(name = "mult")]
    fn mult_py(_py: Python<'_>, a: f64, x: &PyArrayDyn<f64>) {
        let x = unsafe { x.as_array_mut() };
        mult(a, x);
    }

    #[pyfn(m)]
    #[pyo3(name = "nalg_ro")]
    fn nalg_ro_py(py: Python, x: PyObject) -> PyResult<()> {
        let x = x.as_ref(py);
        println!("x = {:?}", x);
        let x: Matrix<
            f64,
            Dynamic,
            Dynamic,
            SliceStorage<'_, f64, Dynamic, Dynamic, Dynamic, Dynamic>,
        > = unsafe {
            matrix_slice_from_numpy(py, x)
                .map_err(|nae| PyTypeError::new_err(format!("Matrix cast failed: {:?}", nae)))
        }?;
        println!("nalgebra matrix {:?}", x.shape());
        for i in 0..x.shape().0 {
            let mut row = vec![];
            for j in 0..x.shape().1 {
                row.push(x[(i, j)]);
            }
            println!("{:?}", row);
        }

        Ok(())
    }

    #[pyfn(m)]
    #[pyo3(name = "nalg_ones")]
    fn nalg_ones_py(py: Python, m: usize, n: usize) -> PyResult<PyObject> {
        Ok(matrix_to_numpy(
            py,
            &DMatrix::from_diagonal_element(m, n, 1f64),
        ))
    }

    #[pyfn(m)]
    #[pyo3(name = "signal_sosfiltfilt")]
    fn signal_sosfiltfilt<'py>(
        py: Python<'py>,
        sos: PyReadonlyArrayDyn<f64>,
        x: PyReadonlyArrayDyn<f64>,
        axis: usize,
    ) -> PyResult<&'py PyArray1<f64>> {
        let sos = sos.as_array();
        let sos_shape = sos.shape();
        if sos_shape.len() != 2 || sos_shape[0] > 10 || sos_shape[1] != 6 {
            return Err(PyValueError::new_err(format!(
                "Invalid sos shape: {:?}",
                sos_shape
            )));
        }

        if axis > x.shape().len() {
            return Err(PyValueError::new_err(format!(
                "Invalid axis {} for shape {:?}",
                axis,
                x.shape()
            )));
        }

        let y = x.as_array();
        let lanes = y.lanes(Axis(axis)).into_iter().next().unwrap();
        let lane_itr = lanes.iter();
        let z: Vec<f64> = match sos_shape[0] {
            1 => {
                const N: usize = 1;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            2 => {
                const N: usize = 2;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            3 => {
                const N: usize = 3;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            4 => {
                const N: usize = 4;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            5 => {
                const N: usize = 5;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            6 => {
                const N: usize = 6;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            7 => {
                const N: usize = 7;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            8 => {
                const N: usize = 8;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            9 => {
                const N: usize = 9;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            10 => {
                const N: usize = 10;
                const M: usize = N * 6;
                let mut sos_arr: [f64; M] = [0.; M];
                let mut k = 0;
                for i in 0..N {
                    for j in 0..6 {
                        sos_arr[k] = sos[[i, j]];
                        k += 1;
                    }
                }
                let sos: [Sos<f64>; N] = Sos::from_scipy(sos_arr);
                sosfiltfilt_dyn(lane_itr, &sos)
            }
            _ => {
                unreachable!();
            }
        };

        Ok(Array::from_vec(z).into_pyarray(py))
    }

    Ok(())
}
