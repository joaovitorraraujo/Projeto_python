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
from tkinter import PhotoImage
from tkinter import RIGHT
import function
import re
from PIL import Image

lista_registers = []


window = ctk.CTk()


class TelaLogin:
    def __init__(self):
        self.window = window
        self.theme()
        self.config_window()
        self.screen_login()
        self.window.mainloop()

    # tema
    def theme(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

    label_welcome = ctk.CTkLabel(
        master=window,
        text="Bem-Vindo ao Projeto",
        font=("Arial 20", 15, "underline"),
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
    label_presentation3.place(x=110, y=105)

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
            font=("Arial 20", 30),
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

        def on_enter_pressed(event):
            event.widget.tk_focusNext().focus()
    
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

        entry_email.bind("<Return>", on_enter_pressed)

        view_password = ctk.BooleanVar()

        checkbox_view_password = ctk.CTkCheckBox(
            master=frame_login, text="Mostrar senha", width=100, variable=view_password
        )
        checkbox_view_password.place(x=25, y=250)

        def toggle_password_visibility(*args):
            if view_password.get():
                entry_password.configure(show="")
            else:
                entry_password.configure(show="*")

        view_password.trace("w", toggle_password_visibility)

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

                    entry_email.delete(0, "end")
                    entry_password.delete(0, "end")

                    # serve para esconder a uma tela
                    window.withdraw()
                    create_menu()
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

        # função p mostrar os registros atuais
        def show_items():
            number_list = len(lista_registers)
            if len(lista_registers) == 0:
                msg_successfully = CTkMessagebox(
                    title="Lista de cadastros",
                    icon=None,
                    message="Não houve nenhum cadastro!",
                )
            else:
                message = ""
                for i in range(number_list):
                    message += f"Lista {i + 1} = {lista_registers[i]}\n"

                msg_successfully = CTkMessagebox(
                    title="Lista de cadastros",
                    icon=None,
                    message=message,
                )

        button_forgot_password = ctk.CTkButton(
            master=frame_login,
            text="Esqueci a senha",
            width=100,
            font=("Roboto", 11, "underline"),
            fg_color="#6a6a7c",
            hover_color="#4d4c4c",
            command=show_items,
        )
        button_forgot_password.place(x=225, y=250)
        
        def create_menu():
            screen_menu = ctk.CTkToplevel(master=window)
            screen_menu.title("Sistema de login")
            screen_menu.geometry("1366x768")
            screen_menu.resizable(True, True)
            screen_menu.wm_iconbitmap("imagens/icon.ico")

            home_image = ctk.CTkImage(
                dark_image=Image.open("imagens/home_light.png"), size=(40, 40)
            )
            chat_image = ctk.CTkImage(
                dark_image=Image.open("imagens/chat_light.png"), size=(40,40)
            )
            
            img_options_menu = ctk.CTkImage(
                dark_image=Image.open("imagens/user.png"), size=(40, 40)
            )
            img_add_user = ctk.CTkImage(
                dark_image=Image.open("imagens/add_user_light.png"), size=(40, 40)
            )

            navigation_frame = ctk.CTkFrame(master=screen_menu, corner_radius=0,width=300 ,height=768)
            navigation_frame.grid(row=0, column=0, sticky="nsew")
            navigation_frame.grid_rowconfigure(4, weight=1)
            
            label_logo1 = ctk.CTkLabel(
                master=navigation_frame,
                text="Sistema ",
                font=(
                    "Impact",
                    30,
                ),
                text_color="white",
                bg_color="transparent",
            )
            label_logo1.place(x=20, y=20)

            label_logo2 = ctk.CTkLabel(
                master=navigation_frame,
                text="De",
                font=(
                    "Impact",
                    16,
                ),
                text_color="white",
                bg_color="transparent",
            )
            label_logo2.place(x=129, y=29)

            label_logo3 = ctk.CTkLabel(
                master=navigation_frame,
                text="Login",
                font=("Impact", 59),
                text_color="#0080e4",
                bg_color="transparent",
            )
            label_logo3.place(x=20, y=45)

            label_logo3.lift()
            label_logo2.lift()
            label_logo1.lift()
            

            home_button = ctk.CTkButton(
                master=navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text="Menu Principal",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=home_image,
                anchor="w",
            )
            home_button.grid(row=1, column=0,pady=(120,0) ,sticky="ew")

            chat_button = ctk.CTkButton(
                navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text="Chat",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=chat_image,
                anchor="w",
            )
            chat_button.grid(row=2, column=0,pady=(0,0), sticky="ew")
            
            add_button_friend = ctk.CTkButton(
                navigation_frame,
                corner_radius=0,
                height=40,
                border_spacing=10,
                text="Adicionar amigo",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                image=img_add_user,
                anchor="w",
            )
            add_button_friend.grid(row=3, column=0,pady=(0,0), sticky="ew")
            
            def options_menu(escolha):
                if escolha == "Sair":
                    msg_exit = CTkMessagebox(
                        title="Sair?",
                        message="Deseja sair do programa?",
                        icon="question",
                        option_1="Cancelar",
                        option_2="Sair e voltar para tela de login",
                        option_3="Sair e fechar programa",
                        button_color="Red",
                        button_hover_color="#b30000",
                        button_width=40,
                        width=440,
                    )

                    response = msg_exit.get()

                    if response == "Sair e fechar programa":
                        window.destroy()
                        screen_menu.destroy()

                    elif response == "Sair e voltar para tela de login":
                        # > deiconify() serve para mostrar a tela que tinha sido escondida
                        window.deiconify()
                        screen_menu.destroy()

            label_img_menu = ctk.CTkLabel(
                master=navigation_frame, text="", image=img_options_menu
            )
            label_img_menu.place(x=20, y=630)
            
            label_user = ctk.CTkLabel(
                master=navigation_frame, text="User"
            )
            label_user.place(x=65, y=630)
            
            label_user = ctk.CTkLabel(
                master=navigation_frame, text="E-mail@gmail.com",font=("Arial", 10, "underline")
            )
            label_user.place(x=65, y=650)

            combobox = ctk.CTkOptionMenu(
                master=navigation_frame,
                values=["Configurações", "Sair"],
                command=options_menu,
            )
            combobox.grid(row=5, column=0, padx=20, pady=(365,50), sticky="s")
            combobox.set("Opções")

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
                font=(
                    "Arial 20",
                    30,
                ),
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

            entry_user_register.bind("<Return>", on_enter_pressed)
            entry_email_register.bind("<Return>", on_enter_pressed)
            entry_password_register.bind("<Return>", on_enter_pressed)
            entry_confirm_password.bind("<Return>", on_enter_pressed)

            confirm_terms = ctk.BooleanVar()

            checkbox_terms = ctk.CTkCheckBox(
                master=frame_register,
                text="Aceito os termos de serviço",
                width=145,
                variable=confirm_terms,
            )
            checkbox_terms.place(x=25, y=270)

            def show_terms():
                # Termos de uso simples

                # Mostrar messagebox com os termos de uso
                view_terms = CTkMessagebox(
                    title="Termos de Uso",
                    icon=None,
                    message="Bem-vindo ao nosso sistema de login!\n\nAo usar este aplicativo, você concorda em seguir estas regras simples:\n\n- Não compartilhe suas credenciais com outras pessoas.\n- Não faça atividades ilegais usando este serviço.\n- Respeite a privacidade de outros usuários.\n\nObrigado por usar nosso serviço!",
                )

            button_terms = ctk.CTkButton(
                master=frame_register,
                text="Acesse os termos",
                width=100,
                font=("Roboto", 11, "underline"),
                fg_color="#6a6a7c",
                hover_color="#4d4c4c",
                command=show_terms,
            )
            button_terms.place(x=225, y=270)

            def coonfirm_register():
                add_user = entry_user_register.get()
                add_email = entry_email_register.get()
                add_password = entry_password_register.get()
                add_password_confirm = entry_confirm_password.get()

                # Verifica se o email inserido é válido
                if (
                    all([add_user, add_email, add_password, add_password_confirm])
                    and confirm_terms.get()
                ):
                    if function.is_valid_email(add_email):
                        if not function.user_exists(
                            add_user, add_email, lista_registers
                        ):
                            if not function.email_exists(
                                add_user, add_email, lista_registers
                            ):
                                if add_password_confirm == add_password:
                                    lista_registers.append(
                                        (
                                            add_user,
                                            add_email,
                                            add_password,
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
                                    title="Info",
                                    icon="warning",
                                    message="E-mail já existente!",
                                )

                                entry_email_register.delete(0, "end")
                        else:
                            msg_successfully = CTkMessagebox(
                                title="Info",
                                icon="warning",
                                message="Usuário já existente!",
                            )

                            entry_user_register.delete("end", "end")
                    else:
                        msg_successfully = CTkMessagebox(
                            title="Info",
                            icon="warning",
                            message="Formato de E-mail inválido!",
                        )

                else:
                    msg_successfully = CTkMessagebox(
                        title="Info",
                        icon="warning",
                        message="Por favor preencha todos os campos!",
                    )

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
