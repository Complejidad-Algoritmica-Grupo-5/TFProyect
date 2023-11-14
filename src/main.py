def main():
    try:
        start_node = int(input("Ingrese el nodo inicial: "))
        end_node = int(input("Ingrese el nodo final: "))
        visualize_shortest_path(start_node, end_node, graph_data)
    except ValueError:
        print("Error: Ingrese números enteros para los nodos.")
    except FileNotFoundError:
        print("Error: No se encontraron archivos de datos en la ubicación especificada.")

if __name__ == "__main__":
    main()
    
