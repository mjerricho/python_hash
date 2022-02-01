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
