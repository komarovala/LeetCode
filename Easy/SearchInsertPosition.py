# https://leetcode.com/problems/search-insert-position/

nums = [1, 3, 5, 6]
target = 2


# O(n)
def search(nums, target):
    left = 0
    rigth = len(nums) - 1

    while left <= rigth:
        mid = (left + rigth) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            rigth = mid - 1
        else:
            left = mid + 1
    return left


print(search(nums, target))
