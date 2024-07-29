import tkinter as tk
from tkinter import messagebox

# Lista para armazenar as despesas
despesas = []

# Função para adicionar uma despesa
def adicionar_despesa():
    nome = entry_nome.get()
    valor = entry_valor.get()
    
    if nome and valor:
        try:
            valor = float(valor)
            despesa = {"nome": nome, "valor": valor}
            despesas.append(despesa)
            atualizar_lista()
            entry_nome.delete(0, tk.END)
            entry_valor.delete(0, tk.END)
            messagebox.showinfo("Sucesso", "Despesa adicionada com sucesso!")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico.")
    else:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

# Função para listar todas as despesas
def atualizar_lista():
    listbox_despesas.delete(0, tk.END)
    for despesa in despesas:
        listbox_despesas.insert(tk.END, f"{despesa['nome']}: R${despesa['valor']:.2f}")

# Função para calcular o total de despesas
def total_despesas():
    total = sum(despesa['valor'] for despesa in despesas)
    messagebox.showinfo("Total de Despesas", f"Total de despesas: R${total:.2f}")

# Configurar a janela principal
root = tk.Tk()
root.title("Sistema de Gerenciamento de Despesas")

# Labels e entradas
tk.Label(root, text="Nome da Despesa:").grid(row=0, column=0, padx=10, pady=10)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Valor da Despesa:").grid(row=1, column=0, padx=10, pady=10)
entry_valor = tk.Entry(root)
entry_valor.grid(row=1, column=1, padx=10, pady=10)

# Botões
btn_adicionar = tk.Button(root, text="Adicionar Despesa", command=adicionar_despesa)
btn_adicionar.grid(row=2, column=0, columnspan=2, pady=10)

btn_total = tk.Button(root, text="Total de Despesas", command=total_despesas)
btn_total.grid(row=3, column=0, columnspan=2, pady=10)

# Listbox para exibir as despesas
listbox_despesas = tk.Listbox(root, width=40)
listbox_despesas.grid(row=4, column=0, columnspan=2, pady=10)

# Executar a aplicação
root.mainloop()