frrom functools import reduce
def E3(a, b):
    c = a + b
    return c
print(
reduce(E3,[23, 2, 3],1))