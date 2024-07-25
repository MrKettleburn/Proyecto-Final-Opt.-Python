import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función que se llama al presionar una tecla
def key_pressed(event):
    key = event.char
    play_sound(key)

# Configuración de la interfaz gráfica con tkinter
root = tk.Tk()
root.title("Teclado Musical")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Etiqueta para el Combobox
ttk.Label(frame, text="Selecciona una opción:").grid(column=0, row=0, padx=5, pady=5)

# Opciones para el Combobox
options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4"]

# Crear el Combobox
combobox = ttk.Combobox(frame, values=options)
combobox.grid(column=1, row=0, padx=5, pady=5)
combobox.current(0)  # Establecer la opción predeterminada

# Función para manejar el evento del botón
def show_selected():
    selected_option = combobox.get()
    messagebox.showinfo("Selección", f"Has seleccionado: {selected_option}")

# Crear un botón
button = ttk.Button(frame, text="Mostrar selección", command=show_selected)
button.grid(column=0, row=1, columnspan=2, padx=5, pady=5)

# Ajustar el diseño
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

play_initial_sound()

# Asociar la función de tecla presionada
root.bind("<Key>", key_pressed)

# Ejecutar la interfaz
root.mainloop()