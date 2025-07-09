import pandas as pd
import pkg_resources

def load_data(data_name: str):
    """
    Returns a pandas.DataFrame of a CSV file that is bundled in this package.

    Looks for data_name.csv in this package's resources and 
    raises an error if the file is missing.

    Parameters
    ----------
    data_name : str
        The filename (excluding the .csv extension) of the data
        resource to load.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the parsed contents of data_name.

    Raises
    ------
    FileNotFoundError
        If data_name cannot be found in the installed package.

    Example
    --------
    >>> import diversedata as dd
    >>> df = dd.load_data("wildfire")
    >>> df.head()
       year     fire_number     current_size  ...
    0  2006     PWF001          0.1           ...
    """
    # check if data is in this package
    if not pkg_resources.resource_exists(__name__, data_name):
        raise FileNotFoundError(f"{data_name} is not found in the {__name__} package.")
    
    # access file in package
    stream = pkg_resources.resource_stream(__name__, "data/", data_name, ".csv") 
    data = pd.read_csv(stream)

    return data

def list_available_datasets():
    """
    Prints a list of the data available in this package and
    which function loads the data.
    """
    data_dir = "data"
    files = pkg_resources.resource_listdir(__name__, data_dir)
    csv_files = [f for f in files if f.endswith('.csv')]

    if not csv_files:
        print("No datasets found.")
        return None

    # List all files in the 'data' directory of this package
    print("Available datasets:\n")
    for file in sorted(csv_files):
        dataset_name = file.replace(".csv", "")
        print(f"• {dataset_name}")
        print(f"  Load with:    load_{dataset_name}()\n")
        print(f"  View documentation with:  help(load_{dataset_name})\n")