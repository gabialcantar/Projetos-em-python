import tkinter as tk

def somar():
    numero = int(entry_numero1.get())
    numero2 = int(entry_numero2.get())
    soma = numero + numero2
    label_resultado.config(text=f"A soma do seu resultado é: {soma}")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Cria e posiciona os widgets (componentes da interface)
label_numero1 = tk.Label(root, text="Escreva o seu primeiro número:")
label_numero1.pack()

entry_numero1 = tk.Entry(root)
entry_numero1.pack()

label_numero2 = tk.Label(root, text="Escreva seu segundo número:")
label_numero2.pack()

entry_numero2 = tk.Entry(root)
entry_numero2.pack()

botao_somar = tk.Button(root, text="Somar", command=somar)
botao_somar.pack()

label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Inicia o loop principal da interface
root.mainloop()