# read version from installed package
from importlib.metadata import version
__version__ = version("diversedata")

# populate package namespace
from diversedata.diversedata import load_data, list_data
from diversedata._bcindigenousbiz import load_bcindigenousbiz
from diversedata._genderassessment import load_genderassessment
from diversedata._globalrights import load_globalrights
from diversedata._hcmst import load_hcmst
from diversedata._wildfire import load_wildfire
from diversedata._womensmarchmadness import load_womensmarchmadness