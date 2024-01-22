### Generate random graphs by two different method.

import graph

import random

### Method 1: Erdos-Renyi random graph, n vertices and probability p for each edge to appear
def ErdosRenyi(n: int, p: float) -> graph.Graph:
  G = graph.Graph(n)
  for u in range(n):
    for v in range(n):
      if (u == v):
        continue
      if random.random() < p:
        G.addEdge(u, v)
  return G

### Method 2: Barabasi-Albert random graph, n final vertices, m0 initial vertices and m edges for each new vertex
def BarabasiAlbert(n: int, m0: int, m: int) -> graph.Graph:
  assert(m0 <= n)
  assert(m <= m0)
  G = graph.Graph(n)
  for u in range(m0):
    for v in range(m0):
      if (u == v):
        continue
      G.addEdge(u, v)
  for u in range(m0, n):
    # Take a random sample of m vertices from the vertices 0 to u-1, with probabilities proportional to their degrees
    # The sample is returned as a list of vertices
    sample = random.choices(range(u), weights=[len(G.adj[i]) for i in range(u)], k=m)
    for v in sample:
      G.addEdge(u, v)
  return G

