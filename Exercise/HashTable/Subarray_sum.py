# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
# def subarray_sum(nums, target):
#     sum_index = {0: -1}
#     current_sum = 0
#     for i, num in enumerate(nums):
#         current_sum += num
#         if current_sum - target in sum_index:
#             return [sum_index[current_sum - target] + 1, i]
#         sum_index[current_sum] = i
#     return []

def subarray_sum(nums, target):
    left = 0
    right = len(nums)-1
    nSum = 0
    totalS = 0
    for i in nums:
        totalS += i
    while left <= right:
        if totalS == target:
            return [left,right]
        elif totalS-nums[right]>=target:
            totalS -= nums[right]
            right -= 1
        elif totalS-nums[left]>=target:
            totalS -= nums[left]
            left += 1
        else:
            break
    return []



nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
