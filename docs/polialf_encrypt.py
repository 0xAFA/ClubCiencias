import js
import string

message = js.document.getElementById("message").value
alfabeto = js.document.getElementById("p1").value

resultado = ""

if len(alfabeto) != 26:
    resultado = "El alfabeto de encriptación debe tener 26 letras."
else:
    message = message.replace("Ñ", "N").replace("ñ", "n").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
    chars = string.ascii_uppercase

    def encrypt_letter(letter):
        if letter in chars:
            return alfabeto[chars.index(letter)]
        return letter

    encrypted_message_list = [encrypt_letter(letter) for letter in message]
    resultado = "".join(encrypted_message_list)

resultado