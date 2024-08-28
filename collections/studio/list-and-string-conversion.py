proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for each_string in strings:
    if "," in each_string:
        separator = ","
    elif ";" in each_string:
        separator = ";"
    elif " " in each_string:
        separator = " "
    else:
        separator = "nothing has separator"
    print(f"{each_string} has {separator} separator")



# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for each_string in strings:
    if "," in each_string:
        words_array = each_string.split(",")
    # Reverse the array
        words_array.reverse()
    # Join the array back into a new comma-separated string
        modified_string = ",".join(words_array)
        print(modified_string)

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for each_string in strings:
    if ";" in each_string:
        words_array = each_string.split(";")
    # Reverse the array
        words_array.sort()
    # Join the array back into a new comma-separated string
        modified_string = ",".join(words_array)
        print(modified_string)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
for each_string in strings:
    if " " in each_string:
        words_array = each_string.split(" ")
    # Reverse the array
        words_array.sort()
        words_array.reverse()
    # Join the array back into a new comma-separated string
        modified_string = ",".join(words_array)
        print(modified_string)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for each_string in strings:
    if ", " in each_string:
        words_array = each_string.split(", ")
    # Reverse the array
        words_array.reverse()
    # Join the array back into a new comma-separated string
        modified_string = ",".join(words_array)
        print(modified_string)