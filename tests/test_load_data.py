import pandas as pd
import pytest
from io import StringIO
from diversedata import load_data
from unittest import mock

# Expected case
def test_load_data_expected_case():
    """
    Test that load_data correctly loads a valid .csv file into a DataFrame.
    Uses mocking to simulate reading a .csv file from the package's data resources.
    """
    # Simulate csv content as a string
    sample_csv = "col1,col2\n1,2\n3,4"

    # Expected dataframe after loading the csv
    expected_df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})

    # Mock resources.files(...) call chain to simulate opening a file
    with mock.patch("importlib.resources.files") as mock_files:
        # Set return value of .open() to a file-like object containing the csv string
        mock_files.return_value.joinpath.return_value.open.return_value = StringIO(sample_csv)

        # Call load_data
        result = load_data("valid_data")

        # Assert resulting dataframe is equal to expected one
        pd.testing.assert_frame_equal(result, expected_df)

# Edge case
def test_load_data_empty_string_file_exists():
    """
    Test that load_data successfully loads a .csv file named '.csv' when
    data_name is an empty string. Simulates the presence of 'data/.csv' in
    the package resources.
    """
    # Sample csv content for the '.csv' file
    sample_csv = "col1,col2\n10,20\n30,40"

    # Expected dataframe after loading the csv
    expected_df = pd.DataFrame({"col1": [10, 30], "col2": [20, 40]})

    # Mock resources.files(...) call chain to simulate opening a file
    with mock.patch("importlib.resources.files") as mock_files:
         # Set return value of .open() to a file-like object containing the csv string
        mock_files.return_value.joinpath.return_value.open.return_value = StringIO(sample_csv)

        # Call load_data with empty string, which corresponds to the filename '.csv'
        result = load_data("")

        # Assert the loaded dataframe matches expected
        pd.testing.assert_frame_equal(result, expected_df)

# Error cases
def test_load_data_non_string_input():
    """
    Test that load_data raises a TypeError when the input is not a string.
    
    This test loops through a list of invalid input types (e.g., int, float, None,
    list, dict, bool) and checks that load_data raises a TypeError for each.
    """
    bad_input = [123, 3.14, None, [], {}, True]
    for input in bad_input:
        with pytest.raises(TypeError):
            load_data(input)

def test_load_data_file_not_found():
    """
    Test that load_data raises a FileNotFoundError when the specified csv file does not exist.
    """
    with pytest.raises(FileNotFoundError, match="file_that_does_not_exist_!!!!!!.csv is not found in the diversedata package."):
        load_data("file_that_does_not_exist_!!!!!!")