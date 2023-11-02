import string
import random

def generar_contrasena(longitud, usar_letras, usar_numeros, usar_simbolos):
    caracteres = ''
    if usar_letras:
        caracteres += string.ascii_letters  # Añade letras mayúsculas y minúsculas
    if usar_numeros:
        caracteres += string.digits  # Añade números del 0 al 9
    if usar_simbolos:
        caracteres += string.punctuation  # Añade símbolos especiales

    if not caracteres:
        raise ValueError("Debes seleccionar al menos un tipo de caracter para generar la contraseña")

    # Generar contraseña aleatoria
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))

    return contrasena

# Uso de la función
longitud_de_contrasena = 12  # Define la longitud de la contraseña deseada
incluye_letras = True  # Define si quieres incluir letras
incluye_numeros = True  # Define si quieres incluir números
incluye_simbolos = True  # Define si quieres incluir símbolos

# Generar y mostrar la contraseña
contrasena_segura = generar_contrasena(longitud_de_contrasena, incluye_letras, incluye_numeros, incluye_simbolos)
print(f"Tu contraseña segura es: {contrasena_segura}")
