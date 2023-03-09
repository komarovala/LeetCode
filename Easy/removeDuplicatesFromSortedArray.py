# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# O(n)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums: List[int]) -> int:
    i = len(nums) - 1
    cnt = len(nums)

    while i > 0:
        if nums[i] == nums[i - 1]:
            nums.pop(i)
            nums.append('-')
            i -= 1
            cnt -= 1
        else:
            i -= 1
    return cnt