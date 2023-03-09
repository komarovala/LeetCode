#https://leetcode.com/submissions/detail/909002631/
def twoSum(nums: List[int], target: int) -> List[int]:
    d = {}

    for i, n in enumerate(nums):

        diff = target - n

        if diff not in d:
            d[n] = i
        else:
            return (i, d[diff])