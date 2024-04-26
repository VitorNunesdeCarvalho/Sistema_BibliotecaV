from cadastro import *
from tkinter import *


janela = Tk()
janela.geometry("700x400")
janela.title("Painel de Login")
janela.iconbitmap("icon.ico")
janela.resizable(False, False)

img = PhotoImage(file="R.jpg")
label_img = Label(master= janela, image=img)
label_img.place(x=5, y=65)