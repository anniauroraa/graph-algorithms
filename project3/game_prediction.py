from graph_fixed import Graph
from copy import deepcopy as copy
from queue import Queue
import sys

class PredictionNetwork:
    def __init__(self,G) -> None:
        self.G = G
        print(self.G.adj)
        print(self.G.n)

    def BFSHighLevel(self):
        centralities = {}
        delta = {}          # δ
        dist = {}
        sigma = {}          # σ
        pred = {}

        # mark initial centrality to 0
        for vertice in range(self.G.n):
            centralities[vertice] = 0

        for start in range(self.G.n):
            for vertice in range(self.G.n):
                delta[start] = 0    
                dist[start] = 0
                sigma[(start,vertice)] = 0
                pred[vertice] = None
            stack = []
            self.BrandesBFS(start, stack, sigma)
            self.MagicDelta(start, stack, delta, sigma)

            print(f"centralities {start}. {centralities}")
        return
    
    def BrandesBFS(self,s,S,sigma):
        return
    
    def MagicDelta(self,s,S,delta,sigma):
        return
    
    def topTen(self, centralities):
        # sorted_players = sorted(centralities.items(), key=lambda x: x[1], reverse=True)
        # top_10 = [player[0] for player in sorted_players[:10]]
        return "no one"


if __name__ == "__main__":
    G = Graph()
    inputgraph = sys.argv[1]
    G.readgraph(inputgraph)
    F = PredictionNetwork(G)
    F.BFSHighLevel()
    winners = F.topTen()

    print("------------------")
    print("The top 10 players: " + str(winners))