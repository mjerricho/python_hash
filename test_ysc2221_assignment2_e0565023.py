from ysc2221_assignment2_e0565023 import (
    read_rainbow_table,
    read_hashed_file,
    unhash_file,
    write_bytes_to_file
)


def test_read_rainbow_table():

    try:
        read_rainbow_table
    except NameError:
        assert False, "read_rainbow_table not defined"

    filename = "rainbow-table.txt"
    dict, status = read_rainbow_table(filename)
    assert status == ""
    assert len(dict) == 256

    assert dict["2144df1c"] == 0
    assert dict["99f8b879"] == 1


def test_read_hashed_file():

    try:
        read_hashed_file
    except NameError:
        assert False, "read_hashed_file not defined"

    filename = "hashed.txt"
    hashes, columns, rows, status = read_hashed_file(filename)
    assert status == ""
    assert columns == 640
    assert rows == 360
    assert len(hashes) == 360

    assert hashes[0][0][0] == "70234eba"
    assert hashes[0][0][1] == "3af5f102"
    assert hashes[0][0][2] == "28405eec"


def test_unhash_file():

    try:
        unhash_file
    except NameError:
        assert False, "unhash_file not defined"

    rainbow_table_file = "rainbow-table.txt"
    rainbow_table, status = read_rainbow_table(rainbow_table_file)

    hashed_file = "hashed.txt"
    hashes, columns, rows, status = read_hashed_file(hashed_file)

    pixel_data = unhash_file(rainbow_table, hashes)

    assert len(pixel_data) == 360

    for row in pixel_data:
        assert len(row) == 640

    assert pixel_data[0][0][0] == 251
    assert pixel_data[0][0][1] == 247
    assert pixel_data[0][0][2] == 244


def test_write_bytes_to_file():

    try:
        write_bytes_to_file
    except NameError:
        assert False, "write_bytes_to_file not defined"

    hw_bytes = "Hello World!".encode()

    dummy_filename = "dummy_bin_file"

    status = write_bytes_to_file(hw_bytes, dummy_filename)
    assert status == ""

    with open(dummy_filename, "r") as dummy_file:
        assert dummy_file.read() == "Hello World!"
