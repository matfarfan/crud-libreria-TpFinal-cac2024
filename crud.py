import tkinter as tk
from tkinter import simpledialog, messagebox, Toplevel, Label, Entry, Button
from database import cargar_productos, guardar_productos

#Función que crea un frame para poder mostrar lista con scrollbar
def agregar_frame_lista(parent):
    frame_lista = tk.Frame(parent, bg="#f0f8ff")
    frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    text_widget = tk.Text(frame_lista, yscrollcommand=scrollbar.set, wrap=tk.WORD, font=("Arial", 12), bg="#ffffff", fg="#000000")
    text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

    scrollbar.config(command=text_widget.yview)

    return text_widget

#Función para agregar libro
def agregar_libro_ui(frame):
    #Limpia el frame
    for widget in frame.winfo_children():
        widget.destroy()

    #Agrega título
    tk.Label(frame, text="Agregar Libro", bg="#f0f8ff", font=("Arial", 18, "bold")).pack(pady=10)

    #Función para obtener los datos nuevos y los valida
    def guardar_libro():
        nombre = entry_nombre.get()
        autor = entry_autor.get()
        descripcion = entry_descripcion.get()
        genero = entry_genero.get()
        precio = entry_precio.get()

        if nombre and autor and descripcion and genero and precio:
            try:
                #Guarda en base de datos productos.json
                precio = float(precio)
                productos = cargar_productos()
                productos.append({'nombre': nombre, 'autor': autor, 'descripcion': descripcion, 'genero': genero, 'precio': precio})
                guardar_productos(productos)
                messagebox.showinfo("Agregar Libro", "Libro agregado exitosamente.", parent=ventana)
                ventana.destroy()
            except ValueError:
                messagebox.showwarning("Agregar Libro", "El precio debe ser un número válido.", parent=ventana)
        else:
            messagebox.showwarning("Agregar Libro", "Debe ingresar todos los campos.", parent=ventana)

    #Crea una ventana emergente
    ventana = Toplevel(frame)
    ventana.title("Agregar Libro")
    ventana.geometry("500x400")
    ventana.configure(bg="#f0f8ff")

    #Configura la ventana emergente y entrada de datos
    Label(ventana, text="Nombre:", bg="#f0f8ff").pack(pady=5)
    entry_nombre = Entry(ventana)
    entry_nombre.pack(pady=5)

    Label(ventana, text="Autor:", bg="#f0f8ff").pack(pady=5)
    entry_autor = Entry(ventana)
    entry_autor.pack(pady=5)

    Label(ventana, text="Descripción:", bg="#f0f8ff").pack(pady=5)
    entry_descripcion = Entry(ventana)
    entry_descripcion.pack(pady=5)

    Label(ventana, text="Género:", bg="#f0f8ff").pack(pady=5)
    entry_genero = Entry(ventana)
    entry_genero.pack(pady=5)

    Label(ventana, text="Precio:", bg="#f0f8ff").pack(pady=5)
    entry_precio = Entry(ventana)
    entry_precio.pack(pady=5)

    #Crea botón para guardar
    Button(ventana, text="Guardar", command=guardar_libro).pack(pady=20)

#Función para listar libros
def listar_libros_ui(frame):
    #Limpieza del frame
    for widget in frame.winfo_children():
        widget.destroy()

    #Agrega título
    tk.Label(frame, text="Listar Libros", bg="#f0f8ff", font=("Arial", 18, "bold")).pack(pady=10)

    #Crea el frame llamando a la funcion agregar_frame_lista 
    text_widget = agregar_frame_lista(frame)
    #Carga productos
    productos = cargar_productos()

    #Muestra los datos iterando la lista
    if productos:
        for producto in productos:
            nombre = producto['nombre']
            autor = producto['autor']
            descripcion = producto['descripcion']
            genero = producto['genero']
            precio = producto['precio']
            
            # Formato de presentación en el Text widget
            text_widget.insert(tk.END, f"Nombre: {nombre}\nAutor: {autor}\nGénero: {genero}\nPrecio: ${precio}\nDescripción: {descripcion}\n")
            text_widget.insert(tk.END, "--------------------------------------------------\n")
    else:
        text_widget.insert(tk.END, "No hay libros disponibles.")

