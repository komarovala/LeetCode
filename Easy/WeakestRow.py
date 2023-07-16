#https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

len_rows = [sum(i) for i in mat]

zlist = list(zip(len_rows, range(len(mat))))
print(sorted(zlist))
k=2

print([i[1] for i in sorted(zlist)][0:k])