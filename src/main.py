import tkinter as tk
from graph_visualization import visualize_shortest_path


class ShortestPathVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Visualizador de Ruta Más Corta")

        self.create_widgets()

    def create_widgets(self):
        start_label = tk.Label(self.master, text="Nodo Inicial:")
        start_label.pack()

        self.start_entry = tk.Entry(self.master)
        self.start_entry.pack()

        end_label = tk.Label(self.master, text="Nodo Final:")
        end_label.pack()

        self.end_entry = tk.Entry(self.master)
        self.end_entry.pack()

        visualize_button = tk.Button(self.master, text="Visualizar Ruta", command=self.visualize_path)
        visualize_button.pack()

    def visualize_path(self):
        try:
            start_node = int(self.start_entry.get())
            end_node = int(self.end_entry.get())
            visualize_shortest_path(start_node, end_node, graph_data)
        except ValueError:
            tk.messagebox.showerror("Error", "Ingrese números válidos para los nodos")


def main():
    window = tk.Tk()
    app = ShortestPathVisualizer(window)
    window.mainloop()


if __name__ == "__main__":
    main()

