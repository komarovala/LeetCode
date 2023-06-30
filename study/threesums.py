nums = [2, 1, 3, 4, 5]
target = 10
l, r = 0, len(nums) - 1

cur = None
nums.sort()
print(nums)
for i, n in enumerate(nums):
    cur = n
    l, r = i + 1, len(nums) - 1
    while l < r:
        if cur + nums[l] + nums[r] > target:
            r -= 1
        elif cur + nums[l] + nums[r] == target:
            print(cur, nums[l], nums[r])
            break
        else:
            l += 1

