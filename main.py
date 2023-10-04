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

# Combobox(lista para escolher o material)
combobox_selecione_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecione_tipo.grid(
    row=3, column=2, padx=10, pady=10, sticky="nswe", columnspan=2
)

entry_quantidade = tk.Entry()
entry_quantidade.grid(row=4, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)


janela.mainloop()"""

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import *
import function
import re

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
        font=("Arial 20", 25, "underline"),
        text_color="white",
        width=300,
    ).place(x=25, y=5)

    label_presentation1 = ctk.CTkLabel(
        master=window,
        text="Sistema ",
        font=(
            "Impact",
            30,
        ),
        text_color="white",
        bg_color="transparent",
    )
    label_presentation1.place(x=110, y=80)

    label_presentation2 = ctk.CTkLabel(
        master=window,
        text="De",
        font=(
            "Impact",
            16,
        ),
        text_color="white",
        bg_color="transparent",
    )
    label_presentation2.place(x=219, y=89)

    label_presentation3 = ctk.CTkLabel(
        master=window,
        text="Login",
        font=("Impact", 59),
        text_color="#0080e4",
        bg_color="transparent",
    )
    label_presentation3.place(x=110, y=110)

    label_presentation3.lift()
    label_presentation2.lift()
    label_presentation1.lift()

    # janela configuração
    def config_window(self):
        window.title("Sistema de login")
        window.geometry("700x460")
        window.resizable(False, False)
        window.iconbitmap("imagens/icon.ico")

    def screen_login(self):
        # imagem da janela
        img_log = PhotoImage(file="imagens/log.png")
        label_img = ctk.CTkLabel(master=window, text="", image=img_log).place(
            x=75, y=190
        )

        # frame
        frame_login = ctk.CTkFrame(master=window, width=350, height=456)
        frame_login.pack(side=RIGHT)

        # imagem do frame
        img_user = PhotoImage(file="imagens/user.png")
        label_img = ctk.CTkLabel(
            master=frame_login, text="", width=300, image=img_user
        ).place(x=25, y=50)

        img_google = PhotoImage(file="imagens/google.png")
        button_img = ctk.CTkButton(
            master=frame_login,
            text="Continue com Google",
            image=img_google,
            width=300,
            fg_color="#db4a3b",
            text_color=("black"),
            hover_color="#dc5e50",
        ).place(x=25, y=379)

        img_fecebook = PhotoImage(file="imagens/facebook.png")
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
            font=("Times New Roman", 30, "italic"),
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
        )
        entry_email.place(x=25, y=165)

        entry_password = ctk.CTkEntry(
            master=frame_login,
            placeholder_text="Digite sua senha",
            font=("Roboto", 11, "bold"),
            width=300,
            show="*",
        )
        entry_password.place(x=25, y=205)

        checkbox_user = ctk.CTkCheckBox(
            master=frame_login, text="Lembrar email ou usuário", width=100
        ).place(x=25, y=250)

        def confirm_login():
            validate_user = entry_email.get()
            validate_email = entry_email.get()
            validate_password = entry_password.get()

            # Percorra a lista_registers para verificar se o usuário, email e senha estão presentes
            for user_info in lista_registers:
                stored_user, stored_email, stored_password, *_ = user_info
                # Verifique se o usuário, email e senha correspondem aos valores armazenados
                if (
                    validate_user == stored_user or validate_email == stored_email
                ) and validate_password == stored_password:
                    msg_successfully = CTkMessagebox(
                        title="Info",
                        icon="check",
                        message="Login efetuado com sucesso!",
                    )
                    # Se encontrarmos uma correspondência, podemos sair do loop
                    break
            else:
                # Se o loop não encontrar correspondência, exiba a mensagem de erro
                msg_successfully = CTkMessagebox(
                    title="Info", icon="cancel", message="Usuário ou senha incorretos!"
                )
                # Limpe os campos de entrada
                entry_password.delete(0, "end")

        # botões de login, register e recuperar senha
        button_login = ctk.CTkButton(
            master=frame_login,
            text="Login",
            width=300,
            command=confirm_login,
        )
        button_login.place(x=25, y=290)

        button_forgot_password = ctk.CTkButton(
            master=frame_login,
            text="Esqueci a senha",
            width=100,
            font=("Roboto", 11, "underline"),
            fg_color="#6a6a7c",
            hover_color="#4d4c4c",
            command=function.button_function,
        )
        button_forgot_password.place(x=225, y=250)

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

            def is_valid_email(email):
                # Verifica se o email tem um formato válido
                email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                return re.match(email_regex, email) is not None

            def coonfirm_register():
                add_user = entry_user_register.get()
                add_email = entry_email_register.get()
                add_password = entry_password_register.get()
                add_password_confirm = entry_confirm_password.get()

                # Verifica se o email inserido é válido
                if all([add_user, add_email, add_password, add_password_confirm]):
                    if is_valid_email(add_email):
                        if add_password_confirm == add_password:
                            lista_registers.append(
                                (
                                    add_user,
                                    add_email,
                                    add_password,
                                    add_password_confirm,
                                )
                            )

                            # Limpar os campos de entrada após armazenar os valores
                            entry_user_register.delete(0, "end")
                            entry_email_register.delete(0, "end")
                            entry_password_register.delete(0, "end")
                            entry_confirm_password.delete(0, "end")

                            msg_successfully = CTkMessagebox(
                                title="Info",
                                icon="check",
                                message="Cadastrado com sucesso!",
                            )

                            frame_register.pack_forget()
                            frame_login.pack(side=RIGHT)
                        else:
                            msg_successfully = CTkMessagebox(
                                title="Info",
                                icon="warning",
                                message="Campo de 'senha' e 'confirmar senha' devem ser iguais!",
                            )

                            entry_confirm_password.delete(0, "end")
                    else:
                        msg_successfully = CTkMessagebox(
                            title="Info", icon="warning", message="Email inválido!"
                        )

                else:
                    msg_successfully = CTkMessagebox(
                        title="Info",
                        icon="warning",
                        message="Por favor preencha todos os campos!",
                    )

            # teste para ver se a varial esta adicionando a lista
            def show_items():
                print("Itens armazenados:")
                for item in lista_registers:
                    print(item)

            show_button = ctk.CTkButton(
                master=frame_register, text="Mostrar Itens", command=show_items
            )
            show_button.place(x=25, y=1)

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

            img_google = PhotoImage(file="imagens/google.png")
            Button_img = ctk.CTkButton(
                master=frame_register,
                text="Vincule com Google",
                image=img_google,
                width=300,
                fg_color="#db4a3b",
                text_color=("black"),
                hover_color="#dc5e50",
            ).place(x=25, y=379)

            img_fecebook = PhotoImage(file="imagens/facebook.png")
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
