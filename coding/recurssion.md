# Recursion
## Work 1

<p>This is an explanation of the recursion algorithm found below.</p>

```
def my_func(n):
    if n == 0:
        return 1

    return n * my_func(n-1)
```

<p>The above formula can be used for things such as a factoral mahcine, etc.</p>

<p>The input we use is seen below.</p>

```
my_func(5)
```

<p>If we add in 5 in place of n we get the following result.</p>

```
def my_func(5):
    if 5 == 0:
        return 1
        # This is not true so does not carry out

    return 5 * my_func(5-1)
    # We now iterate the same function again but with n (5) minus 1 (4)
```

Initially we check to see if n equals to 0, which it doesn't, and then we pass to the next part of the function. This part returns our value of 5 times my_func(4). We now need to go back into the function but replace n with 4 to find the result.

```
def my_func(4):
    if 4 == 0:
        return 1
        # This is not true so does not carry out

    return 4 * my_func(4-1)
    # This now carries out a function in a function and will keep doing this till n - 1 equals to 0
```

In the end we get the final result and go back through al the functions we went through, finding the result:

```
# We start with the lowest n we can have, which is 1
my_func(1) = 1
my_func(2) = 2 * my_func(1) = 2
my_func(3) = 3 * my_func(2) = 6
my_func(4) = 4 * my_func(3) = 24
my_func(5) = 5 * my_func(4) = 120
```

The past results keep getting used int he next results.

## Work 2

<p>The next formula is as follows:</p>

```
def my_func(n):
    if n == 0:
        return
    print(n)
    my_func(n-1)
```

<p>The n and results will be as follows.</p>

```
my_func(4) = 4
my_func(3) = 3
my_func(2) = 2
my_func(1) = 1
```

## Work 3

```
def my_func(n):
    if n == 0:
        return
    print(n)
    my_func(n-1)
    print(n)
```

<p>The n and results are as follows.</p>

```
my_func(4) = 4, my_func(3), n
my_func(3) = 3, my_func(2), n
my_func(2) = 2, my_func(1), n
my_func(1) = 1, my_func(0), n
```

<p>This round two where we go back and get the ns from the last function.</p>

```
my_func(1) = n = 1
my_func(2) = n = 2
my_func(3) = n = 3
my_func(4) = n = 4
```

<p>The result of this will look like...</p>

```
4
3
2
1
1
2
3
4
```