l = [7, 2, 5, 4, 6]
n = len(l)

# -- bubble sort --
def bubble_sort(n, l):
    for i in range(n):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l

# -- selection sort --
def selection_sort(n, l):
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l

# -- insertion sort --
def insertion_sort(n, l):
    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] > key:
            l[j + 1] = l[j]
            j = j - 1
        
        l[j + 1] = key

    return l

print(insertion_sort(n, l))

# -- task --
# a = ["Bikram", "Josh", "Vitor", "Helloss"]
# n = len(a)

# for i in range(n):
#     for j in range(i + 1, n):
#         if len(a[i]) > len(a[j]):
#             a[i], a[j] = a[j], a[i]

# print(a)
