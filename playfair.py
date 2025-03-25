import numpy as np

def criar_matriz_chave(chave):
    chave = chave.upper().replace("J", "I")
    alfabeto = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matriz = []
    usada = set()

    for letra in chave + alfabeto:
        if letra not in usada:
            matriz.append(letra)
            usada.add(letra)

    return np.array(matriz).reshape(5, 5)

def encontrar_posicao(matriz, letra):
    for i in range(5):
        for j in range(5):
            if matriz[i, j] == letra:
                return i, j

def preparar_texto(texto):
    texto = texto.upper().replace("J", "I").replace(" ", "")
    pares = []
    i = 0
    while i < len(texto):
        a = texto[i]
        b = texto[i + 1] if i + 1 < len(texto) else "X"
        if a == b:
            pares.append(a + "X")
            i += 1
        else:
            pares.append(a + b)
            i += 2
    return pares

def cifra_playfair(texto, chave, modo="criptografar"):
    matriz = criar_matriz_chave(chave)
    pares = preparar_texto(texto)
    resultado = ""

    for a, b in pares:
        linha1, col1 = encontrar_posicao(matriz, a)
        linha2, col2 = encontrar_posicao(matriz, b)

        if linha1 == linha2:
            if modo == "criptografar":
                resultado += matriz[linha1, (col1 + 1) % 5] + matriz[linha2, (col2 + 1) % 5]
            else:
                resultado += matriz[linha1, (col1 - 1) % 5] + matriz[linha2, (col2 - 1) % 5]

        elif col1 == col2:
            if modo == "criptografar":
                resultado += matriz[(linha1 + 1) % 5, col1] + matriz[(linha2 + 1) % 5, col2]
            else:
                resultado += matriz[(linha1 - 1) % 5, col1] + matriz[(linha2 - 1) % 5, col2]

        else:
            resultado += matriz[linha1, col2] + matriz[linha2, col1]

    return resultado
