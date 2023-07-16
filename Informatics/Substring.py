#https://informatics.msk.ru/mod/statements/view.php?id=63548&chapterid=112554#1
#s="abaacbbabcaa"

#s = "abaabcca"
k = 2
n, k = map(int,  input().split())
s = input()

dic = {}
max_string = 0
l_max = -1
l = -1
r = 0

while r < len(s):
    if s[r] not in dic:
        dic[s[r]] = 1
        r += 1
    elif (dic[s[r]]) >= k:
        if max_string < len(s[l+1:r]):
            max_string = len(s[l+1:r])
            l_max = l + 1
        dic.clear()
        l += 1
        r = l + 1
    else:
        dic[s[r]] += 1
        r += 1

print(f"{max_string} {l_max + 1}")
