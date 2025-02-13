
# 1. Name:
#      Brodric Young

# 2. Assignment Name:
#      Lab 04: Monopoly

# 3. Assignment Description:
#      Deterimine if the player can place a hotel on Pennsylvania Avenue or not

# 4. What was the hardest part? Be as specific as possible.
#      The hardest part of this was trying to figure out how to run through all
#       the test cases very quickly while also not having to put in a lot of extra
#       work. Everything else was easy after making the flowcharts already.

# 5. How long did it take for you to complete the assignment?
#      About 2 hours.


# Determines if user owns all green properties
all_color_group = input("Do you own all the green properties? (y/n) ")
if all_color_group == "y":
    
    # Determines if there's a hotel or a number of houses on Pennsylvania Ave
    pa = int(input("What is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
    if pa < 5:
        
        # Determines if there's a hotel or a number of houses on N Carolina
        nc = int(input("What is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
        if nc < 5:

            # Determins if there's a hotel or a number of houses on Pacific Ave
            pc = int(input("What is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel) "))
            if pc < 5:

                # Determins if there's at least one hotel available
                num_hotels = int(input("How many hotels are there to purchase? "))
                if num_hotels > 0:

                    # Calculates how many houses each property needs, total needed houses, and total cash needed
                    houses_pa_need = 4 - pa
                    houses_nc_need = 4 - nc
                    houses_pc_need = 4 - pc
                    total_needed_houses = houses_pa_need + houses_nc_need + houses_pc_need
                    total_cash_needed = (total_needed_houses + 1) * 200

                    # Determines if user has enough cash to purchase everything needed
                    cash = int(input("How much cash do you have to spend? "))
                    if cash >= total_cash_needed:

                        # Determines if theres enough houses for whats needed
                        num_houses = int(input("How many houses are there to purchase? "))
                        if num_houses >= total_needed_houses:

                            # Displays the total cost, amount of houses to purchase, and to put a hotel on Pennsylvania Ave
                            print()
                            print(f"This will cost ${total_cash_needed}")
                            print(f"     Purchase 1 hotel and {total_needed_houses} house(s).")
                            print("     Put 1 hotel on Pennsylvania and return any houses to the bank.")

                            # Displays how many houses to put on NC and Pacific if they need any
                            if houses_nc_need > 0:
                                print(f"     Put {houses_nc_need} house(s) on North Carolina.")
                            if houses_pc_need > 0:
                                print(f"     Put {houses_pc_need} house(s) on Pacific.")

                        else:
                            print("There are not enough houses available for purchase at this time.")
                    else:
                        print("You do not have sufficient funds to purchase a hotel at this time.")
                else:
                    print("There are not enough hotels available for purchase at this time.")
            else:
                print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
        else:
            print("Swap North Carolina's hotel with Pennsylvania's 4 houses.")
    else:
        print("You cannot purchase a hotel if the property already has one.")
else:
    print("You cannot purchase a hotel until you own all the properties of a given color group.")
