use std::collections::HashMap;

use anyhow::anyhow;
use bitcoin::consensus::{deserialize, serialize};
use bitcoin::secp256k1::{ecdsa::Signature, Secp256k1};
use bitcoin::{consensus::Decodable, psbt::PartiallySignedTransaction};
use bitcoin::{Address, EcdsaSighashType, Network, Transaction, Witness};

pub fn serialized_transaction_from_psbt(
    psbt: Vec<u8>,
    signatures: HashMap<usize, Vec<u8>>,
    scripts: HashMap<usize, Vec<u8>>,
    address: String,
) -> anyhow::Result<Vec<u8>> {
    let mut psbt = PartiallySignedTransaction::consensus_decode(&mut &psbt[..])?;
    let address: Address = address.parse()?;

    let mut witness_vec = Vec::with_capacity(psbt.inputs.len());
    for (input_idx, _) in psbt.inputs.iter().enumerate() {
        witness_vec[input_idx] = gen_witness(input_idx, &signatures, &scripts)?;
    }
    witness_vec
        .into_iter()
        .enumerate()
        .for_each(|(input_idx, witness)| {
            psbt.inputs[input_idx].final_script_witness = Some(witness)
        });
    Ok(serialize(&psbt.extract_tx()))
}

fn gen_witness(
    input_idx: usize,
    signatures: &HashMap<usize, Vec<u8>>,
    scripts: &HashMap<usize, Vec<u8>>,
) -> anyhow::Result<Witness> {
    let sigdata = signatures
        .iter()
        .find(|s| *s.0 == input_idx)
        .ok_or(anyhow!("signature not found for index={}", input_idx))?
        .1;
    let local_delayedsig = Signature::from_compact(&sigdata)?;
    let mut witness_vec = Vec::with_capacity(3);
    witness_vec.push(local_delayedsig.serialize_der().to_vec());
    witness_vec[0].push(EcdsaSighashType::All as u8);
    witness_vec.push(vec![]);
    witness_vec.push(
        scripts
            .iter()
            .find(|s| *s.0 == input_idx)
            .ok_or(anyhow!("signature not found for index={}", input_idx))?
            .1
            .clone(),
    );
    Ok(Witness::from_vec(witness_vec))
}
