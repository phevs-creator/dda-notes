# start

def area_cyl(r, h):
    area = (2*3.14*r*h) + (2*3.14*(r**2))
    return area

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
        left = left + 1
        right = right - 1

        if a[left] == a[right]:
            print(a[left])

def middle(val1, val2):
    mid = (val2+val1)//2
    return mid

def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    mid = 1

    ans = -1

    while left <= right:
        mid = (right + left)//2

        if nums[mid] == target:
            ans = mid
            break
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    
    return ans


# this is to test the search function
# w = [1, 3, 5, 7, 8, 10, 11, 15, 23, 54, 101, 102]
a = [-1,0,3,5,9,12]
target = 9

# print(binary_search(a, target))
print(binary_search(a, target))
