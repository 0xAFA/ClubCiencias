import js
import string

mensaje = js.document.getElementById("message").value

mensaje = mensaje.replace("Ñ", "N").replace("ñ", "n").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
resultado = ""

diccionario = {letra: mensaje.count(letra) for letra in string.ascii_uppercase if mensaje.count(letra) > 0}

for letra, veces in sorted(diccionario.items(), key=lambda x: x[1], reverse=True):
    resultado += f"La letra {letra} aparece {veces} veces, un {veces * 100 / len(mensaje):.2f}%.\n"

resultado