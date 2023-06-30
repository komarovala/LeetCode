# https://leetcode.com/problems/search-in-rotated-sorted-array/
nums = [4,5,6,7,0,1,2]
target = 0


# def search(nums, target) -> int:
#     def find_rotated_num(nums):
#         l = 0
#         r = len(nums) - 1
#         while l + 1 < r:
#             median = (l + r) // 2
#             if nums[l] > nums[median]:
#                 r = median
#             else:
#                 l = median
#
#         if nums[l] > nums[r]:
#             return l
#         else:
#             return r
#
#     if len(nums) == 1 and nums[0] == target:
#         return 0
#     elif len(nums) == 1 and nums[0] != target:
#         return -1
#     else:
#         rot_index = find_rotated_num(nums)
#         if (nums[rot_index] >= target) and (nums[0] <= target):
#             start = 0
#             end = rot_index
#         else:
#             start = rot_index + 1
#             end = len(nums) - 1
#
#         while start <= end:
#             if (start == end) and (nums[start] == target):
#                 return start
#             elif (start == end) and (nums[start] != target):
#                 return -1
#             else:
#                 median = (start + end) // 2
#
#                 if nums[median] == target:
#                     return (median)
#                 elif nums[median] > target:
#                     end -= 1
#                 else:
#                     start += 1
#     return -1
#

def search(nums, target) -> int:
    l = 0
    r = len(nums)

    while (r - l) > 1:
        m = (r + l) // 2
        if (nums[m] > target) and (nums[m] > nums[0]):
            r = m
        else:
            l = m

    return l


print(search(nums, target))
