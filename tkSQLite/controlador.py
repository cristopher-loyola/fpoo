import tkinter as tk
from tkinter import messagebox, Text, Tk, ttk
import sqlite3
import bcrypt

class controlador:

    def conexion(self):
        try:
            conex = sqlite3.connect("C:\\Users\\USUARIO\\Documents\\github\\fpoo\\tkSQLite\\db195.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def encriptapass(self, cont):
        passPlana = cont
        passPlana = passPlana.encode()
        sal = bcrypt.gensalt()
        passHash = bcrypt.hashpw(passPlana, sal)
        return passHash
    
    def insertUsuario(self, nom, corr, cont):
        if nom == "" or corr == "" or cont == "":
            messagebox.showerror("Error", "¡Inputs vacíos no son permitidos!")
            return
        
        conH = self.encriptapass(cont)
        datos = (nom, corr, conH)
        sqlInsert = "INSERT INTO tbUsuarios(nombre, correo, contra) VALUES (?,?,?)"
        
        try:
            with self.conexion() as conexion:
                cursor = conexion.cursor()
                cursor.execute(sqlInsert, datos)
                conexion.commit()
                messagebox.showinfo("Éxito", "Usuario insertado exitosamente")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo insertar el usuario: {e}")
            
    def buscarUsuario(self, id):
        conex = self.conexion()
        if id == '':
            messagebox.showwarning("Cuidado", "inputs vacíos")
            conex.close()
        else:
            try:
                cursor = conex.cursor()
                sqlSelect = f"SELECT * FROM tbUsuarios WHERE id={id}"
                cursor.execute(sqlSelect)
                usuario = cursor.fetchone()
                conex.close()
                if usuario:
                    return usuario
                else:
                    messagebox.showwarning("Nada", "Id no existe en BD")
            except sqlite3.OperationalError:
                print("No se pudo ejecutar la búsqueda")
    def mostrarTodosUsuarios(self):
        conex = self.conexion()
        cursor = conex.cursor()
        try:
            cursor.execute("select * from tbUsuarios")
            usuarios = cursor.fetchall()
            conex.close()
            return usuarios
        except sqlite3.OperationalError:
            print("No existen registros aun")
            conex.close()
            return []
    