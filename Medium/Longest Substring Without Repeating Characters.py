#https://leetcode.com/problems/longest-substring-without-repeating-characters/
s = "abcabcbb"


def lengthOfLongestSubstring(s) -> int:
    left = right = 0
    maximum = 0
    last_seen = set()

    while right < len(s):
        if s[right] not in last_seen:
            last_seen.add(s[right])
            right += 1
            maximum = max(maximum, right - left)
        else:
            last_seen.remove(s[left])
            left += 1
    return maximum


print(lengthOfLongestSubstring(s))
