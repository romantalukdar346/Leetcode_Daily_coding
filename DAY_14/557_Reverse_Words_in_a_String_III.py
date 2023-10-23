def reverseWords( s):
    new_s=[]
    new_s=s.split(" ")
    for i in range(len(new_s)):
        new_s[i]=new_s[i][::-1]
    return " ".join(new_s)

# return ""+join([i[::-1] for i in s.split(" ")])

    


n= input()
print(reverseWords(n))