import unittest

from . import strcrypt
from .strcrypt import encrypt, decrypt

class TestBasic(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("123"), "XEtA")

    def test_decrypt(self):
        self.assertEqual(decrypt("XEtA"), "123")

    def test_encrypt_long_text(self):
        self.assertEqual(encrypt("This is a long text"), "OREaFkMbFlQKRRUCFxRFFxcdAA==")

    def test_decrypt_long_text(self):
        self.assertEqual(decrypt("OREaFkMbFlQKRRUCFxRFFxcdAA=="), "This is a long text")

    def test_encrypt_multi_lines_text(self):
        self.assertEqual(encrypt("This is a long text\nThis is another line"), "OREaFkMbFlQKRRUCFxRFFxcdAGExEQQKUwwQUgQaBBERCAtTCQocAA==")

    def test_decrypt_multi_lines_text(self):
        self.assertEqual(decrypt("OREaFkMbFlQKRRUCFxRFFxcdAGExEQQKUwwQUgQaBBERCAtTCQocAA=="), "This is a long text\nThis is another line")


class TestCustomKey(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.KEY = "jVDjHg1OmBt"
    
    def test_encrypt(self):
        self.assertEqual(encrypt("123", self.KEY), "W2R3")

    def test_decrypt(self):
        self.assertEqual(decrypt("W2R3", self.KEY), "123")

    def test_encrypt_long(self):
        self.assertEqual(encrypt("This is a long text", self.KEY), "Pj4tGWgOQm8MYhgFOCNKPAJJOw==")
    
    def test_decrypt_long(self):
        self.assertEqual(decrypt("Pj4tGWgOQm8MYhgFOCNKPAJJOw==", self.KEY), "This is a long text")

    def test_encrypt_multi_lines_text(self):
        self.assertEqual(encrypt("This is a long text\nThis is another line", self.KEY), "Pj4tGWgOQm8MYhgFOCNKPAJJO2cWHAMlZAM7R1AhAjYcDyRkBiEJVA==")

    def test_decrypt_multi_lines_text(self):
        self.assertEqual(decrypt("Pj4tGWgOQm8MYhgFOCNKPAJJO2cWHAMlZAM7R1AhAjYcDyRkBiEJVA==", self.KEY), "This is a long text\nThis is another line")

