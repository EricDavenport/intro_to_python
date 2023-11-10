# exit a while loop
x = 1
while x <= 10:
    if x == 5:
        break  # this will break out of the loop immediately

    print(x)
    x += 1

# exit a loop using continue
for number in range(1, 21):

    #test for odd numbers
    if (number % 2 != 0):

        #test for multiple of 3
        if (number % 3 == 0):
            continue

        print(number)
# nested loopp is a loop within a loop
for i in range(1, 4):
    print('i:', i)
    for j in range(1, 3):
        print('\t', 'j:', j)
