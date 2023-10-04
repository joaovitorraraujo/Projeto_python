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


janela.mainloop()"""
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import *
import function

lista_registers = []

window = ctk.CTk()


class TelaLogin:
    def __init__(self):
        self.window = window
        self.theme()
        self.config_window()
        self.screen_login()
        window.mainloop()

    # tema
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    label_description = ctk.CTkLabel(
        master=window,
        text="Bem-Vindo ao Projeto",
        font=("Roboto", 25, "bold"),
        text_color="#00B0F0",
    ).place(x=55, y=50)

    # janela
    def config_window(self):
        window.title("Login")
        window.geometry("700x460")
        window.resizable(False, False)
        window.iconbitmap("icon.ico")

    def screen_login(self):
        # imagem da janela
        img_log = PhotoImage(file="log.png")
        label_img = ctk.CTkLabel(master=window, text="", image=img_log).place(
            x=75, y=120
        )

        # frame
        frame_login = ctk.CTkFrame(master=window, width=350, height=456)
        frame_login.pack(side=RIGHT)

        # imagem do frame
        img_user = PhotoImage(file="user.png")
        label_img = ctk.CTkLabel(
            master=frame_login, text="", width=300, image=img_user
        ).place(x=25, y=50)

        img_google = PhotoImage(file="google.png")
        button_img = ctk.CTkButton(
            master=frame_login,
            text="Continue com Google",
            image=img_google,
            width=300,
            fg_color="#db4a3b",
            text_color=("black"),
            hover_color="#dc5e50",
        ).place(x=25, y=379)

        img_fecebook = PhotoImage(file="facebook.png")
        button_img = ctk.CTkButton(
            master=frame_login,
            text="Continue com Facebook",
            image=img_fecebook,
            width=300,
            fg_color="#3d5a98",
            text_color=("black"),
            hover_color="#5b6886",
        ).place(x=25, y=419)

        # widgets dentro do frame
        label_login = ctk.CTkLabel(
            master=frame_login,
            text="Login",
            font=("Courie", 30, "italic"),
            text_color=("white"),
            width=300,
        ).place(x=25, y=5)

        label_or = ctk.CTkLabel(
            master=frame_login,
            text="Ou",
            font=("Courie", 10),
            text_color=("white"),
            width=300,
        ).place(x=25, y=349)

        entry_email = ctk.CTkEntry(
            master=frame_login,
            placeholder_text="Digite seu E-mail ou usuário",
            font=("Roboto", 11, "bold"),
            width=300,
        ).place(x=25, y=165)

        entry_password = ctk.CTkEntry(
            master=frame_login,
            placeholder_text="Digite sua senha",
            font=("Roboto", 11, "bold"),
            width=300,
            show="*",
        ).place(x=25, y=205)

        checkbox_user = ctk.CTkCheckBox(
            master=frame_login, text="Lembrar email ou usuário", width=100
        ).place(x=25, y=250)

        # botões de login, register e recuperar senha
        button_login = ctk.CTkButton(
            master=frame_login,
            text="Login",
            width=300,
            command=function.button_function,
        ).place(x=25, y=290)

        button_forgot_password = ctk.CTkButton(
            master=frame_login,
            text="Esqueci a senha",
            width=100,
            font=("Roboto", 11, "underline"),
            fg_color="#6a6a7c",
            hover_color="#4d4c4c",
            command=function.button_function,
        ).place(x=225, y=250)

        def screen_register():
            # apagar tela do login e mostar a de cadastro
            frame_login.pack_forget()

            # criar frame da tela de registro
            frame_register = ctk.CTkFrame(master=window, width=350, height=456)
            frame_register.pack(side=RIGHT)

            # widgts dentro do frame de resgistro
            label_register = ctk.CTkLabel(
                master=frame_register,
                text="Crie sua conta",
                font=("Courie", 30, "italic"),
                text_color=("white"),
                width=300,
            ).place(x=25, y=25)

            label_descripiton_register = ctk.CTkLabel(
                master=frame_register,
                text="-Confira todos os campos antes de confirmar\n-Todos os campos são obrigatórios ",
                font=("Courie", 11, "italic"),
                text_color=("white"),
                width=300,
            ).place(x=25, y=70)

            entry_user_register = ctk.CTkEntry(
                master=frame_register,
                placeholder_text="Digite seu usuário",
                font=("Roboto", 11, "bold"),
                width=300,
            )
            entry_user_register.place(x=25, y=110)

            entry_email_register = ctk.CTkEntry(
                master=frame_register,
                placeholder_text="Digite seu E-mail",
                font=("Roboto", 11, "bold"),
                width=300,
            )
            entry_email_register.place(x=25, y=150)

            entry_password_register = ctk.CTkEntry(
                master=frame_register,
                placeholder_text="Digite sua senha",
                font=("Roboto", 11, "bold"),
                width=300,
            )
            entry_password_register.place(x=25, y=190)

            entry_confirm_password = ctk.CTkEntry(
                master=frame_register,
                placeholder_text="Confirme sua senha",
                font=("Roboto", 11, "bold"),
                width=300,
            )
            entry_confirm_password.place(x=25, y=230)

            checkbox_terms = ctk.CTkCheckBox(
                master=frame_register, text="Aceito os termos de serviço", width=145
            )
            checkbox_terms.place(x=25, y=270)

            button_terms = ctk.CTkButton(
                master=frame_register,
                text="Acesse os termos",
                width=100,
                font=("Roboto", 11, "underline"),
                fg_color="#6a6a7c",
                hover_color="#4d4c4c",
                command=function.button_function,
            )
            button_terms.place(x=225, y=270)

            def coonfirm_register():
                add_user = entry_user_register.get()
                add_email = entry_email_register.get()
                add_password = entry_password_register.get()
                add_password_confirm = entry_confirm_password.get()
                lista_registers.append((add_user,add_email,add_password,add_password_confirm))
                # Limpar o CTkEntry após armazenar o valor
                entry_user_register.delete(0, "end")
                entry_email_register.delete(0, "end")
                entry_password_register.delete(0, "end")
                entry_confirm_password.delete(0, "end")

                msg_successfully = CTkMessagebox(
                    title="Info", icon="check", message="Cadastrado com sucesso!"
                )

                
            # teste para ver se a varial esta adicionando a lista
            """def show_items():
                print("Itens armazenados:")
                for item in lista_registers:
                    print(item)

            show_button = ctk.CTkButton(
                master=frame_register, text="Mostrar Itens", command=show_items
            )
            show_button.place(x=25, y=1)"""

            button_register = ctk.CTkButton(
                master=frame_register,
                text="Confirmar",
                width=145,
                fg_color="green",
                hover_color="#025f03",
                command=coonfirm_register,
            ).place(x=180, y=310)

            def back():
                # apagar frame de registro
                frame_register.pack_forget()

                # devolver frame de login
                frame_login.pack(side=RIGHT)

            button_back = ctk.CTkButton(
                master=frame_register,
                text="Voltar",
                width=145,
                fg_color="black",
                hover_color="#0f0f0f",
                command=back,
            ).place(x=25, y=310)

            label_or = ctk.CTkLabel(
                master=frame_register,
                text="Ou",
                font=("Courie", 10),
                text_color=("white"),
                width=300,
            ).place(x=25, y=349)

            img_google = PhotoImage(file="google.png")
            Button_img = ctk.CTkButton(
                master=frame_register,
                text="Vincule com Google",
                image=img_google,
                width=300,
                fg_color="#db4a3b",
                text_color=("black"),
                hover_color="#dc5e50",
            ).place(x=25, y=379)

            img_fecebook = PhotoImage(file="facebook.png")
            Button_img = ctk.CTkButton(
                master=frame_register,
                text="Vincule com Facebook",
                image=img_fecebook,
                width=300,
                fg_color="#3d5a98",
                text_color=("black"),
                hover_color="#5b6886",
            ).place(x=25, y=419)

        button_register = ctk.CTkButton(
            master=frame_login,
            text="Cadastre-se",
            width=300,
            fg_color="black",
            hover_color="#0f0f0f",
            command=screen_register,
        ).place(x=25, y=325)


TelaLogin()
