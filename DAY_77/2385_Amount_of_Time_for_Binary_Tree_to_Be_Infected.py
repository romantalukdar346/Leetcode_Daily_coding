def amountOfTime(self, root, start):
    from collections import defaultdict
    from collections import deque
    graph=defaultdict(list)
    self.dfs(root,graph)

    visited = set()
    queue = deque([start])
    time = -1
    while queue:
        time += 1
        for _ in range(len(queue)):
            current_node = queue.popleft()
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return time


def dfs(self,root,graph):
    if not root:
        return
    if root.left:
        graph[root.val].append(root.left.val)
        graph[root.left.val].append(root.val)
    if root.right:
        graph[root.val].append(root.right.val)
        graph[root.right.val].append(root.val)
    self.dfs(root.left,graph)
    self.dfs(root.right,graph)