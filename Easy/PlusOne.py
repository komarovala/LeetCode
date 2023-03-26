# https://leetcode.com/problems/plus-one/
# O(n^2)
from typing import List

digits = [4,3,2,1]


def plusOne(digits) -> List[int]:
    s = ''

    for i in digits:
        s += str(i)

    nums = int(s) + 1

    n = [int(i) for i in str(nums)]

    return n


# plusOne(digits)

# Fair solution


def plusOne(digits: List[int]) -> List[int]:
    last_num = len(digits) - 1
    in_mind = 1

    while last_num > 0:
        digits[last_num] = digits[last_num] + in_mind

        if digits[last_num] == 10:
            digits[last_num] = 0
            in_mind = 1
            last_num -= 1
        else:
            return digits

    if digits[0] + in_mind == 10:
        return ([1, 0] + digits[1:])
    else:
        digits[0] += in_mind

    return digits
