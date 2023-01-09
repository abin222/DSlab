
from typing import List, Tuple

def ford_fulkerson(graph: List[List[int]], source: int, sink: int) -> int:
    residual_graph = [row[:] for row in graph]
    print("residual graph:",residual_graph)
    n = len(graph)

    parent = [-1] * n
    print("parent:",parent)
    max_flow = 0

    while True:

        dfs_result = depth_first_search(residual_graph, source, sink, parent)
        if not dfs_result:
            break


        path_flow = float("Inf")
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, residual_graph[u][v])
            v = parent[v]


        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]
        print("residual graph:",residual_graph)

        max_flow += path_flow

    return max_flow

def depth_first_search(graph: List[List[int]], source: int, sink: int, parent: List[int]) -> bool:
    visited = [False] * len(graph)
    stack = []
    stack.append(source)
    while stack:
        u = stack.pop()
        if u == sink:
            return True
        visited[u] = True
        for v, capacity in enumerate(graph[u]):
            if capacity > 0 and not visited[v]:
                parent[v] = u
                stack.append(v)
    return False
graph = [    
	[0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

source = 0
sink =5
print("maximum number:",ford_fulkerson(graph,source,sink))

    