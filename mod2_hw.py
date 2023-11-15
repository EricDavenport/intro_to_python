def getFactors(x):
    """Returns a list of factors of the given number x.
       Basically finds the numbers between 1 and the given integer that divide the number evenly.

       for example:
       - If we call getFactors(2), we'll get [1, 2] in return
       - If we call getFactors(12), we''ll get [1, 2, 3, 4, 6, 12] in return
       """

    # your code here
    factors = []

    for num in range(1, x + 1):
        if x % num == 0:
            factors.append(num)

    print(factors)


# getFactors(12)

def isPrime(x):
    """Returns whether or not the given number x is a prime number or not.
       A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.

       For example:
       - Calling isPrime(11) will return True
       - Calling isPrime(71) will return True
       - Calling isPrime(12) will return False
       - Calling isPrime(76) will return False
    """
    
    # your code here
    for num in range(2, x):
        print(num)
        if x % num == 0:
            return False

    return True

# print(isPrime(49))

def isComposite(x):
    """Returns whether or not the given number x is composite

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a
        composite number
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """

    # Keep track of the amount of factors the number has 
    factors = 0

    # iterate beginning with the number 2
    for num in range(1, x + 1):
        # if the number we are looking at divides evenly into the give x
        if x % num == 0:
            print(num)
            # increase the amount of factors tracker
            factors += 1
        # if the factors goes over 2 -> return True, 3+ facotrs for the given x
        if factors > 2:
            return True

    print(factors)
    # return False since the factors count is less than 3
    return False

# print(isComposite(79))


def isPerfect(x):
    """Returns whether or not the given number x is perfet

    A number is said to be perfect if it is equal to the sum of all its factors
        (for obvious reasons the list of factors beign considered does now
        include the number itself

    Example: 6 + 3 + 2 + 1, hence 6 is perfect.
    Exaample: 28 is another example since 1 + 2+ 4 + 7 + 14 is 28
    Note, the number 1 is not a perfect number
    """
    pn = 0
    # your code here
    # since 1 is not a Perfect number == return false if given
    if x == 1:
        return False

    # iterate through the givven range beginning at
    for num in range(1, x):
        print(num)
        if x % num == 0:
            pn += num

    if pn ==  x:
        return True
    else:
        return False


print(isPerfect(3))
