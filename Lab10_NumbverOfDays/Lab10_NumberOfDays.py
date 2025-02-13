# 1. Name:
#      Brodric Young
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      Counts the number of days between two dates
# 4. What was the hardest part? Be as specific as possible.
#      Getting the test cases and the regular user input parts to work together to not duplicate code but be seperate at the same time
# 5. How long did it take for you to complete the assignment?
#      About 3.5 hours


def is_leap_year(year):
    """
    Determine whether a given year is a leap year.
    A leap year is:
    - Divisible by 4
    - Not divisible by 100, unless it is also divisible by 400
    """
    # makes sure the year passed in is an integer and is not less than 1753
    assert type(year) == type(1), "year passed into is_leap_year() should be and integer"
    assert year >= 1753, "the program shouldnt be working with years less than 1753"

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    

def get_days_in_month(month, year):
    """
    Gets the number of days in a given month.
    Input:  month: integer of month number to get days in
            year: integer of year to get the days in the onth for (leap years are differnet for february)
    Output: integer of days in the given month
    """
    # asserts the inputs are valid numbers and integers
    assert 0 < month <= 12, "Invalid month input to get_days_in_month() (should be a number 1-12)"
    assert year >= 1753, "Year input for get_days_in_month() should be >=1753"
    assert type(month) == type(1), "month passed in to get_days_in_month() should be an integer"
    assert type(year) == type(1), "year passed in to get_days_in_month() should be an integer"

    # sets days to the right number for a given month number, accounting for leap years as well
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            days = 31
        case 4 | 6 | 9 | 11:
            days = 30
        case 2:
            if is_leap_year(year): days = 29
            else: days = 28
        case _:
            days = 0
    # makes sure to catch anything weird that happens, days should always be between 28 and 31
    assert 28 <= days <= 31, "Somehow got invalid days return in get_days_in_month() (should be 28, 29, 30, or 31)"
    return days


def check_for_valid_input(start_year, start_month, start_day, end_year, end_month, end_day):
    """
    Checks that the input dates are valid using assert statements
    Inputs: integers for the year, month, and day for both start and end dates.
    Output: Boolean of if the inputs were valid. (Valid is true, invalid is false)
    """
    try:
        assert all(type(x) == type(1) for x in [start_year, start_month, start_day, end_year, end_month, end_day]), "All inputs should be integers."

        assert start_year >= 1753, "Enter a valid start year ( >= 1753)" # years should be after 1753

        assert 0 < start_month <= 12, "Enter a valid start month (between 1 and 12)" # month numbers should be between 1 and 12

        assert 0 < start_day <= 31, "Enter a valid start day (between 1 and 31)" # day numbers should be between 1 and 31

        assert end_year >= start_year, "End year must be >= start year." # end year should be after start year and therefore greater than 1753 too

        assert 0 < end_month <= 12, "Enter a valid end month (between 1 and 12)" # month numbers should be between 1 and 12
        if end_year == start_year:
            assert end_month >= start_month, "For dates in the same year, end month must be >= start month." # end month cant be before start month if in the same year

        assert 0 < end_day <= 31, "Enter a valid end day (between 1 and 31)" # day numbers should be between 1 and 31
        if end_year == start_year and end_month == start_month:
            assert end_day >= start_day, "For dates in the same year and month, end day must be >= start day."# end day cant be before start day if in the same year and month
        print()
        valid_input = True

    except AssertionError as e:
        print(f"\n{e}")
        valid_input = False
    
    return valid_input


