import string

print("Introduce tu mensaje.")
mensaje = input()
mensaje = mensaje.replace("Ñ", "N").replace("ñ", "n").upper().replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")

for letra in string.ascii_uppercase:
    veces = mensaje.count(letra)
    if veces > 0:
        print(f"La letra {letra} aparece {veces} veces, un {veces * 100 / len(mensaje):.2f}%.")

# Códigos para colorear la salida de terminal:
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    print("Introduce una letra para reemplazar, o 'Salir' para salir.")
    letra = input().upper()
    if letra=="SALIR": break
    print("Introduce con qué letra reemplazarla.")
    letra2 = input().upper()
    print(mensaje.replace(letra, "\033[91m" + letra2 + "\033[0m").capitalize())
    mensaje = mensaje.replace(letra, "\033[94m" + letra2 + "\033[0m")
