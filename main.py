import Diseños as ds
import Comparador_General as cg


ds.Inicio()
ds.Menu()


while True:
    Seleccion_Usuario = int(input("Ingresa un numero: "))
    if Seleccion_Usuario == 1:
        cg.main_Comparador_Contraseña()
    elif Seleccion_Usuario == 2:
        cg.main_Comparador_Hash()
    elif Seleccion_Usuario == 3: 
        pass #aqui va funcionamiento por division de archivo y multiproceso para la comparacion


    elif Seleccion_Usuario == 4:
        print("Saliendo del Programa...")
        break
    else:
        print("Numero Invalido Selecciona otro")
        



