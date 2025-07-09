import pandas as pd
import pkg_resources
import os
from os.path import dirname, exists, expanduser, isdir, join, splitext

def load_data(data_name: str):
    """
    """
    if not pkg_resources.resource_exists(__name__, data_name):
        raise FileNotFoundError(f"{data_name} is not found in the {__name__} package.")
    
    stream = pkg_resources.resource_stream(__name__, "data/", data_name, ".csv") # access file in package
    data = pd.read_csv(stream)
    
    return data