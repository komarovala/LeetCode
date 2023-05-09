#https://leetcode.com/problems/create-target-array-in-the-given-order/description/
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
lst=[]
for n,i in zip(nums,index):
    lst.insert(i, n)

print(lst)