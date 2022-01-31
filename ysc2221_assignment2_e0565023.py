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
    rainbow_dict = dict()

    try:
        with open(filename, "r") as file:
            for line in file:
                try:
                    hashed_value = line.replace("\n", "").split(" ")
                    rainbow_dict[hashed_value[0]] = int(hashed_value[1])
                except IndexError as e:
                    return tuple((rainbow_dict, repr(e)))
                except TypeError as e:
                    return tuple((rainbow_dict, repr(e)))
    except FileNotFoundError as e:
        print(repr(e))
        return None
    except PermissionError as e:
        print(repr(e))
        return None
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
    list_hash = list()

    try:
        with open("hashed.txt", "r") as file:
            try:
                num_col_row = file.readline().replace("\n", " ").split(" ")
                num_col = int(num_col_row[0])
                num_row = int(num_col_row[1])
                for row_number in range(num_row):
                    list_col = list()
                    for col_number in range(num_col):
                        line = file.readline()
                        hashed_pixel_data = line.replace("\n", "").split(" ")
                        list_col.append(tuple(hashed_pixel_data))
                    list_hash.append(list_col)
            except IndexError as e:
                return(None, 0, 0, repr(e))
            except TypeError as e:
                return(None, 0, 0, repr(e))
    except FileNotFoundError as e:
        print(repr(e))
        return None
    except PermissionError as e:
        print(repr(e))
        return None
    return tuple([list_hash, num_col, num_row, ""])


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

    pass


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

    pass


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
    status = write_bytes_to_file(raw_jpeg_bytes, "eXXX.jpg")

    if status != "":
        print(status)
