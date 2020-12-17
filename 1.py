

def E2(a):
   return a%2==0
print(list(
filter(E2, [1, 500, 6, 4, 7])))


frrom functools import reduce
def E3(a, b):
    c = a + b
    return c
print(
reduce(E3,[23, 2, 3],1))