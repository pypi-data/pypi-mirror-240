import re
import gzip
import json
import struct
import pathlib
from typing import Generator, List, Union

def finder(
    path: str,
    pattern: str = None,
    full_names: bool = False,
    recursive: bool = False
) -> List[str]:
    """
    Returns a sorted list of file paths in the given directory.

    Args:
        path (str): The directory path to search for files.
        pattern (str, optional): A pattern to match file names against. Defaults to None.
        full_names (bool, optional): Whether to return full file paths or just file names. Defaults to False.
        recursive (bool, optional): Whether to search for files recursively. Defaults to False.

    Returns:
        List[str]: A sorted list of file paths or names.
    """
    files = list(list_file_gen(path, pattern, full_names, recursive))
    files_str = [str(file) for file in files]
    files_str.sort()
    return files_str


def list_file_gen(
    path: Union[str, pathlib.Path],
    pattern: str = None,
    full_names: bool = False,
    recursive: bool = False
) -> Generator[Union[pathlib.Path, str], None, None]:
    """
    Returns a generator of file paths or names in the given directory.

    Args:
        path (Union[str, pathlib.Path]): The directory path to search for files.
        pattern (str, optional): A pattern to match file names against. Defaults to None.
        full_names (bool, optional): Whether to return full file paths or just file names. Defaults to False.
        recursive (bool, optional): Whether to search for files recursively. Defaults to False.

    Yields:
        Generator[Union[pathlib.Path, str], None, None]: A generator of file paths or names.
    """
    path = pathlib.Path(path)
    for file in path.iterdir():
        if file.is_file():
            if pattern is None:
                if full_names:
                    yield file
                else:
                    yield file.name
            elif pattern is not None:
                regex_cond = re.compile(pattern=pattern)
                if regex_cond.search(str(file)):
                    if full_names:
                        yield file
                    else:
                        yield file.name
        elif recursive:
            yield from list_file_gen(file, pattern, full_names, recursive)


def read_metadata_safetensor(
        file: Union[str, pathlib.Path],
        compress: bool = True
) -> None:
    if isinstance(file, str):
        file = pathlib.Path(file)

    if compress:
        with gzip.open(file, "rb") as f:
            data = f.read()
    else:
        with open(file, "rb") as f:
            data = f.read()

    # Get the metadata of the dataset
    length_of_header = struct.unpack('<Q', data[:8])[0]
    metadata = json.loads(data[8:8+length_of_header])
    
    # Save the metadata
    metadata_dict = metadata.pop("__metadata__")
    for key, value in metadata.items():
        metadata_dict[key + "__dtype"] = value["dtype"]
        metadata_dict[key + "__shape"] = "[%s]" % ", ".join([str(i) for i in value["shape"]])
        metadata_dict[key + "__offset"] = "[%s]" % ", ".join([str(i) for i in value["data_offsets"]])

    return metadata_dict