# https://leetcode.com/problems/number-of-good-pairs/
# 1 сек 10^8 операций

nums = [1,1,1,1]


def good_pairs(nums):
     cnt = 0
     for i, n in enumerate(nums):
         j = i + 1
         while j < (len(nums)):
             if (n == nums[j]) and i < j:
                 cnt += 1
                 j += 1
     return cnt

print(good_pairs(nums))

#Вариант со словарем
def good_pairs(nums):
    dic = {}
    cnt = 0
    for i, n in enumerate(nums):
        if n in dic:
            cnt += dic[n]
            dic[n] += 1
        else:
            dic[n] = 1
    return cnt

print(good_pairs(nums))


