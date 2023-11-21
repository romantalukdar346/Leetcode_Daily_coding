def garbageCollection(self, garbage, travel):
    from collections import defaultdict
    total_time=0
    mapping=defaultdict(list)
    for i in range(len(garbage)):
        if len(garbage[i])==1:
            mapping[str(garbage[i])].append(i)
        else:
            for j in garbage[i]:
                mapping[str(j)].append(i)
    string='MPG'
    for i in string:
        if len(mapping[i])!=0:
            max_=max(mapping[i])
            if max_==len(travel):
                total_time+=sum(travel)+len(mapping[i])
            else:
                total_time+=sum(travel[:max_])+len(mapping[i])
    return total_time