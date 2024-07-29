print("Seja muito bem-vindo ao quiz da Gaby!")
answer_user = input("Quer começar? (S/N) ").strip().upper()

if answer_user != "S":
    quit()

score = 0

print("Começando...")
print("Quem desenvolveu o jogo Free Fire? \n (A) Garena \n (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ").strip().upper()

if answer_1 == "A":
    print("Correto!Parabéns jogador!")
    score += 1
else:
    print("Incorreto! Tente novamente jogador!")

print("Qual ano foi lançado o Free Fire?\n (A) 2016 \n (B) 2017 \n (C) 2018 \n (D) 2019 \n")
answer_2 = input("Resposta: ").strip().upper()

if answer_2 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto! Tente novamente jogador!")

print(f"Quiz acabou... Parabéns por ter chegado aqui, jogador! Pontuação: {score}/2")