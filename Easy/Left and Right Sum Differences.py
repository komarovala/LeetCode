# https://leetcode.com/problems/left-and-right-sum-differences/
nums = [10, 4, 8, 3]


def leftRigthDifference(nums):
    leftSum = []
    rightSum = []
    for i in range(len(nums)):
        leftSum.append(sum(nums[:i]))
        rightSum.append(sum(nums[i + 1:]))

    for i in range(len(nums)):
        nums[i] = abs(leftSum[i] - rightSum[i])
    return nums


print(leftRigthDifference(nums))
