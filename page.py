import tkinter as tk
from tkinter import Tk
janela = tk.Tk()

janela.title("Cotação de Moedas")

mensagem = tk.Label(text="Sistema de Busca de Cotação de Moedas", fg="white", bg='#0092FF', width=50, height=10)
mensagem.pack()

mensagem2= tk.Label(text= "Selecione a moeda desejada")
mensagem2.pack()

moeda = tk.Entry()
moeda.pack()
janela.mainloop()
