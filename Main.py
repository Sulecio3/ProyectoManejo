import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser
import json
import os
import shutil

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
    except json.JSONDecodeError:
        messagebox.showwarning("Aviso", "El archivo esta corrupto, se va a usar valores por defecto")
        return DEFAULT_CONFIG.copy()
    except PermissionError:
        messagebox.showerror("Error", "No hay permisos para leer el archvo")
        return DEFAULT_CONFIG.copy()
    except:
        return DEFAULT_CONFIG.copy()

config_actual = cargar_configuracion()
color_barra_temp = config_actual.get("color_barra", "#FFFFFF")
color_letra_temp = config_actual.get("color_letra", "#000000")
foto_temp = config_actual.get("foto_perfil", "")
img_perfil = None

def aplicar_configuracion():
    global img_perfil
    try:
        fuente = ("Arial", config_actual.get("tamano_fuente", 12))
        lbl_bienvenida.config(
            text=f"Bienvenido, {config_actual.get('nombre_usuario', 'Usuario')}",
            font=fuente,
            fg=config_actual.get("color_letra", "#000000")
        )
        if config_actual.get("tema", "").lower() == "oscuro":
            root.config(bg="#333333")
            lbl_bienvenida.config(bg="#333333")
            lbl_imagen.config(bg="#333333")
        else:
            root.config(bg="#FFFFFF")
            lbl_bienvenida.config(bg="#FFFFFF")
            lbl_imagen.config(bg="#FFFFFF")
        
        color_b = config_actual.get("color_barra", "#FFFFFF")
        color_l = config_actual.get("color_letra", "#000000")
        barra_menu.config(bg=color_b)
        btn_archivo.config(bg=color_b, fg=color_l)
        btn_edicion.config(bg=color_b, fg=color_l)
        btn_ver.config(bg=color_b, fg=color_l)
        btn_settings.config(bg=color_b, fg=color_l)
        
        ruta_foto = config_actual.get("foto_perfil", "")
        if ruta_foto and os.path.exists(ruta_foto):
            img_perfil = tk.PhotoImage(file=ruta_foto)
            lbl_imagen.config(image=img_perfil)
    except:
        pass

def abrir_settings():
    global color_barra_temp, color_letra_temp, foto_temp
    
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
    entry_fuente.insert(0, str(config_actual.get("tamano_fuente", "12")))
    entry_fuente.pack(pady=2)

    def elegir_color_barra():
        global color_barra_temp
        color = colorchooser.askcolor(title="Elegir color de barra")[1]
        if color:
            color_barra_temp = color
        
    tk.Button(ventana_settings, text="Color Barra Menu", command=elegir_color_barra).pack(pady=5)

    def elegir_color_letra():
        global color_letra_temp
        color = colorchooser.askcolor(title="Elegir color de letra")[1]
        if color:
            color_letra_temp = color
        
    tk.Button(ventana_settings, text="Color de Letra", command=elegir_color_letra).pack(pady=5)

    def elegir_foto():
        global foto_temp
        ruta = filedialog.askopenfilename(title="Seleccionar foto de perfil")
        if ruta:
            foto_temp = ruta

    tk.Button(ventana_settings, text="Seleccionar Foto", command=elegir_foto).pack(pady=5)

    def guardar():
        config_actual["nombre_usuario"] = entry_usuario.get()
        config_actual["tema"] = entry_tema.get()
        config_actual["idioma"] = entry_idioma.get()
        try:
            config_actual["tamano_fuente"] = int(entry_fuente.get())
        except:
            config_actual["tamano_fuente"] = 12
        config_actual["color_barra"] = color_barra_temp
        config_actual["color_letra"] = color_letra_temp
        config_actual["foto_perfil"] = foto_temp
        
        try:
            if os.path.exists(CONFIG_FILE):
                shutil.copy(CONFIG_FILE, "config.bak")
                
            with open("config.tmp", "w", encoding="utf-8") as f:
                json.dump(config_actual, f, ensure_ascii=False, indent=4)
            os.replace("config.tmp", CONFIG_FILE)
            
            aplicar_configuracion()
            messagebox.showinfo("Exito", "Configuracion guardada y aplicada")
            ventana_settings.destroy()
        except PermissionError:
            messagebox.showerror("Error", "Sin permisos para escribir el archivo")
        except Exception as e:
            messagebox.showerror("Error", "Ocurrio un problema al guardar")

    tk.Button(ventana_settings, text="Guardar", command=guardar).pack(pady=10)

root = tk.Tk()
root.title("App de Configuracion")
root.geometry("1800x900")

barra_menu = tk.Frame(root)
barra_menu.pack(side=tk.TOP, fill=tk.X)

btn_archivo = tk.Menubutton(barra_menu, text="Archivo", relief=tk.FLAT)
menu_archivo = tk.Menu(btn_archivo, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
btn_archivo.config(menu=menu_archivo)
btn_archivo.pack(side=tk.LEFT, padx=5, pady=2)

btn_edicion = tk.Menubutton(barra_menu, text="Edicion", relief=tk.FLAT)
menu_edicion = tk.Menu(btn_edicion, tearoff=0)
menu_edicion.add_command(label="Copiar")
btn_edicion.config(menu=menu_edicion)
btn_edicion.pack(side=tk.LEFT, padx=5, pady=2)

btn_ver = tk.Menubutton(barra_menu, text="Ver", relief=tk.FLAT)
menu_ver = tk.Menu(btn_ver, tearoff=0)
menu_ver.add_command(label="Zoom")
btn_ver.config(menu=menu_ver)
btn_ver.pack(side=tk.LEFT, padx=5, pady=2)

btn_settings = tk.Button(barra_menu, text="Settings", command=abrir_settings, relief=tk.FLAT)
btn_settings.pack(side=tk.LEFT, padx=5, pady=2)

lbl_imagen = tk.Label(root)
lbl_imagen.pack(pady=20)
lbl_bienvenida = tk.Label(root, text="Bienvenido")
lbl_bienvenida.pack(expand=True)

aplicar_configuracion()
root.mainloop()