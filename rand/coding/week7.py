l = [7, 2, 5, 4, 6]
n = len(l)


# -- bubble sort --
# for i in range(n):
#     for j in range(n - i - 1):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]


# -- selection sort --
# for i in range(n):
#     for j in range(i + 1, n):
#         if l[i] > l[j]:
#             l[i], l[j] = l[j], l[i]


# -- insertion sort --
# for i in range(1, n):
#     key = l[i]
#     j = i - 1
    
#     while j >= 0 and l[j] > key:
#         l[j + 1] = l[j]
#         j = j - 1
    
#     l[j + 1] = key

# print(l)


# -- task --
a = ["Bikram", "Josh", "Vitor", "Helloss"]
n = len(a)

for i in range(n):
    for j in range(i + 1, n):
        if len(a[i]) > len(a[j]):
            a[i], a[j] = a[j], a[i]

print(a)
