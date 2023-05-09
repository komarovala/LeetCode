# https://leetcode.com/problems/running-sum-of-1d-array/

nums = [1, 1, 1, 1, 1]


def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i - 1]
    return nums


print(nums)
