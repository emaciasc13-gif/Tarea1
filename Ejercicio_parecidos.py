# EJERCICIO 1 — CONTROL DE EDADES
# Crear una clase ControlEdades que permita validar si una edad está entre 0 y 120,
# cargar varias edades usando *args y guardar únicamente las edades válidas.
# Además, debe tener un método que calcule el promedio de las edades almacenadas.

class ControlEdades:
    def __init__(self):
        self.edades = []

    def validar_edad(self, edad):
        if edad >= 0 and edad <= 120:
            return True
        else:
            return False

    def cargar_variasedades(self, *args):
        for edad in args:
            if self.validar_edad(edad) == True:
                self.edades.append(edad)

        return self.edades

    def calcular_promedio(self):
        suma_edades = 0
        promedio_edades = 0

        for edad in self.edades:
            suma_edades = suma_edades + edad

        promedio_edades = suma_edades / len(self.edades)

        return promedio_edades


# EJERCICIO 2 — GESTOR DE COLORES
# Crear una clase GestorColores que guarde colores en una lista y también en un conjunto.
# Debe permitir agregar un color, contar cuántos colores únicos existen y agregar varios
# colores usando *args.

class GestorColores:
    def __init__(self):
        self.lista_colores = []
        self.conjunto_colores = set()

    def agregar_color(self, color):
        self.lista_colores.append(color)
        self.conjunto_colores.add(color)

    def colores_unicos(self):
        return len(self.conjunto_colores)

    def agregar_varios(self, *args):
        for color in args:
            self.agregar_color(color)


# EJERCICIO 3 — TIENDA DE PRODUCTOS
# Crear una clase Tienda que guarde productos y precios en un diccionario.
# Debe permitir agregar productos, calcular la suma total de todos los precios y
# devolver una lista con los productos cuyo precio sea menor o igual a un valor indicado.

class tienda:
    def __init__(self):
        self.productos = {}

    def agregar_productos(self, producto, precio):
        self.productos[producto] = precio

    def suma_precios(self):
        suma_precios = 0

        for producto, precio in self.productos.items():
            suma_precios = suma_precios + precio

        return suma_precios

    def total_precios(self, valor):
        productos_encontrados = []

        for producto, precio in self.productos.items():
            if precio <= valor:
                productos_encontrados.append(producto)

        return productos_encontrados


# EJERCICIO 4 — ROTADOR DE LISTAS
# Crear una clase RotadorLista que reciba una lista y mueva su primer elemento al final.
# También debe poder recibir varias listas mediante *args, rotarlas reutilizando
# el primer método y guardar los resultados en un diccionario.

class RotadorLista:
    def __init__(self):
        self.listas_rotadas = {}

    def mover_alfinal(self, lista):
        lista_rotada = []

        posicion = 1

        while posicion < len(lista):
            lista_rotada.append(lista[posicion])
            posicion = posicion + 1

        lista_rotada.append(lista[0])

        return lista_rotada

    def varias_lista(self, *args):
        for lista in args:
            self.listas_rotadas[tuple(lista)] = self.mover_alfinal(lista)

        return self.listas_rotadas


# EJERCICIO 5 — CLASIFICADOR DE NÚMEROS
# Crear una clase ClasificadorNumeros que determine si un número es positivo,
# negativo o cero. Debe recibir varios números usando *args,
# separarlos en un diccionario con tres listas y devolver también una tupla
# con la cantidad de positivos, negativos y ceros.

class clasificadornumeros:
    def __init__(self):
        self.numeros_clasificados = {
            "positivos": [],
            "negativos": [],
            "ceros": []
        }

    def clasificador(self, numero):
        if numero > 0:
            return "positivo"
        elif numero < 0:
            return "negativo"
        else:
            return "cero"

    def varios_numeros(self, *args):
        for numero in args:
            if self.clasificador(numero) == "positivo":
                self.numeros_clasificados["positivos"].append(numero)

            elif self.clasificador(numero) == "negativo":
                self.numeros_clasificados["negativos"].append(numero)

            else:
                self.numeros_clasificados["ceros"].append(numero)

        return self.numeros_clasificados

    def cantidad(self):
        cantidad_positivos = len(self.numeros_clasificados["positivos"])
        cantidad_negativos = len(self.numeros_clasificados["negativos"])
        cantidad_ceros = len(self.numeros_clasificados["ceros"])

        return (cantidad_positivos, cantidad_negativos, cantidad_ceros)


# EJERCICIO 6 — REGISTRO DE LLUVIAS
# Crear una clase RegistroLluvias que permita registrar cantidades de lluvia en una lista.
# Debe calcular el valor mínimo, máximo y promedio.
# También debe permitir registrar varias cantidades utilizando *args.

