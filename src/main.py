import tkinter as tk
from graph_visualization import visualize_shortest_path


def main():
    window = tk.Tk()
    window.title("Visualizador de Ruta Más Corta")

    start_label = tk.Label(window, text="Nodo Inicial:")
    start_entry = tk.Entry(window)
    start_label.pack()
    start_entry.pack()

    end_label = tk.Label(window, text="Nodo Final:")
    end_entry = tk.Entry(window)
    end_label.pack()
    end_entry.pack()

    def visualize_path():
        start_node = int(start_entry.get())
        end_node = int(end_entry.get())
        visualize_shortest_path(start_node, end_node)

    visualize_button = tk.Button(window, text="Visualizar Ruta", command=visualize_path)
    visualize_button.pack()

    window.mainloop()

if __name__ == "__main__":
    main()
