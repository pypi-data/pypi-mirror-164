use pyo3::{prelude::*, wrap_pymodule};

mod convert;
mod signal;

/// A Python module implemented in Rust.
#[pymodule]
fn sciprs(py: Python, m: &PyModule) -> PyResult<()> {
    // Wrap a submodule and add it as importable
    // https://github.com/PyO3/pyo3/issues/759
    let signal = wrap_pymodule!(signal::signal);
    m.add_wrapped(signal)?;
    py.import("sys")?
        .getattr("modules")?
        .set_item("sciprs.signal", signal(py))?;

    Ok(())
}