class registrolluvias:
    def __init__(self):
        self.lluvias = []

    def registrar_lluvia(self, cantidad):
        self.lluvias.append(cantidad)

    def calcular(self):
        lluvia_maxima = max(self.lluvias)
        lluvia_minima = min(self.lluvias)
        promedio_lluvia = sum(self.lluvias) / len(self.lluvias)

        return lluvia_maxima, lluvia_minima, promedio_lluvia

    def varias(self, *args):
        for cantidad in args:
            self.registrar_lluvia(cantidad)

        return self.lluvias


# EJERCICIO 7 — AGENDA DE CONTACTOS
# Crear una clase AgendaContactos que guarde nombres y números de teléfono en un diccionario.
# Debe permitir agregar contactos, buscar el teléfono de una persona por su nombre
# y devolver una lista con los nombres que comiencen con una letra determinada.

class agendacontactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, numero):
        self.contactos[nombre] = numero

    def buscar_numero(self, nombre):
        for nombre_contacto, numero in self.contactos.items():
            if nombre_contacto == nombre:
                return numero

    def buscar_nombre(self, letra):
        nombres_encontrados = []

        for nombre in self.contactos.keys():
            if nombre[0].lower() == letra.lower():
                nombres_encontrados.append(nombre)

        return nombres_encontrados


# EJERCICIO 8 — CURSOS Y ESTUDIANTES
# Crear una clase Cursos que permita crear cursos dentro de un diccionario,
# donde cada curso tenga una lista de estudiantes.
# Debe permitir agregar estudiantes y encontrar el curso que tenga
# la menor cantidad de integrantes.

class cursos:
    def __init__(self):
        self.cursos_registrados = {}

    def crear_curso(self, curso):
        self.cursos_registrados[curso] = []

    def agregar_estudiante(self, curso, nombre):
        if curso not in self.cursos_registrados:
            self.crear_curso(curso)

        self.cursos_registrados[curso].append(nombre)

    def menor_integrantes(self):
        curso_menor = ""
        cantidad_menor = None

        for curso, estudiantes in self.cursos_registrados.items():
            if cantidad_menor == None or len(estudiantes) < cantidad_menor:
                curso_menor = curso
                cantidad_menor = len(estudiantes)

        return curso_menor


# EJERCICIO 9 — ANALIZADOR DE CARACTERES
# Crear una clase AnalizadorCaracteres que tenga un método para comprobar
# si una letra es mayúscula.
# Debe analizar un texto y devolver un diccionario con la cantidad
# de letras mayúsculas, minúsculas y dígitos.
# También debe guardar el último texto analizado.

class analizador_caracteres:
    def __init__(self):
        self.ultimo_texto = ""

    def comprobar(self, caracter):
        if caracter != caracter.lower():
            return True
        else:
            return False

    def analizar_texto(self, texto):
        conteo_caracteres = {
            "mayusculas": 0,
            "minusculas": 0,
            "digitos": 0
        }

        self.ultimo_texto = texto

        for caracter in texto:
            if self.comprobar(caracter):
                conteo_caracteres["mayusculas"] += 1

            else:
                if caracter.isalpha():
                    conteo_caracteres["minusculas"] += 1

                elif caracter.isdigit():
                    conteo_caracteres["digitos"] += 1

        return conteo_caracteres


# EJERCICIO 10 — RECORDATORIOS
# Crear una clase Recordatorios que guarde cada recordatorio como una tupla
# formada por el texto y su estado.
# Debe permitir agregar recordatorios, devolver una lista con los que tengan
# estado "pendiente" y eliminar un recordatorio mediante su texto.

class recordatorios:
    def __init__(self):
        self.recordatorios = []

    def agregar_recordatorio(self, texto, estado):
        self.recordatorios.append((texto, estado))

    def estado_pendiente(self):
        recordatorios_pendientes = []

        for recordatorio in self.recordatorios:
            if recordatorio[1] == "pendiente":
                recordatorios_pendientes.append(recordatorio[0])

        return recordatorios_pendientes

    def eliminar_recordatorio(self, texto):
        posicion = 0

        for recordatorio in self.recordatorios:
            if recordatorio[0] == texto:
                del(self.recordatorios[posicion])
                return True

            posicion += 1

        return False


# EJERCICIO 11 — CONTADOR DE VISITAS
# Crear una clase ContadorVisitas que registre cuántas veces se visita cada página
# utilizando un diccionario.
# Debe permitir registrar visitas, obtener la página más visitada
# y consultar cuántas visitas tiene una página determinada.

