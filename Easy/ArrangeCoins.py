#https://leetcode.com/problems/arranging-coins/description/
def arrangeCoins(n: int) -> int:
    l = 1
    r = n
    x = ((l + r) * r) // 2
    while (r - l) > 1:
        m = (l + r) // 2
        if ((1 + m) * m) // 2 <= n:
            l = m
        else:
            r = m
    return l


print(arrangeCoins(8))