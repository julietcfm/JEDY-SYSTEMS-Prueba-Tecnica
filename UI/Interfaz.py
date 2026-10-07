import tkinter as tk
from tkinter import messagebox

from BL.DatosBL import DatosBL


class Interfaz:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Jedy Systems - Prueba Técnica")
        self.ventana.geometry("450x300")
        self.ventana.resizable(False, False)

        self.bl = DatosBL()

        # Título
        titulo = tk.Label(
            ventana,
            text="Prueba Técnica - Jedy Systems",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=20)

        # Etiqueta
        etiqueta = tk.Label(
            ventana,
            text="Ingrese un dato:",
            font=("Arial", 11)
        )
        etiqueta.pack(pady=5)

        # TextBox
        self.textbox = tk.Entry(
            ventana,
            width=40,
            font=("Arial", 11)
        )
        self.textbox.pack(pady=5)

        # Botón Guardar
        boton_guardar = tk.Button(
            ventana,
            text="Guardar",
            width=15,
            command=self.guardar
        )
        boton_guardar.pack(pady=10)

        # Botón Consultar
        boton_consultar = tk.Button(
            ventana,
            text="Consultar",
            width=15,
            command=self.consultar
        )
        boton_consultar.pack(pady=5)

        # Resultado
        self.resultado = tk.Label(
            ventana,
            text="Resultado: -",
            font=("Arial", 10)
        )
        self.resultado.pack(pady=15)

    def guardar(self):
        valor = self.textbox.get().strip()

        if not valor:
            messagebox.showwarning(
                "Aviso",
                "Ingrese un dato."
            )
            return

        self.bl.guardar_dato(valor)

        messagebox.showinfo(
            "Éxito",
            "El dato fue guardado correctamente."
        )

        self.textbox.delete(0, tk.END)

    def consultar(self):
        valor = self.bl.obtener_dato()

        if valor:
            self.resultado.config(
                text=f"Resultado: {valor}"
            )
        else:
            self.resultado.config(
                text="Resultado: No hay datos guardados."
            )


if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = Interfaz(ventana)
    ventana.mainloop()