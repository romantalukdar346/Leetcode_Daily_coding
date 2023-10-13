def addBinary(a, b):
    carry=0
    c=""
    while a or b or carry:
        if a:
            carry+=a.pop()
        if b:
            carry+=b.pop()
        c+="".join(str(carry%2))
        carry//=2
    return c[::-1]
   

a=list(map(int,input().split(",")))
b=list(map(int,input().split(",")))
k=str(addBinary(a,b))
print(k)
        