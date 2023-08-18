# https://informatics.msk.ru/mod/statements/view.php?id=63550&chapterid=111402#1
# N, K = map(int, input().split())
# print(N, K)
# nums = []
# for i in range(N):
#     nums.append(int(input()))

N, K = 7, 13
nums = [3318,
5775,
7318,
336,
9490,
5712,
2379]

l = 0
r = max(nums)
cnt = 0
while r - l > 1:
    cnt = 0
    mid = (r + l) // 2
    for i in nums:
        cnt += (i // mid)
    if cnt >= K:
        l = mid
    else:
        r = mid
    print(cnt)

print(sum([i // l for i in nums]))

if sum([i // l for i in nums]) < K:
    print(0)
else:
    print(l)
