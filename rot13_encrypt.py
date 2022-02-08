import js
import string

message = js.document.getElementById("message").value

message = message.replace("Ñ", "N").replace("ñ", "n").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")

chars = string.ascii_uppercase

def encrypt_letter(letter):
    if letter in chars:
        return chars[ (chars.index(letter) +13)%len(chars) ]
    return letter

encrypted_message_list = [encrypt_letter(letter) for letter in message]
"".join(encrypted_message_list)