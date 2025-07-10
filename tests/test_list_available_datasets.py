from diversedata import list_available_datasets

# Expected cases
# .csv datasets and matching .txt description files are correctly listed and sorted alphabetically

# Edge cases
# Dataset exists but no description file
# No .csv files in the data directory
# Non-csv files in the data directory (they should be ignored)

# Error case
# Data directory is missing entirely