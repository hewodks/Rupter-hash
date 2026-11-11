from charset_normalizer import from_bytes

hex_Prueba_utf_8 = "d181d0bbd0bed0b6d0bdd18bd0b9d0bfd0b0d180d0bed0bbd18c" #
hex_Prueba2_cp1252 = "636f6e7472617365f161313233"
hex_Prueba3_cp1251 = "eceef7e0ebeae8ede0313937350d" #
hex_Prueba4_cp1250 = "6d616c6f706f6c736b61e2"
hex_Prueba5_utf_16_le = "700061007300730077006f0072006400310032003300" #

def lol():
    

    resultados = []

    resultados.append(hex_Prueba_utf_8)
    resultados.append(hex_Prueba2_cp1252)
    resultados.append(hex_Prueba3_cp1251)
    resultados.append(hex_Prueba4_cp1250)
    resultados.append(hex_Prueba5_utf_16_le)

    return resultados



#los_bytes = bytes.fromhex(hex_Prueba4_cp1250)

#final2 = los_bytes.decode("cp1250")

#print(final2)

def Decodificadors(bytes_crudos):
    Decodificadores_5 = ["utf-8", "cp1252", "cp1251", "cp1250", "utf-16-le"]
    Bytes_Puros = bytes.fromhex(bytes_crudos)
    for enc in Decodificadores_5:  
        try:
            no_valido = False
            Decodificado_valido = True
            Decodificado = Bytes_Puros.decode(enc)            
        
            if Decodificado_valido:
                for letra in Decodificado:
                    Rango = ord(letra)
                    
                    if Rango < 32 and letra != "\r" and letra != "\n" and letra != "\t":
                        no_valido = True
                        break
                
                    if enc in "cp1251" and not (1024 <= Rango <= 1279 or 32 <= Rango <= 127 or letra in ["\r", "\n", "\t"]) :
                        no_valido = True
                        break

                    if enc in ["cp1252", "cp1250"] and Rango > 127:
                        if not letra.isalnum():
                            no_valido = True
                            break
                

            if no_valido:
                #print("esta mal el codificado")
                correcto = Decodificado
                continue#return correcto
            
            if no_valido == False:
                print("esta bien el codificado siendo.")
                return Decodificado

        except:
            continue

#lol = Decodificadors(hex_Prueba_utf_8)
#print(lol)
#for hex in lol():
 #   lol = bytes.fromhex(hex)
  #  pop = Decodificadors(lol)
   # print(pop)


#from charset_normalizer import from_bytes

# Los bytes del texto en cirílico/ruso

#mis_bytes = bytes.fromhex("eceef7e0ebeae8ede0313937350d")

# Le pedimos que analice los bytes
#resultado = from_bytes(mis_bytes).best()

#print(resultado.encoding)   # Resultado: 'cp1251'
#print(resultado.coherence)  # Qué tanta coherencia lingüística encontró (ej: 0.98)

# Puedes obtener el texto traducido directamente desde el resultado
#print(resultado.output())   # Resultado: мочалкина1975 