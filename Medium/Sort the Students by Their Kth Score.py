# https://leetcode.com/problems/sort-the-students-by-their-kth-score/

score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
k = 2


def sortTheStudents(score, k):
    dic_scores = {}

    for i, n in enumerate(score):
        dic_scores[n[k]] = n

        my_list = sorted(dic_scores.items(), reverse=True)

    return [i[1] for i in my_list]



