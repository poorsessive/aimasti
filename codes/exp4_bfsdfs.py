visited = [] 
queue = []
 
 
 
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0) 
        print (s, end = " ") 
        for neighbour in graph[s]:
              if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                    
def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)                    
 
 
graph = {
  'A' : ['B','C'],
  'B' : ['D','E'],
  'C' : ['D','F'],
  'D' : ['E'],
  'E' : ['G'],
  'F' : ['G'],
  'G' : ['E','F']
}
 
 
print("Following is BFS from (starting from vertex A)")
bfs(visited, graph, 'A')
visited = set() 
print(" ")
 
print("Following is DFS from (starting from vertex A)")
 
 
dfs(visited, graph, 'A')