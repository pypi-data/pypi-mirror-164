use numpy::{
    ndarray::{Array, Axis},
    IntoPyArray, PyArray1, PyReadonlyArrayDyn,
};
use pyo3::{exceptions::PyValueError, prelude::*, types::PyDict};
use sci_rs::signal::filter::{design::Sos, sosfiltfilt_dyn};

use crate::convert::extract_kwarg_axis;

#[pyfunction(kwargs = "**")]
pub fn sosfiltfilt<'py>(
    py: Python<'py>,
    sos: PyReadonlyArrayDyn<f64>,
    x: PyReadonlyArrayDyn<f64>,
    kwargs: Option<&PyDict>,
) -> PyResult<&'py PyArray1<f64>> {
    let sos = sos.as_array();
    let sos_shape = sos.shape();
    if sos_shape.len() != 2 || sos_shape[0] > 10 || sos_shape[1] != 6 {
        return Err(PyValueError::new_err(format!(
            "Invalid sos shape: {:?}",
            sos_shape
        )));
    }

    // Extract the axis kwarg
    let axis = extract_kwarg_axis(&kwargs, "axis", x.shape().len())?;
    println!("Found axis: {:?}", axis);

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
