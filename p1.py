import tkinter as tk

root = tk.Tk()
root.title('Trabalho')
root.geometry('400x400')
root.configure(bg='#004544')

# Label for "Nome"
tk.Label(root, text='Nome ', font=('Arial', 12), bg='#004544', fg='white').pack(
    padx=5, pady=5)

entrada_nome = tk.Entry(root, width=35)
entrada_nome.pack(padx=5, pady=5)


root.mainloop()
