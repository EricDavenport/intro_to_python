x = 4
while (x < 20):
    x = 2 * x
    print(x)
    
inp = input('Hi!, Please say hello')

while inp != 'Hello':
    inp = input('Please say hello again!')

print('it\'s about time')


# before watching
# password = input('Please enter secret password: ')

# while password != 'secret':
#    password = input('Sorry, the password you entered in incorrect, Please try again: ')

# print('Welcome!')

# They way shown
password = ""
while password != 'secret':

    password = input('Please enter the password.')
    if password == 'secret':
        print('Welcome!')
    else:
        print('Sorry, the password you enter is incorrect. Please try again.')
