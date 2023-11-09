# define list if numbers
numbers = [5, 3, 8,-1, -2.2, 0]

#define the min number variable
min_number = numbers[0]

#find the minimum value
for number in numbers:
    if number < min_number:
        min_number = number

print(min_number, 'is the min number in the list')