class contadorvisitas:
    def __init__(self):
        self.visitas_paginas = {}

    def registro(self, pagina):
        if pagina not in self.visitas_paginas:
            self.visitas_paginas[pagina] = 1

        else:
            self.visitas_paginas[pagina] += 1

    def pagina_visitada(self):
        pagina_mas_visitada = ""
        cantidad_mayor_visitas = None

        for pagina, cantidad_visitas in self.visitas_paginas.items():
            if cantidad_mayor_visitas == None or cantidad_mayor_visitas < cantidad_visitas:
                pagina_mas_visitada = pagina
                cantidad_mayor_visitas = cantidad_visitas

        return pagina_mas_visitada

    def consultar_visitas(self, pagina):
        cantidad_visitas = self.visitas_paginas[pagina]

        return cantidad_visitas


# EJERCICIO 12 — RANGOS PARES
# Crear una clase RangosPares que reciba un inicio y un fin
# y devuelva una tupla con los números pares de ese rango.
# También debe recibir varios rangos mediante *args, combinarlos
# y devolver una lista sin números repetidos utilizando un conjunto.

class rangopares:
    def __init__(self):
        self.numeros_pares = set()

    def pares(self, inicio, fin):
        pares_encontrados = []

        for numero in range(inicio, fin + 1):
            if numero % 2 == 0:
                pares_encontrados.append(numero)

        return tuple(pares_encontrados)

    def varios(self, *args):
        self.numeros_pares = set()

        for rango in args:
            pares_del_rango = self.pares(rango[0], rango[1])

            for numero in pares_del_rango:
                self.numeros_pares.add(numero)

        return list(self.numeros_pares)


# EJERCICIO 13 — UNIÓN DE LISTAS
# Crear una clase UnionListas que una dos listas sin repetir elementos.
# También debe tener un método que permita recibir varias listas mediante *args
# y unirlas reutilizando el método anterior.

class unionlistas:

    def unir(self, lista1, lista2):
        elementos_unicos = set()

        for elemento in lista1:
            elementos_unicos.add(elemento)

        for elemento in lista2:
            elementos_unicos.add(elemento)

        return list(elementos_unicos)

    def varias(self, *args):
        if len(args) == 0:
            return []

        lista_unida = args[0]

        for lista in args[1:]:
            lista_unida = self.unir(lista_unida, lista)

        return lista_unida


# EJERCICIO 14 — REGISTRO DE PUNTAJES
# Crear una clase RegistroPuntajes que guarde jugadores y puntajes en un diccionario.
# Debe devolver una lista con los jugadores que tengan un puntaje mayor
# o igual a un mínimo indicado y devolver una tupla con el jugador
# que tenga el menor puntaje y su puntuación.

class registropuntajes:
    def __init__(self):
        self.puntajes_jugadores = {}

    def registro(self, jugador, puntaje):
        if jugador not in self.puntajes_jugadores:
            self.puntajes_jugadores[jugador] = puntaje

    def mayor_igual(self, minimo):
        jugadores_encontrados = []

        for jugador, puntaje in self.puntajes_jugadores.items():
            if puntaje >= minimo:
                jugadores_encontrados.append(jugador)

        return jugadores_encontrados

    def menor_puntuacion(self):
        puntaje_menor = None
        jugador_menor = ""
        puntuacion_menor = 0

        for jugador, puntaje in self.puntajes_jugadores.items():
            if puntaje_menor == None or puntaje < puntaje_menor:
                jugador_menor = jugador
                puntuacion_menor = puntaje
                puntaje_menor = puntaje

        return (jugador_menor, puntuacion_menor)


# EJERCICIO 15 — BUSCADOR DE MÚLTIPLOS
# Crear una clase MultiploFinder que encuentre todos los múltiplos de un número
# hasta un límite y los devuelva como una tupla.
# Debe tener un método que determine si un valor es múltiplo de otro número
# y otro método que procese varios números usando *args.

class MultiploFinder:
    def __init__(self):
        self.multiplos_por_numero = {}

    def encontrar_multiplos(self, numero, limite):
        multiplos_encontrados = []

        for valor in range(numero, limite + 1):
            if valor % numero == 0:
                multiplos_encontrados.append(valor)

        return tuple(multiplos_encontrados)

    def es_multiplo(self, numero, valor):
        if valor % numero == 0:
            return True
        else:
            return False

    def varios(self, limite, *args):
        for numero in args:
            self.multiplos_por_numero[numero] = self.encontrar_multiplos(numero, limite)

        return self.multiplos_por_numero


# EJERCICIO 16 — REEMPLAZADOR DE VOCALES
# Crear una clase ReemplazadorVocales que tenga un método para reemplazar
# una vocal por el símbolo "*".
# Debe tener otro método que recorra una palabra completa reutilizando
# el método anterior y guardar en un diccionario la palabra original
# junto con su resultado.

