import WordList as wl
import hashlib
#Contraseñas Proporcionadas por el usuario
#import Contra_usu as cu

#Importaciones
#Diccionario_Craker = wl.diccionario_craker #diccionario con las contraseñas a provar
#contraseñas, has_craker = wl.Craker()

#Hash_Usuario, Usuario = cu.Contraseña_Usuario() #contraseña dada por el usuario y la contraseña echa hash
#Usuario_Hash_Comparar = cu.Hash_Usuario() #Hash-256 para comparar y buscar que contraseña es


#Contraseña_correcta = "No existe"


#if hash in Diccionario_Craker:
#    print(Diccionario_Craker[hash], "siesat")

from charset_normalizer import from_bytes

hex_Prueba_utf_8 = "61646d696e23c3b16f" 
hex_Prueba2_cp1252 = "636f6e7472617365f161313233"
hex_Prueba3_cp1251 = "eceef7e0ebeae8ede0313937350d" # Ruso
hex_Prueba4_cp1250 = "6d616c6f706f6c736b61e2"
hex_Prueba5_utf_16_le = "700061007300730077006f0072006400310032003300" 

def lol():
    return [
        hex_Prueba_utf_8, 
        hex_Prueba2_cp1252, 
        hex_Prueba3_cp1251, 
        hex_Prueba4_cp1250, 
        hex_Prueba5_utf_16_le
    ]

def Decodificadors_Optimizado(bytes_crudos):
    # La librería hace todo el trabajo pesado de analizar el idioma y los bytes
    resultado = from_bytes(bytes_crudos).best()
    if resultado:
        print(f"Codificación detectada: {resultado.encoding}")
        return str(resultado) # Retorna el texto ya decodificado
    return "Error al decodificar"

# Ejecución
for hex_str in lol():
    los_bytes = bytes.fromhex(hex_str)
    texto_final = Decodificadors_Optimizado(los_bytes)
    print(f"Texto: {texto_final}\n{'-'*20}")