# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################
def longest_consecutive_sequence(arr):
    nSet = set(arr)
    max_count = 0
    for val in nSet:
        complement = val - 1
        count=1
        while complement in nSet:
            count += 1
            complement -= 1
        max_count = max(count, max_count)
    return max_count


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""