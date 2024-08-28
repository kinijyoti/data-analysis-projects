my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

modified_string = my_string[3:] + my_string [:3]
print(modified_string)

# Use a template literal to print the original and modified string in a descriptive phrase.
modified_string = my_string[3:]
print(f"The original string was {my_string}, and after removing the first three characters, it becomes '{modified_string}")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
number_of_letters = int(input("Enter the number of letters that will be relocated: "))
modified_string = my_string [number_of_letters:]
print(f"The original string was {my_string}, and after removing the first three characters, it becomes '{modified_string}")


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
num_letter = int(input("Enter the number of letters that will be relocated: "))
if num_letter > len(my_string):
    print(f"error: The number of letters to remove ({num_letter})is greater than the length of the string ({len(my_string)}). Defaulting to 3 characters.")
else:
    modified_string = my_string [num_letter:]
    print(f"The original string was {my_string}, and after removing the first three characters, it becomes '{modified_string}")
