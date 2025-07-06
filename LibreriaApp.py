import tkinter as tk
from tkinter import PhotoImage, Scrollbar
from crud import (
    agregar_libro_ui, listar_libros_ui, buscar_libro_ui, eliminar_libro_ui, actualizar_libro_ui, agregar_frame_lista
)

def salir(root):
    root.destroy()

#Se crea ventana principal
def crear_ventana_principal(root=None):
    if root is None:
        root = tk.Tk()
    root.title("Gestión de Librería")
    root.geometry("800x600")
    root.configure(bg="#f0f8ff")

    #Creación de frame
    global main_frame
    main_frame = tk.Frame(root, bg="#f0f8ff")
    main_frame.pack(fill="both", expand=True)

    # Mensaje de bienvenida
    welcome_label = tk.Label(main_frame, text="¡BIENVENIDOS A LA GESTIÓN DE LIBRERÍA!", font=("Helvetica", 18), bg="#f0f8ff")
    welcome_label.pack(pady=10)
    
    # Cargar la imagen
    img = PhotoImage(file="imagen2.gif")
    
    # Crear un widget Label y asigna la imagen
    img_label = tk.Label(main_frame, image=img, bg="#f0f8ff")
    img_label.pack(pady=20)

    #Segundo mensaje
    description_label = tk.Label(main_frame, text="Utiliza el menú superior para gestionar los libros de la librería.", font=("Helvetica", 12), bg="#f0f8ff")
    description_label.pack(pady=5)
    
    menu = tk.Menu(root)
    root.config(menu=menu)

    #Se crea el menu cascada
    menu_libros = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Libros", menu=menu_libros)
    menu_libros.add_command(label="Agregar Libro", command=lambda: mostrar_agregar_libro(root))
    menu_libros.add_command(label="Listar Libros", command=lambda: mostrar_listar_libros(root))
    menu_libros.add_command(label="Buscar Libro", command=lambda: mostrar_buscar_libro(root))
    menu_libros.add_command(label="Eliminar Libro", command=lambda: mostrar_eliminar_libro(root))
    menu_libros.add_command(label="Actualizar Libro", command=lambda: mostrar_actualizar_libro(root))
    menu.add_command(label="Salir", command=lambda: salir(root))

    root.mainloop()

#Funciones que limpian el frame para ejecutarse
def mostrar_agregar_libro(root):
    limpiar_frame(main_frame)
    agregar_libro_ui(main_frame)

def mostrar_listar_libros(root):
    limpiar_frame(main_frame)
    listbox = agregar_frame_lista(main_frame)
    listar_libros_ui(listbox)

def mostrar_buscar_libro(root):
    limpiar_frame(main_frame)
    listbox = agregar_frame_lista(main_frame)
    buscar_libro_ui(listbox)

def mostrar_eliminar_libro(root):
    limpiar_frame(main_frame)
    listbox = agregar_frame_lista(main_frame)
    eliminar_libro_ui(listbox)

def mostrar_actualizar_libro(root):
    limpiar_frame(main_frame)
    listbox = agregar_frame_lista(main_frame)
    actualizar_libro_ui(listbox)

#Función para limpiar
def limpiar_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

