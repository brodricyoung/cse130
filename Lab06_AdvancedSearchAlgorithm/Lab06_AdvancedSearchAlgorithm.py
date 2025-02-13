# 1. Name:
#      Brodric Young
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      Efficiently search a list of items for a specified item by the user
# 4. Algorithmic Efficiency
#      O(log n)
# 5. What was the hardest part? Be as specific as possible.
#      Coming up with the algorithmic efficiency, the rest was pretty easy after already 
#      creating the pseudocode for the program.
# 6. How long did it take for you to complete the assignment?
#      About an hour total




import json
filename = input("What is the name of the file? ")

with open(filename) as file:
    names_text = file.read()
    names_json = json.loads(names_text)
    names_list = names_json["array"]

    element = input("What name are we looking for? ")

    i_first = 0                                 # O(1)
    i_last = len(names_list) - 1                # O(1)

    found = False                               # O(1)
    while i_first <= i_last and not found:      # O(log n) because of next line
        i_middle = int((i_first + i_last) / 2)    # O(1) but indicates loop is O(log n)
        if names_list[i_middle] < element:        # O(1)
            i_first = i_middle + 1                  # O(1)
        elif names_list[i_middle] > element:      # O(1)
            i_last = i_middle - 1                   # O(1)
        else:                                     # O(1)
            found = True                            # O(1) 
    print(found)                                