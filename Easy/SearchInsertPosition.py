# https://leetcode.com/problems/search-insert-position/

nums = [1, 3, 6]
target = 5


# O(n)
def search(nums, target):
    for i, n in enumerate(nums):
        if n == target:
            return i
    return 'No'


search(nums, target)


