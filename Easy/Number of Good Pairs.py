# https://leetcode.com/problems/number-of-good-pairs/

nums = [1, 2, 3, 1, 1, 3]


def good_pairs(nums):
    cnt = 0
    for i, n in enumerate(nums):
        j = i + 1
        while j < (len(nums)):
            if (n == nums[j]) and i < j:
                cnt += 1
            j += 1
    return cnt


print(good_pairs(nums))

