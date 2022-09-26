# crypto
Performance comparison between CBC-DES, CBC-TDES, CBC-AES128, CBC-AES192, and CBC-AES256.
Performance is measured in Python 3.9.2 and the encryption algorithms are implemented in PyCryptodome 3.15.0.
The results are given in microseconds as an average of 1000000 run using 1000 different keys.
The test was performed on a Raspberry Pi 4 Model B with 8GB of RAM and a SanDisk Ultra 32GB microSDHC card.
The Raspberry Pi OS Desktop 32-bit operating system was used (built on Debian 11 bullseye) with kernel version 5.15 and released on 2022-09-06.

https://www.python.org/downloads/release/python-392/

https://pycryptodome.readthedocs.io/en/latest/index.html

https://www.nist.gov/publications/advanced-encryption-standard-aes

https://csrc.nist.gov/publications/detail/fips/46/3/archive/1999-10-25

https://csrc.nist.gov/publications/detail/sp/800-67/rev-1/archive/2012-01-23

https://csrc.nist.gov/publications/detail/sp/800-38a/final

https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/

https://www.westerndigital.com/en-se/products/memory-cards/sandisk-ultra-uhs-i-microsd

https://downloads.raspberrypi.org/raspios_armhf/release_notes.txt
