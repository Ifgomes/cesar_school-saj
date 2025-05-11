print("Bem vindo(a) a Love's Burguer! <3")
print("Escolha seu Hambúrguer.")
print("Temos 3 opções: Carne, Frango ou Soja")
hamburguer = input("Seu hambúrguer será de: ")
total = 0

if hamburguer == "Carne":
    total += 10
elif hamburguer == "Frango":
    total += 11
elif hamburguer == "Soja":
    total += 15
else:
    total

print("Deseja molho extra? Caso queira, digite 's' para confirmar ou 'n' para negar.")
extra = input()
if extra == "s":
    total +=2
    
print("Deseja uma bebida?. Temos suco, refrigerante ou nada")
bebida = input()

if bebida == "suco":
    total+=5
elif bebida == "refrigerante":
    total+=8
else:
    total

print(f"Sua escolha foi do Hambúguer de {hamburguer} com a bebida: {bebida}")
print(f"Total a pagar: R$ {total} ")
print("Agredecemos pela sua preferência, volte sempre <3")
