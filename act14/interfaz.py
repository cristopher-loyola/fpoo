import tkinter as tk
from tkinter import messagebox, simpledialog
from cajapupo import CuentaCajaPopular

class InterfazCajaPopular:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Caja Popular")
        self.color_fondo = "white"
        self.color_boton = "red"
        self.color_texto = "black"

        self.ventana.configure(bg=self.color_fondo)

        self.etiqueta_cuenta = tk.Label(ventana, text="No. Cuenta:", bg=self.color_fondo, fg=self.color_texto)
        self.etiqueta_cuenta.grid(row=0, column=0)

        self.etiqueta_titular = tk.Label(ventana, text="Titular:", bg=self.color_fondo, fg=self.color_texto)
        self.etiqueta_titular.grid(row=1, column=0)

        self.etiqueta_edad = tk.Label(ventana, text="Edad:", bg=self.color_fondo, fg=self.color_texto)
        self.etiqueta_edad.grid(row=2, column=0)

        self.etiqueta_saldo = tk.Label(ventana, text="Saldo:", bg=self.color_fondo, fg=self.color_texto)
        self.etiqueta_saldo.grid(row=3, column=0)

        self.numero_cuenta = tk.Entry(ventana)
        self.numero_cuenta.grid(row=0, column=1)

        self.titular = tk.Entry(ventana)
        self.titular.grid(row=1, column=1)

        self.edad = tk.Entry(ventana)
        self.edad.grid(row=2, column=1)

        self.saldo = tk.Entry(ventana)
        self.saldo.grid(row=3, column=1)

        self.boton_consultar_saldo = tk.Button(ventana, text="Consultar Saldo", command=self.consultar_saldo, bg=self.color_boton, fg="white")
        self.boton_consultar_saldo.grid(row=4, column=0, columnspan=2, pady=5)

        self.boton_ingresar_efectivo = tk.Button(ventana, text="Ingresar Efectivo", command=self.ingresar_efectivo, bg=self.color_boton, fg="white")
        self.boton_ingresar_efectivo.grid(row=5, column=0, columnspan=2, pady=5)

        self.boton_retirar_efectivo = tk.Button(ventana, text="Retirar Efectivo", command=self.retirar_efectivo, bg=self.color_boton, fg="white")
        self.boton_retirar_efectivo.grid(row=6, column=0, columnspan=2, pady=5)

        self.cantidad_retirar = tk.Entry(ventana)
        self.cantidad_retirar.grid(row=7, column=1)

        self.boton_depositar_otra_cuenta = tk.Button(ventana, text="Depositar a otra cuenta", command=self.depositar_otra_cuenta, bg=self.color_boton, fg="white")
        self.boton_depositar_otra_cuenta.grid(row=8, column=0, columnspan=2, pady=5)

        self.cuenta = None

    def consultar_saldo(self):
        numero_cuenta = self.numero_cuenta.get()
        self.cuenta = CuentaCajaPopular(122240391, "Cristopher Loyola", 30, 1000) 
        saldo = self.cuenta.consultar_saldo()
        self.saldo.delete(0, tk.END) 
        self.saldo.insert(tk.END, saldo)

    def ingresar_efectivo(self):
        if self.cuenta:
            cantidad = float(self.saldo.get())
            self.cuenta.ingresar_efectivo(cantidad)
            messagebox.showinfo("Ingresar Efectivo", "Se ha ingresado el efectivo correctamente.")
        else:
            messagebox.showerror("Error", "Primero debe consultar una cuenta.")

    def retirar_efectivo(self):
        if self.cuenta:
            cantidad = float(self.cantidad_retirar.get())
            exito = self.cuenta.retirar_efectivo(cantidad)
            if exito:
                messagebox.showinfo("Retirar Efectivo", "Se ha retirado el efectivo correctamente.")
            else:
                messagebox.showerror("Error", "Saldo insuficiente para realizar la operación.")
        else:
            messagebox.showerror("Error", "Primero debe consultar una cuenta.")

    def depositar_otra_cuenta(self):
        if self.cuenta:
            numero_cuenta_destino = tk.simpledialog.askstring("Depositar a otra cuenta", "Ingrese el número de cuenta destino:")
            cantidad = float(self.saldo.get())
            cuenta_destino = CuentaCajaPopular(1023, "Antonio Martinez", 25, 0)
            exito = self.cuenta.depositar_otra_cuenta(cuenta_destino, cantidad)
            if exito:
                messagebox.showinfo("Depositar a otra cuenta", "Se ha depositado el efectivo correctamente.")
            else:
                messagebox.showerror("Error", "Saldo insuficiente para realizar la operación.")
        else:
            messagebox.showerror("Error", "Primero debe consultar una cuenta.")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = InterfazCajaPopular(ventana_principal)
    ventana_principal.mainloop()
