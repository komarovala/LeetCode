N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))
l = 0
r = len(nums)
x = 0
while r - l > 1:
    mid = (l + r) // 2
    diff = 0
    if nums[mid] > min(nums):
        diff = nums[mid] - min(nums)
        nums[mid] = nums[mid] - diff
        x += diff
        l = mid
    else:
        r = mid

print(max(max(nums), x), x)