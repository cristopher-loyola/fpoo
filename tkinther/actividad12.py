from tkinter import Tk, Frame, Button, Label, messagebox, Entry
import tkinter as tk

class Login:
    def criar_login(self, objPeople):
        def executar_validacao():
            status = objPeople.validar_usuario(var1.get(), var2.get())
            if status:
                print(messagebox.showinfo('Bem-vindo', 'Acesso Concedido'))
            else:
                print(messagebox.showerror('Erro', 'Usuário não encontrado'))

        Ventana = Tk()
        Ventana.title("Login de Pessoa")
        Ventana.geometry("600x400")
        seccion1 = Frame(Ventana)
        seccion1.pack(expand=True, fill='both')
        Label(seccion1, text="Login FP00", bg="black", fg="white", font=("Mono", 18)).pack()
        var1 = tk.StringVar()
        Label(seccion1, text="Usuário:", font=("Helvetica", 14)).pack()
        Entry(seccion1, takefocus=True, textvariable=var1).pack()
        var2 = tk.StringVar()
        Label(seccion1, text="Senha:", font=("Helvetica", 14)).pack()
        Entry(seccion1, show="+", textvariable=var2).pack()
        botonAcessar = Button(seccion1, text="Acessar", command=executar_validacao)
        botonAcessar.pack()
        Ventana.mainloop()

# Exemplo de uso
# Substitua objPeople.validar_usuario por sua lógica de validação de usuário
# objPeople é um objeto que tem o método validar_usuario implementado
# Aqui está um exemplo simplificado apenas para demonstração

class People:
    def validar_usuario(self, usuario, senha):
        # Lógica de validação simplificada apenas para demonstração
        if usuario == "admin" and senha == "admin":
            return True
        else:
            return False

# Criando uma instância de People
people_instance = People()

# Criando uma instância de Login e chamando o método criar_login
login_instance = Login()
login_instance.criar_login(people_instance)
