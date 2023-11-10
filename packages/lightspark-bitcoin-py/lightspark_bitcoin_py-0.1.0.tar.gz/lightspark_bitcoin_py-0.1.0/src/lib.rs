use pyo3::{exceptions::PyRuntimeError, prelude::*};
use std::collections::HashMap;

pub mod psbt;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn transaction_from_psbt(
    psbt: Vec<u8>,
    signatures: HashMap<usize, Vec<u8>>,
    scripts: HashMap<usize, Vec<u8>>,
    address: String,
) -> PyResult<Vec<u8>> {
    let tx = psbt::serialized_transaction_from_psbt(psbt, signatures, scripts, address)
        .map_err(|err| PyRuntimeError::new_err(err.to_string()))?;
    Ok(tx)
}

/// A Python module implemented in Rust.
#[pymodule]
fn lightspark_bitcoin_py(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(transaction_from_psbt, m)?)?;
    Ok(())
}
