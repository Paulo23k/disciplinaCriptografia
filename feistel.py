# feistel.py

def cifra_feistel(texto, chave):
    if len(texto) % 2 != 0:
        texto += 'X'

    blocos = [texto[i:i+2] for i in range(0, len(texto), 2)]
    texto_cifrado = ''.join(blocos[::-1])
    
    return texto_cifrado

def des_cifra_feistel(texto, chave):
    if len(texto) % 2 != 0:
        texto += 'X'

    blocos = [texto[i:i+2] for i in range(0, len(texto), 2)]
    texto_decifrado = ''.join(blocos[::-1])

    return texto_decifrado
