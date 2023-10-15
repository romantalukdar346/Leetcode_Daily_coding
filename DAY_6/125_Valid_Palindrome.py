def isPalindrome(s):
    s=s.lower()
    new_str=''
    for i in s:
        if i.isalnum():
            new_str+=i
    return (new_str==new_str[::-1])


n=str(input())
isPalindrome(n)