# start

def search(a, target):
    # alternate solution - cuts down time by removing flag
    # ans = "Not Found"
    not_found = True

    for val in a:
        if val == target:
            print("Found")
            not_found = False
            # ans = "Found"
            break
    
    # print(ans)
    if not_found:
        print("Not Found")

def add_pairs(a):
    left = 0
    right = len(a)-1

    while left < right:
        print(a[left] + a[right])
        left = left + 1
        right = right - 1

        if a[left] == a[right]:
            print(a[left])

def binary_search(a, target):
    answer = "not found"
    val1 = 0
    val2 = len(a)

    for num in a:
        mid = (val2+val1)//2

        if a[mid] > target:
            val2 = mid
        elif a[mid] < target:
            val1 = mid
        else:
            answer = "found"
            break

    print(answer)



# this is to test the search function
a = [1, 3, 5, 7, 11, 15, 23]
target = 3

binary_search(a, target)
