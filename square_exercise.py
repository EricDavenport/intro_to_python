def square(x):
    y = x * x
    return y

result = square(10)
print(result)

def greater_than(x, y):
    if (x > y):
        return True
    else:
        return False


a = 2
b = 3
result = greater_than(a, b)
print('{} is greater than {}: {}'.format(a, b, result))
