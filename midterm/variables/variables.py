lst1 = [1, [2, 3], 4]
lst2 = [5, [6, 7, 7]]
lst1.extend(lst2)
lst2.append(10)
print("1: " + str(lst1))
# [1, [2,3], 4, 5, [6,7,7]]

lst2[0] = 15
# [15, [6, 7, 7], 10]
print("2: " + str(lst1))
# [1, [2,3], 4, 5, [6,7,7]]

lst2[1].append(100)
# [15, [6, 7, 7, 100], 10]
print("3: " + str(lst1))



# lst1.append(99)
# print(lst1)


# print(lst2)


# lst1[3] = 25
# print(lst1)


# print(lst2)


# lst1[4][1] = 1001
# print(lst1)


# print(lst2)