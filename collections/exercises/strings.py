# ---- Exercise 2: Bracket Notation Basics ----

text = 'Strings_are_sequences_of_characters.'
word = 'tomato'

# 1. Print a slice of the first 12 characters from 'text'.
new_string = text[0:13]
print(new_string)

# 2. Print a slice of the last 12 characters from 'text'. You should NOT have to count the index values yourself!
new_string = text[-12:]
print(new_string)

# 3. Print a slice of the middle 12 characters from 'text'.
middle_start = len(text) - 12
middle_end = middle_start + 12
print(text[middle_start : middle_end])

# ---- Exercise 3: Looping Through a String ----

# Use index values to loop backwards through 'word'.

# 1. Print 1 letter per line.
for letter in word:
    print(letter)

# 2. Refactor the code to use the accumulator pattern to build up and print the reversed string. For example, if given 'good', print 'doog' on one line.
reverse = ''
for item in word:
    reverse = item + reverse
print(reverse)

# 3. Refactor the code to print a combination of the original and reversed string. For example, given 'tomato', print 'tomatootamot'. (If you want to be fancy, print 'tomato | otamot').
reverse = ''
for item in word:
    reverse = item + reverse
print(word,reverse)
