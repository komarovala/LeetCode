#https://leetcode.com/problems/guess-number-higher-or-lower/
def guessNumber(n: int) -> int:
    l = 0
    r = n + 1
    while (r - l) < 1:
        m = (r + l) // 2
        if m <= pick:
            l = m
        else:
            r = m
    return l, r

pick = 6
n = 10
print(guessNumber(n))
