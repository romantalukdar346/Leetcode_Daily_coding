def lengthOfLastWord(s):
    substring= s.split()
    return len(substring[-1])





s=input()
k=lengthOfLastWord(s)
print(k)