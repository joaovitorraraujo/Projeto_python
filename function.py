import customtkinter as ctk
import CTkMessagebox
import re


# validar formato de email
def is_valid_email(email):
    # Verifica se o email tem um formato válido
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None


def second_window():
    window_teste = ctk.CTk()

    window_teste.title("Sistema de login")
    window_teste.geometry("700x460")
    window_teste.resizable(False, False)
    window_teste.iconbitmap("imagens/icon.ico")

    window_teste.mainloop()


# verificar se email ja existe
def email_exists(user, email, lista):
    for stored_user, stored_email, *_ in lista:
        if stored_email == email:
            return True
    return False


# verificar se usuario ja existe
def user_exists(user, email, lista):
    for stored_user, stored_email, *_ in lista:
        if stored_user == user:
            return True
    return False

