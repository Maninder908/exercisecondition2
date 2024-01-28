def cruise_ship_description(cabin_class):
    if cabin_class == "LUX":
        description = "Upper-deck cabin with a balcony."
    elif cabin_class == "A":
        description = "Above the car deck, equipped with a window."
    elif cabin_class == "B":
        description = "Windowless cabin above the car deck."
    elif cabin_class == "C":
        description = "Windowless cabin below the car deck."
    else:
        description = "Invalid cabin class."

    return description

# Get user input
user_input = input("Enter the cabin class of the cruise ship (LUX, A, B, C): ").upper()

# Print the description based on the user input
print(cruise_ship_description(user_input))
