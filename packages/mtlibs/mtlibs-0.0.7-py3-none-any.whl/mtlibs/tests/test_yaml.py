import os
# import sys
# from pathlib import Path
import tempfile
import unittest
from ..yaml import load_yaml_file


class Test_yaml(unittest.TestCase):

    def setUp(self) -> None:
        # configtest.configMainAwsKey()
        self.bucketname = "zappa-zapdemo-001"
        return super().setUp()

    def test_upload(self):
         load_yaml_file()


if __name__ == '__main__':
    unittest.main()
