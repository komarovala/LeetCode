# https://leetcode.com/problems/build-array-from-permutation/
# O(n)

nums = [0, 2, 1, 5, 3, 4]


def permutated_array(nums):
    nums_new = []
    for i in range(len(nums)):
        nums_new.append(nums[nums[i]])

    return print(nums_new)


permutated_array(nums)
