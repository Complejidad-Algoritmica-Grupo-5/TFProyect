import networkx as nx
import matplotlib.pyplot as plt

# Función para cargar los datos del grafo
def load_graph_data():
    nodes = {}
    edges = {}

    with open('data/nodes.txt', 'r') as nodes_file:
        for line in nodes_file:
            data = line.split()
            node_id = int(data[0])
            x_coordinate = float(data[1])
            y_coordinate = float(data[2])
            nodes[node_id] = {'x': x_coordinate, 'y': y_coordinate, 'neighbors': {}}

    with open('data/edges.txt', 'r') as edges_file:
        for line in edges_file:
            data = line.split()
            edge_id = int(data[0])
            start_node = int(data[1])
            end_node = int(data[2])
            weight = float(data[3])
            edges[edge_id] = {'start_node': start_node, 'end_node': end_node, 'weight': weight}
            if start_node in nodes:
                nodes[start_node]['neighbors'][end_node] = weight

    return nodes, edges

# Cargamos los datos del grafo
nodes, edges = load_graph_data()

# Creamos el grafo
G = nx.Graph()

# Añadimos los nodos
G.add_nodes_from(nodes.keys())

# Añadimos las aristas
for edge in edges.values():
    G.add_edge(edge['start_node'], edge['end_node'], weight=edge['weight'])

# Creamos el diseño del grafo
pos = nx.spring_layout(G)

# Graficamos el grafo
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", font_color="black")
plt.title("Grafo del Camino Más Corto")
plt.show()