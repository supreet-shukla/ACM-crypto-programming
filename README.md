# ACM-crypto-programming-Supreet

# Cryptography Exercises

This repository contains Python implementations of various cryptographic protocols and their simulations between two communicating parties: Alice and Bob.

---

## 🔐 Exercises Overview

### 1. Diffie-Hellman Key Exchange
- **Files**: `Diffie_Hellman_Alice.py`, `Diffie_Hellman_Bob.py`
- **Objective**: Securely generate a shared secret key between Alice and Bob using the Diffie-Hellman protocol.

### 2. RSA Encryption/Decryption
- **Files**: `RSA_Alice.py`, `RSA_Bob.py`
- **Objective**: Encrypt and decrypt messages using the RSA public-key cryptosystem.

### 3. ElGamal Encryption
- **Files**: `ElGamal_Alice.py`, `ElGamal_Bob.py`
- **Objective**: Implement ElGamal encryption to securely send messages from Alice to Bob.

### 4. RSA Digital Signatures
- **Files**: `RSA_Signature_Alice.py`, `RSA_Signature_Bob.py`
- **Objective**: Use RSA to sign and verify messages for authenticity and integrity.

### 5. Benchmarking and Utilities
- **Files**: `benchmark.py`, `helper.py`
- **Objective**:
  - `helper.py`: Shared functions (e.g., modular inverse, primality testing).
  - `benchmark.py`: Measure performance of cryptographic operations (encryption/decryption/signing/verifying).

---

## 📦 Requirements

- Python 3.x
- No external dependencies (all algorithms implemented using built-in libraries)

---

## ▶️ How to Run

Example (for RSA):
```bash
python RSA_Alice.py
python RSA_Bob.py
