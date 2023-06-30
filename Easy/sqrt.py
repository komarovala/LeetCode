#https://leetcode.com/problems/sqrtx/
x = 4
l = 0
r = x + 1
target = x
while (r - l) > 1:
    m = (r + l) // 2
    if (m*m) <= target:
        l = m
    else:
        r = m

print(l,r)