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
    ### TODO
    priority_queue = [] # initializes priority queue 
    
    distances = {} # initializes distances dict
    for v in graph: # iterates through all vertexes in the graph and initializes distances entry for each
        distances[v] = (float('inf'), float('inf'))
        
    distances[source] = (0,0) # initializes distance to the source node
    heappush(priority_queue, (0, 0, source)) # adds source node to priority queue
    
    while priority_queue: # iterates through all values in priority queue
        cur_sit, cur_edges, u = heappop(priority_queue) # removes and returns smallest item to initialize variables 
        
        if (cur_dist, cur_edges) != distances[u]: # skipped popped value if worse
            continue
            
        for v, w, in graph.get(u, []): 
            new_dist = cur_dist + w # new total weight
            new_edges = cur_edges + 1 # new total number of edges
            old_dist, old_edges = distances[v]
            # if new distance is strictly smaller or same distance with fewer edges, update
            if (new_dist < old_dist) or (new_dist == old_dist and new_edges < old_edges):
                distances[v] = (new_dist, new_edges)
                heappush(priority_queue, (new_dist, new_edges, v))
                
    return distances
                
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None} # no parent exists for source
    queue = deque([source]) # # queue from source starting point

    while queue: # iterates through entire queue until empty
        u = queue.popleft() # initializes next node to explore
        for v in graph.get(u, []): # iterates through neighboring nodes of u
            if v not in parents: # if v not set, find
                parents[v] = u # u set as parent of v
                queue.append(v) # append v to fronteir of BFS
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
    ###TODO
    path = [] # initialize empty path
    curr = parents.get(destination) # begins current node at parents of destination

    while curr is not None: # iterates through all parent nodes until source whose parents are None
        path.append(curr) # adds current node to path
        curr = parents.get(curr) # sets new current node to parent

    path.reverse() # reverses path to begin at source, not parent of destination
    return path

