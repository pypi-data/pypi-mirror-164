mod sosfiltfilt;
use pyo3::{prelude::*, wrap_pyfunction};

#[pymodule]
pub fn signal(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sosfiltfilt::sosfiltfilt, m)?)?;
    Ok(())
}
