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

    def decrypt_letter(letter):
        if letter in chars:
            return chars[alfabeto.index(letter)]
        return letter

    decrypted_message_list = [decrypt_letter(letter) for letter in message]
    resultado = "".join(decrypted_message_list)

resultado