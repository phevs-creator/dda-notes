def my_func(n):
    if n == 0:
        return
    
    print(n)
    my_func(n-1)

def my_func1(n):
    if n == 0:
        return
    
    print(n)
    my_func1(n-1)
    print(n)

def my_func2(n):
    if n == 0 or n == 1:
        return n
    
    return my_func2(n-1) + my_func2(n-2)

print(my_func2(4))
