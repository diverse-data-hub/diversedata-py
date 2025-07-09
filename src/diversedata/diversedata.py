import pandas as pd
import pkg_resources
import os
from os.path import dirname, exists, expanduser, isdir, join, splitext

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

    Examples
    --------
    >>> from diversedata import load_data
    >>> df = load_data("wildfire")
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