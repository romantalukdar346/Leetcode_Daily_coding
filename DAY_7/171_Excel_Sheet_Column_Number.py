def titleToNumber(columnTitle):
        ans, pos = 0, 0
        while len(columnTitle) >0:
            digit = ord(columnTitle[-1])-64
            ans += digit * 26**pos
            pos += 1
            columnTitle=columnTitle[:-1]
            
        return ans

n= input()

print(titleToNumber(n))