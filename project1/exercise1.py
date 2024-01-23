
### Read in a graph, a set of vertices, and a pair of vertices. 

import graph
import sys
from queue import Queue

## Implement your algorithm here:
def algorithm(g, B, s, e):

  print("adj:", g.adj)
  print("w: ", g.w)
  print("B:", B)
  print("start & end:", s, e)
  print("-----------")

  distances = []

  # mark initial distance None
  for u in range(len(g.adj)):
    distances.append(None)

  # starting point
  distances[s] = 0
  print(distances)

  # FIFO queue
  queue = Queue()
  queue.put(s)

  path = {}
  alt_path = {}
  b_on_path = []

  # Breadth first algorithm
  u = queue.get()
  while u != e:     
    print("dequeued:", u)

    for v in g.adj[u]:
      if distances[v] == None:
        print(f"new edge: ({u}, {v})")
        distances[v] = distances[u] + 1
        path[v] = u
        queue.put(v)

      # log alternative paths that maximize Bs in shortest path
      elif distances[v] == distances[u] + 1:
        alt_path[v] = u
        print(f"alternative path found: ({u} -> {v})")

      else:
        print(f"Edge ({u}, {v}) ot part of the shortest route")
    
    # move along in the list
    u = queue.get()

  print("----------")
  print("path: ")
  print(path)
  print("alternative paths:")
  print(alt_path)

  min_path = 1
  next = path[e]
  while next != s:
    print(next)
    next = path[next]
    min_path += 1

  max_b = 0

  str1 = f"Shortest path from {s} to {e} is: {min_path}\n"
  str2 = f"Maximum amout edges in any shortest path: {max_b}"
  return str1 + str2

### Read in a set of vertices from a file. These are just numbers separated by whitespace.
def readset(filename):
  f = open(filename, 'r')
  s = set()
  for line in f:
    for v in line.split():
      s.add(int(v))
  return s

## Read the pair, again, just two integers separated by whitespace.
def readpair(filename):
  f = open(filename, 'r')
  for line in f:
    (v,w) = line.split()
    return (int(v), int(w))


### If ran from the command line:
if __name__ == "__main__":
  # Graph is the first command line argument:
  g = graph.Graph()
  g.readgraph(sys.argv[1])
  # Vertices are the second command line argument:
  B = readset(sys.argv[2])
  # Pair is the third command line argument:
  (v,w) = readpair(sys.argv[3])

  ### Call your algorithm:

  n = algorithm(g, B, v, w)

  # Print the result:
  print(n)
  

