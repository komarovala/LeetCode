# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

nums = [1, 2, 1]


def search(nums, target):
    l, r = 0, len(nums) - 1

    if len(nums) < 3:
        for n in nums:
            if n == target:
                return True
    else:
        while l < r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target and target < nums[mid]:
                    l = mid - 1
                else:
                    r = mid + 1
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

    return False


print(search(nums, 0))
