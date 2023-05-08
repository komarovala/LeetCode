#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

sentences = ["please wait", "continue to fight", "continue to win"]


def mostWordsFound(sentences):
    maximum = 0
    for i in sentences:
        if maximum < len(i.split()):
            maximum = len(i.split())

    return maximum

print(mostWordsFound(sentences))