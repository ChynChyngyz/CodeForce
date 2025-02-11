import matplotlib.pyplot as plt
import networkx as nx
import random

def build_graph(additional_nodes):
    def is_graph_valid(G, initial_nodes, additional_nodes):
        for node in initial_nodes:
            if G.in_degree(node) + G.out_degree(node) != 2:
                return False

        for node in range(5, 5 + additional_nodes):
            degree = G.in_degree(node) + G.out_degree(node)
            if degree < 3:
                return False
        return True

    initial_nodes = [1, 2, 3, 4]
    max_attempts = 1000

    for attempt in range(max_attempts):
        G = nx.DiGraph()
        G.add_nodes_from(initial_nodes)

        for node in initial_nodes:
            targets = random.sample([n for n in initial_nodes if n != node], 2)
            G.add_edge(node, targets[0])
            G.add_edge(targets[1], node)

        current_last_node = 4
        for _ in range(additional_nodes):
            current_last_node += 1
            G.add_node(current_last_node)

            sources = random.sample(list(G.nodes()), 3)
            for src in sources:
                G.add_edge(src, current_last_node)
                G.add_edge(current_last_node, src)

        if is_graph_valid(G, initial_nodes, additional_nodes):
            # Рисуем граф
            pos = nx.spring_layout(G)
            node_colors = ['lightgreen' if n in initial_nodes else 'lightblue' for n in G.nodes()]
            nx.draw(G, pos,
                    with_labels=True,
                    node_color=node_colors,
                    edge_color='gray',
                    node_size=800,
                    font_size=10)
            plt.title("Custom Graph")
            plt.show()
            return "Норм" if nx.is_strongly_connected(G) else "Не норм"

    return "Неа".format(max_attempts)

additional_nodes = int(input("Введите количество дополнительных вершин: "))
result = build_graph(additional_nodes)
print(result)