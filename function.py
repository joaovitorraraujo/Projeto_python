import customtkinter as ctk

def second_window():
    window_teste = ctk.CTk()
    
    
    window_teste.title("Sistema de login")
    window_teste.geometry("700x460")
    window_teste.resizable(False, False)
    window_teste.iconbitmap("imagens/icon.ico")
        
    window_teste.mainloop()