#https://leetcode.com/problems/guess-number-higher-or-lower/
peak = 1
def guess(n):
    if n > peak:
        return -1
    elif n < peak:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    l = 0
    r = n + 1
    while (r - l) > 1:
        m = (r + l) // 2
        if guess(m) >= 0:
            l = m
        else:
            r = m
    return l, r

print(guessNumber(1))
