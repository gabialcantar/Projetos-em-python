#LER A ENTRADA DO USUARIO 
meses = [ "January", "February", "March", "April", "May", "June", "July", "August", "Setember", "Outuber"
      , "November", "December"

]
numero = int(input())

#VERIFICAR SE O NUMERO ESTA ENTRE 1 E 12
if 1<numero<=12:
    print(meses[numero - 1])
else:
    print("numero fora do intervalo esperado")