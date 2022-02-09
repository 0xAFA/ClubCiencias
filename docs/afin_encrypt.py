import js
import string

message = js.document.getElementById("message").value
a = int(js.document.getElementById("p1").value)
b = int(js.document.getElementById("p2").value)

message = message.replace("Ñ", "N").replace("ñ", "n").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")

chars = string.ascii_uppercase

def encrypt_letter(letter):
    if letter in chars:
        return chars[ (a*chars.index(letter)+b)%len(chars) ]
    return letter

encrypted_message_list = [encrypt_letter(letter) for letter in message]
"".join(encrypted_message_list)