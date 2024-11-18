# gui.py
import tkinter as tk
from tkinter import ttk

class LaundryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lavandería")
        self.root.geometry("600x400")

        # Crear un frame de bienvenida
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both", expand=True)

        # Label de bienvenida
        welcome_label = tk.Label(self.main_frame, text="Bienvenidos a la Lavandería", font=("Arial", 16))
        welcome_label.pack(pady=20)

        # Botones para las secciones
        tk.Button(self.main_frame, text="Registrar Pedido", command=self.open_pedidos).pack(pady=10)
        tk.Button(self.main_frame, text="Ver Finanzas", command=self.open_finanzas).pack(pady=10)
        tk.Button(self.main_frame, text="Gestionar Clientes", command=self.open_clientes).pack(pady=10)

    def open_pedidos(self):
        print("Abrir sección de pedidos")

    def open_finanzas(self):
        print("Abrir sección de finanzas")

    def open_clientes(self):
        print("Abrir sección de clientes")

if __name__ == "__main__":
    root = tk.Tk()
    app = LaundryApp(root)
    root.mainloop()
