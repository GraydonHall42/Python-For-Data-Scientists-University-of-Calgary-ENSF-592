# school_data.py
# Graydon Hall
#
# A terminal-based application for computing and printing statistics based on given input.
# Detailed specifications are provided via the Assignment 4 git repository.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np

# dictionaries used to get school name based on code, or vice versa.
from school_codes import school_codes_dict, school_names_dict

def main():
    """
    This script imports data from a CSV which contains statistics on enrollment in 20 Calgary highschools from
    2013 - 2020, and presents the user with the following information:
    Mean enrollment in 2013 and 2020 for all schools
    Total graduating class size for 20200 for all schools
    Highest and lowest enrollment in a single grade across all grades from all schools
    Mean enrollment for Grade 10-12, highest and lowest enrollment over time, and
    enrollment by year, for a school specified by the user

    :param no parameters
    :return nothing
    """
    # obtain data
    my_data = np.genfromtxt('Assignment4Data.csv', delimiter=',', dtype='int32')  # import csv
    reformatted_data = my_data[1:,[0,2,3,4,5]].copy()  # remove first row (headers), take columns 0,2,3,4,5
    my_data_yearly = reformatted_data.reshape(8,20,5)  # 8 Layers (years), 20 rows (schools), 5 columns (grades)

    # Print Stage 1 requirements here
    print("ENSF 592 School Enrollment Statistics")
    print(f"Shape of full data array: {my_data_yearly.shape}")
    print(f"Dimensions of full data array: {my_data_yearly.ndim}")


    # obtain school from user
    while True:  # continue till valid school is obtained.
        school_input = input("Please enter the high school name or school code: ")  # prompt user.

        # use try catch block to differentiate if they enter code or school name.
        try:
            school_code = int(school_input)  # if they entered code
            try:  # try to see if school is valid
                if school_code in reformatted_data[:, 1]:  # check code is valid.
                    school_name = school_names_dict[school_code]  # obtain
                    break  # exit while loop.
                else:
                    raise ValueError  # raise valid error due to invalid code
            except ValueError:
                print("You must enter a valid school name or code")
                continue  # retry getting input from user

        except ValueError:  # means a school name was entered.
            school_name = school_input  # if they entered name.
            try:  # try to see if school is valid
                if school_name in school_codes_dict:  # check for existence.
                    school_code = school_codes_dict[school_name]  # get school code based on school_name
                    break  # exit while loop
                else:
                    raise ValueError  # raise valid error due to invalid school name
            except ValueError:
                print("You must enter a valid school name or code")
                continue  # retry getting input from user


    # # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    print(f"School Name: {school_name}, School Code: {school_code}")

    school_view = reformatted_data[reformatted_data[:, 1] == school_code]  # filter down based on school code.
    mean_enrollment = school_view.mean(axis=0)  # collapse rows and find mean.

    # FOR MARKING... this is a subarray view.
    enrollment_array = school_view[:, 2:]  # all enrollments, year and school code excluded

    print(f"Mean enrollment for Grade 10: {mean_enrollment[2]} ")
    print(f"Mean enrollment for Grade 11: {mean_enrollment[3]} ")
    print(f"Mean enrollment for Grade 12: {mean_enrollment[4]} ")
    print(f"Higheset enrollment for a single grade: {enrollment_array.max()}")
    print(f"Lowest enrollment for a single grade: {enrollment_array.min()}")
    enrollment_by_year = enrollment_array.sum(axis=1)  # collapse on rows
    for i in range(8):
        print(f"Total Enrollment for {2013+i}: {enrollment_by_year[i]}")


    any_above_500 = enrollment_array > 500  # boolean array of entries > 500.
    if any_above_500.sum()>0:  # will return >0 if any entries > 500.
        # masking operation:
        median_above_500 = np.median(enrollment_array[enrollment_array > 500])  # calculate median of entries > 500
        print(f"For all enrollments over 500, the median value was: {median_above_500}")
    else:
        print("No Enrollments over 500")


    # # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    print(f"Mean Enrollment for 2013: {my_data_yearly[0,:,2:].mean()}")  # mean of 2013 g10,g11,g12 columns
    print(f"Mean Enrollment for 2020: {my_data_yearly[7,:,2:].mean()}")  # mean of 2020 g10,g11,g12 columns
    print(f"Total graduating class of 2020: {my_data_yearly[7,:,4].sum()}")  # sum of all 2020 g12 column
    print(f"Highest enrollment for a single grade: {my_data_yearly[:,:,2:].max()}")  # max of all g10,g11,g12 columns
    print(f"Lowest enrollment for a single grade: {my_data_yearly[:,:,2:].min()}")  # min of all g10,g11,g12 columns




if __name__ == '__main__':
    main()

