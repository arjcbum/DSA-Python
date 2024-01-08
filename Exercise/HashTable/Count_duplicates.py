# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################
from collections import defaultdict

# def find_duplicates(myList):
#     myDict = defaultdict(int)
#     myResult = []
#     for i in myList:
#         myDict[i] += 1
#     for j in myDict.items():
#         if j[1] > 1:
#             myResult.append(j[0])
#     return myResult

def find_duplicates(myList):
    myDict = {}
    for i in myList:
        myDict[i] = myDict.get(i,0) + 1
    myResult = [i for i, count in myDict.items() if count > 1]
    return myResult


print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

