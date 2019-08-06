import random


def encrypt(msg):
    encMsg = ""
    otp = ""
    binOtp = ""
    for i in range(len(msg)):
        key = chr(random.randint(0, 127))
        otp += key
        bnMsg = ord(msg[i])
        bnKey = ord(key)
        cipherMsg = bnMsg ^ bnKey
        cipherMsg = bin(cipherMsg)[2:].zfill(8)
        encMsg += cipherMsg

    for letter in otp:
        binaryChar = str(bin(ord(letter))[2:].zfill(8))
        binOtp += binaryChar
    return encMsg, binOtp


def decrypt(msg, key):
    intMsg = int(msg, base=2)
    intKey = int(key, base=2)
    return to_chars(bin(intMsg ^ intKey)[2:].zfill(len(msg)))


def to_chars(message):
    message = int(message, 2)
    return message.to_bytes((message.bit_length() + 7) // 8, 'big').decode()


def main():
    print("Bienvenido al ejercicio OTP\nOpciones:\n1. Encriptar mensaje\n2. Desencriptar mensaje (Para esta opcion "
          "asegurese de que el archivo del mensaje cifrado y el archivo de la llave esten en esta misma carpeta)")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        msg = input("Ingrese el mensaje a encriptar: ")
        encriptedMsg, otp = encrypt(msg)
        f = open("encriptedMessage.txt", "w+")
        f.write(encriptedMsg)
        f.close()
        f = open("otp.txt", "w+")
        f.write(otp)
        f.close()
        print("Mensaje encriptado!")
    elif op == 2:
        f = open("encriptedMessage.txt", "r")
        encriptedMsg = f.read()
        f.close()
        f = open("otp.txt", "r")
        otp = f.read()
        f.close()
        msg = decrypt(encriptedMsg, otp)
        print("Mensaje: " + msg)


main()