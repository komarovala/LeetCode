# https://leetcode.com/problems/boats-to-save-people/

people = [2, 4]
limit = 5


def numRescueBoats(people, limit) -> int:
    l = 0
    r = len(people) - 1
    cnt = 0
    people = sorted(people)
    while l <= r:
        people_weigth = people[l] + people[r]
        if people_weigth > limit:
            r -= 1
        else:
            l += 1
            r -= 1
        cnt += 1
    return cnt

print(numRescueBoats(people, limit))