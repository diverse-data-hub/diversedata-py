import pandas as pd
import pytest
from io import StringIO
from unittest import mock
from diversedata import print_data_description

# Expected case
def test_print_data_description_expected_case(capsys):
    """
    Test that print_data_description correctly reads and prints content from a
    valid .txt file. Uses mocking to simulate a data description file in the package.
    """
    # Simulated text content of the data description file
    sample_txt = "This is a sample description."

    # Mock the resource loading to return our sample text
    with mock.patch("importlib.resources.files") as mock_files:
        mock_files.return_value.joinpath.return_value.open.return_value = StringIO(sample_txt)

        # Call the function with a valid data_name
        print_data_description("valid_data")

        # Check printed output
        captured = capsys.readouterr()
        assert captured.out == sample_txt

# Edge cases
def test_print_data_description_empty_string_file_exists(capsys):
    """
    Test that print_data_description successfully prints content from a .txt file
    named '.txt' when data_name is an empty string. Simulates the presence of
    'data_descriptions/.txt' in the package resources.
    """
    sample_txt = "This is a sample description."
    
    with mock.patch("importlib.resources.files") as mock_files:
        mock_files.return_value.joinpath.return_value.open.return_value = StringIO(sample_txt)

        print_data_description("")

        captured = capsys.readouterr()
        assert captured.out == sample_txt

# Error cases
def test_print_data_description_non_string_input():
    """
    Test that print_data_description raises a TypeError when the input is not a string.
    
    This test loops through a list of invalid input types (e.g., int, float, None,
    list, dict, bool) and checks that print_data_description raises a TypeError for each.
    """
    bad_inputs = [123, 3.14, None, [], {}, True]
    for bad_input in bad_inputs:
        with pytest.raises(TypeError, match="must be a string"):
            print_data_description(bad_input)

def test_print_data_description_file_not_found():
    """
    Test that print_data_description raises a FileNotFoundError when the specified
    .txt file does not exist.
    """
    with mock.patch("importlib.resources.files") as mock_files:
        # Simulate FileNotFoundError when trying to open the file
        mock_files.return_value.joinpath.return_value.open.side_effect = FileNotFoundError
        
        with pytest.raises(FileNotFoundError,
                           match="file_that_does_not_exist_!!!!!!.txt is not found in the diversedata package."):
            print_data_description("file_that_does_not_exist_!!!!!!")