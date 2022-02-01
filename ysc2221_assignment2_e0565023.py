# YSC2221 Assignment 2
#
# Name: Marcellinus Jerricho
# Student ID: e0565023
# Resources used:
#  ...
# What is described in the original image?:
# Comments to grader: NA or fill in if any
# Grader's comment: "To be filled by grader"
################
# Install libraries `pip3 install -r requirements.txt`
# You can run this file as `python ysc2221_assignment2.py`
################


def read_rainbow_table(filename: str) -> "tuple[dict[str, int], str]":
    """
    Opens the rainbow table file and provides a mapping of hash values

    Parameters:
    ----
    filename<str>: Filepath to rainbow table

    Return:
    ----
    tuple(table, status): Tuple of the following values

    table <tuple[dict[str, int], str]>:
        * Mapping of hashstrings to pixel colour value
        * None if problems are encountered
    status <str>:
        * empty string "" if no problems encountered reading and processing
        * custom message that best describes the problem

    Implementation:
    ----
    * Function cannot crash on abnormal inputs like None, empty string etc
    * Handle abnormal file conditions like missing file, no permissions etc
    * Provided file can be assumed to always be in the correct format
    * At least one specific exception handling must be demonstrated
    * Simply catching a (Base)Exception will not earn full credit
    """
    try:
        rainbow_dict = dict()
        with open(filename, "r") as file:
            for line in file:
                [hash_key, hash_value] = line.split()
                rainbow_dict[hash_key] = int(hash_value)
    except (FileNotFoundError, PermissionError, TypeError,
            IndexError, OSError) as e:
        return tuple((None, repr(e)))
    return tuple((rainbow_dict, ""))


def read_hashed_file(filename: str) -> \
        "tuple[list[list[tuple[str, str, str]]], int, int, str]":

    """
    Opens the hashed file

    Parameters:
    ----
    filename<str>: Filepath to hash file

    Return:
    ----
    tuple(hashes, columns, rows, status): Tuple of the following values

    hashes <list[list[tuple[str, str, str]]]>:
        * Multi-dimensional list of hashed pixel data
            in rows x cols x 3 colour (RGB) hashed values
        * None if error is found

    columns <int>: number of columns specified in the hashed file. 0 if error.

    rows <int>: number of rows specified in the hashed file. 0 if error.

    status <str>:
        * empty string "" if no problems encountered reading and processing
        * custom message that best describes the problem

    Implementation:
    ----
    * Function cannot crash on abnormal inputs like None, empty string etc
    * Handle abnormal file conditions like missing file, no permissions etc
    * Provided file can be assumed to always be in the correct format
    * At least one specific exception handling must be demonstrated
    * Simply catching a (Base)Exception will not earn full credit
    """
    try:
        with open(filename, "r") as file:
            num_col_row = file.readline().replace("\n", " ").split(" ")
            num_col, num_row = int(num_col_row[0]), int(num_col_row[1])
            list_row = list()
            for row_number in range(num_row):
                list_col = list()
                for col_number in range(num_col):
                    list_col.append(tuple(file.readline().split()))
                list_row.append(list_col)
    except (FileNotFoundError, PermissionError, TypeError,
            IndexError, OSError) as e:
        return(None, 0, 0, repr(e))
    return tuple([list_row, num_col, num_row, ""])


def unhash_file(rainbow_table: "dict[str, int]",
                hash_content: "list[list[tuple[str, str, str]]]") -> \
                "list[list[tuple[int, int, int]]]":
    """
    Convert the hashes back to original pixel data

    Parameters:
    ----
    rainbow_table <dict[str, int]>: Mapping of hashes to integers
    hash_content <list[list[tuple[str, str, str]]]>: hashed data

    Return:
    ----
    original_pixels <list[list[tuple[int, int, int]]]>:
        * Multi-dimensional list of hashed pixel data
            in rows x cols x 3 colour (RGB) integer values
    """
    try:
        original_pixels = list()
        for hashed_row in hash_content:
            original_pixels_row = list()
            for hashed_col in hashed_row:
                original_pixels_col = list()
                for hashed_pixel in hashed_col:
                    if rainbow_table.get(hashed_pixel) is None:
                        print("Could not unhash the pixel")
                        return None
                    original_pixels_col.append(rainbow_table.get(hashed_pixel))
                original_pixels_row.append(tuple(original_pixels_col))
            original_pixels.append(original_pixels_row)
        return original_pixels
    except (IndexError, OSError):
        return None


def write_bytes_to_file(bytes_to_write: bytes, filename: str) -> str:
    """
    Write the image bytes to file

    Parameters:
    ----
    bytes_to_write <bytes>: Raw binary data of the image file
    filename <str>: Filename to write to

    Return:
    ----
    status <str>:
        * empty string "" if no problems encountered reading and processing
        * custom message that best describes the problem

    Implementation:
    ----
    * Function cannot crash on abnormal inputs like None, empty string etc
    * Handle abnormal file conditions like no permissions etc
    * bytes_to_write data is generated from produce_image()
    * At least one specific exception handling must be demonstrated
    * Simply catching a (Base)Exception will not earn full credit
    """
    try:
        with open(filename, "wb") as file:
            file.write(bytes_to_write)
    except (FileNotFoundError, PermissionError, TypeError,
            IndexError, OSError) as e:
        return repr(e)
    return ""


def produce_image(pixel_data: "list[list[tuple[int, int, int]]]",
                  display_image=False) \
                  -> bytes:
    """
    # DO NOT MODIFY THIS HELPER FUNCTION
    Take in the pixel data to produce the image

    Parameters:
    ----
    pixel_data <list[list[tuple[int, int, int]]]>:
        Multi-dimensional list of hashed pixel data
            in rows x cols x 3 colour (RGB) integer values
    display_image <bool>:
        True: Will show image in default image viewer
        False: Will not show image

    Return:
    ----
    bytes : Raw bytes of a JPEG image

    """

    from PIL import Image
    import numpy as np
    import io

    # Convert the pixel data into an array using numpy
    array = np.array(pixel_data, dtype=np.uint8)

    new_image = Image.fromarray(array)

    if display_image:
        new_image.show()

    img_binary_data = io.BytesIO()
    new_image.save(img_binary_data, format='JPEG')

    return img_binary_data.getbuffer()


if __name__ == "__main__":

    import sys

    rainbow_table_file = "rainbow-table.txt"
    rainbow_table, status = read_rainbow_table(rainbow_table_file)

    if status != "":
        print(status)
        sys.exit()

    hashed_file = "hashed.txt"
    hashes, columns, rows, status = read_hashed_file(hashed_file)

    if status != "":
        print(status)
        sys.exit()

    pixel_data = unhash_file(rainbow_table, hashes)

    # You may set the display_image parameter to True to view the image
    raw_jpeg_bytes = produce_image(pixel_data, display_image=False)

    # You may change eXXXX to your student ID
    status = write_bytes_to_file(raw_jpeg_bytes, "e0565023.jpg")

    if status != "":
        print(status)
