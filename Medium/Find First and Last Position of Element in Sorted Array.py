# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
nums = [5,7,7,8,8,10]
target = 6


def searchRange(nums, target):
    l = 0
    r = len(nums)
    while (r - l) > 1:
        m = (r + l) // 2
        if nums[m] < target:
            l = m
        else:
            r = m
    return l + 1, r + 1

print(searchRange(nums, target))
