#declarando a variavel input(login do usuario e senha)
login = input("Qual sera seu login: " )
senha = len(input("Escreva sua senha: "))
#condicao para que seja avisado de quantos digitos deve ter
if senha <= 8 :
    print("Para uma melhor seguranca use uma senha com mais digitos")
else:
    print("Secesso")
print(login, senha)