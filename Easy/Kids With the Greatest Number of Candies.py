# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
candies = [2, 3, 5, 1, 3]
extraCandies = 3


def max_candies_check(candies, extraCandies):
    lst = []
    max_candies = max(candies)
    for i in candies:

        if (i + extraCandies) >= max_candies:
            lst.append(True)
        else:
            lst.append(False)
    return lst


print(max_candies_check(candies, extraCandies))
