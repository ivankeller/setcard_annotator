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

    def test_list_examples_to_annotate(self):
        with TemporaryDirectory() as tmpdir:
            # arrange
            # put 3 image files in tmpdir
            Path(os.path.join(tmpdir, 'image1.png')).touch()
            Path(os.path.join(tmpdir, 'image2.jpg')).touch()
            Path(os.path.join(tmpdir, 'image3.png')).touch()
            # create Annotator object
            annot = Annotator(directory=tmpdir)
            labels_dir = annot.output_dir
            # add files in label_dir
            Path(os.path.join(labels_dir, 'image1.json')).touch()
            Path(os.path.join(labels_dir, 'image2.json')).touch()
            # act
            result = annot.list_examples_to_annotate()
            # assert
            expected = [os.path.join(tmpdir, 'image3.png')]
            self.assertListEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
