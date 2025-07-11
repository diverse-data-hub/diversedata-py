import pytest
from unittest import mock
from types import SimpleNamespace
from diversedata import list_available_datasets

# Expected cases
def test_list_available_datasets_expected_case(capsys):
    """
    Test that datasets with matching .csv and .txt files are listed and sorted
    alphabetically by list_available_datasets.
    """
    # Fake .csv files
    csv_files = [
        SimpleNamespace(name="b.csv"),
        SimpleNamespace(name="a.csv"),
        SimpleNamespace(name="c.csv"),
    ]

    # Mock for .is_file() to return True for all matching .txt files
    def fake_joinpath_desc(name):
        return mock.Mock(is_file=mock.Mock(return_value=True))

    with mock.patch("importlib.resources.files") as mock_files:
        # Setup mocks for data and data_descriptions directories
        mock_files.return_value.joinpath.side_effect = lambda subpath: {
            "data": mock.Mock(iterdir=mock.Mock(return_value=csv_files)),
            "data_descriptions": mock.Mock(joinpath=fake_joinpath_desc)
        }[subpath]

        # Run list_available_datasets and check output
        list_available_datasets()
        output = capsys.readouterr().out

        # Validate sorted output and presence of loading and doc instructions
        assert "Available datasets:" in output
        assert "• a" in output
        assert "• b" in output
        assert "• c" in output
        assert "load_data('a')" in output
        assert "print_data_description('a')" in output

# Edge cases
def test_list_available_datasets_missing_description(capsys):
    """
    Test that datasets are listed even if a description file is missing,
    and the list_available_datasets prints a note instead of a doc reference.
    """
    # Fake .csv file
    csv_files = [SimpleNamespace(name="data_only.csv")]

    # Mock for .is_file() to return False
    def fake_joinpath_desc(name):
        return mock.Mock(is_file=mock.Mock(return_value=False))

    with mock.patch("importlib.resources.files") as mock_files:
        # Setup mocks for data and data_descriptions directories
        mock_files.return_value.joinpath.side_effect = lambda subpath: {
            "data": mock.Mock(iterdir=mock.Mock(return_value=csv_files)),
            "data_descriptions": mock.Mock(joinpath=fake_joinpath_desc)
        }[subpath]

        # Run list_available_datasets and check output
        list_available_datasets()
        output = capsys.readouterr().out

        # Validate output and presence of loading but no doc instructions
        assert "• data_only" in output
        assert "load_data('data_only')" in output
        assert "Description file not found." in output

def test_list_available_datasets_no_csv_files(capsys):
    """
    Test that list_available_datasets prints a message when no .csv files
    are found in the data directory.
    """
    with mock.patch("importlib.resources.files") as mock_files:
        # Setup mocks for data and data_descriptions directories,
        # the mock data directory has no .csv files
        mock_files.return_value.joinpath.side_effect = lambda subpath: {
            "data": mock.Mock(iterdir=mock.Mock(return_value=[])),
            "data_descriptions": mock.Mock()
        }[subpath]

        # Run list_available_datasets and check output
        list_available_datasets()
        output = capsys.readouterr().out

        # Validate output that no datasets were found
        assert "No datasets found." in output

def test_list_available_datasets_ignores_non_csv(capsys):
    """
    Test that non-csv files in the data directory are ignored.
    """
    # Fake files
    files = [
        SimpleNamespace(name="ignore.txt"),
        SimpleNamespace(name="ignore.md"),
        SimpleNamespace(name="valid.csv"),
    ]

    # Mock for .is_file() to return True for all files
    def fake_joinpath_desc(name):
        return mock.Mock(is_file=mock.Mock(return_value=True))

    with mock.patch("importlib.resources.files") as mock_files:
        # Setup mocks for data and data_descriptions directories
        mock_files.return_value.joinpath.side_effect = lambda subpath: {
            "data": mock.Mock(iterdir=mock.Mock(return_value=files)),
            "data_descriptions": mock.Mock(joinpath=fake_joinpath_desc)
        }[subpath]

        # Run list_available_datasets and check output
        list_available_datasets()
        output = capsys.readouterr().out

        # Make sure that output only mentions information related to
        # the .csv files in the data directory (and not other file types)
        assert "• valid" in output
        assert "• ignore" not in output
        assert "load_data('valid')" in output

# Error case
def test_list_available_datasets_data_dir_missing():
    """
    Test that list_available_datasets raises FileNotFoundError
    when the data directory is missing.
    """
    with mock.patch("importlib.resources.files") as mock_files:
        # Simulate exception when trying to access 'data'
        def side_effect(subpath):
            if subpath == "data":
                raise FileNotFoundError
            return mock.Mock()
        
        mock_files.return_value.joinpath.side_effect = side_effect

        with pytest.raises(FileNotFoundError, match="Data directory not found in package."):
            list_available_datasets()