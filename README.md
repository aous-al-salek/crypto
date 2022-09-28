# Crypto
Performance comparison between CBC-DES, CBC-TDES, CBC-AES128, CBC-AES192, and CBC-AES256.
Performance is measured in Python 3.9.2 and the encryption algorithms are implemented in PyCryptodome 3.15.0.
The results are given in microseconds as an average of 1000000 run using 1000 different keys.
The test was performed on a Raspberry Pi 4 Model B with 8GB of RAM and a SanDisk Ultra 32GB microSDHC card.
The Raspberry Pi 4 Model B was powered using an Raspberry Pi Official USB-C Power Supply rated at 5.1V / 3.0A DC output.
The Raspberry Pi OS 11 Desktop 32-bit operating system was used (built on Debian 11 bullseye) with kernel version 5.15 and released on 2022-09-06.
The Raspberry Pi ran EEPROM version 2022-04-26.

## Results of encrypting "Cryptology is awesome!"
<table>
    <tr>
        <td colspan="4"><b><p align="center">Encryption of "Cryptology is awesome!"</p></b></td>
    </tr>
    <tr>
        <td><b>Algorithm</b></td>
        <td><b>Key Length</b></td>
        <td><b>Operation</b></td>
        <td><b>Average Time in μs</b></td>
    </tr>
    <tr>
        <td>AES</td>
        <td>128 bits</td>
        <td>Encryption</td>
        <td>90.651</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>128 bits</td>
        <td>Decryption</td>
        <td>92.295</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>192 bits</td>
        <td>Encryption</td>
        <td>86.449</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>192 bits</td>
        <td>Decryption</td>
        <td>91.612</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>256 bits</td>
        <td>Encryption</td>
        <td>86.396</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>256 bits</td>
        <td>Decryption</td>
        <td>91.396</td>
    </tr>
    <tr>
        <td>DES</td>
        <td>56 bits</td>
        <td>Encryption</td>
        <td>97.268</td>
    </tr>
    <tr>
        <td>DES</td>
        <td>56 bits</td>
        <td>Decryption</td>
        <td>97.977</td>
    </tr>
    <tr>
        <td>TDES</td>
        <td>168 bits</td>
        <td>Encryption</td>
        <td>230.951</td>
    </tr>
    <tr>
        <td>TDES</td>
        <td>168 bits</td>
        <td>Decryption</td>
        <td>230.583</td>
    </tr>
</table>

## Results of encrypting a million zeros
<table>
    <tr>
        <td colspan="4"><b><p align="center">Encryption of a million zeros</p></b></td>
    </tr>
    <tr>
        <td>Algorithm</td>
        <td>Key Length</td>
        <td>Operation</td>
        <td>Average Time in ms</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>128 bits</td>
        <td>Encryption</td>
        <td>56.622</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>128 bits</td>
        <td>Decryption</td>
        <td>49.143</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>192 bits</td>
        <td>Encryption</td>
        <td>59.183</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>192 bits</td>
        <td>Decryption</td>
        <td>51.596</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>256 bits</td>
        <td>Encryption</td>
        <td>61.691</td>
    </tr>
    <tr>
        <td>AES</td>
        <td>256 bits</td>
        <td>Decryption</td>
        <td>54.107</td>
    </tr>
    <tr>
        <td>DES</td>
        <td>56 bits</td>
        <td>Encryption</td>
        <td>75.640</td>
    </tr>
    <tr>
        <td>DES</td>
        <td>56 bits</td>
        <td>Decryption</td>
        <td>68.907</td>
    </tr>
    <tr>
        <td>TDES</td>
        <td>168 bits</td>
        <td>Encryption</td>
        <td>131.653</td>
    </tr>
    <tr>
        <td>TDES</td>
        <td>168 bits</td>
        <td>Decryption</td>
        <td>125.361</td>
    </tr>
</table>

<details><summary>References</summary>

- Python 3.9.2: https://www.python.org/downloads/release/python-392
- PyCryptodome 3.15.0: https://pycryptodome.readthedocs.io/en/latest
- AES: https://www.nist.gov/publications/advanced-encryption-standard-aes
- DES: https://csrc.nist.gov/publications/detail/fips/46/3/archive/1999-10-25
- TDES: https://csrc.nist.gov/publications/detail/sp/800-67/rev-1/archive/2012-01-23
- CVE-2016-2183: https://nvd.nist.gov/vuln/detail/CVE-2016-2183
- Block Cipher Modes of Operation: https://csrc.nist.gov/publications/detail/sp/800-38a/final
- Raspberry Pi 4: https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications
- Raspberry Pi PSU: https://www.raspberrypi.com/products/type-c-power-supply
- SanDisk microSD: https://www.westerndigital.com/en-se/products/memory-cards/sandisk-ultra-uhs-i-microsd
- Raspberry Pi OS (2022-09-06): https://www.raspberrypi.com/software/operating-systems/#raspberry-pi-os-32-bit
- Raspberry Pi EEPROM 2022-04-26: https://github.com/raspberrypi/rpi-eeprom/releases/tag/v2022.04.26-138a1
</details>
