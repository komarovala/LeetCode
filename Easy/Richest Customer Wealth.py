# https://leetcode.com/problems/richest-customer-wealth/
accounts = [[2,8,7],[7,1,3],[1,9,5]]

def max_wealth(accounts):
    return (max([sum(i) for i in accounts]))

print(max_wealth(accounts))
