"""En esta parte se leera todo el .txt para posteriormente pasarlo a un diccionario para su comparacion"""

"""This part the script read all .txt to before diccionarie pass it compare"""

import hashlib
diccionario_craker = {}

def Craker():
    
    #other diccionary hashmob.net_2025.large.txt
    #claves.txt
    with open("claves.txt", "r", encoding="utf-8") as Archivowl:
        Archivo_Craker = Archivowl.readlines()  

        for Lineas in Archivo_Craker:
            contraseñas = Lineas.strip()
            usuario = contraseñas
            has_craker = hashlib.sha256(contraseñas.encode("utf-8")).hexdigest()
            diccionario_craker[has_craker] = contraseñas
            print(contraseñas, has_craker)

    return contraseñas, has_craker

#for i, j in diccionario_craker.items():
#    print(j)
# para una comparacion rapida debo invertir el como el diccionario busca 

Craker()