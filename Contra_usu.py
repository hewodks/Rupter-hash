"""This part the usuario introduce a password that convert to hash and will compare"""
import hashlib

def Contraseña_Usuario():
    print("Introduce la contraseña |Texto Plano| para convertir en Hash y comparar")
    
    Usuario = input(": ")
    print("------------------------------------------------")
    print()
    print(f"Contraseña Introducida {Usuario}")

    hash_usuario = hashlib.sha256(Usuario.encode("utf-8")).hexdigest()

    print(f"Hash |{hash_usuario}| Generado")
    print("---------------------------------------------------------------------")
    print()

    return hash_usuario, Usuario

def Hash_Usuario():
    print("Introduce el Hash para comparar")

    Usuario_Hash_Comparar = input(": ")
    print("---------------------------------------------------------------------")
    print()
    print(f"Hash Introducido |{Usuario_Hash_Comparar}|")
    print("---------------------------------------------------------------------")
    print()

    return Usuario_Hash_Comparar


#Debugger

if __name__ == "__main__":
    Hash_Usuario()