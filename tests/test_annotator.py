import unittest
import os
from tempfile import TemporaryDirectory
from pathlib import Path
from tests.testbase_class import TestBaseClass
from setcard_annotator.annotator import Annotator


class TestAnnotator(TestBaseClass):
    def test_get_basenames_in_directory(self):
        with TemporaryDirectory() as tmpdir:
            # arrange
            Path(os.path.join(tmpdir, 'file1.json')).touch()
            Path(os.path.join(tmpdir, 'file2.json')).touch()
            # act
            result = Annotator.get_basenames_in_directory(tmpdir)
            # assert
            expected = ['file1', 'file2']
            self.assertEqual(len(result), len(expected))
            self.assertSetEqual(set(result), set(expected))


if __name__ == '__main__':
    unittest.main()
