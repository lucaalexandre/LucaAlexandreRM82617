###############Declaracao da escolha da resposta de saida da enquete
resposta= ""
##################Declaracao das variaveis da quatidade de votos
qtde_windows = 0
qtde_unix = 0
qtde_linux = 0
qtde_netware = 0
qtde_macOS = 0
qtde_outro = 0
################lista de escolhas de sistemas operacionais
tabela = ['windows','unix','linux','netware','macOS','outro']
################print das escolhas para o usuario
print(tabela)
################condicao de repeticao de enquete
while(resposta!= "SIM"):
      sistema=""
      while sistema!= 0 and sistema!=1 and sistema!=2 and sistema!=3 and sistema!=4 and sistema!=5:
          sistema=int(input("Qual sistema voce escolhe para que seja usado como servidor? Escolha usando valores de 0 à 5, sendo 0 = Windows e 5 = outros sistemas "))

      if sistema== 0:
          qtde_windows+=1
      elif sistema==1:
          qtde_unix+=1
      elif sistema==2:
          qtde_linux+=1
      elif sistema==3:
          qtde_netware+=1
      elif sistema==4:
          qtde_macOS+=1
      elif sistema==5:
          qtde_outro+=1
#############escolha entre sair e continuar a enquete
      resposta = input("Deseja sair da votacao? ").upper()
######################resultado da enquete
print("Resultado dos votos")
print("O total de pessoas que votaram para que seja o Windows foi de {}".format(qtde_windows))
print("O total de pessoas que votaram para que seja o Unix foi de {}".format(qtde_unix))
print("O total de pessoas que votaram para que seja o Linux foi de {}".format(qtde_linux))
print("O total de pessoas que votaram para que seja o Netware foi de {}".format(qtde_netware))
print("O total de pessoas que votaram para que seja o MacOS foi de {}".format(qtde_macOS))
print("O total de pessoas que votaram para que seja outros sistemas foi de {}".format(qtde_outro))



