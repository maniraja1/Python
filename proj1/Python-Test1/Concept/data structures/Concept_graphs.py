'''
    Graph consists of nodes which consists of vertices and edges. G(v,e).
    Directed Graphs and Undirected Graphs
    Graphs can be modelled using adjacency matrices or edge list representation
    Adjacency matrix
        Example of the matrix is below. Nodes with edges are represented by 1

          A B C D
        A 0 1 1 0
        B 1 0 0 1
        C 1 0 0 1
        D 0 1 1 0
    Edge list representation
        we create a vertex class that stores neighbors accordingly

        class vertex
            vertexname
            visited
            vertex[] neighbors
    Graph traversal algorithm
        Breadth first search
            we have to visit every edge exactly once. we visit neighbors then neighbors of these new vertices and so on
            memory complexity is not good so we generally use Depth first search DPS.
            BFS constructs the shortest path
            complexity: O(V+E), memory complexity: O(N)
            Start at a vertex--> populate its neighbor in a queue and mark the vertex as visited--> pick the next vertex
            from the queue and populate ist neighbor and mark the vertex as visited--> continue till queue is empty
        Depth first search
            traverse ever branch as deep as possible before backtracking
            Complexity: O(V+E), memory complexity: O(log N)
            memory complexity is a bit better than BFS
            You can implement DFS the same way you do BFS but instead of using queue use a stack
    ShortestPathAlgo
        Dijkstra Algorithm
            only works with positive edge weights
            It can find shortest path between 2 nodes and also shortest path tree shortest path from a node to all
            other nodes
            complexity O(V*logV+E)
            This is a greedy algorithm
            data structure used binary heaps, fibonacci heaps or priority queue

'''