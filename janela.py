from tkinter import *
from bd import insert, update, delete, query, register, login, to_lend, give_back
from conexao import connect

mydb = connect()

def login_action():
    email = entry_email.get()  # Recupera o e-mail inserido pelo usuário
    senha = entry_senha.get()  # Recupera a senha inserida pelo usuário
    user = login(mydb, email, senha)  # Chama a função de login
    if user:
        print("Login bem-sucedido.")
        # Adicione aqui o código para as ações após o login bem-sucedido
    else:
        print("Credenciais inválidas.")

def register_action():
    nome = entry_nome.get()  # Recupera o nome inserido pelo usuário
    email = entry_email.get()  # Recupera o e-mail inserido pelo usuário
    senha = entry_senha.get()  # Recupera a senha inserida pelo usuário
    data_nascimento = ''  # Recupera a data de nascimento inserida pelo usuário
    rua = ''  # Recupera a rua inserida pelo usuário
    bairro = ''  # Recupera o bairro inserido pelo usuário
    cidade = ''  # Recupera a cidade inserida pelo usuário
    estado = ''  # Recupera o estado inserido pelo usuário
    cep = ''  # Recupera o CEP inserido pelo usuário
    register(mydb, nome, email, senha, data_nascimento, rua, bairro, cidade, estado, cep)  # Chama a função de registro
    print("Usuário registrado com sucesso.")

janela = Tk()
janela.title('Ola Mundo')
janela.geometry('450x250')
janela.config(bg='#242323')

label_login = Label(janela, text="Digite o seu login")
label_login.grid(column=4, row=0)

entry_nome = Entry(janela)  # Campo de entrada para o nome
entry_nome.grid(column=4, row=1)

label_email = Label(janela, text="Digite seu e-mail")
label_email.grid(column=4, row=2)

entry_email = Entry(janela)  # Campo de entrada para o e-mail
entry_email.grid(column=4, row=3)

label_senha = Label(janela, text="Digite sua senha")
label_senha.grid(column=4, row=4)

entry_senha = Entry(janela, show='*')  # Campo de entrada para a senha
entry_senha.grid(column=4, row=5)

botao_login = Button(janela, text="Login", command=login_action)
botao_login.grid(column=0, row=6)

botao_cadastro = Button(janela, text="Cadastro", command=register_action)
botao_cadastro.grid(column=1, row=6)

janela.mainloop()