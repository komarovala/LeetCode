# https://leetcode.com/problems/3sum/
# nums = [-1,0,1,2,-1,-4]
nums = [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]


def threeSum(nums):
    nums = sorted(nums)
    f = 0
    l = 1
    r = len(nums) - 1
    out = {}
    while f < len(nums) - 2:
        while l < r:
            if nums[f] + nums[l] + nums[r] == 0:
                if frozenset({f, l, r}) not in out:
                    out[frozenset({nums[f], nums[l], nums[r]})] = frozenset({f, l, r})
                r -= 1
            elif nums[f] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                l += 1
        f += 1
        l = f + 1

    lst = [list(x) for x in out.values()]

    return [[nums[number] for number in group] for group in lst]


print(threeSum(nums))
