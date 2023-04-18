#https://leetcode.com/problems/merge-strings-alternately/

word1 = "ab"
word2 = "pqrs"


def mergeAlternately(word1, word2) -> str:
    min = len(word1)
    if min > len(word2):
        min = len(word2)
        add = word1[min:]
    else:
        add = word2[min:]

    return (''.join([x + y for x, y in zip(word1, word2)]) + add)