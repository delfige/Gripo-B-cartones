import random
import math
import csv

#cada carton es de 3x9
def nueveXtres(mi_carton):
    if len(mi_carton) != 3:
        return False
        for fila in mi_carton:
            if len(fila) != 9:
                return False
    return True

#rango 1 a 90
def uno_noventa(mi_carton):
    for fila in mi_carton:
        for celda in fila:
            if not(celda >= 0 and celda <= 90):
                return False
    return True

#no hay numeros repetidos
def sin_repetir(mi_carton):
    aux = mi_carton[0] + mi_carton[1] + mi_carton[2]

    if len(set(aux)) != 16:
        return False

    return True

#cuenta celdas en un carton
def contar_celdas_ocupadas(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                contador = contador + 1

    return contador

#cuenta celdas en una fila del carton
def contar_celdas_ocupadas_en_fila(mi_fila):
    contador = 0
    for celda in mi_fila:
        if celda > 0:
            contador += 1
    return contador

#se fija que no haya columnas vacias
def columnas_no_vacias(mi_carton):
    for columna in range(9):
        if not(mi_carton[0][columna] or mi_carton[1][columna] or mi_carton[2][columna]):
            return False
    return True

#se fija que no haya filas vacias
def filas_no_vacias(mi_carton):
    for fila in mi_carton:
        sum = 0
        for celda in fila:
            sum += celda
        if sum == 0:
            return False
    return True

# Se fija que vayan aumentando los numeros de izquierda a derecha
def filas_aumentan(mi_carton):
    x = 0
    y = 9
    for columna in range(9):
        for fila in range(3):
            if mi_carton[fila][columna] != 0:
                if not(x <= mi_carton[fila][columna] <= y):
                    return False
        x += 10
        y += 10
        if y == 89:
            y = 90
    return True

#van bajando el valor por columna
def columnas_bajan(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] != 0:
            if mi_carton[1][columna] != 0:
                if mi_carton[0][columna] > mi_carton[1][columna]:
                    return False
            if mi_carton[2][columna] != 0:
                if mi_carton[0][columna] > mi_carton[2][columna]:
                    return False

        if mi_carton[1][columna] != 0:
            if mi_carton[2][columna] != 0:
                if mi_carton[1][columna] > mi_carton[2][columna]:
                    return False
    return True

#no puede haber una columna con sus tres casillas ocupadas
def sin_colums_llenas(mi_carton):
    for columna in range(9):
        if mi_carton[0][columna] and mi_carton[1][columna] and mi_carton[2][columna]:
            return False
    return True

#No puede haber 3 celdas ocupadas consecutivas
def celdas_ocupadas_consecutivas(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda == 0:
                contador = 0
            else:
                contador += 1
            if contador == 3:
                return False
    return True

#No puede haber 3 celdas vacias consecutivas
def celdas_vacias_consecutivas(mi_carton):
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            if celda != 0:
                contador = 0
            else:
                contador += 1
            if contador == 3:
                return False
    return True


def intento_carton():
    contador = 0

    carton = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
        contador += 1
        if contador == 50 :
            return intento_carton()
        numero = random.randint(1, 90)

        columna = int(math.floor(numero / 10))
        if columna == 9:
            columna = 8
        huecos = 0
        for i in range(3):
            if carton[i][columna] == 0:
                huecos += 1
            if carton[i][columna] == numero:
                huecos = 0
                break
        if(huecos < 2):
            continue

        fila = 0
        for j in range(3):
            huecos = 0
            for i in range(9):
                if carton[fila][i] == 0:
                    huecos += 1
            if huecos < 5 or carton[fila][columna] != 0:
                fila += 1
            else:
                break
        if fila == 3:
            continue

        carton[fila][columna] = numero
        numerosCarton += 1
        contador = 0

    for x in range(9):
        huecos = 0
        for y in range(3):
            if carton[y][x] == 0:
                huecos += 1
        if huecos == 3:
            return intento_carton()

    return carton

def generar_carton():
    while True:
        carton = intento_carton()
        if(nueveXtres(carton)
        and uno_noventa(carton)
        and sin_repetir(carton)
        and contar_celdas_ocupadas(carton) == 15
        and contar_celdas_ocupadas_en_fila(carton[0]) == 5
        and contar_celdas_ocupadas_en_fila(carton[1]) == 5
        and contar_celdas_ocupadas_en_fila(carton[2]) == 5
        and columnas_no_vacias(carton)
        and filas_no_vacias(carton)
        and filas_aumentan(carton)
        and columnas_bajan(carton)
        and sin_colums_llenas(carton)
        and celdas_ocupadas_consecutivas(carton)
        and celdas_vacias_consecutivas(carton)):
            break
    return carton

carton = generar_carton()


def generar_cartones_sin_repetir(n):
    cartones = []
    while len(cartones) < n:
        carton = generar_carton()
        if carton not in cartones:
            cartones.append(carton)
    return cartones

def guardar_cartones_en_csv(cartones, cantidad_cartones, nombre_archivo):
    with open(nombre_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['ID', 'Cartones'])
        for i in range(cantidad_cartones):
            carton = cartones[i]
            carton_id = i+1
            carton_l = []
            for fila in carton:
                for numero in fila:
                    carton_l.append(str(numero))
            escritor_csv.writerow([carton_id, ' '.join(carton_l)])
    print(f"Se han guardado {cantidad_cartones} cartones en el archivo {nombre_archivo}.")


cantidad_cartones = int(input("Ingrese la cantidad de cartones a generar: "))
cartones_sin_repetir = generar_cartones_sin_repetir(cantidad_cartones)
nombre_archivo = 'cartones_bingo.csv'
guardar_cartones_en_csv(cartones_sin_repetir, cantidad_cartones, nombre_archivo)

def cargar_cartones(nombre_archivo):
    ''' Devuelve una lista de diccionarios con la información del datos del archivo especificado '''
    import csv
    
    datos_dict = []
    try:
        f = open(nombre_archivo, 'rt', encoding='utf8')
        filas = csv.reader(f)
        cabecera = next(filas)
        for fila in filas:
            item =  dict(zip(cabecera,fila))
            datos_dict.append(item)
        f.close()
    except Exception as e:
        datos_dict.append(f'A sucedido un Error {e}')
    finally:
        return datos_dict