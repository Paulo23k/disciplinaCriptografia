def vigenere(texto, chave, modo="criptografar"):
    texto = texto.upper()
    chave = chave.upper()
    resultado = ""
    chave_expandida = (chave * ((len(texto) // len(chave)) + 1))[:len(texto)]
    
    for i in range(len(texto)):
        if texto[i].isalpha():
            deslocamento = ord(chave_expandida[i]) - ord('A')
            if modo == "criptografar":
                resultado += chr((ord(texto[i]) - ord('A') + deslocamento) % 26 + ord('A'))
            else:
                resultado += chr((ord(texto[i]) - ord('A') - deslocamento) % 26 + ord('A'))
        else:
            resultado += texto[i]
    return resultado
