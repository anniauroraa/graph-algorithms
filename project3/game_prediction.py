from graph_fixed import Graph
from copy import deepcopy as copy
from queue import Queue
import sys

class PredictionNetwork:
    def __init__(self,G) -> None:
        self.G = G
        self.centralities = {}
        self.delta = {}          # δ
        self.d = {}
        self.sigma = {}          # σ
        self.pred = {}

        # define the first vertex that has edges as the starting point of the graph (usually 1 or 0)
        for u in range(self.G.n):
            # print(len(self.G.adj[u]))
            if len(self.G.adj[u]) > 0:
                self.s = u
                return
        # if the graph doesn't have edges
        self.s = 0
        return

    def BFSHighLevel(self):

        # mark initial centrality to 0
        for vertice in range(self.s,self.G.n):
            self.centralities[vertice] = 0

        # go through the algorithm n times so that every vertex is ones the start vertex
        for start in range(self.s, self.G.n):
            for vertice in range(self.G.n):
                self.delta[vertice] = 0    
                self.d[vertice] = None
                self.sigma[(start,vertice)] = 0
                self.pred[vertice] = []
            self.stack = []
            self.BrandesBFS(start)
            #print(f"sigma {self.sigma}")
            self.MagicDelta(start)

            # print(f"centralities {start}. {self.centralities}")

        return
    
    def BrandesBFS(self,s):
        # starting point
        d = self.d
        d[s] = 0
        queue = Queue()   # FIFO
        queue.put(s)
        self.sigma[(s,s)] = 1

        # Breadth first algorithm
        while not queue.empty():    
            current = queue.get()
            self.stack.append(current)
            #print(f"stack iteration {self.stack}")
            for neighbor in self.G.adj[current]:
                #print(neighbor)
                if d[neighbor] == None:
                    d[neighbor] = d[current] + 1
                    queue.put(neighbor)

                # print(d[neighbor], d[current])
                if d[neighbor] == d[current] + 1:
                    self.sigma[(s,neighbor)] = self.sigma[(s,neighbor)] + self.sigma[(s,current)]
                    self.pred[neighbor].append(current)
        # print(f"distances {self.d}")
        return
    
    def MagicDelta(self,s):
        # print(f"stack {self.stack}")
        stack = self.stack
        sigma = self.sigma
        delta = self.delta 

        while len(stack) > 0:
            succ = stack.pop()
            # print(f"going through stack {succ}")
            for pred in self.pred[succ]:
                # delta magic equation
                delta[pred] = delta[pred] + sigma[(s,pred)]/sigma[(s,succ)]*(1+delta[succ])
            if succ != s:
                self.centralities[succ] = self.centralities[succ] + delta[succ]

        return
    
    def topTen(self, C):
        sorted_players = sorted(C.items(), key=lambda x: x[1], reverse=True)
        top_10 = [player[0] for player in sorted_players[:10]]
        return top_10


if __name__ == "__main__":
    G = Graph()
    inputgraph = sys.argv[1]
    G.readgraph(inputgraph)
    F = PredictionNetwork(G)
    F.BFSHighLevel()
    winners = F.topTen(F.centralities)

    print(f"centralities {F.centralities}")
    print("------------------")
    print("The top 10 players: " + str(winners))