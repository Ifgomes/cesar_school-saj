print("Bem vindo(a) a Love's Tapiocaria")

ingrediente1 = ""
ingrediente2 = ""
ingrediente3 = ""
ingrediente4 = ""
ingrediente5 = ""

contador = 1

while contador <= 5:
    print(f"Digite o ingrediente {contador}")
    escolha = input()

    if escolha == "sair":
        print("Você saiu da Love's Tapiocaria")
        break
    
    else:
        if contador == 1:
            ingrediente1 = escolha
        elif contador == 2:
            ingrediente2 = escolha
        elif contador == 3:
            ingrediente3 = escolha
        elif contador == 4:
            ingrediente4 = escolha
        elif contador == 5:
            ingrediente5 = escolha
        
        contador = contador + 1 
        
print("Sua tapioca está pronta")
