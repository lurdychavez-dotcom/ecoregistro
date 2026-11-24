
import tkinter as tk
from tkinter import messagebox

# Lista para guardar los materiales
materiales = []

# Funcion para registrar materiales
def registrar():

    nombre = entrada_material.get()

    try:
        cantidad = float(entrada_cantidad.get())

        if nombre.strip() == "" or cantidad <= 0:
            messagebox.showwarning("Aviso", "Ingresa datos validos")
            return

        materiales.append((nombre, cantidad))

        lista.insert(tk.END, nombre + " - " + str(cantidad) + " kg")

        entrada_material.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)

        actualizar_total()

    except ValueError:
        messagebox.showerror("Error", "Ingresa una cantidad numerica")

# Funcion para calcular el total
def actualizar_total():

    total = sum(cantidad for nombre, cantidad in materiales)

    etiqueta_total.config(
        text="Total reciclado: " + str(round(total, 2)) + " kg"
    )

# Funcion para eliminar materiales
def eliminar():

    seleccion = lista.curselection()

    if seleccion:
        indice = seleccion[0]

        lista.delete(indice)
        materiales.pop(indice)

        actualizar_total()

    else:
        messagebox.showwarning("Aviso", "Selecciona un registro")

# Crear ventana
ventana = tk.Tk()
ventana.title("EcoRegistro - Software Libre")
ventana.geometry("430x450")
ventana.config(bg="#E8F5E9")

# Titulo
tk.Label(
    ventana,
    text="ECOREGISTRO",
    font=("Arial", 20, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20"
).pack(pady=15)

# Campo material
tk.Label(
    ventana,
    text="Nombre del material:",
    bg="#E8F5E9"
).pack()

entrada_material = tk.Entry(ventana, width=30)
entrada_material.pack(pady=5)

# Campo cantidad
tk.Label(
    ventana,
    text="Cantidad en kilogramos:",
    bg="#E8F5E9"
).pack()

entrada_cantidad = tk.Entry(ventana, width=30)
entrada_cantidad.pack(pady=5)

# Boton registrar
tk.Button(
    ventana,
    text="Registrar material",
    command=registrar,
    bg="#4CAF50",
    fg="white",
    width=22
).pack(pady=10)

# Lista de materiales
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Boton eliminar
tk.Button(
    ventana,
    text="Eliminar registro",
    command=eliminar,
    bg="#E53935",
    fg="white",
    width=22
).pack(pady=5)

# Total
etiqueta_total = tk.Label(
    ventana,
    text="Total reciclado: 0 kg",
    font=("Arial", 13, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20"
)
etiqueta_total.pack(pady=15)

# Ejecutar
ventana.mainloop()
