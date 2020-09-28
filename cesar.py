continuar = input("Deseja continuar? [digite 0 para fechar o programa]: ")

while (continuar != "0"):
    print("="*50)
    opcao = input("Deseja cifrar ou decifrar? [0 para cifrar, 1 para decifrar]: ")

    if opcao != "0" and opcao != "1":
        print("Opção não existe.")
        break
    
    print("="*50)
    mensagem = input("Digite a mensagem [use apenas letras e espaços]: ")
    mensagem = mensagem.lower()
    chave = input("Qual chave quer usar: ")
    chave = chave.lower()
    print("="*50)
    if len(mensagem) == 0:
        print("Mensagem de tamanho inválido.")
        break

    for caractere in mensagem:
        if caractere not in "abcdefghijklmnopqrstuvwxyz ":
            print("A mensagem possui caracteres inválidos.")
            exit()
        
    if len(chave) != 1 or chave not in "abcdefghijklmnopqrstuvwxyz":
        print("Chave de tamanho errado ou possui caracteres inválidos.")
        break
    
    alfabeto_normal = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_modificado = ""

    for letra in range(26):
        posicao_da_letra = alfabeto_normal.index(chave) + letra

        if posicao_da_letra >= 26:
            posicao_da_letra -= 26

        alfabeto_modificado += alfabeto_normal[posicao_da_letra]

    nova_mensagem = ""

    if opcao == "0": 

        for caractere_mensagem in mensagem:
            if caractere_mensagem == " ":
                nova_mensagem += " "

            else:
                nova_mensagem += alfabeto_modificado[alfabeto_normal.index(caractere_mensagem)]

    if opcao == "1":

        for caractere_mensagem in mensagem:
            if caractere_mensagem == " ":
                nova_mensagem += " "
            
            else:
                nova_mensagem += alfabeto_normal[alfabeto_modificado.index(caractere_mensagem)]

    print(f'Mensagem original: {mensagem}')
    print(f'Mensagem decifrada: {nova_mensagem}')
    print("="*50)

    continuar = input("Deseja continuar? [digite 0 para fechar o programa]: ")