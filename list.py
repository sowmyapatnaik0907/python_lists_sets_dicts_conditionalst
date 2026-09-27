# 1. List Creation

age_list = [24, 25, 26, 27, 28]

name_list = ["Sowmya", "Parimala", "Ramya", "Janani", "Swathi"]

print("Original age list:", age_list)
print("Original name list:", name_list)


# 2. List Operations / Modifications

# a. Append Yazhini
name_list.append("Yazhini")
print("After append:", name_list)

# b. Insert 30 at index 2
age_list.insert(2, 30)
print("After inserting 30:", age_list)

# c. Remove Yazhini
name_list.remove("Yazhini")
print("After removing Yazhini:", name_list)

# d. Pop the last element
age_list.pop()
print("After popping last element:", age_list)

# e. Extend age_list
age_list.extend([29, 30, 26])
print("After extending:", age_list)

# f. Sort in descending order
age_list.sort(reverse=True)
print("Descending order:", age_list)

# g. Find maximum, minimum and sum
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of all ages:", sum(age_list))


# 3. Accessing List Elements

# a. First element
print("First name:", name_list[0])

# b. Last element
print("Last name:", name_list[-1])

# c. Index 2 to index 4
print("Index 2 to 4:", name_list[2:5])

# d. Reverse order
print("Reverse order:", name_list[::-1])