# https://leetcode.com/problems/most-profit-assigning-work/
difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]
max_pofit = 0
sum_pofit = 0
nums = [i for i in sorted(zip(difficulty, profit))]
print(nums)
l = 0
r = 0

while r < len(nums) and l < len(worker):
    if nums[r][0] <= worker[l]:
        r += 1
    else:
        if worker[l] >= nums[r - 1][0]:
            sum_pofit += max(nums[r - 1][1], max_pofit)
            max_pofit = nums[r - 1][1]
            l += 1

print(sum_pofit)



def maxProfitAssignment(difficulty, profit, worker) -> int:
    max_pofit = 0
    sum_pofit = 0
    nums = [i for i in sorted(zip(difficulty, profit))]
    l = 0
    r = 0
    while r < len(nums) and l < len(worker):
        if nums[r][0] <= worker[l]:
            r += 1
        else:
            if worker[l] >= nums[r - 1][0]:
                sum_pofit += max(nums[r - 1][1], max_pofit)
                max_pofit = nums[r - 1][1]
                l += 1
    return sum_pofit

print(maxProfitAssignment(difficulty, profit, worker))

