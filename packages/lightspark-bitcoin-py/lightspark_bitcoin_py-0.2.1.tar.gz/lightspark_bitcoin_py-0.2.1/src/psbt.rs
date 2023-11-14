// Copyright ©, 2023, Lightspark Group, Inc. - All Rights Reserved

use bitcoin::consensus::serialize;
use bitcoin::psbt::Psbt;
use bitcoin::secp256k1::ecdsa::Signature;
use bitcoin::util::sighash;
use bitcoin::{consensus::Decodable, psbt::PartiallySignedTransaction};
use bitcoin::{Address, EcdsaSighashType, Script, Sighash, Witness};
use pyo3::pyclass;

/// Helper struct to be used with Bitcoin functions, since internal structs are not exposed to Python.
#[pyclass]
#[derive(Clone)]
pub struct Tx {
    pub psbt: Psbt,
}

/// Generates [Tx] from consensus encoded PSBT, updates it with a desired output address and offsets the output to include some constant fee.
pub fn psbt_bytes_to_tx(psbt: Vec<u8>, address: String, fee_offset_sat: u64) -> anyhow::Result<Tx> {
    let mut psbt = PartiallySignedTransaction::consensus_decode(&mut &psbt[..])?;
    let address: Address = address.parse()?;
    psbt.unsigned_tx.output[0].script_pubkey = address.payload.script_pubkey();
    psbt.unsigned_tx.output[0].value = psbt.unsigned_tx.output[0].value - fee_offset_sat;

    Ok(Tx { psbt })
}

/// Generate Sighash for signing from a PSBT input at position input_idx to be used in a witness script.
/// Requires the witness script and the amount of the input.
/// Sighash has to be calculated in Sparkcore, because this is where we update the transaction's output address and adjust the fee.
/// The input scripts are not signed and not a part of the sighash.
pub fn generate_sighash(
    psbt: Psbt,
    input_idx: usize,
    witness_script: Vec<u8>,
    amount_sats: u64,
) -> anyhow::Result<Sighash> {
    let witness_script = Script::from(witness_script);
    let sighash = sighash::SighashCache::new(&psbt.unsigned_tx).segwit_signature_hash(
        input_idx,
        &witness_script,
        amount_sats,
        EcdsaSighashType::All,
    )?;

    Ok(sighash)
}

/// Generates signed Bitcoin Transaction from PSBT using redeem scripts and signatures, then serializes it to raw bytes.
/// List of signatures and redeem scripts is used to construct witness scripts.
/// The resulting bytes can be hex encoded to broadcast using bitcoin-cli:
/// ```
/// RUN_BTC_CLI decoderawtransaction "0200000000010104ef6bc59e69fe2c23805d80061c1e2bcf157d734d9b74a1f22bafb8e972952200000000009000000001141e0000000000001600146ca4a629f18d3346ed3aaf79e453d491ad92966e03483045022100dd8714e2e3673e64a941d37ad5b71fa22f0706cea444c7083fefe9abbfd3007802200d67d4f2b71601bcd6ba064c42876e0302496d67b96fd351a7f2136569042d3501004d632102df786d95757b15e31a5f6032176f8912312c9bba6af1a4d8ddcfb7561acc7af567029000b275210360be4409297004205e6bdf726b83ec6c560c4d0a6a5b1aa545536ce05368549568ac00000000"
/// ```
pub fn signed_serialized_tx(
    mut tx: Tx,
    signatures: Vec<Vec<u8>>,
    scripts: Vec<Vec<u8>>,
) -> anyhow::Result<Vec<u8>> {
    let r = signatures
        .into_iter()
        .zip(scripts.into_iter())
        .enumerate()
        .map(|(input_idx, (signature, script))| (input_idx, gen_witness(&signature, &script)));
    for (input_idx, wit_res) in r {
        tx.psbt.inputs[input_idx].final_script_witness = Some(wit_res?);
    }
    Ok(serialize(&tx.psbt.extract_tx()))
}

fn gen_witness(signature: &Vec<u8>, script: &Vec<u8>) -> anyhow::Result<Witness> {
    let local_delayedsig = Signature::from_compact(&signature)?;
    let mut witness_vec = Vec::with_capacity(3);
    witness_vec.push(local_delayedsig.serialize_der().to_vec());
    witness_vec[0].push(EcdsaSighashType::All as u8);
    witness_vec.push(vec![]);
    witness_vec.push(script.clone());
    Ok(Witness::from_vec(witness_vec))
}

#[cfg(test)]
mod test {

    use super::*;
    use base64::{engine::general_purpose, Engine as _};
    use bitcoin::{consensus::deserialize, Network, Transaction};

    #[test]
    fn test_serialized_transaction_from_psbt() {
        let tx = psbt_bytes_to_tx(general_purpose::STANDARD.decode("cHNidP8BAD0CAAAAAQTva8Weaf4sI4BdgAYcHivPFX1zTZt0ofIrr7jpcpUiAAAAAACQAAAAAdweAAAAAAAAAWoAAAAAAAEBK0AfAAAAAAAAIgAgXf3xfjEkzIErgLE6DfYEPSRbFIKLTUOeNcEaNr8oa4YBCJkDSDBFAiEAqtqw/yUfYQ2homChjBlTVk0RirKs3bVTJyQE+ZiRXqQCIEK4vf3N9ct88b0CZE47J7ILuHBZOwSt30k/hK8CRq1DAQBNYyEC33htlXV7FeMaX2AyF2+JEjEsm7pq8aTY3c+3VhrMevVnApAAsnUhA2C+RAkpcAQgXmvfcmuD7GxWDE0KalsapUVTbOBTaFSVaKwAAA==").expect("psbt base64"), "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek".to_string(), 0).expect("psbt");
        assert_eq!(
            format!(
                "{}",
                Address::from_script(
                    &tx.psbt.unsigned_tx.output[0].script_pubkey,
                    Network::Regtest
                )
                .unwrap()
            ),
            "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek".to_string()
        );

        let _sighash = generate_sighash(tx.psbt.clone(), 0, hex::decode("632102df786d95757b15e31a5f6032176f8912312c9bba6af1a4d8ddcfb7561acc7af567029000b275210360be4409297004205e6bdf726b83ec6c560c4d0a6a5b1aa545536ce05368549568ac").expect("hex"),
        8000).expect("sighash");

        let tx_ser = signed_serialized_tx(tx, vec![hex::decode("dd8714e2e3673e64a941d37ad5b71fa22f0706cea444c7083fefe9abbfd300780d67d4f2b71601bcd6ba064c42876e0302496d67b96fd351a7f2136569042d35").expect("bytes")], vec![hex::decode("632102df786d95757b15e31a5f6032176f8912312c9bba6af1a4d8ddcfb7561acc7af567029000b275210360be4409297004205e6bdf726b83ec6c560c4d0a6a5b1aa545536ce05368549568ac").expect("hex")]);
        let tx: Transaction = deserialize(tx_ser.unwrap().as_slice()).unwrap();
        // signature der format is 71 bytes
        assert_eq!(hex::encode(tx.input[0].witness.to_vec()[0].as_slice()), "3045022100dd8714e2e3673e64a941d37ad5b71fa22f0706cea444c7083fefe9abbfd3007802200d67d4f2b71601bcd6ba064c42876e0302496d67b96fd351a7f2136569042d3501");
    }
}
