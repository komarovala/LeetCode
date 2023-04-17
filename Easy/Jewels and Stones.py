#https://leetcode.com/problems/jewels-and-stones/
jewels = "z"
stones = "ZZ"


def jewels_stones(jewels, stones):
    cnt = 0
    for i in stones:
        if i in jewels:
            cnt += 1
    return cnt


print(jewels_stones(jewels, stones))
