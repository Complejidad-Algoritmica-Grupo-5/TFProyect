import tkinter as tk
from tkinter import messagebox
from graph_visualization import visualize_shortest_path

def is_valid_number(entry):
    try:
        int(entry.get())
        return True
    except ValueError:
        return False

def visualize_path(start_entry, end_entry):
    if is_valid_number(start_entry) and is_valid_number(end_entry):
        start_node = int(start_entry.get())
        end_node = int(end_entry.get())
        visualize_shortest_path(start_node, end_node)
    else:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def add_hour_entry(frame):
    hour_label = tk.Label(frame, text="Hora:", font=("Arial", 12))
    hour_label.grid(row=2, column=0, padx=5, pady=5)

    hour_entry = tk.Entry(frame, font=("Arial", 12))
    hour_entry.grid(row=2, column=1, padx=5, pady=5)

def main():
    window = tk.Tk()
    window.title("Visualizador de Ruta Más Corta")
    window.geometry('400x400')

    title_label = tk.Label(window, text="Ingrese los Nodos Inicial y Final", font=("Arial", 16))
    title_label.pack(pady=20)

    frame = tk.Frame(window)
    frame.pack(padx=20, pady=10)

    start_label = tk.Label(frame, text="Nodo Inicial:", font=("Arial", 12))
    start_label.grid(row=0, column=0, padx=5, pady=5)

    start_entry = tk.Entry(frame, font=("Arial", 12))
    start_entry.grid(row=0, column=1, padx=5, pady=5)

    end_label = tk.Label(frame, text="Nodo Final:", font=("Arial", 12))
    end_label.grid(row=1, column=0, padx=5, pady=5)

    end_entry = tk.Entry(frame, font=("Arial", 12))
    end_entry.grid(row=1, column=1, padx=5, pady=5)

    def visualize_and_center():
        visualize_path(start_entry, end_entry)

    visualize_button = tk.Button(window, text="Visualizar Ruta", command=visualize_and_center, font=("Arial", 12))
    visualize_button.pack(pady=10)

    def add_hour():
        add_hour_entry(frame)

    load_map_button = tk.Button(window, text="Incluir hora", command=add_hour, font=("Arial", 12))
    load_map_button.pack(pady=10)

    center_window(window)
    window.mainloop()

if __name__ == "__main__":
    main()
