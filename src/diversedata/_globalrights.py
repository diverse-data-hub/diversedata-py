## check out difference in variables from R and .csv!!!!!

from diversedata import load_data

def load_globalrights():
    """
    Returns the Global Rights Dataset (2001-2023) as a pandas.DataFrame.
    This function takes no arguments.

    This dataset compiles global indicators related to LGBTIQ+ rights and broader social and economic context.
    It draws from a range of open-access sources curated by Our World in Data. Topics include gender-affirming care,
    same-sex marriage legislation, employment protections, censorship of LGBT+ topics, education spending, GDP,
    and civil liberties.

    Terminology is aligned with the United Nations' "Free and Equal" campaign for LGBTIQ+ equality.

    Variables
    ----------
    year : Observation year.
    country : Country name.
    country-code : Three letter country code.
    gdp-per-capita : GDP per capita.
    education-spending-gdp : Government education spending as % of GDP.
    same-sex-marriage : Legal status of same-sex marriage.
    lgbtq-censorship : Presence of censorship related to LGBT+ content.
    employment-discrimination
    gender-affirming-care : Availability of gender-affirming care.
    legal-gender : Right to change legal gender

    Source
    ------
    Our World in Data. Detailed indicators compiled from:
    Gender-affirming care : https://ourworldindata.org/grapher/gender-affirming-care
    Same-sex marriage : https://ourworldindata.org/grapher/marriage-same-sex-partners-equaldex
    Employment discrimination : https://ourworldindata.org/grapher/employment-discrimination-lgbt-equaldex
    Censorship : https://ourworldindata.org/grapher/censorship-of-lgbt-issues
    Legal gender change : https://ourworldindata.org/grapher/right-to-change-legal-gender-equaldex
    GDP per capita : https://ourworldindata.org/grapher/gdp-per-capita-worldbank
    Education spending : https://ourworldindata.org/grapher/total-government-expenditure-on-education-gdp
    Fertility rate : https://ourworldindata.org/grapher/children-born-per-woman
    Gini Index : https://ourworldindata.org/grapher/economic-inequality-gini-index
    Human rights index : https://ourworldindata.org/grapher/human-rights-index-vdem

    Notes
    -----
    Data sourced from Our World in Data is available under the Creative Commons Attribution 4.0 International License (CC BY 4.0):
    https://creativecommons.org/licenses/by/4.0/

    Example
    --------
    >>> import diversedata as dd
    >>> df = dd.load_globalrights()
    >>> df.head()
        year     country      country-code    ...
    0  2001     Algeria      DZA             ...
    """
    return load_data("globalrights")