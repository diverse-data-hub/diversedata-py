# Changelog

<!--next-version-placeholder-->

## v1.0.0 (30/07/2025)

- First release of `diversedata`!

## v1.0.1 (08/08/2025)

### Fixes

- Update variable descriptions for gender assessment data.

## v1.0.2 (18/08/2025)

### Fixes

- Update variable descriptions of wildfire data set to be more consistent with data source data dictionary.

## v1.0.3 (14/11/2025)

### Fixes

- Clean BC Indigenous Business data, combine 'Vancouver Island and Coast' and 'Vancouver Island / Coast' into one category: 'Vancouver Island / Coast'.

## v1.0.4 (21/11/2025)

### Fixes

- Clean BC Indigenous Business data:
  - city names: removed periods and commas, removed "B.C."/"BC", applied capwords, replaced spaces larger than one space with one space, removed trailing and leading spaces, and fixed known typos.
  - ownership types: converted ': Community Owned Company' and 'Community Owned' to 'Community Owned Company', and converted 'Partnershp' to 'Partnership'
  - number of employees data: converted ' ' to nan, removed any leading and trailing spaces, and converted '55 to 99' to '50 to 99' since the range '55 to 99' overlaps with the more frequent '50 to 99'.