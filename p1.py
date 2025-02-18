import tkinter as tk
from tkinter import messagebox

def exibir_info():
    nome = entrada_nome.get()
    genero = opcao.get()
    idade = entrada_idade.get()
    nascimento = entrada_nascimento.get()
    
    info = f"Nome: {nome}\nGênero: {genero}\nIdade: {idade}\nData de Nascimento: {nascimento}"
    messagebox.showinfo("Informações", info)

root = tk.Tk()
root.title('Trabalho')
root.geometry('400x400')
root.configure(bg='black')

# "Nome"
tk.Label(root, text='Nome ', font=('Arial', 12), bg='black', fg='white').pack(padx=5, pady=5)
entrada_nome = tk.Entry(root, width=35)
entrada_nome.pack(padx=5, pady=5)

# Gênero
opcao = tk.StringVar(value='Não informado')
tk.Label(root, text='Gênero', font=('Arial', 12), bg='black', fg='white').pack(padx=5, pady=5)
tk.Radiobutton(root, text='Masculino', variable=opcao, value='Masculino', bg='black', fg='white', font=('Arial', 12)).pack(padx=5, pady=5)
tk.Radiobutton(root, text='Feminino', variable=opcao, value='Feminino', bg='black', fg='white', font=('Arial', 12)).pack(padx=5, pady=5)

# Idade
tk.Label(root, text="Idade:", font=('Arial', 12), bg="black", fg="white").pack(padx=5, pady=5)
entrada_idade = tk.Entry(root, width=5)
entrada_idade.pack(padx=5, pady=5)

# Data de nascimento
tk.Label(root, text="Data de Nascimento:", font=('Arial', 12), bg='black', fg='white').pack(padx=5, pady=5)
entrada_nascimento = tk.Entry(root, width=10)
entrada_nascimento.pack(padx=5, pady=5)

# Botão para exibir informações
tk.Button(root, text="Mostrar Informações", command=exibir_info, font=('Arial', 12), bg='#008080', fg='white').pack(padx=5, pady=10)

root.mainloop()
