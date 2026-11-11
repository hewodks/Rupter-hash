"""Para el Funcionamiento correcto del Comparaador se Necesita tener una amplia disponibilidad de RAM |dependiendo del world list|"""

#You are need enought memory RAM because the worldlist used a lot of RAM 
import WordList as wl
import sys
#Contraseñas Proporcionadas por el usuario
import Contra_usu as cu

#Importaciones
Diccionario_Craker = wl.diccionario_craker #diccionario con las contraseñas a provar


#Hash_Usuario, Usuario = cu.Contraseña_Usuario() #contraseña dada por el usuario y la contraseña echa hash
#Usuario_Hash_Comparar = cu.Hash_Usuario() #Hash-256 para comparar y buscar que contraseña es
#contraseñas = wl.Craker()

Contraseña_correcta = "No existe"

def Comparador_Contraseña(Hash_Usuario, Usuario): #aqui la funcion se encarga de comparar contraseña -> hash y buscar parentesco
    if Hash_Usuario in Diccionario_Craker: #se usa la busqueda por diccionario por tabla de hash
        Contraseña_correcta = Diccionario_Craker[Hash_Usuario]  #si se encuentra se procede a guardar la contraseña plana y pasarla a una variable str
        print(f"La {Contraseña_correcta} se encuentra siendo el hash {Hash_Usuario}")
        print("----------------------------------------------------------------------------------")
        #se imprime la contraseña plana correcta y se pone el hash de la contraseña
    else:
        print(f"no esta la |{Usuario}| del hash |{Hash_Usuario}|")
        print("----------------------------------------------------------------------------------")
        #si no es correcta se imprime la contraseña del usuario plano y el hash que lanzo


def Comparador_Hash(Usuario_Hash_Comparar):
    if Usuario_Hash_Comparar in Diccionario_Craker:
        print(f"La comparacion del hash |{Usuario_Hash_Comparar}|")
        print(f"Fue encontrado siendo la contraseña |{Diccionario_Craker[Usuario_Hash_Comparar]}|")
        print("----------------------------------------------------------------------------------")
    else:
        print(f"El Hash a comparar siendo el |{Usuario_Hash_Comparar}| no se encontro en la lista.")
        print("----------------------------------------------------------------------------------")


def main_Comparador_Contraseña():
    print("Iniciando Compararcion... \n" \
            "El proceso puede tardar unos minutos debido a la RAM \n" \
            "-------------------------------------------------------")
    Hash_Usuario, Usuario = cu.Contraseña_Usuario()
    contraseñas = wl.Craker()
    print(contraseñas)
    
    Comparador_Contraseña(Hash_Usuario, Usuario)


def main_Comparador_Hash():
    print("Iniciando Compararcion...\n" 
            "El proceso puede tardar unos minutos debido a la RAM \n" 
            "-------------------------------------------------------")
    Usuario_Hash_Comparar = cu.Hash_Usuario()
    #contraseñas = wl.Craker()

    Comparador_Hash(Usuario_Hash_Comparar)


if __name__ == "__main__":
    #main_Comparador_Hash()
    main_Comparador_Contraseña()

