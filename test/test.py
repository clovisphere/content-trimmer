import unittest
from app import trim


class ContentTrimmer(unittest.TestCase):
    def test(self):
        name = '01_dummy_test_.txt'
        self.assertEqual('01 dummy test.txt', trim(name), 'Names do not match')


if __name__ == '__main__':
    unittest.main()
