import unittest
import os
from tempfile import TemporaryDirectory
from tests.testbase_class import TestBaseClass
from setcard_annotator.annotator import Annotator


class TestAnnotator(TestBaseClass):
    def test_get_basenames_in_directory(self):
        with TemporaryDirectory() as tmpdir:
            # arrange
            self.touch_file('file1.json', tmpdir)
            self.touch_file('file2.json', tmpdir)
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
            self.touch_file('image1.png', tmpdir)
            self.touch_file('image2.jpg', tmpdir)
            self.touch_file('image3.png', tmpdir)
            # create Annotator object
            annot = Annotator(directory=tmpdir)
            labels_dir = annot.output_dir
            # add files in label_dir
            self.touch_file('image1.json', labels_dir)
            self.touch_file('image2.json', labels_dir)
            # act
            result = annot.list_examples_to_annotate()
            # assert
            expected = [os.path.join(tmpdir, 'image3.png')]
            self.assertListEqual(result, expected)

    def test_set_output_dir_None(self):
        with TemporaryDirectory() as tmpdir:
            # arrange and act
            annot = Annotator(directory=tmpdir, output_directory=None)
            result = annot.output_dir
            # assert
            expected = os.path.join(tmpdir, 'labels')
            self.assertEqual(result, expected)

    def test_set_output_dir_provided_exist(self):
        with TemporaryDirectory() as tmpdir:
            # arrange and act
            annot = Annotator(directory=tmpdir, output_directory=tmpdir)
            result = annot.output_dir
            # assert
            expected = os.path.join(tmpdir)
            self.assertEqual(result, expected)

    def test_set_output_dir_provided_does_not_exist(self):
        with TemporaryDirectory() as tmpdir:
            # arrange and act
            label_dir = os.path.join(tmpdir, 'a/unknown/directory')
            annot = Annotator(directory=tmpdir, output_directory=label_dir)
            result = annot.output_dir
            # assert
            expected = label_dir
            self.assertEqual(result, expected)





if __name__ == '__main__':
    unittest.main()
