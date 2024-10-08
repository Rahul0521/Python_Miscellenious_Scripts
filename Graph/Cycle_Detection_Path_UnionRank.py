from collections import defaultdict, Counter


# Create A Graph
class Graph:
    def __init__(self, num_of_vertices):
        self.num_of_vertices = num_of_vertices
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)


# Initialize Rank and Parents
class Subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


# Get Ulitmate Parents for Each Node
def find(subsets, node):
    if subsets[node].parent != node:
        subsets[node].parent = find(subsets, subsets[node].parent)
    return subsets[node].parent


# Union All Subsets Based on Ranks
def union(subsets, u, v):
    if subsets[u].rank > subsets[v].rank:
        subsets[v].parent = u
    elif subsets[v].rank > subsets[u].rank:
        subsets[u].parent = v
    else:
        subsets[v].parent = u
        subsets[u].rank += 1


# Cycle Detection

def isCyclic(graph):
    subsets = []
    for u in range(graph.num_of_vertices):
        subsets.append(Subset(u, 0))
    for u in graph.edges:
        u_rep = find(subsets, u)
        for v in graph.edges[u]:
            v_rep = find(subsets, v)
            if v_rep == u_rep:
                return True
            else:
                union(subsets, u_rep, v_rep)


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
if isCyclic(g):
    print("Cyclic Graph")
else:
    print("Non Cyclic")
