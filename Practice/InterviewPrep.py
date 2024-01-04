def print_value(x, *y):
    print('count:', x)
    print([i for i in y])


# # Reading single integer:
# n = int(input().strip())
# print_value(1, n)
#
# # Reading a list of integers:
# n = list(map(int, input().split()))
# print_value(2, n)
#
# # Reading multiple integers on a line:
# a, b = map(int, input().split())
# print_value(3, a, b)
#
# # Reading a string:
# s = input().strip()
# # Formatting  a string:
# print_value(4)
# print(f'The result is : {s}')
#
# Output a list without spaces:
arr = [1, 2, 3, 4]
print_value(5, arr)
print(arr)
print(*arr)

# Sorting a list:
arr = [5, 2, 9, 4]
print_value(6, sorted(arr))

# Sorting a list in descending order:
print_value(7, sorted(arr, reverse=True))

# Soring a list of tuples by second elements:
arr = [(9, 8), (8, 7), (7, 6)]
print_value(8, sorted(arr, key=lambda x: x[1]))

from collections import defaultdict, Counter

# DefaultDic for counting occurrences:
count_dic = defaultdict(int)
count_dic['a'] += 1
count_dic['b'] += 1
count_dic['a'] += 1
print_value(9, list(count_dic.items()))

# Counter for counting occurrence in list:
my_list = [2, 5, 2, 4, 6, 7, 4]
counter = Counter(my_list)
print_value(10, list(counter.items()))

import heapq

# Creating a min-heap:
heap = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(heap)
heapq.heappush(heap, 6)
print_value(11, heapq.heappop(heap))
print_value(12, heapq.nlargest(2, heap))

# Binary Search:
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False


arr = [1, 2, 3, 4, 5, 6, 9]
print_value(13, binary_search(arr, 3))

# Reversing a string:
s = "My name is Abhishek"
print_value(14, s[::-1])

# Joining a list of strings:
my_list = ['good', 'job', '!']
new_str = ' '.join(my_list)
print_value(15, new_str)

# is palindrome?
s = 'owowo'
is_palindrome = s == s[::-1]
print_value(16, is_palindrome)

# Creating a set
my_set = set([1, 2, 3, 4])
print_value(17, my_set)

# Checking membership
is_present = 3 in my_set
print_value(18, is_present)

# Union and intersection of sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
union_set = set1.union(set2)
print_value(19, union_set)
intersection_set = set1.intersection(set2)
print_value(20, intersection_set)