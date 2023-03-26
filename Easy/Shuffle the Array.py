# https://leetcode.com/problems/shuffle-the-array/
nums = [2, 5, 1, 3, 4, 7]
n = 3


def shuffle(nums, n):
    nums2 = [list(i) for i in zip(nums, nums[n:])]
    return sum(nums2, [])


shuffle(nums, n)
