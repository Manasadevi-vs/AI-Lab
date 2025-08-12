import heapq

graph={}

num_edges=int(input("Edges? "))
for _ in range (num_edges):
  u,v,c=input("From to Cost: ").strip().split(',')
  graph.setdefault(u,[]).append((v,int(c)))

def uniform_cost_search(graph,start,goal):
  visited=set()
  queue = [(0,start,[])]
  while queue:
    cost,node,path=heapq.heappop(queue)
    if node in visited:
      continue
    visited.add(node)
    new_path=path+[node]
    if node==goal:
      return cost,new_path
    for neighbor,edge_cost in graph.get(node,[]):
      if neighbor not in visited:
        heapq.heappush(queue,(cost+edge_cost,neighbor,new_path))
    return float('inf'),[]

start= input("Start node:").strip()
goal= input("Goal Node: ").strip()

final_cost,final_path=uniform_cost_search(graph,start,goal)

if final_path:
  print(f"Least cost from {start} to {goal}: {'->'.join(final_path)}(cost:{final_cost})")
else:
  print(f"No path found from {start} to {goal}.")
  

