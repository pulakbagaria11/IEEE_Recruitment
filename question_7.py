#define the lists
list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7]
list2 = [5, 8, 2, 9, 9, 4, 6, 3]

#find the intersection without duplicates
intersection = list(set(list1) & set(list2))

#print the result
print("Intersection (no duplicates):", intersection)
