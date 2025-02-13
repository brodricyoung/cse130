# 1. Name:
#      Brodric Young

# 2. Assignment Name:
#      Lab 02: Authentication

# 3. Assignment Description:
#      This program reads in two lists from a file containing usernames
#       and passwords, then asks the user for their username and password
#       and checks if they are authenticated or not

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was trying to figure out how to do it in the most
#       concise and efficient way without reusing the same line of code or
#       including unnecessary steps. Working with a json file would've been
#       hard if we didn't go over it in class, but the rest of it was relatively
#       easy and went well. But I also tried to make a test function for all
#       the test cases and I had a hard time getting it to work, something was
#       wrong with it so I ended up giving up on that and testing all the test
#       cases quickly a different way

# 5. How long did it take for you to complete the assignment?
#      2 hours


import json

# used for testing and printing which test case is being executed
test_cases = ['Incorrect username',
              'Incorrect password',
              'Both incorrect',
              'Wrong index',
              'Valid Black Knight',
              'Valid King Arthur',
              'Valid French Soldier']


def authentication():

    # Used to keep looping through to test all test cases at once and print which one it is
    # I copied all the inputs and then pasted them to put in every input quickly
    for test_case in test_cases:
        print(f'>> {test_case}')

        # Opens and stores the json file, then seperates into two lists for usernames and passwords
        try:
            filename = 'Lab02.json'
            file = open(filename, 'r')
            file_data = json.loads(file.read())

            usernames = file_data['username']
            passwords = file_data['password']

            file.close()
        except:
            print(f'Unable to open file {filename}')

        # Gets the user input for their username and password
        user_username = input('Username: ')
        user_password = input('Password: ')

        # Checks if the provided username exists and if it and password have the same index
        try:
            user_username_index = usernames.index(user_username)
            authenticated = user_password == passwords[user_username_index]
            if authenticated:
                print('You are authenticated!')
            else:
                raise
        except:
            print('You are not authorized to use the system.')

        # Gives space between test cases so it's easier to read
        print()
        print()


def main():
    authentication()


if __name__ == '__main__':
    main()
