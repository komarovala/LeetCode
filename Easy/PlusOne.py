#https://leetcode.com/problems/plus-one/
#O(n^2)
from typing import List

digits = [4, 3, 2, 1]


def plusOne(digits) -> List[int]:
    s = ''

    for i in digits:
        s += str(i)

    nums = int(s) + 1

    n = [int(i) for i in str(nums)]

    return n

plusOne(digits)
