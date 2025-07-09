import pandas as pd
import importlib.resources as resources

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
    Prints a list of the data available in this package and
    which function loads the data.
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
            print(f"  Load with:    load_data('{dataset_name}')\n")
            print(f"  View documentation with:  help(load_data)\n")
            
    except FileNotFoundError:
        print("Data directory not found in package.")
        return None