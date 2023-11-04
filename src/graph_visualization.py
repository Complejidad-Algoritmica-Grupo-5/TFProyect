import networkx as nx
import matplotlib.pyplot as plt
from data_processing import load_graph_data
from search_algoritms import dijkstra, get_shortest_path

def visualize_shortest_path(start_node, end_node):
    graph_data = load_graph_data()
    nodes, edges = graph_data

    G = nx.Graph()
    G.add_nodes_from(nodes.keys())

    for edge in edges.values():
        G.add_edge(edge['start_node'], edge['end_node'], weight=edge['weight'])

    pos = {node: (data['x'], data['y']) for node, data in nodes.items()}

    graph = {'nodes': graph_data[0], 'edges': graph_data[1]}
    distances, predecessors = dijkstra(graph, start_node, end_node)
    shortest_path = get_shortest_path(start_node, end_node, predecessors)
    print(f"El camino más corto del punto {start_node} al punto {end_node} es el siguiente:")
    print(shortest_path)
    print(f"La distancia recorrida total es: {distances[end_node]}")
    #Si quieren ver todas las posibles opciones para start_node y end_node: pongan el with_labels=True y usando el zoom ustedes mismos busquen los caminos posibles
    nx.draw(G, pos, with_labels=False, node_size=30, node_color="skyblue", font_size=12, font_weight="bold", font_color="black", alpha=0.7, width=0.5, edge_color='gray')

    for i in range(len(shortest_path)-1):
        nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i+1])], edge_color='r', width=2)

    plt.title("Grafo del Camino Más Corto")
    plt.show()
