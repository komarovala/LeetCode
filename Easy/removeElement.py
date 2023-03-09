# https://leetcode.com/problems/remove-element/
#O(n)

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


# i = len(nums) - 1
# for j in range(len(nums)):
#     print(i, j, nums, nums[i - j])
#     if nums[i - j] == val:
#         nums.pop(i - j)
#
# print(nums)


def removelement(nums, val):
    num = nums
    i = len(num) - 1
    for j in range(len(num)):
        if num[i - j] == val:
            num.pop(i - j)
    return num


removelement(nums, val)
