def cifra_cesar(texto, chave, modo="criptografar"):
    resultado = []
    for char in texto:
        if char.isalpha():
            deslocamento = chave if modo == "criptografar" else -chave
            novo_char = chr((ord(char.upper()) - ord('A') + deslocamento) % 26 + ord('A'))
            resultado.append(novo_char)
        else:
            resultado.append(char)
    return ''.join(resultado)
