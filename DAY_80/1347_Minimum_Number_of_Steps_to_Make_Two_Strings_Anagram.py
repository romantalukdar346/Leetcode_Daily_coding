def minSteps(self, s, t):
    from collections import Counter
    t_set=set(t)
    s_map=Counter(s)
    t_map=Counter(t)
    
    for val in t_set:
        if val in s_map:
            s_map[val]-=t_map[val]
    res=0
    for c in s_map.values():
        if c>0:
            res+=c
    return res
        