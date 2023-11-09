# Prompt the user for their first name
name = input('What is your first name? ')
letter_count = 0

print(name, 'is spelled:')

# using a for loop
for letter in name:
    #  Print each letter of the name (on the same line)
    print(letter, end = ' ')

    #  Count each letter in the name
    letter_count += 1

print("")
# print the count of letters in the name
print(letter_count, 'letters in  the name', name)
