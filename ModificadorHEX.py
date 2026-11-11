"""Destripador es el sistema de preparacion Big Data"""
#se busca dividir los diccionarios txt con claves en partes mas pequeñas para ser sometidas a multiproceso

#HEX[eceef7e0ebeae8ede0313937350d]

#debo poner este hex en algun archivo usar un for in y cuando lo encuentre traducirlo y escribirlo donde se quedo 

import DecodificadorHEX as dhex
import os 

print("Recuerda cargar los archivos a revision y modificar el ModificadorHEX.py")

Archivo_Original = "Cambios.txt"   #<-- you must mod the .txt for which used 
Archivo_Copia = "Cambios_2.txt"

with open(Archivo_Original, "r", encoding="utf-8") as c, \
    open(Archivo_Copia, "w", encoding= "utf-8") as c2:
    
    for linea in c:
        linea2 = linea.strip()
       
        if linea2.startswith("$HEX[") and linea2.endswith("]"):
            Hex_Limpio = linea2.removeprefix("$HEX[").removesuffix("]")
            Resuelto = dhex.Decodificadors(Hex_Limpio)
            c2.write(f"{Resuelto} \n")
            print(f"siesta {linea2}")

        else: 
            c2.write(f"{linea2}\n")
            #c.write("\n")
            pass
    
    try:
        os.replace(Archivo_Copia, Archivo_Original)
    except:
        pass
    #print(linea)