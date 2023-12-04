def countCharacters(self, words, chars):
    from collections import Counter
    total=0
    char_map=Counter(str(chars))

    for string in words:

        string_map=Counter(str(string))
        good=True
        for ch,value in string_map.items():
            if char_map[ch] < value:
                good=False
                break
        if good:
            total+=len(string)
    return total