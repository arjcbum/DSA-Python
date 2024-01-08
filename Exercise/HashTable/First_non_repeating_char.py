# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################
def first_non_repeating_char(nString):
    myDict = {}
    for i in nString:
        myDict[i] = myDict.get(i, 0) + 1
    for j in myDict.items():
        if j[1] == 1:
            return j[0]
    return None


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""