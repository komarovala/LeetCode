#https://informatics.msk.ru/mod/statements/view.php?id=63548&chapterid=112560#1
nums = "2 4 2 3 3 1"
#nums = "1 2 1 3 2"
nums = "".join(nums.split())
l, r = 0, 0
dic = {}
N, K = 6, 4
cnt, left, right = 0, 0, 0

while r < len(nums) + 1:
    if len(dic) == K:
        left, right = l, r
        dic[nums[l]] -= 1
        if dic[nums[l]] < 1:
            del dic[nums[l]]
        l += 1
    else:
        if nums[r] not in dic:
            dic[nums[r]] = 1
        else:
            dic[nums[r]] += 1
        r += 1

print(l, r, left, right)
