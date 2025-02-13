# 1. Name:
#      Brodric Young

# 2. Assignment Name:
#      Lab 08: Sort

# 3. Assignment Description:
#      From a given json filename, put all the values in the file into a list then sort that list and display it back

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to make the program fail gracfully when handling a non-valid filename or empty list

# 5. How long did it take for you to complete the assignment?
#      About 1.5 hours


import json


def read_file(filename):
    """
    Read the data from a .json file and return the data in a list
    Input: Filename
    Output: List of values from filename
    """
    # assert that the filename passed in is a json file
    assert filename[-5:] == ".json", "File should be a json file with .json extension"

    try: 
        # open the json file and read the contents into a list
        with open(filename) as file:
            file_text = file.read()
            file_json = json.loads(file_text)
            file_list = file_json["array"]

            # assert that file_list is actually a list
            assert type(file_list) == list, "file_list is not a list"

    except: 
        print(f"Unable to open file {filename}.")
        # set file_list to 0 so the program later doesn't do anything with it and nothing else is displayed
        file_list = 0
    return file_list


def sort_list(values):
    """
    Sort list of values from least to greatest
    Input: List of values
    Output: Sorted list
    """
    # assert that the values passed in are in a list
    assert type(values) == list, "values passed into the sort_list function should be in a list"

    # iterates through the list from the last index to the 2nd index
    for i_pivot in range(len(values) - 1, 0, -1):
        i_largest = 0

        # iterates throught the list from the 2nd index to the last, gets the index of the largest value
        for i_check in range(1, i_pivot, 1):
            if values[i_check] > values[i_largest]:
                i_largest = i_check
        
        # if the value at the pivot index isn't the largest, swap it places with the largest
        if values[i_largest] > values[i_pivot]:
            values[i_largest], values[i_pivot] = values[i_pivot], values[i_largest]

    # assert that the list is actually sorted
    for i in range(len(values) - 1):
        assert values[i] <= values[i + 1], "List is not sorted"

    return values


def display_values(filename):
    """
    Displays the values from the file
    Input: Filename
    """
    file_list = read_file(filename)

    # if the file is empty, just display that its empty
    if file_list == []:
        print(f"The file {filename} is empty.")
    # if it not empty and the file was found in the read_file function, sort and display the values
    elif file_list != 0:
        values = sort_list(file_list)
        print(f"The values in {filename} are:")
        for value in values:
            print(f"    {value}")
    


def main():
    # asks for if user wants to run the test cases or use the regular user interface
    run_tests = bool(int(input("Do you want to:\n  0. Use the regular interface?\n  1. Run tests\n >> ")))
    
    # if user wnats to run the test cases
    if run_tests:
        test_cases = [("Empty list","Lab08.empty.json"),
                      ("List with one element", "Lab08.trivial.json"),
                      ("Small list", "Lab08.languages.json"),
                      ("Medium list", "Lab08.states.json"),
                      ("Large list", "Lab08.cities.json")]
        for test_case in test_cases:
            print("---------------------------------------------------------------------------")
            print(f"Test case: {test_case[0]}")
            display_values(test_case[1])
            print()
    # if the user wnats to use the regular user interface
    else:
        filename = input("What is the name of the file? ")
        display_values(filename)
        


if __name__ == "__main__":
    main()
    