#PROVA 4 LOGICA DE PROGRAMAÇÃO
senha_cadastrada = input("Definir senha: ")

print("Ligue o celular e insira a senha para desbloquear.")

# Número máximo de tentativas
tentaivas = 3

for tentativa in range(tentaivas):
    senha_inserida = input("Insira a senha: ")
    
    if senha_inserida == senha_cadastrada:
        print("Bem-vindo.")
        break
    else:
        tentativas_restantes = tentaivas - (tentativa + 1)
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem {tentativas_restantes} tentativa(s) restante(s).")
        else:
            print("Senha incorreta. O celular está bloqueado!")