# https://leetcode.com/problems/friends-of-appropriate-ages/
ages = [16, 16]
l = 0
r = len(ages) - 1
cnt = 0
while r > l:
    if (ages[r] > (ages[l]//2) + 7):
        cnt += 1
        r -= 1
    else:
        l += 1

print(cnt)