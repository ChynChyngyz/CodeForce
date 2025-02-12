import networkx as nx
import matplotlib.pyplot as plt

def create_graph(n):
    graph = {i + 1: set() for i in range(4 + n)}

    for i in range(5, 5 + n):
        graph[i] = {j for j in range(5, 5 + n) if j != i}

    for i in range(1, 5):
        while len(graph[i]) < 2:
            target = min((k for k in range(5, 5 + n) if k not in graph[i]), key=lambda k: len(graph[k]))
            graph[i].add(target)
            graph[target].add(i)

    return graph

n = int(input())
graph = create_graph(n)

G = nx.Graph()
for node, neighbors in graph.items():
    G.add_edges_from((node, neighbor) for neighbor in neighbors)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='green', node_size=700, edge_color="gray", font_size=10,
        font_weight="bold")
plt.title("Graph", fontsize=16)
plt.show()
