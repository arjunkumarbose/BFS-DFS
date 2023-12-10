from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            start = queue.popleft()
            print(start, end=" ")

            for i in self.graph[start]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start):
        visited = [False] * (max(self.graph) + 1)
        self.dfs_util(start, visited)

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
