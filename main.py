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
import customtkinter as customtk
import function


janela = customtk.CTk()
customtk.set_appearance_mode("dark")
customtk.set_default_color_theme("blue")

janela.title("Login")
janela.geometry("500x300")

label_descricao = customtk.CTkLabel(janela, text="Faça seu login")
label_descricao.pack(padx=10, pady=10)

entry_email = customtk.CTkEntry(janela, placeholder_text="seu email")
entry_email.pack(padx=10, pady=10)

entry_senha = customtk.CTkEntry(janela, placeholder_text="sua senha", show="*")
entry_senha.pack(padx=10, pady=10)

checkbox_usuario = customtk.CTkCheckBox(janela, text="Lembrar usuário")
checkbox_usuario.pack(padx=10, pady=10)

button_login = customtk.CTkButton(janela, text="Login", command=function.button_function)
button_login.pack(padx=10, pady=10)

janela.mainloop()