#Función para buscar libro
def buscar_libro_ui(frame):
    #Limpieza del frame
    for widget in frame.winfo_children():
        widget.destroy()

    #Agrega título y crea widget
    tk.Label(frame, text="Buscar Libro", bg="#f0f8ff", font=("Arial", 18, "bold")).pack(pady=10)
    text_widget = agregar_frame_lista(frame)

    # Crear una nueva ventana para la selección de la categoría
    categoria_window = tk.Toplevel(frame)
    categoria_window.title("Seleccionar Categoría")
    tk.Label(categoria_window, text="Seleccione la categoría para buscar:", font=("Arial", 14)).pack(pady=10)

    # Variable para almacenar la categoría seleccionada
    categoria_seleccionada = tk.StringVar(value="nombre")

    # Opciones de categorías con iteracion
    categorias = ["nombre", "autor", "genero"]
    for cat in categorias:
        tk.Radiobutton(categoria_window, text=cat.capitalize(), variable=categoria_seleccionada, value=cat, font=("Arial", 12)).pack(anchor=tk.W)

    # Botón para confirmar la selección
    def confirmar_categoria():
        #Destruye la ventana
        categoria_window.destroy()
        termino = simpledialog.askstring("Buscar Libro", f"Ingrese el término de búsqueda para {categoria_seleccionada.get()}:", parent=frame)

        if termino:
            #Carga json
            productos = cargar_productos()
            #filtra iterando y busca
            resultados = [producto for producto in productos if termino.lower() in producto[categoria_seleccionada.get()].lower()]

            #itera y muestra
            if resultados:
                for producto in resultados:
                    nombre = producto['nombre']
                    autor = producto['autor']
                    descripcion = producto['descripcion']
                    genero = producto['genero']
                    precio = producto['precio']

                    # Formato de presentación en el Text widget
                    text_widget.insert(tk.END, f"Nombre: {nombre}\nAutor: {autor}\nGénero: {genero}\nPrecio: ${precio}\nDescripción: {descripcion}\n")
                    text_widget.insert(tk.END, "--------------------------------------------------\n")
            else:
                text_widget.insert(tk.END, f"No se encontraron resultados para '{termino}' en la categoría '{categoria_seleccionada.get()}'.")
        else:
            messagebox.showwarning("Buscar Libro", "Debe ingresar un término de búsqueda válido.", parent=frame)
    #Boton para confirmar
    tk.Button(categoria_window, text="Confirmar", command=confirmar_categoria, font=("Arial", 12)).pack(pady=10)

#Función para eliminar libro
def eliminar_libro_ui(frame):
    #Limpieza del frame
    for widget in frame.winfo_children():
        widget.destroy()

    #Agrega título y crea widget
    tk.Label(frame, text="Eliminar Libro", bg="#f0f8ff", font=("Arial", 18, "bold")).pack(pady=10)
    text_widget = agregar_frame_lista(frame)
    
    nombre_libro = simpledialog.askstring("Eliminar Libro", "Ingrese el nombre del libro a eliminar:", parent=frame)

    #Verifica, itera y borra
    if nombre_libro:
        productos = cargar_productos()
        libro_encontrado = next((producto for producto in productos if producto['nombre'].lower() == nombre_libro.lower()), None)

        if libro_encontrado:
            productos.remove(libro_encontrado)
            guardar_productos(productos)
            text_widget.insert(tk.END, f"Libro '{nombre_libro}' eliminado exitosamente.\n")
        else:
            text_widget.insert(tk.END, f"No se encontró un libro con el nombre '{nombre_libro}'.\n")
    else:
        messagebox.showwarning("Eliminar Libro", "Debe ingresar un nombre de libro válido.", parent=frame)

