# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]

mat_nums = []
for n, i in enumerate(mat):
    l = -1
    r = len(i)
    while r - l > 1:
        mid = r + l // 2
        if i[mid] >= 1:
            l = mid
        else:
            r = mid
    print(l, r)
    mat_nums.append((r, n))

k = 3
print([i[1] for i in sorted(mat_nums)][:k])
