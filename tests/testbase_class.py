import os
import unittest
from pathlib import Path


class TestBaseClass(unittest.TestCase):
    DIR_PATH = os.path.dirname(os.path.abspath(__file__))
    RESOURCE_DIR = os.path.join(DIR_PATH, 'resources')

    def __init__(self, *args, **kwargs):
        super(TestBaseClass, self).__init__(*args, **kwargs)

    def touch_file(self, filename, directory):
        """Create a file in directory."""
        Path(os.path.join(directory, filename)).touch()
