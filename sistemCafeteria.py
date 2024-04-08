# Jacqueline Villa Asencio | A01736339

def convertir_y_validar_tamanos(tamanos):
    tamanos_int = []
    tamanos_set = set()  # Para verificar duplicados

    for tamano in tamanos:
        tamano = tamano.strip()

        # Se verifica si los valores son números enteros
        if not tamano.lstrip("-").isdigit():
            return False, "Los tamaños deben ser valores enteros."
        valor = int(tamano)

        # Se verifica que los tamaños se encuentren en el rango de 1 a 48
        if not 1 <= valor <= 48:
            return False, "Los tamaños deben estar en el rango de 1 a 48."

        # Se verifica que no se repitan valores
        if valor in tamanos_set:
            return False, "Los tamaños no pueden repetirse valores."
        tamanos_int.append(valor)
        tamanos_set.add(valor)

    # Se verifica que los valores esten de forma ascendente
    if tamanos_int != sorted(tamanos_int):
        return False, "Los tamaños no están en orden ascendente."

    return True, tamanos_int


def validar_bebida(registro):
   # Se eliminan los espacios en blanco
   registro = registro.replace(" ", "")
   registro_separado = registro.split(",")
   # Obtiene el primer valor que es el nombre de la bebida
   bebida = registro_separado[0]
   # Obtiene los siguientes valores que son los tamañis
   tamanos = registro_separado[1:]

   # Valida que el nombre del artículo es alfabético
   if not bebida.isalpha():
      return False

   # Valida que el nombre del artículo tiene de 2 a 15 caracteres de longitud
   if len(bebida) < 2 or len(bebida) > 15:
      return False

   # Valida que la cantidad de tamaños sea de 1 a 5
   if len(tamanos) < 1 or len(tamanos) > 5:
      return False

   # Se utiliza la función auxiliar para convertir y validar tamaños
   valido, resultado = convertir_y_validar_tamanos(tamanos)
   if not valido:
      return False, resultado

   return True


# ******* DEFINICIÓN DE PRUEBAS ********
#                 pytest
def test_bebida():
# El nombre del artículo es alfabético
    # Nombre alfabético (válido)
    assert validar_bebida("Chocolate,2,3,14,20") == True
    # Nombre con números y letras
    assert validar_bebida("C4f3,2,3,14,20") == False
    # Nombre con números
    assert validar_bebida("123456,1,2,3,4") == False

# El nombre del artículo tiene de 2 a 15 caracteres de longitud
    # Nombre con 15 caracteres (válido)
    assert validar_bebida("Refresco cola,1,2,3,4") == True
    # Nombre con 2 caracteres (válido)
    assert validar_bebida("ab,1,2,3,4") == True
    # Nombre con un caracter
    assert validar_bebida("a,1,2,3,4") == False
    # Nombre con más de 15 caracteres
    assert validar_bebida("Refresco7up7up7up,1,2,3,4") == False
    # No se coloca un nombre
    assert validar_bebida(",1,2,3,4") == False

# El valor del tamaño está en el rango de 1 a 48
    #  Se coloca el límite inferior (válido)
    assert validar_bebida("Capuccino,1,2,3,4") == True
    # Se coloca el límite superior (válido)
    assert validar_bebida("Espresso,41,48") == True
    # Se colocan valores menores que el rango (0)
    assert validar_bebida("Espresso,0,2,3,4") == (False, "Los tamaños deben estar en el rango de 1 a 48.")
    # Se colocan tamaños mas grandes que el rango
    assert validar_bebida("Chocolate,50,49") == (False, 'Los tamaños deben estar en el rango de 1 a 48.')
    # Se colocan tamaños con numeros negativos
    assert validar_bebida("Machiato,-3,-5") == (False, 'Los tamaños deben estar en el rango de 1 a 48.')

# El valor del tamaño es un número entero
    # El tamaño es un valor entero (válido)
    assert validar_bebida("Machiato,10") == True
    # Un tamaño es un número decimal
    assert validar_bebida("Mocha,1.5,2,3,4") == (False, 'Los tamaños deben ser valores enteros.')
    # Un tamaño es un string
    assert validar_bebida("Latte,abc,2,3,4") == (False, 'Los tamaños deben ser valores enteros.')

# Los valores del tamaño se ingresan en orden ascendente
    # Los valores están de forma ascendente (válido)
    assert validar_bebida("Gaseosa,10,11,12,13") == True
    # Los valores están de forma descendentes
    assert validar_bebida("jugo,13,12,11,10") == (False, 'Los tamaños no están en orden ascendente.')
    # Los valores estan desordenados
    assert validar_bebida("Cafe,4,3,5,1") == (False, 'Los tamaños no están en orden ascendente.')

# Se ingresan de uno a cinco valores de tamaño
    # Solamente se coloca un tamaño (válido)
    assert validar_bebida("Agua limon,1") == True
    # Se colocan los 5 ramaños (válido)
    assert validar_bebida("Agua,10,11,12,13,23") == True
    # No se agrega ningún tamaño
    assert validar_bebida("Frapuccino") == False
    # Se colocan mas de 5 tamaños
    assert validar_bebida("Te,10,11,12,13,14,20") == False

# El nombre del artículo es el primero en la entrada
    # Colocar el orden correcto (válido)
    assert validar_bebida("Jugo,1,2,3,4") == True
    # Agregar el nombre en el segundo puesto
    assert validar_bebida("1,Cafe,2,3,4") == False

# Una sola coma separa cada entrada en la lista
    # Usar una sola coma (válido)
    assert validar_bebida("Malteada,31,32,33,34") == True
    # Agregar dos comas en un elemento
    assert validar_bebida("Cafe,1,,2,3,4") == (False, 'Los tamaños deben ser valores enteros.')
    # Usar otro caracter para separar que no sea una coma(-)
    assert validar_bebida("Agua-10-11-12-13") == False

# La entrada contiene o no espacios en blanco
    # Usar espacios en el nombre (válido)
    assert validar_bebida("Agua Mineral,1,2,3,4") == True
    # Usar espacios en los tamaños (válido)
    assert validar_bebida("Jugo,1 0,11,12,1  3") == True
    # Se usan espacios pero los caracteres son mayores a 16
    assert validar_bebida("Caramen Frapuccino, 2, 4, 6") == False
    # Se usan espacios pero los tamaños superan el rango
    assert validar_bebida("Chocolate, 3, 8, 6  2") == (False, 'Los tamaños deben estar en el rango de 1 a 48.')