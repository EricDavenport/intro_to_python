# Define a function unique_list that takes a list of numbers
# as a parameter and returns a new list with the unique values
#   - Create a new empty list
#   - Use a for loop to iterate over the provided list of numbers
#   - Add values to the new list if they don't already exist in the new list
#   -Return the new list

# before code along
# def unique_list(nums):
#    empty_list = []
#    for num in nums:
#        if !empty_list.contains(num):
#            empty_list.append(num)

#   return empty_list

# code along
def unique_list(l):
    """Returns a list of unique values from a given list."""
    x = []

    # iterate of provided list
    for a in l:
        # check if number is in the new list
        if a not in x:
            # add it to the new list
            x.append(a)

    return x

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
