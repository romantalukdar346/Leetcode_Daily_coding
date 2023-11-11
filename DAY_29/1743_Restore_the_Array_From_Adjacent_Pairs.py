def restoreArray(self, adjacentPairs):
    from collections import defaultdict
    graph= defaultdict(list)

    for x,y in adjacentPairs:
        graph[x].append(y)
        graph[y].append(x)
    
    root=None
    for num in graph:
        if len(graph[num])==1:
            root=num
            break

    curr=root
    ans=[root]
    prev=None

    while len(ans) < len(graph):
        for neighbors in graph[curr]:
            if neighbors!= prev:
                ans.append(neighbors)
                prev=curr
                curr=neighbors
                break
    return ans