def get_dates(running_tests, test_case_index=None):
    """
    Gets the dates to count days between for and makes sure they're valid for either the test cases or a users input
    Input:  running_tests: boolean for whether to run tests or get user input (run tests is true, get users input is false)
            test_case_index: index for which test case to get the dates for in the list
    Output: integers for the year, month, and day for both start and end dates
    """
    # makes sure it was a boolean passed in for the running_tests paramenter
    assert type(running_tests) == type(True), "running tests should be a boolean input for get_dates()"

    if running_tests:
        # makes sure that if its running tests there was an index provided
        assert test_case_index != None, "No test case index provided when getting dates for test case"
        
        # test case dates are in format [startYear, startMonth, startDay, endYear, endMonth, endDay]
        test_case_dates = [[1752, 1, 1, 2000, 1, 1],     # year less than 1753
                            [2000.5, 1, 1, 2000, 1, 1],  # year that is not an integer
                            [2000, 0, 1, 2000, 1, 1],    # month that is less than 1
                            [2000, 1, 1, 2000, 13, 1],   # month that is greater than 12
                            [2000, 1, 0, 2000, 1, 1],    # day that is less than 1
                            [2000, 1, 32, 2000, 1, 1],   # day that is greater than the number of days for a month
                            [2000, 1, 2, 2000, 1, 1],    # end date before start date
                            [2024, 10, 31, 2024, 10, 31],# start and end date are the same
                            [2025, 5, 10, 2026, 5, 11],  # start and end date are in the same month
                            [2025, 3, 31, 2025, 4, 5],   # start and end date are in the same year
                            [2024, 12, 25, 2025, 1, 8],  # start date is Christmas and end date is two weeks later
                            [2003, 3, 29, 2024, 11, 19]] # your birth date and today's date

        test_case = test_case_dates[test_case_index] # gets the right tast case

        # sets the date variables to the right part of the list
        start_year, start_month, start_day = test_case[0], test_case[1], test_case[2] 
        end_year, end_month, end_day = test_case[3], test_case[4], test_case[5]

    else: 
        valid_input = False
        while not valid_input: # keeps asking for dates until a valid input is given
            try: 
                start_year = int(input("Start year: "))
                start_month = int(input("Start month: "))
                start_day = int(input("Start day: "))
                end_year = int(input("End year: "))
                end_month = int(input("End month: "))
                end_day = int(input("End day: "))

                # checks if the user input dates are valid to count days between
                valid_input = check_for_valid_input(start_year, start_month, start_day, end_year, end_month, end_day)

            except ValueError: # cathces any errors with trying to convert the user input to an integer
                print("\nAll inputs should be integers.")
                valid_input = False

            
        
    return start_year, start_month, start_day, end_year, end_month, end_day
        

def get_days_between(start_year, start_month, start_day, end_year, end_month, end_day):
    if start_year == end_year:
        if start_month == end_month:
            days_between = end_day - start_day # executes when years and months are the same

        else: # Executes when months are different
            # Gets days in the start month after the start day
            days_between = get_days_in_month(start_month, start_year) - start_day

            # Gets days from all the months after the start up to an NOT including the end month
            for i_month in range(start_month + 1, end_month):
                days_between += get_days_in_month(i_month)

            # Gets days in the end month
            days_between += end_day

    else: # Executes when years are different
        # Gets days in the start month after the start day
        days_between = get_days_in_month( start_month, start_year) - start_day

        # Gets days from all the months after the start month through end of the year
        for i_month in range(start_month + 1, 13):
            days_between += get_days_in_month(i_month, start_year)

        # Gets days from each year between the start year and end year
        for i_year in range(start_year + 1, end_year):
            if is_leap_year(i_year):
                days_between = days_between + 366
            else:
                days_between = days_between + 365

        # Gets days from each month preceding the end month in the end year
        for i_month in range(1, end_month):
            days_between += get_days_in_month(i_month, end_year)

        # Gets days in the end month
        days_between = days_between + end_day
    return days_between


def main():
    running_tests = ""
    while type(running_tests) != type(True): # keeps asking for if youre running tests or not until a 0 or any other integer is given
        try:
            running_tests = bool(int(input("Get user input (0) or run tests (any other integer)? ")))
            
        except: # catches any errors converting to an int or bool with an invalid input
            print("Enter either a 0 or 1.")

    if running_tests:
        test_cases = ["1: year less than 1753",
                      "2: year that is not an integer",
                      "3: month that is less than 1",
                      "4: month that is greater than 12",
                      "5: day that is less than 1",
                      "6: day that is greater than the number of days for a month",
                      "7: end date before start date",
                      "8: start and end date are the same",
                      "9: start and end date are in the same month",
                      "10: start and end date are in the same year",
                      "11: start date is Christmas and end date is two weeks later",
                      "12: your birth date and today's date"]

        for i_test_case, test_case in enumerate(test_cases): # runs through each test case
            start_year, start_month, start_day, end_year, end_month, end_day = get_dates(running_tests, i_test_case)

            print("-------------------------------------------------------------------------------------")
            print(f"Test case #{test_case}")
            print()
            print(f"Start year: {start_year}, Start month: {start_month}, Start day: {start_day}")
            print(f"End year: {end_year}, End month: {end_month}, End day: {end_day}")
            print()

            # checks if the test case dates are valid to count days between, prints any error that it comes up with
            valid_input = check_for_valid_input(start_year, start_month, start_day, end_year, end_month, end_day)

            if valid_input:
                print(f"There are {get_days_between(start_year, start_month, start_day, end_year, end_month, end_day)} days.")


    else: # if not running test cases
        days_between = get_days_between(get_dates(running_tests))
        print(f"There are {days_between} days.")

if __name__ == "__main__":
    main()


