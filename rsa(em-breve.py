# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import base64

# def rsa_generate_keys():
#     key = RSA.generate(2048)
#     with open("keys/private.pem", "wb") as priv_file:
#         priv_file.write(key.export_key())
#     with open("keys/public.pem", "wb") as pub_file:
#         pub_file.write(key.publickey().export_key())

# def rsa_encrypt(texto, public_key_path="keys/public.pem"):
#     with open(public_key_path, "rb") as file:
#         key = RSA.import_key(file.read())
#     cipher = PKCS1_OAEP.new(key)
#     encrypted = cipher.encrypt(texto.encode())
#     return base64.b64encode(encrypted).decode()

# def rsa_decrypt(texto_cifrado, private_key_path="keys/private.pem"):
#     with open(private_key_path, "rb") as file:
#         key = RSA.import_key(file.read())
#     cipher = PKCS1_OAEP.new(key)
#     decrypted = cipher.decrypt(base64.b64decode(texto_cifrado))
#     return decrypted.decode()
