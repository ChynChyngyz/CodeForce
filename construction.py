import networkx as nx
import random
import matplotlib.pyplot as plt


def create_graph(num_new_vertices):
    initial_vertices = ['A', 'B', 'C', 'D']

    G = nx.Graph()

    G.add_nodes_from(initial_vertices)

    available_edges_for_initial = {v: 0 for v in initial_vertices}

    for i in range(num_new_vertices):
        new_vertex = f'{i + 1}'
        G.add_node(new_vertex)

        connections = []
        for _ in range(2):
            available_initials = [v for v in initial_vertices if available_edges_for_initial[v] < 2]
            if available_initials:
                connection = random.choice(available_initials)
                connections.append(connection)
                available_edges_for_initial[connection] += 1
                G.add_edge(new_vertex, connection)

        if any(available_edges_for_initial[v] > 2 for v in initial_vertices):
            raise ValueError("Error 404")

        num_edges = random.randint(3, 5)
        for _ in range(num_edges - len(connections)):
            other_vertex = random.choice(list(G.nodes))
            if other_vertex != new_vertex and not G.has_edge(new_vertex, other_vertex):
                G.add_edge(new_vertex, other_vertex)

    node_colors = {v: 'red' if v in initial_vertices else 'skyblue' for v in G.nodes}

    plt.figure(figsize=(8, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=[node_colors[node] for node in G.nodes],
            node_size=1000, font_size=12, edge_color='grey')
    plt.title("Graph")
    plt.show()

    return G

num_new_vertices = int(input())

try:
    graph = create_graph(num_new_vertices)
except ValueError as e:
    print(e)