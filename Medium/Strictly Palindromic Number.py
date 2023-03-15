#https://leetcode.com/problems/strictly-palindromic-number/
#O(n^2)

def strictly_palindrome(n):

    for i in range(2, (n-1)):
        print(i)
        num = n
        base = ''
        while num > 0:
            base += str(num % i)
            num = (num // i)
        #роверяем на палиндром
        left = 0
        right = len(base)-1

        while left < right:
            if base[left] == base[right]:
                left += 1
                right -= 1
            else:
                return False
    return True

print(strictly_palindrome(4))