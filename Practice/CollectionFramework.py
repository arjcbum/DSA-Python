# Lists -

# Ordered collection of items.
# Mutable (can be modified after creation).
# Created using square brackets.
# Lists in Python are dynamic arrays.
# They support indexing, slicing, and various operations like append, pop, extend, etc.
# List comprehensions provide a concise way to create lists.

print("List:")

my_list = [1, 2, 3, 4, 5]
print(my_list)

my_list.append(6)
print(my_list)

my_list.extend([7, 8])
print(my_list)

my_list.insert(2, 10)
print(my_list)

my_list.remove(3)
print(my_list)

popped_value = my_list.pop(1)
print(popped_value)

index_of_four = my_list.index(4)
print(index_of_four)

count_of_five = my_list.count(5)
print(count_of_five)

my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)


# Tuples:

# Similar to lists but immutable.
# Created using parentheses.
# Useful for representing fixed collections of items.

print("Tuples:")

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

index_of_four = my_tuple.index(4)
print(index_of_four)

count_of_five = my_tuple.count(5)
print(count_of_five)


# Sets:

# Unordered collections of unique elements.
# Supports set operations like union, intersection, and difference.
# Mutable.
# Created using curly braces or the set() constructor.

print("Sets:")
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

my_set.remove(3)
print(my_set)

my_set.discard(4)
print(my_set)

popped_value = my_set.pop()
print(popped_value)

union_set = my_set.union({4, 5, 6})
print(union_set)
print(my_set)

intersection_set = my_set.intersection({4, 5, 6})
print(intersection_set)

difference_set = my_set.difference({4, 5, 6})
print(difference_set)


# Dictionaries:

# Key-value pairs.
# Efficient lookups using keys.
# Dictionary comprehensions for creating dictionaries.

print("Dictionaries:")
my_dict = {'one': 1, 'two': 2, 'three': 3}
print(my_dict)

all_keys = my_dict.keys()
print(all_keys)

all_values = my_dict.values()
print(all_values)

all_items = my_dict.items()
print(all_items)

value_for_key = my_dict.get('two', 0)
print(value_for_key)

popped_value = my_dict.pop('three')
print(popped_value)

my_dict.update({'four': 4, 'five': 5})
print(my_dict)
