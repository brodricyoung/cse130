# 1. Name:
#      Brodric Young
# 2. Assignment Name:
#      Lab 13: Power
# 3. Assignment Description:
#      Calculate the maximum average power for any given continuous subset in a full set of power integers
# 4. What was the hardest part? Be as specific as possible.
#      Getting the test cases and the regular user input parts to work together to not duplicate code but be seperate at the same time
# 5. How long did it take for you to complete the assignment?
#      About 2 hours

import json
def read_file(filename: str) -> list:
    """
    Read the data from a .json file and return the data in a list
    Input: Filename
    Output: List of values from filename
    """
    try: 
        # assert that the filename passed in is a json file
        assert filename[-5:] == ".json", "File should be a json file with .json extension"

        # open the json file and read the contents into a list
        with open(filename) as file:
            file_text = file.read()
            file_json = json.loads(file_text)

            file_list = file_json["array"]

            # assert that file_list is actually a list
            assert type(file_list) == list, "file_list is not a list"

            for item in file_list:
                assert type(item) == int, f"Contents of the file should only be integers. {item} is not an integer."
    except AssertionError as e:
        print(e)
         # set file_list to 0 so the program later doesn't do anything with it and nothing else is displayed
        file_list = None
    except: 
        print(f"Unable to open file {filename}.")
        # set file_list to 0 so the program later doesn't do anything with it and nothing else is displayed
        file_list = None
    return file_list


def get_max_average_from_file(filename: str, subset_size: int) -> float:
    try: 
        assert type(subset_size) == int, "Subset size should be an integer"
        assert type(filename) == str, "Filename should be a string"
    except AssertionError as e: 
        print(e)
        return None
    
    full_set = read_file(filename)
    if full_set != None: # if there was an error in opening or reading the file, exit and don't do anything with it
        try:

            assert len(full_set) >= subset_size, "Subset size can't be larger than the full sets size."

            sub_set = []
            current_sum = 0
            # Sets up the sub_set and gets the average for the first sub_set
            for i in range(0, subset_size):
                sub_set.append(full_set[i]) # copies the first part of full_set to sub_set, specified by subset_size
                current_sum += sub_set[i]

            max_average = current_sum / subset_size 

            i_subset = 0 
            for i_fullset in range(0, len(full_set) - subset_size): # for each index in full_set - number of indexes in sub_set
                if i_fullset % subset_size == 0: # used for resetting the subset index back to the beginning once it updates the end of the subset
                    i_subset = 0
                assert i_subset in range(0, subset_size), "i_subset should not be greater than the subset size."

                current_sum = current_sum - sub_set[i_subset] + full_set[subset_size + i_fullset] # remove oldest num, add next num in full_set
                current_average = current_sum / subset_size
                if current_average > max_average: # set the max_average to the avg just calculated if it’s the highest so far
                    max_average = current_average
                # replaces oldest num in sub_set with next num in full_set after the sub_set to move it through full_set
                sub_set[i_subset] = full_set[subset_size + i_fullset] 
                i_subset += 1

            assert type(max_average) == float, "max_average should be a float."
            return max_average
        
        except AssertionError as e:
            print(e)
            return None
          


def main():
    # asks for if user wants to run the test cases or use the regular user interface
    while True:
        try: 
            run_tests = bool(int(input("Do you want to:\n - Use the regular interface (Enter '0')\n - Run tests (Enter any other integer)\n >> ")))
            break
        except: 
            print("\nEnter either a '0' or any other integer.")

    # if user wnats to run the test cases
    if run_tests:
        test_cases = [("Bad File", "banana.txt", 0),
                      ("Bad Subset", "small.json", 1000),
                      ("Small", "small.json", 10),
                      ("Large", "large.json", 100)]
        for test_case in test_cases:
            print("---------------------------------------------------------------------------")
            print(f" - Test case: {test_case[0]}\n - File Name: '{test_case[1]}', Subset Size: {test_case[2]}")
            max_average = get_max_average_from_file(test_case[1], test_case[2])
            if max_average != None:
                print(f"Maximum Average Power: {max_average}")
            print()

    # if the user wants to use the regular user interface
    else:
        filename = input("What is the name of the file? ")
        try:
            subset_size = int(input("What is the size of the subset? "))
            assert subset_size > 0, "Subset size should be greater than 0."

        except ValueError:
            print("Subset size should be an integer")
        except AssertionError as e:
            print(e)

        max_average = get_max_average_from_file(filename, subset_size)
        if max_average != None:
            print(f"Maximum Average Power: {max_average}")
    


if __name__ == "__main__":
    main()
    