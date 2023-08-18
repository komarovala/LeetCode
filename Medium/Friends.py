# https://leetcode.com/problems/friends-of-appropriate-ages/
ages = [16, 17, 18]

l = 0
r = len(ages) - 1
cnt = 0

while l < r:
    if ages[l] > 0.5 * ages[r] + 7:
        cnt += 1
    else:
        l += 1

print(cnt)

#
# def binary_search(nums, x):
#     l = 0
#     r = len(nums) - 1
#     while r - l > 1:
#         mid = (r + l) // 2
#         if ages[mid] > 0.5 * x + 7:
#             r -= 1
#         else:
#             l += 1
#     return r
#
#
# print(ages[::-1])
# ages = ages[::-1]
# for n, i in enumerate(ages[:-1]):
#     print(n, i, ages[n:])
#     print(binary_search(ages[n + 1:], i))
