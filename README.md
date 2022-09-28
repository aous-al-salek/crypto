# Crypto
Performance comparison between CBC-DES, CBC-TDES, CBC-AES128, CBC-AES192, and CBC-AES256.
Performance is measured in Python 3.9.2 and the encryption algorithms are implemented in PyCryptodome 3.15.0.
The results are given in microseconds as an average of 1000000 run using 1000 different keys.
The test was performed on a Raspberry Pi 4 Model B with 8GB of RAM and a SanDisk Ultra 32GB microSDHC card.
The Raspberry Pi 4 Model B was powered using an Raspberry Pi Official USB-C Power Supply rated at 5.1V / 3.0A DC output.
The Raspberry Pi OS Desktop 32-bit operating system was used (built on Debian 11 bullseye) with kernel version 5.15 and released on 2022-09-06.

## Results
Algorithm | Key Length | Operation | Average Time in μs
--- | --- | --- | ---
AES | 128 bits | Encryption | 90.651
AES | 128 bits | Decryption | 92.295
AES | 192 bits | Encryption | 86.449
AES | 192 bits | Decryption | 91.612
AES | 256 bits | Encryption | 86.396
AES | 256 bits | Decryption | 91.396
DES | 56 bits | Encryption | 97.268
DES | 56 bits | Decryption | 97.977
TDES | 168 bits | Encryption | 230.951
TDES | 168 bits | Decryption | 230.583

<details><summary>References</summary>

- Python 3.9.2: https://www.python.org/downloads/release/python-392
- PyCryptodome: https://pycryptodome.readthedocs.io/en/latest
- AES: https://www.nist.gov/publications/advanced-encryption-standard-aes
- DES: https://csrc.nist.gov/publications/detail/fips/46/3/archive/1999-10-25
- TDES: https://csrc.nist.gov/publications/detail/sp/800-67/rev-1/archive/2012-01-23
- CVE-2016-2183: https://nvd.nist.gov/vuln/detail/CVE-2016-2183
- Block Cipher Modes of Operation: https://csrc.nist.gov/publications/detail/sp/800-38a/final
- Raspberry Pi 4: https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications
- Raspberry Pi PSU: https://www.raspberrypi.com/products/type-c-power-supply
- SanDisk microSD: https://www.westerndigital.com/en-se/products/memory-cards/sandisk-ultra-uhs-i-microsd
- Raspberry Pi OS: https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit
</details>
