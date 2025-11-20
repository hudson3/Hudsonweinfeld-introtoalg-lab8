from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    #initalize distances and edge counts
    dist = {source: (0, 0)}  # (weight, num_edges)
    
    # priority queue: weight, num edges, vertex
    pq = [(0, 0, source)]
    
    while pq:
        current_weight, current_edges, u = heappop(pq)
        
        # skip if we found a better path
        if u in dist and (current_weight, current_edges) > dist[u]:
            continue
        
        # see neighbors
        if u in graph:
            for v, weight in graph[u]:
                new_weight = current_weight + weight
                new_edges = current_edges + 1
                
                # update if we found a better path
                if v not in dist or (new_weight, new_edges) < dist[v]:
                    dist[v] = (new_weight, new_edges)
                    heappush(pq, (new_weight, new_edges, v))
    
    return dist
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    parents = {}
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        node = queue.popleft()
        
        if node in graph:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parents[neighbor] = node
                    queue.append(neighbor)
    
    return parents

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    path = []
    current = destination
    
    while current in parents:
        current = parents[current]
        path.append(current)
    
    path.reverse()
    
    return ''.join(path)

