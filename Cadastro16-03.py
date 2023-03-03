import getpass
from tkinter import *
import tkinter as tk
import datetime as dt
from tkinter import ttk
import pyodbc

#Criando uma conexão com o DB

connectdb = dados_conexao = ('Driver={SQL Server};'
                             'Server="";'
                             'Database="";')
conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida!")

#Janela
janela = tk.Tk()
#janela.iconbitmap("C:/Users/Eduardo/Downloads/ICON.ico")

tipos_generos = ["----------","Feminino", "Masculino", "Prefiro não Informar",]

cursor = conexao.cursor()

def botao_cadastro():
    botao_registro = tk.Button(text='Criar uma conta', command= pagina_de_cadastro())
    botao_registro.grid(row=4, column=0, padx=1, pady=1, sticky='nswe', columnspan=1)


def pagina_de_login():
    janela.title('Iconstruct')
    #Texto de boas vindas
    text_label = tk.Label(janela,text="Seja Bem Vindo ao Iconstruct", font ="Arial 15 bold")
    text_label.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=10)

    #Email
    label_email = tk.Label(janela,text='Email:')
    label_email.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_email = tk.Entry(janela)
    entry_email.grid(row=2, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)
    #Senha
    label_senha = tk.Label(janela,text='Senha:')
    label_senha.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_senha = tk.Entry(janela,show='*')
    entry_senha.grid(row=3, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)
    #Func Select no SQL SERVER
    def select_db(self, Email, Senha):
       return self.cursor.execute('SELECT * FROM Dados WHERE Email = ? AND Senha = ?').fetchone()

    def login():
        Email = entry_email.get()
        Senha = getpass.getpass(entry_senha.get())
        auth =  select_db(Senha,Email)
        if Email and Senha in auth:
            print("Voce está logado")
        else:
            print("Deu Bigode")

    #Botao de login
    botao_login = tk.Button(janela,text='Logar', command= login)
    botao_login.grid(row=4, column=8, padx=1, pady=1, sticky='nswe', columnspan=15)
    #Botao de cadastro
    botao_registro = tk.Button(janela, text='Criar uma conta', command= botao_cadastro)
    botao_registro.grid(row=4, column=0, padx=1, pady=1, sticky='nswe', columnspan=1)

def pagina_de_cadastro():
    janela2 = tk.Toplevel()
    janela2.title('Pagina de Cadastro')
    #Tipo de conta
    label_typeconta = tk.Label(janela2,text = 'Tipo de conta:')
    label_typeconta.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan= 2)
    radiobutton1 = tk.Radiobutton(janela2, text="Profissional", value= "p")
    radiobutton2 = tk.Radiobutton(janela2, text="Cliente", value= "c")
    radiobutton1.grid(row=0, column=2, padx=10, pady=10, sticky='nswe', columnspan= 5)
    radiobutton2.grid(row=0, column=6, padx=10, pady=10, sticky='nswe', columnspan=10)
    # Registro de nome completo
    label_nome = tk.Label(janela2,text="Nome Completo:")
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan= 2)
    entry_nome = tk.Entry(janela2)
    entry_nome.grid(row=1, column=4, padx=10, pady=10, sticky='nswe', columnspan= 4)
    # Registro de Email
    label_email = tk.Label(janela2,text='Email:')
    label_email.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_email = tk.Entry(janela2)
    entry_email.grid(row=2, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)
    #Senha
    label_senha = tk.Label(janela2, text='Senha:')
    label_senha.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_senha = tk.Entry(janela2, show="*")
    entry_senha.grid(row=3, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

    # Registro de Endereço
    label_endereco = tk.Label(janela2,text='Endereço:')
    label_endereco.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_endereco = tk.Entry(janela2)
    entry_endereco.grid(row=4, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)
    # Registro de CPF
    label_cpf = tk.Label(janela2,text='CPF:')
    label_cpf.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    entry_cpf = tk.Entry(janela2)
    entry_cpf.grid(row=5, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)

    # Genero
    label_genero = tk.Label(janela2,text='Sexo:')
    label_genero.grid(row=6, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)
    combobox_tipo_de_genero = ttk.Combobox(janela2 , value=tipos_generos)
    combobox_tipo_de_genero.current(0)
    combobox_tipo_de_genero.grid(row=6, column=4, padx=10, pady=10, sticky='nswe', columnspan=4)
    #TERMOS DE US0
    botao_termos = False
    botao_termos = tk.Checkbutton(janela2, text="Ao efetuar o cadastro estou ciente dos termos de uso do Aplicativo", var=botao_termos)
    botao_termos.grid(row=7, column=0, padx=10, pady=10, sticky='nswe', columnspan=10)

    def inserir_dados():
        cursor.execute(f"""INSERT INTO Dados(Tipo_conta, Nome, Email,Senha, Endereco, Cpf, Sexo)
        VALUES	('{1}', '{entry_nome.get()}','{entry_email.get()}','{entry_senha.get()}','{entry_endereco.get()} ','{entry_cpf.get()}','{combobox_tipo_de_genero.get()}')""")
        cursor.commit()
        cadastro_concluido()

    # Botao de criar a conta
    botao = tk.Button(janela2, text='Criar conta', command= inserir_dados)
    botao.grid(row=8, column=10, padx=10, pady=10, sticky='nswe', columnspan=15)

def cadastro_concluido():
    janela3 = tk.Toplevel()
    janela3.title('Pagina de Cadastro')
    text_label = tk.Label(janela3,text="Cadastro Concluído com Sucesso", font="Calibri 15 bold")
    text_label.grid(row=1, column=0, padx=10, pady=10, sticky='nswe', columnspan=10)

"""Botao de voltar para o login
botao = tk.Button(janela3, text='Voltar para o Login', command= pagina_de_login())
botao.grid(row=8, column=0, padx=10, pady=10, sticky='nswe', columnspan=20)"""


pagina_de_login()
janela.mainloop()