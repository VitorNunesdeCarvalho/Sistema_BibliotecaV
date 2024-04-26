from conexao import connect
from bd import insert, update, delete, query, register, login, to_lend, give_back
from livro import Livro
from datetime import datetime
from usuario import Usuario
from tkinter import *

def welcome_window():
    w = Tk()
    w.title("Biblioteca")
    w.geometry("320x420")
    w.configure(background="white")
    w.resizable(width=False, height=False)

    frame_cima = Frame(w, width=310, height=50, bg="white", relief="flat")
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = Frame(w, width=310, height=250, bg="white", relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    c_nome = Label(frame_cima, text="Biblioteca", anchor=NE, font=("Ivy", 25), bg="white", fg="black")
    c_nome.place(x=5, y=5)
    c_linha = Label(frame_cima, text=" ", width=275, anchor=NW, font=("Ivy", 1), bg="white", fg="black")
    c_linha.place(x=10, y=45)

    botao_inserir = Button(frame_baixo, text="Inserir Livros", width=39, height=1, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
    botao_inserir.place(x=15, y=120)

    botao_atualizar = Button(frame_baixo, text="Atualizar livros", width=39, height=1, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
    botao_atualizar.place(x=15, y=150)

    botao_listar = Button(frame_baixo, text="Listar livros", width=39, height=1, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
    botao_listar.place(x=15, y=180)

    botao_emprestar_devolver = Button(frame_baixo, text="Emprestar e Devolver Livros", width=39, height=1, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
    botao_emprestar_devolver.place(x=15, y=210)


    w.mainloop()

def cd_usuario():
    janela = Toplevel()
    janela.title("Cadastro de Usuário")
    janela.geometry("320x290")
    janela.configure(background="white")
    janela.resizable(width=False, height=False)

    frame_cima = Frame(janela, width=310, height=50, bg="white", relief="flat")
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
    frame_baixo = Frame(janela, width=310, height=250, bg="white", relief="flat")
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

    c_nome = Label(frame_cima, text="Cadastro", anchor=NE, font=("Ivy", 25), bg="white", fg="black")
    c_nome.place(x=5, y=5)
    c_linha = Label(frame_cima, text=" ", width=275, anchor=NW, font=("Ivy", 1), bg="white", fg="black")
    c_linha.place(x=10, y=45)

    nome = Label(frame_baixo, text="Nome: ", anchor=NW, font=("Ivy", 10), bg="white", fg="black")
    nome.place(x=10, y=20)
    e_nome = Entry(frame_baixo, width=25, justify="left", font=(" ", 15), highlightthickness=1, relief="solid")
    e_nome.place(x=14, y=50)

    senha = Label(frame_baixo, text="Digite sua senha: ", anchor=NW, font=("Ivy", 10), bg="white", fg="black")
    senha.place(x=10, y=95)
    e_senha = Entry(frame_baixo, width=25, justify="left", font=(" ", 15), highlightthickness=1, relief="solid")
    e_senha.place(x=14, y=130)

    def registrar_user():
        mydb = connect()
        user_data = {
            'nome': e_nome.get(),
            'senha': e_senha.get()
        }
        register(mydb, user_data["nome"], user_data["senha"])

    botao_confirmar = Button(frame_baixo, text="Cadastrar",command=registrar_user, width=39, height=2, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
    botao_confirmar.place(x=15, y=180)

    janela.mainloop()


app = Tk()
app.title("Biblioteca")
app.geometry("320x420")
app.configure(background="white")
app.resizable(width=False, height=False)

frame_cima = Frame(app, width=310, height=50, bg="white", relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_baixo = Frame(app, width=310, height=250, bg="white", relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

c_nome = Label(frame_cima, text="Login", anchor=NE, font=("Ivy", 25), bg="white", fg="black")
c_nome.place(x=5, y=5)
c_linha = Label(frame_cima, text=" ", width=275, anchor=NW, font=("Ivy", 1), bg="white", fg="black")
c_linha.place(x=10, y=45)

nome = Label(frame_baixo, text="Nome: ", anchor=NW, font=("Ivy", 10), bg="white", fg="black")
nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify="left", font=(" ", 15), highlightthickness=1, relief="solid")
e_nome.place(x=14, y=50)

senha = Label(frame_baixo, text="Digite sua senha: ", anchor=NW, font=("Ivy", 10), bg="white", fg="black")
senha.place(x=10, y=95)
e_senha = Entry(frame_baixo, width=25, justify="left", font=(" ", 15), highlightthickness=1, relief="solid")
e_senha.place(x=14, y=130)

def check_login(nome_entry, senha_entry):
    mydb = connect()
    nome = nome_entry.get()
    senha = senha_entry.get()

    user = login(mydb, nome, senha)

    if user:
        print("Login bem sucedido!")
        welcome_window()
    else:
        print("Credenciais inválidas!")
        # Se as credenciais forem inválidas, você pode querer limpar os campos de entrada:
        nome_entry.delete(0, END)
        senha_entry.delete(0, END)


botao_confirmar = Button(frame_baixo, text="Enviar", command=lambda: check_login(e_nome, e_senha), width=39, height=1, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=180)

botao_confirmar = Button(frame_baixo, text="Cadastrar",command=cd_usuario, width=39, height=1, font=("Ivy", 8, "bold"), bg="gray", fg="white", relief=RAISED, overrelief=RIDGE)
botao_confirmar.place(x=15, y=210)

app.mainloop()
