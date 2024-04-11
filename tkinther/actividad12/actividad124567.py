import tkinter as tk
import random
import string

def crear_contaseñas(length=8, mayusculas=False, caracteres_especiales=False):
    caracteres = string.ascii_lowercase
    if mayusculas:
        caracteres += string.ascii_uppercase
    if caracteres_especiales:
        caracteres += string.punctuation
    
    password = ''.join(random.choice(caracteres) for i in range(length))
    return password

def crear_contraseña():
    length = int(length_entry.get())
    mayusculas = uppercase_var.get()
    caracteres_especiales = special_chars_var.get()
    password = crear_contaseñas(length, mayusculas, caracteres_especiales)
    generar_contraseña.config(text=password)

ventana = tk.Tk()
ventana.title("contraseñas")
ventana.configure(bg='black')

length_label = tk.Label(ventana, text="Longitud:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(ventana)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "8") 

uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(ventana, text="Incluir Mayúsculas", variable=uppercase_var)
uppercase_checkbox.grid(row=1, column=0)

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(ventana, text="Incluir Caracteres Especiales", variable=special_chars_var)
special_chars_checkbox.grid(row=2, column=0)

generate_password_button = tk.Button(ventana, text="Generar Contraseña", command=crear_contraseña)
generate_password_button.grid(row=3, column=0)

generar_contraseña = tk.Label(ventana, text="")
generar_contraseña.grid(row=4, column=0)

ventana.mainloop()
