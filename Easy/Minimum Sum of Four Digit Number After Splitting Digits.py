# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

num = 2932


def minimumSum(num) -> int:
    digits = []
    for i in range(4):
        digits.append(num % 10)
        num = num // 10

    digits.sort()
    res = (digits[1] * 10 + digits[2]) + (digits[0] * 10 + digits[3])
    return res

print(minimumSum(num))