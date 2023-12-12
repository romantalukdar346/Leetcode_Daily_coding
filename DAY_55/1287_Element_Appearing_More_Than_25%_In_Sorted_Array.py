def findSpecialInteger(self, arr):
    from collections import Counter
    sset=set(arr)
    num=Counter(arr)
    max_=0
    for value in sset:
        if num[value]> max_:
            max_=num[value]
            ele=value
    return ele