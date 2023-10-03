# from tkinter import *
import tkinter as tk
pantalla = tk.Tk()
pantalla.title("Primera ventana") # Cambiar el nombre de la ventana
pantalla.geometry("560x480") # Configurar tamaño
boton = tk.Button(pantalla, text="Hola, mundo")
boton.place(x=50, y=50)
entrada = tk.Entry()
entrada.place(x=50, y=150, width=150)

pantalla.mainloop()