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
        (for obvious reasons the list of factors being considered does not
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

    # iterate through the givven range beginning at 1
    for num in range(1, x):
        # if the number is a factor is the given x -> add the value to the pn(perfect number)
        if x % num == 0:
            pn += num
    #  if the pn is equal to the given x return True else False
    if pn ==  x:
        return True
    else:
        return False


# print(isPerfect(3))

def isAbundant(x):
    """Returns whether ornot the given number x is abundant.

    A number is considered to be abundant if the sum of its factors (aside from
    the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors is 1 + 3 + 5 + 9 is not abundant.
    """

    # your code here
    # keep track of the factor total
    total = 0

    # iterate from 1 to the number before the given x
    for num in range(1, x):
        # if the number is a mod of the given value(divided evenly into x)
        if x % num == 0:
            #  add it to the total
            total += num
            # check if the total went over the given x
            if total > x:
                return True

    if total > x:
        return True
    else:
        return False

# print(isAbundant(72))
import math

def isTriangle(x):
    """Returns whether or not a given numbrer x is triangle

    The triangle number Tn is a number that can be represented in the form
    of a triangular grid of points where the first row contains a single element
    and each subsequent row contains one more element than the previous

    We canjust use the fact that the nth triangular number can be found by using the formula:
    Tn = n(n + 1) / 2

    Example: 3 is a triangle number since 3 = 2(3) / 2
    3 ---> 2nd position (2 * 3 / 2)

    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position (5 * 6 / 2)
    """
    if x < 0:
        return False
    n = int((-1 + (1 + 8 * x) ** 0.5) / 2)

    return n * (n + 1) // 2 == x
    # a, b = 1, 1
    # c = ( -2 * x)
    # d = (b * b) - (4 * a * c)

    #    if d < 0:
    #        return False

    # find the roots of the equation
    # root1 = ( -b + math.sqrt(d)) / (2 * a)
    # root2 = ( -b - math.sqrt(d)) / (2 * a)

    # if root1 > 0 and math.floor(root1) == root1:
    #     return True

    # if root2 > 0 and math.floor(root2) == root2:
    #     return True

print(isTriangle(232))


