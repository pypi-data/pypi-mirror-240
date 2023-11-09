import unittest

from omemo_dr.util.byteutil import ByteUtil


class ByteUtilTest(unittest.TestCase):
    def test_split(self):
        data = bytearray(i for i in range(0, 80))
        a_data = bytearray(i for i in range(0, 32))
        b_data = bytearray(i for i in range(32, 64))
        c_data = bytearray(i for i in range(64, 80))

        a, b, c = ByteUtil.split(data, 32, 32, 16)

        self.assertEqual(a, a_data)
        self.assertEqual(b, b_data)
        self.assertEqual(c, c_data)
