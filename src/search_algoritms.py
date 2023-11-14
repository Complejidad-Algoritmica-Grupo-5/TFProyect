import heapq
from data_processing import load_graph_data

import heapq

def calculate_traffic(weight, hour):
    # Calcula el factor de trafico
    if hour < 7 or hour >= 20:
        traffic_factor = 1.5
    elif hour >= 7 and hour < 10:
        traffic_factor = 1.2
    elif hour >= 10 and hour < 17:
        traffic_factor = 1.0
    else:
        traffic_factor = 0.8

    # Actualiza el peso de la arista
    return weight * traffic_factor

def dijkstra(graph, start, end, hour):
    distances = {node: float('inf') for node in graph['nodes']}
    distances[start] = 0
    queue = [(0, start)]
    predecessors = {node: None for node in graph['nodes']}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_node in graph['nodes'] and current_node in distances:
            for neighbor, weight in graph['nodes'][current_node]['neighbors'].items():
                distance = current_distance + weight * calculate_traffic(weight, hour)
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))
                    predecessors[neighbor] = current_node

    return distances, predecessors

def get_shortest_path(start, end, predecessors):
    path = []
    current_node = end
    while current_node is not None:
        path.insert(0, current_node)
        current_node = predecessors[current_node]
    return path

#Test
if __name__ == '__main__':
    graph_data = load_graph_data()
    graph = {'nodes': graph_data[0], 'edges': graph_data[1]}

    start_node = 11 
    end_node = 5985
    hour = int(input("Ingrese la hora: "))
    #hour=14
    distances, predecessors = dijkstra(graph, start_node, end_node, hour)
    shortest_path = get_shortest_path(start_node, end_node, predecessors)
    print(f"El camino más corto del punto {start_node} al punto {end_node} es el siguiente:")
    print(shortest_path)
    print(f"La distancia recorrida total es: {distances[end_node]}")
