# https://leetcode.com/problems/reverse-vowels-of-a-string/

# 1. Взять левый указатель и двигать пока не будет гласная
# 2. Правый указатель сдвинуть на l+1 и двигать пока не будет гласная
# 3. Поменять местами элементы l,r и приравнять l = r
# 4. Вернуться в пункт 1.

# l, r = 0, 0
# s = "helloe"
# vowels = ['a', 'e', 'i', 'o']
# s = list(s)
#
# while s[l] not in vowels:
#     l += 1
#
# r = l + 1
#
# while r <= (len(s)) and s[r] not in vowels:
#     r += 1
#
# s[l] = s[r]
# l = r
#
# print(l, r)


def reverseVowels(s: str) -> str:
    l, r = 0, 0
    vowels = ['a', 'e', 'i', 'o', 'A', 'E', 'i', 'o']
    s = list(s)
    while r < (len(s) - 1):
        while (l < len(s) - 2) and (s[l] not in vowels):
            l += 1

        if s[l] not in vowels:
            return "".join(s)

        r = l + 1

        while r <= (len(s) - 2) and (s[r] not in vowels):
                r += 1
        if s[r] not in vowels:
                return "".join(s)
        s[l], s[r] = s[r], s[l]
        l = r

    return "".join(s)


s = "aA"

print(reverseVowels(s))
