
# -- function called in function --
def adding(x, y):
    z = x + y
    return z

def dividing(x, y, z):
    sum = adding(x, y) / z
    return sum

# print(dividing(2, 7, 2))


# -- recursion in functions --
def counter(n):
    if n == 0:
        return
    
    print(n)

    counter(n - 1)

# counter(10)


# -- recursion advanced (factorial machine) --
def cu(n):
    if n == 0:
        return 1
    return n * cu(n-1)

print(cu(23))
