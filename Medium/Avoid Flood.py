# https://leetcode.com/problems/avoid-flood-in-the-city/
dic = {}
rains = [1, 0, 2, 0, 2, 1]
l, r = 0, 0
while l < len(rains):
    if rains[l] != 0:
        if rains[l] not in dic:
            dic[rains[l]] = 1
            rains[l] = -1
            l += 1
            if r < l:
                r += 1
        else:
            print("That's all")
            break
    elif rains[l] == 0:
        if r < len(rains) and rains[r] in dic:
            del (dic[rains[r]])
            rains[l] = rains[r]
            l += 1
        elif r < len(rains):
            r += 1
        else:
            rains[l] = 1
            l += 1

print(rains)
