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


test_dict = {"alpha": 1, "beta": 2, "charlie": 3}
test_tuple = tuple(["alpha", "beta", "charlie"])