class ReemplazadorVocales:
    def __init__(self):
        self.palabras_reemplazadas = {}

    def reemplazar_vocal(self, letra):
        if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u":
            return "*"
        else:
            return letra

    def reemplazar_palabra(self, palabra):
        palabra_resultado = ""

        for letra in palabra:
            palabra_resultado = palabra_resultado + self.reemplazar_vocal(letra)

        self.palabras_reemplazadas[palabra] = palabra_resultado

        return palabra_resultado


# EJERCICIO 17 — CLASIFICADOR DE ALTURAS
# Crear una clase ClasificadorAlturas que clasifique una altura
# como "baja", "media" o "alta".
# Debe recibir varias alturas usando *args, agruparlas en un diccionario
# según su categoría y calcular el promedio de las alturas
# pertenecientes a una categoría indicada.

class ClasificadorAlturas:
    def __init__(self):
        self.alturas_clasificadas = {
            "baja": [],
            "media": [],
            "alta": []
        }

    def clasificar(self, altura):
        if altura < 150:
            return "baja"

        elif altura < 180:
            return "media"

        else:
            return "alta"

    def varias_alturas(self, *args):
        for altura in args:
            categoria_altura = self.clasificar(altura)
            self.alturas_clasificadas[categoria_altura].append(altura)

        return self.alturas_clasificadas

    def promedio_categoria(self, categoria):
        suma_alturas = 0

        for altura in self.alturas_clasificadas[categoria]:
            suma_alturas = suma_alturas + altura

        promedio_alturas = suma_alturas / len(self.alturas_clasificadas[categoria])

        return promedio_alturas


# EJERCICIO 18 — CALCULADOR DE PERÍMETROS
# Crear una clase CalculadorPerimetro que reciba un rectángulo representado
# mediante una tupla (base, altura) y calcule su perímetro.
# Debe guardar todos los perímetros calculados y tener un método
# que reciba varios rectángulos mediante *args y devuelva
# el rectángulo con el menor perímetro.

class CalculadorPerimetro:
    def __init__(self):
        self.perimetros_calculados = []

    def calcular(self, rectangulo):
        base = rectangulo[0]
        altura = rectangulo[1]

        perimetro_rectangulo = 2 * (base + altura)

        self.perimetros_calculados.append(perimetro_rectangulo)

        return perimetro_rectangulo

    def menor_perimetro(self, *args):
        rectangulo_menor = ()
        perimetro_menor = None

        for rectangulo in args:
            perimetro_rectangulo = self.calcular(rectangulo)

            if perimetro_menor == None or perimetro_rectangulo < perimetro_menor:
                rectangulo_menor = rectangulo
                perimetro_menor = perimetro_rectangulo

        return rectangulo_menor


# EJERCICIO 19 — BIBLIOTECA
# Crear una clase Biblioteca que guarde libros y cantidad de copias en un diccionario.
# Debe permitir agregar copias, prestar un libro solamente si existe
# al menos una copia disponible y devolver una lista con los libros
# cuya cantidad sea menor que un mínimo indicado.

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def agregar_copias(self, libro, cantidad):
        if libro in self.libros:
            self.libros[libro] = self.libros[libro] + cantidad

        else:
            self.libros[libro] = cantidad

    def prestar_libro(self, libro):
        if libro in self.libros and self.libros[libro] > 0:
            self.libros[libro] = self.libros[libro] - 1
            return True

        else:
            return False

    def pocas_copias(self, minimo):
        libros_con_pocas_copias = []

        for libro, cantidad in self.libros.items():
            if cantidad < minimo:
                libros_con_pocas_copias.append(libro)

        return libros_con_pocas_copias


# EJERCICIO 20 — BUSCADOR DE PALABRAS
# Crear una clase BuscadorPalabras que encuentre las palabras de un texto
# que terminen con un patrón determinado.
# También debe agrupar las palabras según su primera letra utilizando
# un diccionario y tener un método que devuelva un conjunto
# con las palabras únicas analizadas.

class BuscadorPalabras:
    def __init__(self):
        self.palabras_analizadas = []

    def buscar_patron(self, texto, patron):
        palabras_encontradas = []
        palabras_texto = texto.split()

        for palabra in palabras_texto:
            self.palabras_analizadas.append(palabra)

            if palabra.endswith(patron):
                palabras_encontradas.append(palabra)

        return palabras_encontradas

    def agrupar_inicial(self, texto):
        palabras_por_inicial = {}
        palabras_texto = texto.split()

        for palabra in palabras_texto:
            self.palabras_analizadas.append(palabra)

            inicial = palabra[0]

            if inicial in palabras_por_inicial:
                palabras_por_inicial[inicial].append(palabra)

            else:
                palabras_por_inicial[inicial] = [palabra]

        return palabras_por_inicial

    def palabras_unicas(self):
        return set(self.palabras_analizadas)
