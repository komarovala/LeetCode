#https://leetcode.com/problems/smallest-even-multiple/

def div(n):
    if n % 2 == 0:
        return n
    else:
        return n*2

print(div(6))