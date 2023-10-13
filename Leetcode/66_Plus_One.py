def plusOne(digits):
    rem=0
    if digits[-1]!=9:
        digits[-1]+=1
    else:
        for i in range(len(digits)):
            rem=digits[i]+rem*10
        rem+=1
        digits=[]
        while rem!=0:
                digits.insert(0,rem%10)
                rem//=10

        # for i in str(rem):
        #     digits.append(int(i))

    return digits



n=list(map(int,input().split(",")))
k=plusOne(n)
print(k)