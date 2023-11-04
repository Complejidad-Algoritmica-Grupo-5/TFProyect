from graph_visualization import visualize_shortest_path

def main():
    start_node = int(input("Ingrese el nodo inicial: "))
    end_node = int(input("Ingrese el nodo final: "))
    visualize_shortest_path(start_node, end_node)

if __name__ == "__main__":
    main()
    
