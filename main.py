import tkinter as tk
from ui import verificar
from tkinter import StringVar, font

window = tk.Tk()
window.title('Autómatas')

fuente_titulo = font.Font(family='Helvetica', size=20, weight='bold')
fuente_texto = font.Font(family='Helvetica', size=12)
fuente_rangos = font.Font(family='Helvetica', size=15)

titulo = tk.Label(window, text='Validador de Autómatas', font=fuente_titulo)
titulo.pack(pady=20)
rangos_label = tk.Label(window, text='Rangos: 3-MR-01Z hasta 9-NG-99A', font=fuente_rangos)
rangos_label.pack()

frame = tk.Frame(window)
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

entrada_var = StringVar()
entrada_entry = tk.Entry(frame, textvariable=entrada_var, width=50, font=fuente_texto, borderwidth=2, relief="solid")
entrada_entry.pack(pady=20)

resultado_var = StringVar()
resultado_label = tk.Label(frame, textvariable=resultado_var, width=50, height=4, wraplength=300, font=fuente_texto, borderwidth=2, relief="solid")
resultado_label.pack(pady=20)

canvas = tk.Canvas(window, width=600, height=100, bg='white')
canvas.pack(pady=10)

verificar_btn = tk.Button(frame, text='Verificar', command=lambda: verificar(canvas, resultado_var, entrada_var), font=fuente_texto, borderwidth=2, relief="raised")
verificar_btn.pack(pady=10)

window.mainloop()
