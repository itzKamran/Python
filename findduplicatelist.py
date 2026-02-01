
#Find Duplicate Elements in a List

lst = [1, 2, 3, 2, 4, 5, 1]
duplicates = set([x for x in lst if lst.count(x) > 1])
print(duplicates)
