import aes
# import rsa
import vigenere
import playfair
import cesar
import feistel

def menu():
    print("\nEscolha um algoritmo de criptografia:")
    print("1 - AES")
    print("2 - RSA(em-breve...)")
    print("3 - Vigenère")
    print("4 - Playfair")
    print("5 - Cifra de César")
    print("6 - Cifra de Feistel")
    
    escolha = input("Digite a opção desejada: ")

    texto = input("Digite o texto: ")
    modo = input("Digite 'c' para cifrar ou 'd' para decifrar: ").lower()

    if escolha == "1":
        print("Dica: A chave para AES deve ter 16, 24 ou 32 caracteres.")
        chave = input("Digite a chave (16, 24 ou 32 caracteres): ")
        while len(chave) not in [16, 24, 32]:
            print("Erro: A chave deve ter 16, 24 ou 32 caracteres.")
            chave = input("Digite a chave (16, 24 ou 32 caracteres): ")
        if modo == "c":
            print("Texto cifrado:", aes.aes_encrypt(texto, chave))
        else:
            print("Texto decifrado:", aes.aes_decrypt(texto, chave))

    # elif escolha == "2":
    #     print("Dica: O RSA não exige chave manual para o usuário. As chaves são geradas automaticamente.")
    #     rsa.rsa_generate_keys()  # Gerando as chaves
    #     if modo == "c":
    #         print("Texto cifrado:", rsa.rsa_encrypt(texto)) 
    #     else:
    #         print("Texto decifrado:", rsa.rsa_decrypt(texto))

    elif escolha == "3":
        print("Dica: A chave para a Cifra de Vigenère deve ser uma palavra sem espaços e com letras do alfabeto.")
        chave = input("Digite a chave: ")
        while not chave.isalpha():
            print("Erro: A chave deve ser uma palavra com letras do alfabeto (sem espaços).")
            chave = input("Digite a chave: ")
        print("Texto resultado:", vigenere.vigenere(texto, chave, "criptografar" if modo == "c" else "decifrar"))

    elif escolha == "4":
        print("Dica: A chave para a cifra de Playfair deve ser uma palavra sem repetição de letras e sem espaços.")
        chave = input("Digite a chave para Playfair: ")
        while len(set(chave)) != len(chave) or ' ' in chave:
            print("Erro: A chave não deve ter letras repetidas e não deve conter espaços.")
            chave = input("Digite a chave para Playfair: ")
        print("Texto resultado:", playfair.cifra_playfair(texto, chave, "criptografar" if modo == "c" else "decifrar"))
        
    elif escolha == "5":
        print("Dica: A Cifra de César usa um número como chave. O número deve estar entre 1 e 25.")
        deslocamento = int(input("Digite o deslocamento para a Cifra de César (1-25): "))
        while not (1 <= deslocamento <= 25):
            print("Erro: O deslocamento deve estar entre 1 e 25.")
            deslocamento = int(input("Digite o deslocamento para a Cifra de César (1-25): "))
        print("Texto resultado:", cesar.cifra_cesar(texto, deslocamento, modo="criptografar" if modo == "c" else "decifrar"))

    elif escolha == "6":
        print("Dica: A chave para a Cifra de Feistel pode ser uma string, geralmente de tamanho fixo.")
        chave = input("Digite a chave para a Cifra de Feistel: ")
        if modo == "c":
            print("Texto cifrado:", feistel.cifra_feistel(texto, chave))
        else:
            print("Texto decifrado:", feistel.des_cifra_feistel(texto, chave)) 

    else:
        print("Opção inválida.")

menu()
