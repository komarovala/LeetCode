# https://leetcode.com/problems/avoid-flood-in-the-city/
dic = {}
rains = [1,2,3,4]
l, r = 0, 0
while l < len(rains):
    if rains[l] != 0:
        if rains[l] not in dic:
            dic[rains[l]] = 1
            rains[l] = -1
            r += 1
            l += 1
    else:
        if rains[r] in dic:
            del (dic[rains[r]])
            rains[l] = rains[r]
            l += 1
        else:
            r += 1

print(rains)
