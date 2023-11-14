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

print(isPrime(49))  
