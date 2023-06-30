nums = [1, 2, 3, 1]


def findPeakElement(nums) -> int:
    l = 0
    r = len(nums)
    while r - l > 1:
        m = (l + r) // 2
        if nums[m] > nums[m - 1]:
            l = m
        else:
            r = m

    return l

print(findPeakElement(nums))
