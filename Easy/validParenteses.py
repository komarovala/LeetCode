# https://leetcode.com/submissions/detail/909683865/
#O(n)

def isValid(s: str) -> bool:
    dic_parenteses = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    d = []

    if len(s) < 2:
        return False

    for i, n in enumerate(s):
        if (n not in d):
            d.append(n)
        elif dic_parenteses[d.pop()] != n:
            return False
    return True

print(isValid('(())'))