def insertion_sort(myList):
    for i in range(1, len(myList)):
        temp = myList[i]
        j = i - 1
        while myList[j] > myList[j + 1] and j > -1:
            myList[j + 1] = myList[j]
            myList[j] = temp
            j -= 1
    return myList


print(insertion_sort([4, 2, 6, 5, 1, 3]))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]

 """

