# import matplotlib.pyplot as plt
# import networkx as nx
#
# def build_graph(additional_nodes):
#     G = nx.DiGraph()
#     initial_nodes = [1, 2, 3, 4]
#
#     G.add_nodes_from(initial_nodes)
#
#     for i in range(len(initial_nodes)):
#         G.add_edge(initial_nodes[i], initial_nodes[(i + 1) % len(initial_nodes)])
#
#     current_last_node = 4
#     for _ in range(additional_nodes):
#         current_last_node += 1
#         G.add_node(current_last_node)
#
#         sources = list(G.nodes())[:3]
#         for src in sources:
#             G.add_edge(src, current_last_node)
#             G.add_edge(current_last_node, src)
#
#     valid = True
#     for node in initial_nodes:
#         if G.in_degree(node) + G.out_degree(node) != 2:
#             valid = False
#             break
#
#     for node in range(5, 5 + additional_nodes):
#         degree = G.in_degree(node) + G.out_degree(node)
#         if degree < 3:
#             valid = False
#             break
#
#     if valid:
#         pos = nx.spring_layout(G)
#         node_colors = ['lightgreen' if n in initial_nodes else 'lightblue' for n in G.nodes()]
#         nx.draw(G, pos,
#                 with_labels=True,
#                 node_color=node_colors,
#                 edge_color='gray',
#                 node_size=800,
#                 font_size=10)
#         plt.title("Custom Graph")
#         plt.show()
#         return "Norm" if nx.is_strongly_connected(G) else "Not norm"
#     else:
#         return "Invalid"
#
# additional_nodes = int(input())
# result = build_graph(additional_nodes)
# print(result)

# import matplotlib.pyplot as plt
# import networkx as nx
#
# def build_graph(additional_nodes):
#     G = nx.DiGraph()
#     fixed_nodes = [1, 2, 3, 4]
#     fixed_edges = [(1, 2), (2, 3), (3, 4), (4, 1)]
#
#     G.add_nodes_from(fixed_nodes)
#     G.add_edges_from(fixed_edges)
#
#     current_last_node = 4
#     for i in range(1, additional_nodes + 1):
#         new_node = current_last_node + 1
#         G.add_node(new_node)
#
#         G.add_edge(current_last_node, new_node)
#         current_last_node = new_node
#
#     G.add_edge(current_last_node, 1)
#
#     if nx.is_strongly_connected(G):
#         pos = nx.circular_layout(G)
#         nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000, font_size=10)
#         plt.title("Graph")
#         plt.show()
#         return "Norm"
#     else:
#         return "Not norm"
#
#
# additional_nodes = int(input())
# result = build_graph(additional_nodes)
# print(result)

inf = float('inf')
graph = [
    [0, 3, 9],
    [inf, 0, 1],
    [inf, inf, 0]
]

dist = [row[:] for row in graph]

dist[0][0] = 0

print("graph:", graph)
print("dist:", dist)

