from glob import glob
from typing import List


def list_files_with_extension(directory: str, extension: str) -> List[str]:
    """List all files in directory with given extension.

    Parameters
    ----------
    directory : str
        path to a directory without final '/'
    extension : str
        extension including the '.'

    Returns
    -------
    List of path of the files in the directory with given extension.

    """
    return glob(f'{directory}/*{extension}')


def list_images_in_directory(directory: str, extensions: List[str] = ['jpg', 'JPG', 'JPEG', 'png', 'PNG']) -> List[str]:
    """List all image files in directory, according to list of extensions."""
    image_files = []
    for extension in extensions:
        image_files += list_files_with_extension(directory=directory, extension=extension)
    return image_files
