def groupAnagrams(self, strs):
    from collections import defaultdict
    if not strs:
        return [[""]]
    elif len(strs)==1:
        return [strs]

    string=defaultdict(list)
    for inx, val in enumerate(strs):
        string[str(sorted(val))].append(val)

    return list(string.values())