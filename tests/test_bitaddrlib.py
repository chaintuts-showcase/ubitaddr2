# This file contains unit tests for BitAddr library functionality
#
# Author: Josh McIntyre
#
import hashlib
import unittest
from unittest.mock import patch

import bitaddrlib

class TestBitAddrMocks():

    # Mock private key generation with a brainwallet (secret key hash)
    # for consistent address, privkey generation
    def mock_generate_privkey_raw_with_brainwallet():
    
        key_hash = hashlib.sha256(b"abc123")
        key = key_hash.digest()

        return key

class TestBitAddr(unittest.TestCase):


    @patch("bitaddrlib.BitAddr._generate_privkey_raw")
    def test_generate_address_privkey_btc(self, mock_generate_privkey_raw):
    
        mock_generate_privkey_raw.return_value = TestBitAddrMocks.mock_generate_privkey_raw_with_brainwallet()

        bitaddr = bitaddrlib.BitAddr()
        address, wif = bitaddr.generate_address_privkey_btc()
        
        assert address == "1LG1ibbDtSWpL3UiKKvzspZTce2n7tLpNg"
        assert wif == "5Je8PHUo5YkRsnNvUeG63nmHCz9z1WXErPr3nbmUkWtsKeffhD4"
