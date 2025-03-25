from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

def aes_encrypt(texto, chave):
    chave_bytes = chave.encode('utf-8')
    chave_bytes = chave_bytes.ljust(32, b'\0')[:32]
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(chave_bytes, AES.MODE_CBC, iv)
    texto_bytes = texto.encode('utf-8')
    texto_padded = pad(texto_bytes, AES.block_size)
    texto_cifrado = cipher.encrypt(texto_padded)
    return base64.b64encode(iv + texto_cifrado).decode()

def aes_decrypt(texto_cifrado, chave):
    chave_bytes = chave.encode('utf-8')
    chave_bytes = chave_bytes.ljust(32, b'\0')[:32]
    texto_cifrado_bytes = base64.b64decode(texto_cifrado)
    iv = texto_cifrado_bytes[:AES.block_size]
    texto_cifrado_bytes = texto_cifrado_bytes[AES.block_size:]
    cipher = AES.new(chave_bytes, AES.MODE_CBC, iv)
    texto_decifrado = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size)
    return texto_decifrado.decode('utf-8')
