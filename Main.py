import tkinter as tk
from tkinter import messagebox

def abrir_settings():
    messagebox.showinfo("Settings", "Aquí configuraremos el archivo JSON luego")

root = tk.Tk()
root.title("App de Configuracion")
root.geometry("1800x900")

menubar = tk.Menu(root)

menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

menu_edicion = tk.Menu(menubar, tearoff=0)
menu_edicion.add_command(label="Copiar")
menubar.add_cascade(label="Edicion", menu=menu_edicion)

menu_ver = tk.Menu(menubar, tearoff=0)
menu_ver.add_command(label="Zoom")
menubar.add_cascade(label="Ver", menu=menu_ver)

menubar.add_command(label="Settings", command=abrir_settings)

root.config(menu=menubar)
root.mainloop()