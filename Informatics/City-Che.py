#https://informatics.msk.ru/mod/statements/view.php?id=63548&chapterid=111975#1
left = 0
right = 0
r = 5
nums = "1 4 5 6 10 13 20"
#nums = "1 3 5 8"
nums = [int(x) for x in nums.split()]
print(nums)
cnt = 0
while right < len(nums):
    if (nums[right] - nums[left]) < r:
        right += 1
    else:
        cnt += 1
        left += 1

print(left, right, cnt)
