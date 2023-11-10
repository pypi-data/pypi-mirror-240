import unittest
import zkdex_python_sdk
import json
class TestStringMethods(unittest.TestCase):
    def test_publickey_to_xy(self):
        r = zkdex_python_sdk.public_key_to_xy("0x028dd913a169cf3732c306959e9c2a66a0075663e54e086977ed71c61fd7c273")
        json.JSONDecoder.decode(r)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()