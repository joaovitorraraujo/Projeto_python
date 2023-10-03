"""import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["Saco", "Caixa"]
lista_codigo = []

janela = tk.Tk()

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecione_tipo.get()
    quantidade = entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%H")
    codigo = len(lista_codigo) + 1
    codigo_str = "COD-{}".format(codigo)
    lista_codigo.append((codigo_str, descricao, tipo, quantidade, data_criacao))


# titulo da janela
janela.title("Cadastro de materiais")

# descrição do material
label_descricao = tk.Label(text="Descrição do Material")
label_descricao.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

label_tipo_unidade = tk.Label(text="Tipo da unidade do material")
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

# Combobox(lista para escolher o material)
combobox_selecione_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecione_tipo.grid(
    row=3, column=2, padx=10, pady=10, sticky="nswe", columnspan=2
)

# descrever a quantidade
label_quantidade = tk.Label(text="Quantidade de material")
label_quantidade.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_criar_codigo = tk.Button(text="Criar codigo", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)


janela.mainloop()

print(f'\n{lista_codigo}')"""
import customtkinter as ctk
import tkinter as tk
from tkinter import *
import function

# tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()

label_descricao = ctk.CTkLabel(
    master=janela,
    text="Bem-Vindo ao Projeto",
    font=("Roboto", 25, "bold"),
    text_color="#00B0F0",
)
label_descricao.place(x=55, y=50)

# janela
janela.title("Login")
janela.geometry("700x400")
janela.resizable(False, False)

# imagem da janela
img = PhotoImage(file="log.png")
label_img = ctk.CTkLabel(master=janela, text="", image=img)
label_img.place(x=75, y=120)


# frame
frame_login = ctk.CTkFrame(master=janela, width=350, height=396)
frame_login.pack(side=RIGHT)

# imagem do frame
img = PhotoImage(file="login.png")
label_img = ctk.CTkLabel(master=frame_login, text="", width=300, image=img)
label_img.place(x=25, y=50)

# widgets dentro do frame
label_login = ctk.CTkLabel(
    master=frame_login,
    text="Login",
    font=("Courie", 30, "italic"),
    text_color=("white"),
    width=300,
)
label_login.place(x=25, y=5)

entry_email = ctk.CTkEntry(
    master=frame_login,
    placeholder_text="Digite seu email ou usuário",
    font=("Roboto", 11, "bold"),
    width=300,
)
entry_email.place(x=25, y=165)

entry_senha = ctk.CTkEntry(
    master=frame_login,
    placeholder_text="Digite sua senha",
    font=("Roboto", 11, "bold"),
    width=300,
    show="*",
)
entry_senha.place(x=25, y=210)

checkbox_usuario = ctk.CTkCheckBox(master=frame_login, text="Lembrar email ou usuário")
checkbox_usuario.place(x=25, y=250)

button_login = ctk.CTkButton(
    master=frame_login, text="Login", width=300, command=function.button_function
)
button_login.place(x=25, y=290)

button_register = ctk.CTkButton(
    master=frame_login, text="Registrar", width=300, command=function.button_function
)
button_register.place(x=25, y=330)

janela.mainloop()
