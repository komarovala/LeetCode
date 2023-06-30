# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# O(n)
from typing import List


# решение за O(n^2)
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


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4, 4, 4]
num = 0
val = None
j = 0
for i, n in enumerate(nums):
    if n == val:
        continue
    else:
        nums[j] = nums[i]
        num += 1
        j += 1
    val = n
print(num, nums[0:num])

def removeDuplicates(nums) -> int:
    l = 0
    r = 0

    while r <= len(nums) - 1:
        if nums[l] == nums[r]:
            r += 1
        else:
            l += 1
            nums[l] = nums[r]
            r += 1

    return nums[0:l+1]


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 4, 4, 4]))

