import unittest
from main import Pinats

class TestPinats(unittest.TestCase):
    def test_case_1(self):
        pinats = Pinats([12, 11, 23, 4, 15])
        expected_result = 27830
        self.assertEqual(pinats.max_sum(), expected_result)

    def test_case_2(self):
        pinats = Pinats([5, 6, 7])
        expected_result = 745
        self.assertEqual(pinats.max_sum(), expected_result)

    def test_case_3(self):
        pinats = Pinats([1, 2, 3, 4])
        expected_result = 114
        self.assertEqual(pinats.max_sum(), expected_result)

    def test_case_4(self):
        pinats = Pinats([1, 1, 1, 1])
        expected_result = 4
        self.assertEqual(pinats.max_sum(), expected_result)

    def test_case_5(self):
        pinats = Pinats([10, 20, 30])
        expected_result = 41000
        self.assertEqual(pinats.max_sum(), expected_result)

    def test_case_6(self):
        pinats = Pinats([-1, -2, -3, -4])
        expected_result = 0
        self.assertEqual(pinats.max_sum(), expected_result)

if __name__ == '__main__':
    unittest.main()
