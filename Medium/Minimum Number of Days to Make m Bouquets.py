# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

l = 1
r = max(bloomDay)

while (r - l) > 1:
    mid = (l + r) // 2
    left = 0
    right = 0
    bouquet = 0
    cnt = 0
    while right < len(bloomDay):
        if bouquet >= k:
            cnt += 1
        if bloomDay[right] <= mid:
            bouquet += 1
        else:
            left = right
            bouquet = 0
        right += 1

    if bouquet >= k:
        cnt += 1

    if cnt >= m:
        r = mid
    else:
        l = mid
    cnt = 0

print(l, r)
