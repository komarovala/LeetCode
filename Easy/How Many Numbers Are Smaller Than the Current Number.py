# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

nums = [8, 1, 2, 2, 3]

lenght = []
dic = {}

num_set = sorted(set(nums))

for i in range(len(num_set)):
    cnt = 0
    for j in num_set[:i]:

        if num_set[i] > j:
            cnt += 1
    dic[i] = cnt

# for i in range(len(nums)):
#     nums[i] = dic[nums[i]]

print(num_set, len(nums), dic)

