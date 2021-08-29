# world_data.py
# Graydon Hall
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 5 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library, including numpy and pandas.
# Remember to include docstrings and comments.

# import statements
import pandas as pd

# following 5 lines fixes Dataframe printing options in Pycharm
import numpy as np
desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',14)


# Required function
def find_null(sub_region_df):
    """
    Takes a dataframe which is filtered down to a UN Sub-region, and searches for NaN values in the Sq km column..
    If NaN values exist, NaN values are presented to the user, othewise the user is informed that
    there are no missing measurements.
    :param sub_region_df: dataframe filtered down to a specified sub region
    :return no return values
    """
    is_NaN = sub_region_df.isnull()  # find NaN entries
    row_has_NaN = is_NaN.any(axis=1)  # find rows with a null
    sub_region_null_df = sub_region_df[row_has_NaN]  # return rows with a null value (masking example)
    if sub_region_null_df.empty:
        print("There are no missing sq km values for this sub-region")
    else:
        print("Sq km measurements are missing for: ")
        print(sub_region_null_df['Sq Km'])  # print df with UN Region, sub-region, country.


def main():
    """
    This function begins by obtaining a sub-region as a string from the user, and reprompting them until a correct
    input is provided. Data for all UN-regions is imported into a pandas dataframe, and then filtered down to the
    specified sub-region. For this sub region, the change in population, as well as the population density is calculated.
    Next, number of threatened species in each country of the sub region sq km area per number of threatened species
    in each country is determined. All results are presented to the user through the console.
    :param no parameters
    :return no return values
    """
    # ****** Stage 1: Import data ******
    # index order: UN Region -> UN Sub-Region -> Country
    world_df = pd.read_excel("./Assign5Data.xlsx", index_col=[1,2,0])
    world_df.sort_index(inplace=True)  # sort data
    # world_df.to_excel(r".\testExport.xlsx", index=True, header=True)  # export test

    print("ENSF 592 World Data\n")
    # ****** Stage 2: Request user input ******
    sub_regions = world_df.index.get_level_values(1)  # list of all UN Sub regions
    while True:
        try:
            sub_region = input("Please Enter a Sub-region: ")  # get suer input
            if (sub_region in sub_regions):  # valid name entered
                break
            else:
                raise ValueError  # invalid name
        except ValueError:
            # notify user and restart loop
            print("You must enter a valid UN sub-region name")

    # testing values
    # sub_region = "Northern Africa"
    # sub_region = "Melanesia"

    # ****** Stage 3: Find any missing sq km data values for the chosen sub-region ******
    idx = pd.IndexSlice  # index slice object used to slice df
    sub_region_df = world_df.loc[idx[:,sub_region],:].copy()  # create df for sub region
    find_null(sub_region_df)  # check for null values.

    # ****** Stage 4: Calculations and dataset printing for the chosen sub-region ******
    print("\nCalculating change in population and latest density")
    sub_region_df['Delta Population'] = sub_region_df['2020 Pop'] - sub_region_df['2000 Pop']
    sub_region_df['Density'] = sub_region_df['2020 Pop'] / sub_region_df['Sq Km']
    print(sub_region_df)

    print("\nNumber of threatened species in each country of the sub region")
    print(sub_region_df[['Plants (T)', 'Fish (T)', 'Birds (T)', 'Mammals (T)']])  # get endangered species columns

    print("\nThe calculated sq km area per number of threatened species in each country is: ")
    threatened_spec = sub_region_df[['Plants (T)', 'Fish (T)', 'Birds (T)', 'Mammals (T)']]  # get endangered species columns
    sq_km_per_spec = sub_region_df['Sq Km']/threatened_spec.sum(axis=1)  #  sq km / sum of threatened species for each country
    print(sq_km_per_spec)  # display result

if __name__ == '__main__':
    main()

