import customtkinter

janela = customtkinter.CTk()
janela.title('Conecte-se')
janela.geometry('350x250')
janela.resizable(width=False, height=False)

# configurações de Label
label = customtkinter.CTkLabel(janela, text='Login', text_color="#0000FF")
label.place(relx=0.05, rely=0.05)

# configuração das Entrys
entry = customtkinter.CTkEntry(janela, placeholder_text='Digite seu Email')
entry.place(relx=0.05, rely=0.20)

entry2 = customtkinter.CTkEntry(janela,show='*', placeholder_text='Digite sua senha')
entry2.place(relx=0.05, rely=0.35)

botao = customtkinter.CTkButton(janela, width=60, text='Entrar')
botao.place(relx=0.25, rely=0.50)

janela.mainloop()
