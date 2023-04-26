''' Relógio Digital personalizado que recebe o usuário com boas vindas e exibe o horário em formato 24 h.
   O usuário pode alternar entre modo Claro e Escuro por um controle deslizante.
   Para a construção do relógio, tomei como base um vídeo do canal no youtube Lilizok4 ASMR, que deixarei listado no README.md. 
   O projeto faz uso da biblioteca Tkinter para sua interface gráfica, dos módulos OS para importar informações do sistema operacional (nome do usuário) e TIME para acessar informações de data e hora. '''


import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Relógio Digital')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#1d1d1d')


def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text='Olá, ' + nome_usuario)


def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text=data_atual)


def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

# criando um switch deslizante para alternar entre os modos claro e escuro


switch = Scale(root, from_=0, to=1, orient=HORIZONTAL, length=60,
               showvalue=0, highlightthickness=0, bd=0, troughcolor='#2d2d2d',
               activebackground='#8e27ea', bg='#DCDCDC', sliderlength=20, sliderrelief='raised',
               relief='flat', borderwidth=0, command=lambda val: change_theme(val))
switch.place(x=270, y=290)

# configurando o toogle dark/ligth mode


def change_theme(val):
    if val == '1':
        root.configure(background='#FFFFFF')
        saudacao.config(fg='#1d1d1d', bg='#FFFFFF')
        data.config(fg='#338717', bg='#FFFFFF')
        horas.config(fg='#1d1d1d', bg='#FFFFFF')
        switch.configure(bg='#FFFFFF')
        if switch.get() == 1:
            switch.configure(troughcolor='#FFFFFF')
        else:
            switch.configure(troughcolor='#1d1d1d')
    else:
        root.configure(background='#1d1d1d')
        saudacao.config(fg='#DCDCDC', bg='#1d1d1d')
        data.config(fg='#8e27ea', bg='#1d1d1d')
        horas.config(fg='#DCDCDC', bg='#1d1d1d')
        switch.configure(bg='#2d2d2d')
        if switch.get() == 1:
            switch.configure(troughcolor='#1d1d1d')
        else:
            switch.configure(troughcolor='#1d1d1d')


saudacao = Label(root, bg='#1d1d1d', fg='#DCDCDC', font=('Roboto Mono', 18))
saudacao.pack(pady=20)

data = Label(root, bg='#1d1d1d', fg='#8e27ea', font=('DS-Digital', 14))
data.pack(pady=2)

horas = Label(root, bg='#1d1d1d', fg='#DCDCDC',
              font=('DS-Digital', 102))
horas.pack(pady=2)

get_saudacao()
get_data()
get_horas()

root.mainloop()
