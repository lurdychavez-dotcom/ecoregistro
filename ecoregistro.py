# EcoRegistro - Sistema de control de materiales reciclables
# Copyright (C) 2026 Equipo EcoRegistro
#
# Este programa es software libre: puedes redistribuirlo y/o modificarlo
# bajo los términos de la GNU General Public License, versión 3 o
# (a tu elección) cualquier versión posterior.
#
# Este programa se distribuye con la esperanza de que sea útil,
# pero SIN NINGUNA GARANTÍA. Consulta la licencia para más detalles.
#
# Texto completo de la licencia: https://www.gnu.org/licenses/gpl-3.0.html
 
import tkinter as tk
from tkinter import messagebox
 
# Lista que almacena los registros mientras la aplicación está abierta.
materiales = []
 
 
def actualizar_total():
    """Calcula y muestra la suma de kilogramos registrados."""
    total = sum(cantidad for nombre, cantidad in materiales)
    etiqueta_total.config(
        text=f"Total reciclado: {total:.2f} kg"
    )
 
 
def registrar():
    """Valida y agrega un material a la lista."""
    nombre = entrada_material.get().strip()
 
    try:
        cantidad = float(entrada_cantidad.get())
 
        if nombre == "":
            messagebox.showwarning("Dato faltante", "Escribe el nombre del material.")
            return
 
        if cantidad <= 0:
            messagebox.showwarning("Cantidad inválida", "La cantidad debe ser mayor que cero.")
            return
 
        materiales.append((nombre, cantidad))
        lista.insert(tk.END, f"{nombre} - {cantidad:.2f} kg")
 
        entrada_material.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)
        actualizar_total()
 
    except ValueError:
        messagebox.showerror("Dato inválido", "Escribe una cantidad numérica, por ejemplo 2.5.")
 
 
def eliminar():
    """Elimina el registro seleccionado y actualiza el total."""
    seleccion = lista.curselection()
 
    if not seleccion:
        messagebox.showwarning("Selección requerida", "Selecciona un registro para eliminar.")
        return
 
    indice = seleccion[0]
    lista.delete(indice)
    materiales.pop(indice)
    actualizar_total()
 
 
# Crear y configurar la ventana principal.
ventana = tk.Tk()
ventana.title("EcoRegistro - Control de reciclaje")
ventana.geometry("460x470")
ventana.config(bg="#E8F5E9")
ventana.resizable(False, False)
 
# Título.
tk.Label(
    ventana,
    text="ECOREGISTRO",
    font=("Arial", 20, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20"
).pack(pady=15)
 
# Campo para el nombre del material.
tk.Label(
    ventana,
    text="Nombre del material:",
    bg="#E8F5E9"
).pack()
 
entrada_material = tk.Entry(ventana, width=32, font=("Arial", 11))
entrada_material.pack(pady=5)
 
# Campo para la cantidad.
tk.Label(
    ventana,
    text="Cantidad en kilogramos:",
    bg="#E8F5E9"
).pack()
 
entrada_cantidad = tk.Entry(ventana, width=32, font=("Arial", 11))
entrada_cantidad.pack(pady=5)
 
# Botón para registrar.
tk.Button(
    ventana,
    text="Registrar material",
    command=registrar,
    bg="#4CAF50",
    fg="white",
    width=22
).pack(pady=10)
 
# Lista donde se muestran los registros.
lista = tk.Listbox(ventana, width=45, height=10, font=("Arial", 10))
lista.pack(pady=8)
 
# Botón para eliminar.
tk.Button(
    ventana,
    text="Eliminar registro seleccionado",
    command=eliminar,
    bg="#E53935",
    fg="white",
    width=28
).pack(pady=5)
 
# Etiqueta del total.
etiqueta_total = tk.Label(
    ventana,
    text="Total reciclado: 0.00 kg",
    font=("Arial", 13, "bold"),
    bg="#E8F5E9",
    fg="#1B5E20"
)
etiqueta_total.pack(pady=15)
 
# Mantener la ventana abierta y responder a las acciones del usuario.
ventana.mainloop()

