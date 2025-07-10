import pandas as pd
import importlib.resources as resources

def load_data(data_name: str):
    """
    Returns a pandas.DataFrame of a .csv file that is bundled in this package.

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
        If data_name cannot be found in this package.

    Example
    --------
    >>> import diversedata as dd
    >>> df = dd.load_data("wildfire")
    >>> df.head()
       year     fire_number     current_size  ...
    0  2006     PWF001          0.1           ...
    """
    # Get the root package name
    package_name = __name__.split('.')[0]
    
    # Construct the file path
    file_path = f"data/{data_name}.csv"
    
    try:
        # Use importlib.resources to access the file in this package
        with resources.open_text(package_name, file_path) as file:
            data = pd.read_csv(file)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"{data_name}.csv is not found in the {package_name} package.")

def list_available_datasets():
    """
    Prints a list of available datasets in this package and their corresponding loader function.

    Scans the data/ subpackage for .csv files included in this
    package. For each dataset found, prints:

    - The dataset name (excluding the .csv extension)
    - The function to load the dataset (e.g., load_<datasetname>())
    - The method to view the dataset documentation (e.g., help(load_<datasetname>))

    Assumes datasets are stored as .csv files in the data/ subpackage.

    Parameters
    ----------
    None

    Returns
    -------
    None
        Prints dataset information.
        Prints "No datasets found." if there are no datasets in the data/ subpackage.
        Prints "Data directory not found in package." if the data/ subpackage is not found.

    Raises
    ------
    None

    Examples
    --------
    >>> import diversedata as dd
    >>> dd.list_available_datasets()
    Available datasets:
    • wildfire
      Load with:    load_wildfire()
      View documentation with:  help(load_wildfire)
    ...
    """
    # Get the root package name
    package_name = __name__.split('.')[0]
    
    try:
        # List files in the data directory
        data_files = resources.files(package_name).joinpath("data")
        
        # Get all CSV files
        csv_files = [f.name for f in data_files.iterdir() if f.name.endswith('.csv')]
        
        if not csv_files:
            print("No datasets found.")
            return None
            
        # List all files in the 'data' directory of this package
        print("Available datasets:\n")
        for file in sorted(csv_files):
            dataset_name = file.replace(".csv", "")
            print(f"• {dataset_name}")
            print(f"  Load with:    load_{dataset_name}()")
            print(f"  View documentation with:  help(load_{dataset_name})\n")
            
    except FileNotFoundError:
        print("Data directory not found in package.")
        return None