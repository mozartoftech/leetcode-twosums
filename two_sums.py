print("")

def two_sums(nums, target):

    nums_dict = {} # stores the element and the indices in the nums list as key-value pairs respectively.

    for i, num in enumerate(nums):
        complement = target - num # the complement is needed to reach the target sum

        if complement in nums_dict: 
            return [nums_dict[complement], i] 

        nums_dict[num] = i # this will return if the 

    return []

nums = [2, 3, 4, 5]
target = 7

print(two_sums(nums, target))