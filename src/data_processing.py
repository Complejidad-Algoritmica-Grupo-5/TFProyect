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

#Test
if __name__ == "__main__":
    nodes, edges = load_graph_data()
    print("Nodes:")
    for node_id, node_data in list(nodes.items())[:5]:
        print(f"Node ID: {node_id}, Node Data: {node_data}")
    print("Edges:")
    for edge_id, edge_data in list(edges.items())[:5]:
        print(f"Edge ID: {edge_id}, Edge Data: {edge_data}")
