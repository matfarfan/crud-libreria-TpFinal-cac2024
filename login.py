from tkinter import Label, Entry, Button, messagebox, Tk
from LibreriaApp import crear_ventana_principal
from database import cargar_usuarios

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingresar a Gestión de la Librería")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f8ff")

        Label(root, text="Usuario", bg="#f0f8ff", fg="#000080", font=("Arial", 12)).pack(pady=10)
        self.username_entry = Entry(root, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        Label(root, text="Contraseña", bg="#f0f8ff", fg="#000080", font=("Arial", 12)).pack(pady=10)
        self.password_entry = Entry(root, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        Button(root, text="Login", command=self.login, bg="#000080", fg="#f0f8ff", font=("Arial", 12)).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        usuarios = cargar_usuarios()
        if any(usuario for usuario in usuarios if usuario['username'] == username and usuario['password'] == password):
            self.root.destroy()
            new_root = Tk()
            crear_ventana_principal(new_root)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")

def iniciar_login(root):
    Login(root)