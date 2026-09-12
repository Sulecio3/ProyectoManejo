import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import json
import os

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "nombre_usuario": "Usuario",
    "tema": "claro",
    "idioma": "es",
    "tamano_fuente": 12,
    "color_barra": "#FFFFFF",
    "color_letra": "#000000",
    "foto_perfil": ""
}

def cargar_configuracion():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_CONFIG.copy()
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return DEFAULT_CONFIG.copy()

config_actual = cargar_configuracion()

def abrir_settings():
    ventana_settings = tk.Toplevel(root)
    ventana_settings.title("Configuracion de Usuario")
    ventana_settings.geometry("600x600")

    tk.Label(ventana_settings, text="Nombre de usuario:").pack(pady=2)
    entry_usuario = tk.Entry(ventana_settings)
    entry_usuario.insert(0, config_actual.get("nombre_usuario", ""))
    entry_usuario.pack(pady=2)

    tk.Label(ventana_settings, text="Tema (claro/oscuro):").pack(pady=2)
    entry_tema = tk.Entry(ventana_settings)
    entry_tema.insert(0, config_actual.get("tema", ""))
    entry_tema.pack(pady=2)

    tk.Label(ventana_settings, text="Idioma (es/en):").pack(pady=2)
    entry_idioma = tk.Entry(ventana_settings)
    entry_idioma.insert(0, config_actual.get("idioma", ""))
    entry_idioma.pack(pady=2)

    tk.Label(ventana_settings, text="Tamaño de fuente:").pack(pady=2)
    entry_fuente = tk.Entry(ventana_settings)
    entry_fuente.insert(0, str(config_actual.get("tamano_fuente", "")))
    entry_fuente.pack(pady=2)

    def elegir_color_barra():
        colorchooser.askcolor(title="Elegir color de barra")
        
    tk.Button(ventana_settings, text="Color Barra Menu", command=elegir_color_barra).pack(pady=5)

    def elegir_color_letra():
        colorchooser.askcolor(title="Elegir color de letra")
        
    tk.Button(ventana_settings, text="Color de Letra", command=elegir_color_letra).pack(pady=5)

    def elegir_foto():
        filedialog.askopenfilename(title="Seleccionar foto de perfil")

    tk.Button(ventana_settings, text="Seleccionar Foto", command=elegir_foto).pack(pady=5)

    tk.Button(ventana_settings, text="Guardar").pack(pady=10)

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