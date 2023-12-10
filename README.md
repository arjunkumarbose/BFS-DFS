## Graph Traversal Algorithms in Python

### Overview
This repository contains Python implementations of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for graph traversal.

### Features
- **BFS Implementation:** Utilizes a queue to traverse the graph level by level, starting from a specified vertex.
- **DFS Implementation:** Uses recursion to explore as far as possible along each branch before backtracking.

### How to Use
1. **Input Graph Edges:** Enter the graph edges in the format 'source destination'. Use '#' to indicate the end of input.
2. **Start BFS/DFS:** Input the vertex number to start BFS or DFS traversal from.
3. **View Results:** See the BFS and DFS traversal results starting from the chosen vertex.

### Example Usage
```python
# Creating the graph
g = Graph()
print("Enter edges for the graph (format: 'source destination'). Enter '#' to stop:")

while True:
    edge = input()
    if edge == '#':
        break
    u, v = map(int, edge.split())
    g.add_edge(u, v)

vertex = int(input("Enter the vertex to start BFS and DFS from: "))

print("\nBFS starting from vertex {}:".format(vertex))
g.bfs(vertex)
print("\nDFS starting from vertex {}:".format(vertex))
g.dfs(vertex)
```

### Additional Notes
- The code uses an adjacency list representation for the graph.
- Feel free to modify the example graph or expand it according to your requirements!
