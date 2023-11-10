# write a program that ask the user for numbers(ints).
#   it computes the average of the numbers.
#   Allows the user to enter -1 to quit the program

#list to hold the numbers
num_list = []
# count for the list
i = 0
# flag to indicate it is waitting for user input
playing = True

while (playing == True):

    num = int(input('Enter an int: '))
    if (num == -1):
        playing = False
    else:
        # add numbers to the list of numbers
        num_list.append(num)
        i += 1

#get the sum of all entered numbers
num_sum = 0
for num in num_list:
        num_sum += num

#calculate the average
        num_avg = num_sum / i

print('avg: ', num_avg)
