# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/
operations = ["++X", "++X", "X++"]


def find_value(nums):
    cnt = 0
    dic_operations = {"--X": -1,
                      "X++": 1,
                      "++X": 1,
                      "X--": -1}
    for i in operations:
        cnt += dic_operations[i]
    return cnt


print(find_value(operations))