#Función para actualizar libro
def actualizar_libro_ui(frame):
    #Limpieza del frame
    for widget in frame.winfo_children():
        widget.destroy()

    #Agrega título y crea widget
    tk.Label(frame, text="Actualizar Libro", bg="#f0f8ff", font=("Arial", 18, "bold")).pack(pady=10)

    nombre_libro = simpledialog.askstring("Actualizar Libro", "Ingrese el nombre del libro a actualizar:", parent=frame)

    if nombre_libro:
        productos = cargar_productos()
        libro_encontrado = next((producto for producto in productos if producto['nombre'].lower() == nombre_libro.lower()), None)

        if libro_encontrado:
            #Nueva ventana para carga de datos
            ventana = Toplevel(frame)
            ventana.title("Actualizar Libro")
            ventana.geometry("400x400")
            ventana.configure(bg="#f0f8ff")

            Label(ventana, text="Nuevo Nombre (deje en blanco para no cambiar):", bg="#f0f8ff").pack(pady=5)
            entry_nombre = Entry(ventana)
            entry_nombre.pack(pady=5)

            Label(ventana, text="Nuevo Autor (deje en blanco para no cambiar):", bg="#f0f8ff").pack(pady=5)
            entry_autor = Entry(ventana)
            entry_autor.pack(pady=5)

            Label(ventana, text="Nueva Descripción (deje en blanco para no cambiar):", bg="#f0f8ff").pack(pady=5)
            entry_descripcion = Entry(ventana)
            entry_descripcion.pack(pady=5)

            Label(ventana, text="Nuevo Género (deje en blanco para no cambiar):", bg="#f0f8ff").pack(pady=5)
            entry_genero = Entry(ventana)
            entry_genero.pack(pady=5)

            Label(ventana, text="Nuevo Precio (deje en blanco para no cambiar):", bg="#f0f8ff").pack(pady=5)
            entry_precio = Entry(ventana)
            entry_precio.pack(pady=5)

            #Función para actualizar, si se ingreso dato se actualiza, sino se mantiene el anterior
            def guardar_actualizacion():
                nuevo_nombre = entry_nombre.get()
                nuevo_autor = entry_autor.get()
                nueva_descripcion = entry_descripcion.get()
                nuevo_genero = entry_genero.get()
                nuevo_precio = entry_precio.get()

                if nuevo_nombre:
                    libro_encontrado['nombre'] = nuevo_nombre
                if nuevo_autor:
                    libro_encontrado['autor'] = nuevo_autor
                if nueva_descripcion:
                    libro_encontrado['descripcion'] = nueva_descripcion
                if nuevo_genero:
                    libro_encontrado['genero'] = nuevo_genero
                if nuevo_precio:
                    try:
                        libro_encontrado['precio'] = float(nuevo_precio)
                    except ValueError:
                        messagebox.showwarning("Actualizar Libro", "El precio debe ser un número válido.", parent=ventana)
                        return

                guardar_productos(productos)
                messagebox.showinfo("Actualizar Libro", f"Libro '{nombre_libro}' actualizado exitosamente.", parent=ventana)
                ventana.destroy()

                # Mostrar el libro actualizado en el frame principal
                for widget in frame.winfo_children():
                    widget.destroy()

                tk.Label(frame, text="Libro Actualizado", bg="#f0f8ff", font=("Arial", 18, "bold")).pack(pady=10)

                detalles = (
                    f"Nombre: {libro_encontrado['nombre']}\n"
                    f"Autor: {libro_encontrado['autor']}\n"
                    f"Descripción: {libro_encontrado['descripcion']}\n"
                    f"Género: {libro_encontrado['genero']}\n"
                    f"Precio: ${libro_encontrado['precio']}\n"
                )
                tk.Label(frame, text=detalles, bg="#f0f8ff", justify=tk.LEFT, font=("Arial", 12)).pack(pady=10)
            #Botón para guardar
            Button(ventana, text="Guardar", command=guardar_actualizacion).pack(pady=20)
        else:
            messagebox.showwarning("Actualizar Libro", f"No se encontró un libro con el nombre '{nombre_libro}'.", parent=frame)
    else:
        messagebox.showwarning("Actualizar Libro", "Debe ingresar un nombre de libro válido.", parent=frame)