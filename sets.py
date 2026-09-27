# 1. Create a set

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My set:", my_set)


# 2. Attempt to change a set element

try:
    my_set[4] = 's'
except TypeError:
    print("Error: Sets do not support indexing or item assignment.")


# 3. Create two sets

set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}


# 4. Union

union_result = set1.union(set2)

print("Union:", union_result)


# 5. Intersection

intersection_result = set1.intersection(set2)

print("Intersection:", intersection_result)