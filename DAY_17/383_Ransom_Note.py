def canConstruct(ransomNote, magazine):
    # 1st solution
    for i in set(ransomNote):
        if ransomNote.count(i)<= magazine.count(i):
            continue
        else:
            return False
    return True

    # 2nd solution
    # magazine=Counter(magazine)
    # for i in ransomNote:
    #     if i in magazine and magazine[i]!=0:
    #         magazine[i]-=1
    #     else:
    #         return False
    # return True
