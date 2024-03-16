vertices={'A','B','C','D','E','F'}
class DWGraph:
  def   init (self):
      self.graph = {}

def add_node(self, node):
    if node not in self.graph: 
        self.graph[node] = {}

def add_edge(self, start, end, weight):
    if start not in self.graph: 
        self.add_node(start)
    if end not in self.graph:
        self.add_node(end)
    self.graph[start][end] = weight

def DijkstraAlgo(self,start,end,n): 
    path=[]
    Max= float('inf')
    dist=dict.fromkeys(vertices, Max)
    visited=dict.fromkeys(vertices,False) 
    root=dict.fromkeys(vertices, None)

    dist[start]=0
    for k in range(n): 
      temp=None
      for i in vertices:
         if (temp is None or dist[i]<dist[temp]) and not visited[i]: 
            temp=i

      visited[temp]=True 
      for i in vertices:
         if self.graph[temp].get(i) is not None:
           currentdist = self.graph[temp][i]
           if dist[temp]+currentdist<dist[i]: 
              dist[i]=dist[temp]+currentdist 
              root[i]=temp

    self.printfunc(dist[end],root,start,end)

def printfunc(self,distance,array,start,end):
  print("The shortest distance using dijsktra Algo from ", start, " to ",end,": ")
  print("Path: ") 
  path=[]
  temp = end
  path=path+[end]
  while temp != start:
    temp = array[temp] 
    path=path+[temp]
  path.reverse()
  print(str(path))


g = DWGraph()

# add nodes and edges to the graph
g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 1)
g.add_edge('B', 'C', 4)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 1)
g.add_edge('C', 'F', 2)
g.add_edge('D', 'C', 1)
g.add_edge('D', 'E', 4)
g.add_edge('E', 'F', 1)
g.add_edge('F', 'C', 3)
g.add_edge('F', 'E', 2)
#print(graph)
g.DijkstraAlgo('A','F',6)