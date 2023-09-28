import tkinter as tk
from automata import validar_entrada
from tkinter import StringVar

def verificar(canvas, resultado_var, entrada_var):
    entrada = entrada_var.get()
    es_valido, recorrido, error_idx = validar_entrada(entrada)
    if es_valido:
        resultado_var.set('Entrada válida')
    else:
        if error_idx == -1:
            resultado_var.set('Entrada inválida')
        else:
            resultado_var.set(f'Error en el carácter {error_idx + 1} ({entrada[error_idx]})')
    canvas.delete("all")
    x = 30 
    y = 50  
    radio = 20  
    espacio = 60  
    for i, estado in enumerate(recorrido):
        if i == 0:
            canvas.create_line(x - espacio, y, x - radio, y, arrow=tk.LAST)
        color = "red" if not es_valido and i == len(recorrido) - 1 else "white"
        canvas.create_oval(x-radio, y-radio, x+radio, y+radio, outline="black", fill=color)
        canvas.create_text(x, y, text=estado)
        if int(estado[1:]) in {9, 17, 26, 32}:
            canvas.create_oval(x-radio+5, y-radio+5, x+radio-5, y+radio-5, outline="black")
        if i > 0:
            x_anterior = x - espacio
            canvas.create_line(x_anterior + radio, y, x - radio, y, arrow=tk.LAST)
        x += espacio
    canvas.update()
