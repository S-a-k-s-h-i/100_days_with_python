def isPalindrome(A):
    s = ''.join(e for e in A.lower() if e.isalnum())
    print(s)
    print(s[::-1])
    if s == s[::-1]:
        return 1
    else:
        return 0
i="A man, a plan, a canal: Panama"
print(isPalindrome(i))