# def isPalindrome(x):
#         num=x
#         re_num=0
#         while(num!=0 and num>0):
#             re_num=num % 10+re_num * 10
#             num=num // 10
#         if re_num == x:
#             return True
#         else:
#             return False
        
def isPalindrome(x):
        string = str(x)
        return str(x) == string[::-1]


x=int(input())
result=isPalindrome(x)
print(result)