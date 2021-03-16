import os
import sys
import unittest
import pathlib

TEST_DIRECTORY = pathlib.Path(__file__).resolve()
BASE_DIRECTORY = TEST_DIRECTORY.parent.parent
CODE_DIRECTORY = os.path.join(BASE_DIRECTORY, 'src')
sys.path.append(CODE_DIRECTORY)

from rangers_and_ruffians import core

class rnrTests(unittest.TestCase):
    def test_load_files(self):
        try:
            core.load_Rangers_And_Ruffians_Data()
        except:
            self.fail("ERROR: Could not load RNR Data")



if __name__ == '__main__':
    unittest.main()

