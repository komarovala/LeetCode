# https://leetcode.com/problems/roman-to-integer/
# O(n)

dict_nums = {'I': 1,
             'V': 5,
             'X': 10,
             'L': 50,
             'C': 100,
             'D': 500,
             'M': 1000}

s = 'XIX'
cnt = 0

for i in range(len(s)-1):
    if dict_nums[s[i]] < dict_nums[s[i + 1]]:
        add_num = dict_nums[s[i + 1]] - dict_nums[s[i]]
        cnt -= dict_nums[s[i]]
    else:
        cnt += dict_nums[s[i]]

print(cnt + dict_nums[s[-1]])
