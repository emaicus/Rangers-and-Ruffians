import unittest
from ..code import rnr_utils

class rnrTests(unittest.TestCase):
    def test_load_files(self):
        try:
            rnr_utils.load_Rangers_And_Ruffians_Data()
        except:
            self.fail("ERROR: Could not load RNR Data")


if __name__ == '__main__':
    unittest.main()

