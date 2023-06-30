# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

def findMaxK(nums) -> int:
    l = 0
    maxK = 0
    nums = sorted(nums)
    while (l<= len(nums)- 1) and (nums[l] < 0):
        if abs(nums[l]) in nums and maxK < abs(nums[l]):
            maxK = abs(nums[l])
        l += 1
    return maxK

print(findMaxK([-1]))