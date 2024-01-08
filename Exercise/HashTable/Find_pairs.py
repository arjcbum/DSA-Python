# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def find_pairs(arr1, arr2, target):
    myResult = []
    for a1 in arr1:
        complement = target-a1
        if complement in arr2:
            myResult.append((a1, complement))
    return myResult


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""