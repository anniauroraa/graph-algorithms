
### Read in a graph, a set of vertices, and a pair of vertices. 

import graph
import sys
from queue import Queue

## Implement your algorithm here:
def algorithm(g, B, s, e):

  print("neighbors:", g.adj)
  print("weighted: ", g.w)
  print("B:", B)
  print("start & end:", s, e)
  print("-----------")

  # starting point
  visited = []
  max_b = 0
  queue = Queue()   # FIFO

  # initialize algorithm with starting point s
  visited.append(s)
  if s in B:
    queue.put((s,1))
  else:
    queue.put((s,0))

  # Breadth first algorithm
  while not queue.empty():     
    u, b_count = queue.get()
    print("current B count:", b_count)

    for v in g.adj[u]:
      if v not in visited:
        visited.append(v)
        print(f"new edge: ({u}, {v})")
        new_b_count = b_count
        if v in B:
          new_b_count += 1

        queue.put((v, new_b_count))
      if v == e:
        # end found from a neighbor, update max count
        max_b = max(max_b, b_count)
        print(f"compare: B count = {b_count}, max_b = {max_b}")

  # consider if e was part of B
  if e in B:
    max_b += 1

  print("-----------")
  return max_b

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
  print(f"Maximum amout of B vertices in any shortest path: {n}")
  

