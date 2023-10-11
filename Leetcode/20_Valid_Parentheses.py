def isValid(s):
    stack=[]
    for i in s:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        elif i==')' or i=='}' or i==']':
            if len(stack)==0:
                return False
            if i==')' and stack[-1]=='(':
                stack.pop()
            elif i=='}' and stack[-1]=='{':
                stack.pop()
            elif i==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True


symols=input()
print(isValid(symols))



#    mappping={'(':0,'{':0,'[':0}
#    for i in range(len(s)+1):
#         if s[i]=='(' or s[i]=='{' or s[i]=='[':
#             mappping[s[i]]+=1
#         elif s[i]==')':
#             if mappping['(']==0:
#                 return False
#             else:
#                 mappping['(']-=1
#         elif s[i]=='}':
#             if mappping['{']==0:
#                 return False
#             else:
#                 mappping['{']-=1
#         elif s[i]==']':
#             if mappping['[']==0:
#                 return False
#             else:
#                 mappping['[']-=1
                
#         if mappping['(']==0 and mappping['{']==0 and mappping['[']==0 :
#             return True


         
         