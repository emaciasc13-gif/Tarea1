# EJERCICIO 1 — Validador de notas con promedio

# PASO 1. ENTENDER (Entrada, Proceso y Salida)

# Entrada:
# Una o varias notas.

# Proceso:
# Validar que cada nota esté entre 0 y 100.
# Guardar solamente las notas válidas.
# Calcular el promedio de las notas guardadas.

# Salida:
# Lista de notas válidas y promedio.

# Ejemplo:
# 85, 92, 110, 78, -5, 88
# Válidas: [85, 92, 78, 88]
# Promedio: 85.75

# PASO 2. BOSQUEJO A MANO

# 85  -> válida
# 92  -> válida
# 110 -> inválida
# 78  -> válida
# -5  -> inválida
# 88  -> válida

# Suma = 85 + 92 + 78 + 88 = 343
# Cantidad = 4
# Promedio = 343 / 4 = 85.75

# PASO 3. PATRÓN

# validar_nota() revisa una nota.
# cargar_notas() reutiliza validar_nota() para varias notas.
# self.notas guarda las notas válidas.
# promedio() usa sum() y len().

# PASO 4. CÓDIGO

class Calificador:
    def __init__(self):
        self.notas=[]

    def validar_nota(self,nota):
        if nota >=0 and nota <=100:
            return True
        else:
            return False

    def cargar_notas(self,*args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        return sum(self.notas)/len(self.notas)


cal = Calificador()
print(cal.cargar_notas(85,92,110,78,-5,88))
print(cal.promedio())

# PASO 5. PRUEBA DE ESCRITORIO

# Acción                                  Lista                  Salida
# Calificador()                           []                     -
# cargar_notas(85,92,110,78,-5,88)       [85,92,78,88]          [85,92,78,88]
# promedio()                              [85,92,78,88]          85.75

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 2 — Contador de palabras únicas

# PASO 1. ENTENDER

# Entrada:
# Palabras individuales o varias palabras.

# Proceso:
# Guardar las palabras en una lista y también en un conjunto.
# El conjunto evita duplicados.

# Salida:
# Lista de palabras y cantidad de palabras únicas.

# PASO 2. BOSQUEJO

# "hola"  -> lista ["hola"]               conjunto {"hola"}
# "mundo" -> lista ["hola","mundo"]       conjunto {"hola","mundo"}
# "hola"  -> lista ["hola","mundo","hola"] conjunto {"hola","mundo"}
# Únicas = 2

# PASO 3. PATRÓN

# agregar_palabra() agrega en las dos colecciones.
# agregar_multiples() reutiliza agregar_palabra().
# contar_palabras() cuenta el conjunto.

# PASO 4. CÓDIGO

class AnalizadorTexto:
    def __init__(self):
        self.palabras=set()
        self.lista=[]

    def agregar_palabra(self,palabra):
        self.palabras.add(palabra)
        self.lista.append(palabra)

    def contar_palabras(self):
        return len(self.palabras)

    def agregar_multiples(self,*args):
        for palabra in args:
            self.agregar_palabra(palabra)
        return self.lista


at = AnalizadorTexto()
print(at.agregar_multiples("hola","mundo","hola"))
print(at.contar_palabras())

# PASO 5. PRUEBA DE ESCRITORIO

# Palabra   Lista                         Conjunto
# hola      ["hola"]                      {"hola"}
# mundo     ["hola","mundo"]              {"hola","mundo"}
# hola      ["hola","mundo","hola"]       {"hola","mundo"}
# contar_palabras() = 2

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 3 — Gestor de compras con totales

# PASO 1. ENTENDER

# Entrada:
# Nombre de artículo y precio.

# Proceso:
# Guardar nombre -> precio en un diccionario.
# Sumar precios y filtrar artículos por rango.

# Salida:
# Total y lista de artículos en un rango.

# PASO 2. BOSQUEJO

# pan = 2.50
# leche = 3.00
# Total = 5.50

# Rango 2.60 a 3.20:
# pan   -> no entra
# leche -> sí entra

# PASO 3. PATRÓN

# agregar_articulo() guarda una clave y un valor.
# total_carrito() recorre los valores.
# articulos_por_rango() recorre items().

# PASO 4. CÓDIGO

class CarroCompras:
    def __init__(self):
        self.articulos={}

    def agregar_articulo(self,nombre,precio):
        self.articulos[nombre]=precio

    def total_carrito(self):
        total=0
        for precio in self.articulos.values():
            total=total+precio
        return total

    def articulos_por_rango(self,precio_min,precio_max):
        articulos=[]
        for nombre,precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                articulos.append(nombre)
        return articulos


carro = CarroCompras()
carro.agregar_articulo("pan",2.50)
carro.agregar_articulo("leche",3.00)

print(carro.total_carrito())
print(carro.articulos_por_rango(2.60,3.20))

# PASO 5. PRUEBA DE ESCRITORIO

# Acción                  Diccionario                         Salida
# agregar pan             {"pan":2.50}                       -
# agregar leche           {"pan":2.50,"leche":3.00}          -
# total_carrito()         igual                              5.5
# rango(2.60,3.20)        igual                              ["leche"]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 4 — Inversor de secuencias

# PASO 1. ENTENDER

# Entrada:
# Una lista o varias listas.

# Proceso:
# Recorrer la lista desde la última posición hasta la primera.

# Salida:
# Lista invertida o diccionario con varias listas invertidas.

# PASO 2. BOSQUEJO

# Lista: [1,2,3]
# Índice 2 -> 3
# Índice 1 -> 2
# Índice 0 -> 1
# Resultado: [3,2,1]

# PASO 3. PATRÓN

# Se empieza en len(lista)-1.
# Se va restando 1 al índice.
# invertir_multiples() reutiliza invertir_lista().
# Se usa tuple(lista) como clave porque una lista no puede ser clave.

# PASO 4. CÓDIGO

class InversorSecuencia:
    def __init__(self):
        self.invertidas={}

    def invertir_lista(self,lista):
        invertida=[]
        i=len(lista)-1

        while i>=0:
            invertida.append(lista[i])
            i=i-1

        return invertida

    def invertir_multiples(self,*listas):
        self.invertidas={}

        for lista in listas:
            self.invertidas[tuple(lista)]=self.invertir_lista(lista)

        return self.invertidas


inversor = InversorSecuencia()

print(inversor.invertir_lista([1,2,3]))
print(inversor.invertir_multiples([1,2,3],[4,5,6]))

# PASO 5. PRUEBA DE ESCRITORIO

# i      Elemento       Resultado
# 2      3              [3]
# 1      2              [3,2]
# 0      1              [3,2,1]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 5 — Detector de números pares e impares

# PASO 1. ENTENDER

# Entrada:
# Varios números.

# Proceso:
# Comprobar si cada número es divisible para 2.

# Salida:
# Diccionario con pares e impares y una tupla con cantidades.

# PASO 2. BOSQUEJO

# 1 -> impar
# 2 -> par
# 3 -> impar
# 4 -> par
# 5 -> impar

# Pares: [2,4]
# Impares: [1,3,5]
# Cantidades: (2,3)

# PASO 3. PATRÓN

# es_par() usa numero % 2.
# separar() reutiliza es_par().
# cantidad_pares_impares() usa len().

# PASO 4. CÓDIGO

class AnalizadorNumeros:
    def __init__(self):
        self.resultado={"pares":[],"impares":[]}

    def es_par(self,numero):
        if numero % 2 == 0:
            return True
        else:
            return False

    def separar(self,*numeros):
        self.resultado={"pares":[],"impares":[]}

        for numero in numeros:
            if self.es_par(numero):
                self.resultado["pares"].append(numero)
            else:
                self.resultado["impares"].append(numero)

        return self.resultado

    def cantidad_pares_impares(self):
        cantidad_pares=len(self.resultado["pares"])
        cantidad_impares=len(self.resultado["impares"])
        return (cantidad_pares,cantidad_impares)


an = AnalizadorNumeros()

print(an.separar(1,2,3,4,5))
print(an.cantidad_pares_impares())

# PASO 5. PRUEBA DE ESCRITORIO

# Número      Tipo        Pares       Impares
# 1           impar       []          [1]
# 2           par         [2]         [1]
# 3           impar       [2]         [1,3]
# 4           par         [2,4]       [1,3]
# 5           impar       [2,4]       [1,3,5]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 6 — Estadísticas de temperatura

# PASO 1. ENTENDER

# Entrada:
# Temperaturas individuales o varias.

# Proceso:
# Guardar temperaturas y calcular mínima, máxima y promedio.

# Salida:
# Lista y estadísticas.

# PASO 2. BOSQUEJO

# [20,25,18,30]
# Mínima = 18
# Máxima = 30
# Suma = 93
# Promedio = 93 / 4 = 23.25

# PASO 3. PATRÓN

# registrar_temperatura() agrega un valor.
# registrar_multiples() reutiliza el método anterior.
# min(), max(), sum() y len() calculan las estadísticas.

# PASO 4. CÓDIGO

class GestorTemperatura:
    def __init__(self):
        self.temperaturas=[]

    def registrar_temperatura(self,temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas)/len(self.temperaturas)

    def registrar_multiples(self,*temps):
        for temp in temps:
            self.registrar_temperatura(temp)
        return self.temperaturas


gt = GestorTemperatura()

print(gt.registrar_multiples(20,25,18,30))
print(gt.minima())
print(gt.maxima())
print(gt.promedio())

# PASO 5. PRUEBA DE ESCRITORIO

# Temperaturas           Mínima       Máxima       Promedio
# [20,25,18,30]          18           30           23.25

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 7 — Mapeador de edades

# PASO 1. ENTENDER

# Entrada:
# Nombres y edades.

# Proceso:
# Guardar nombre -> edad.
# Filtrar por edad mínima.
# Calcular promedio de edades.

# Salida:
# Lista filtrada y promedio.

# PASO 2. BOSQUEJO

# Ana = 28
# Bob = 17

# Edad mínima = 18
# Ana entra.
# Bob no entra.
# Resultado: ["Ana"]

# Promedio = (28 + 17) / 2 = 22.5

# PASO 3. PATRÓN

# agregar_persona() guarda en diccionario.
# personas_mayores() usa items().
# edad_promedio() recorre values().

# PASO 4. CÓDIGO

class GestorPersonas:
    def __init__(self):
        self.personas={}

    def agregar_persona(self,nombre,edad):
        self.personas[nombre]=edad

    def personas_mayores(self,edad_minima):
        mayores=[]

        for nombre,edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)

        return mayores

    def edad_promedio(self):
        total=0

        for edad in self.personas.values():
            total=total+edad

        return total/len(self.personas)


gp = GestorPersonas()
gp.agregar_persona("Ana",28)
gp.agregar_persona("Bob",17)

print(gp.personas_mayores(18))
print(gp.edad_promedio())

# PASO 5. PRUEBA DE ESCRITORIO

# Persona      Edad      ¿>=18?
# Ana          28        Sí
# Bob          17        No
# Resultado: ["Ana"]
# Promedio: 22.5

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 8 — Asignador de equipos

# PASO 1. ENTENDER

# Entrada:
# Nombre del equipo y jugadores.

# Proceso:
# Crear equipos con listas vacías.
# Agregar jugadores.
# Comparar cuántos jugadores tiene cada equipo.

# Salida:
# Nombre del equipo con más integrantes.

# PASO 2. BOSQUEJO

# A = [Juan, Pedro]
# B = [Carlos]
# A tiene 2.
# B tiene 1.
# Mayor = A

# PASO 3. PATRÓN

# Cada equipo es una clave.
# Cada valor es una lista.
# len(jugadores) permite comparar cantidades.

# PASO 4. CÓDIGO

class Equipos:
    def __init__(self):
        self.equipos={}

    def crear_equipo(self,nombre_equipo):
        self.equipos[nombre_equipo]=[]

    def agregar_jugador(self,equipo,jugador):
        if equipo in self.equipos:
            self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor=""
        cantidad=-1

        for equipo,jugadores in self.equipos.items():
            if len(jugadores)>cantidad:
                cantidad=len(jugadores)
                mayor=equipo

        return mayor


eq = Equipos()
eq.crear_equipo("A")
eq.crear_equipo("B")
eq.agregar_jugador("A","Juan")
eq.agregar_jugador("A","Pedro")
eq.agregar_jugador("B","Carlos")

print(eq.equipos)
print(eq.equipo_mayor_integrantes())

# PASO 5. PRUEBA DE ESCRITORIO

# Equipo      Jugadores             Cantidad
# A           [Juan,Pedro]          2
# B           [Carlos]              1
# Mayor: A

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 9 — Validador de caracteres

# PASO 1. ENTENDER

# Entrada:
# Un texto.

# Proceso:
# Recorrer carácter por carácter.
# Contar vocales, consonantes y dígitos.
# Guardar el texto más largo analizado.

# Salida:
# Diccionario con cantidades.

# PASO 2. BOSQUEJO

# "Hola123"
# H -> consonante
# o -> vocal
# l -> consonante
# a -> vocal
# 1 -> dígito
# 2 -> dígito
# 3 -> dígito

# Resultado:
# vocales = 2
# consonantes = 2
# dígitos = 3

# PASO 3. PATRÓN

# solo_vocales() reconoce a,e,i,o,u.
# contar_por_tipo() recorre el texto.
# isdigit() identifica números.
# isalpha() identifica letras.

# PASO 4. CÓDIGO

class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo=""

    def solo_vocales(self,letra):
        letra=letra.lower()

        if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
            return True
        else:
            return False

    def contar_por_tipo(self,texto):
        resultado={"vocales":0,"consonantes":0,"digitos":0}

        if len(texto)>len(self.texto_mas_largo):
            self.texto_mas_largo=texto

        for letra in texto:
            if letra.isdigit():
                resultado["digitos"]=resultado["digitos"]+1

            elif letra.isalpha():
                if self.solo_vocales(letra):
                    resultado["vocales"]=resultado["vocales"]+1
                else:
                    resultado["consonantes"]=resultado["consonantes"]+1

        return resultado


astr = AnalizadorString()

print(astr.contar_por_tipo("Hola123"))
print(astr.texto_mas_largo)

# PASO 5. PRUEBA DE ESCRITORIO

# Carácter   Tipo
# H          consonante
# o          vocal
# l          consonante
# a          vocal
# 1          dígito
# 2          dígito
# 3          dígito

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 10 — Gestor de tareas con prioridad

# PASO 1. ENTENDER

# Entrada:
# Descripción y prioridad.

# Proceso:
# Guardar tuplas, filtrar prioridad alta y eliminar tareas.

# Salida:
# Lista de prioritarias y True/False al eliminar.

# PASO 2. BOSQUEJO

# ("Estudiar","alta")
# ("Leer","baja")

# Prioridad alta:
# [("Estudiar","alta")]

# Eliminar "Leer":
# queda [("Estudiar","alta")]

# PASO 3. PATRÓN

# Cada tarea es una tupla.
# tarea[0] es descripción.
# tarea[1] es prioridad.

# PASO 4. CÓDIGO

class Tareas:
    def __init__(self):
        self.tareas=[]

    def agregar_tarea(self,descripcion,prioridad):
        self.tareas.append((descripcion,prioridad))

    def tareas_prioritarias(self):
        prioritarias=[]

        for tarea in self.tareas:
            if tarea[1]=="alta":
                prioritarias.append(tarea)

        return prioritarias

    def eliminar_completada(self,descripcion):
        for tarea in self.tareas:
            if tarea[0]==descripcion:
                self.tareas.remove(tarea)
                return True

        return False


t = Tareas()
t.agregar_tarea("Estudiar","alta")
t.agregar_tarea("Leer","baja")

print(t.tareas_prioritarias())
print(t.eliminar_completada("Leer"))
print(t.tareas)

# PASO 5. PRUEBA DE ESCRITORIO

# Acción              Lista de tareas
# Agregar Estudiar    [("Estudiar","alta")]
# Agregar Leer        [("Estudiar","alta"),("Leer","baja")]
# Prioritarias        [("Estudiar","alta")]
# Eliminar Leer       [("Estudiar","alta")]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 11 — Contador de frecuencia

# PASO 1. ENTENDER

# Entrada:
# Elementos.

# Proceso:
# Contar cuántas veces aparece cada elemento.

# Salida:
# Elemento más frecuente y frecuencia de un elemento.

# PASO 2. BOSQUEJO

# a -> {"a":1}
# b -> {"a":1,"b":1}
# a -> {"a":2,"b":1}

# Más frecuente = "a"

# PASO 3. PATRÓN

# Si existe se suma 1.
# Si no existe se crea con 1.
# Para encontrar el mayor se comparan cantidades.

# PASO 4. CÓDIGO

class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias={}

    def agregar_elemento(self,elemento):
        if elemento in self.frecuencias:
            self.frecuencias[elemento]=self.frecuencias[elemento]+1
        else:
            self.frecuencias[elemento]=1

    def elemento_mas_frecuente(self):
        elemento_mayor=None
        cantidad_mayor=0

        for elemento,cantidad in self.frecuencias.items():
            if cantidad>cantidad_mayor:
                cantidad_mayor=cantidad
                elemento_mayor=elemento

        return elemento_mayor

    def frecuencia_elemento(self,elemento):
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        else:
            return 0


cf = ContadorFrecuencia()
cf.agregar_elemento("a")
cf.agregar_elemento("b")
cf.agregar_elemento("a")

print(cf.frecuencias)
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("a"))

# PASO 5. PRUEBA DE ESCRITORIO

# Acción        Frecuencias
# agregar a     {"a":1}
# agregar b     {"a":1,"b":1}
# agregar a     {"a":2,"b":1}
# Mayor         "a"

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 12 — Selector de rango con tuplas

# PASO 1. ENTENDER

# Entrada:
# Pares (inicio,fin).

# Proceso:
# Crear rangos, convertirlos en tuplas y unirlos sin duplicados.

# Salida:
# Tupla o lista de elementos únicos.

# PASO 2. BOSQUEJO

# (1,3) -> (1,2,3)
# (2,4) -> (2,3,4)
# Unión sin repetir -> [1,2,3,4]

# PASO 3. PATRÓN

# crear_rango() genera los números.
# elementos_en_multiples_rangos() reutiliza crear_rango().
# El conjunto evita repetir números.

# PASO 4. CÓDIGO

class SelectorRango:
    def __init__(self):
        self.elementos=set()

    def crear_rango(self,inicio,fin):
        numeros=[]

        for numero in range(inicio,fin+1):
            numeros.append(numero)

        return tuple(numeros)

    def elementos_en_multiples_rangos(self,*rangos):
        self.elementos=set()
        resultado=[]

        for rango in rangos:
            numeros=self.crear_rango(rango[0],rango[1])

            for numero in numeros:
                if numero not in self.elementos:
                    self.elementos.add(numero)
                    resultado.append(numero)

        return resultado


sr = SelectorRango()

print(sr.crear_rango(1,3))
print(sr.elementos_en_multiples_rangos((1,3),(2,4)))

# PASO 5. PRUEBA DE ESCRITORIO

# Rango        Tupla        Resultado acumulado
# (1,3)        (1,2,3)      [1,2,3]
# (2,4)        (2,3,4)      [1,2,3,4]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 13 — Combinador de listas

# PASO 1. ENTENDER

# Entrada:
# Dos o más listas.

# Proceso:
# Alternar los elementos usando índices.

# Salida:
# Lista intercalada.

# PASO 2. BOSQUEJO

# Lista1 = [1,2]
# Lista2 = [3,4]

# Posición 0 -> 1,3
# Posición 1 -> 2,4

# Resultado = [1,3,2,4]

# PASO 3. PATRÓN

# Se usa el mismo índice para las dos listas.
# Primero se agrega lista1[i] y después lista2[i].
# intercalar_multiples() reutiliza intercalar().

# PASO 4. CÓDIGO

class CombinadorListas:
    def __init__(self):
        self.resultado=[]

    def intercalar(self,lista1,lista2):
        self.resultado=[]
        i=0

        while i<len(lista1) or i<len(lista2):

            if i<len(lista1):
                self.resultado.append(lista1[i])

            if i<len(lista2):
                self.resultado.append(lista2[i])

            i=i+1

        return self.resultado

    def intercalar_multiples(self,*listas):
        if len(listas)==0:
            return []

        resultado=listas[0]
        i=1

        while i<len(listas):
            resultado=self.intercalar(resultado,listas[i])
            i=i+1

        return resultado


cl = CombinadorListas()

print(cl.intercalar([1,2],[3,4]))
print(cl.intercalar_multiples([1,2],[3,4],[5,6]))

# PASO 5. PRUEBA DE ESCRITORIO

# i      lista1[i]      lista2[i]      Resultado
# 0      1              3              [1,3]
# 1      2              4              [1,3,2,4]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 14 — Mapeo de estudiantes a notas

# PASO 1. ENTENDER

# Entrada:
# Estudiante y nota.

# Proceso:
# Guardar estudiante -> nota.
# Buscar aprobados.
# Buscar la nota mayor.

# Salida:
# Lista de aprobados y tupla del mejor estudiante.

# PASO 2. BOSQUEJO

# Ana = 95
# Bob = 70

# Nota mínima = 75
# Ana aprueba.
# Bob no aprueba.

# Mejor = ("Ana",95)

# PASO 3. PATRÓN

# registrar() guarda en diccionario.
# estudiantes_aprobados() compara la nota.
# mejor_estudiante() guarda la mejor nota encontrada.

# PASO 4. CÓDIGO

class RegistroNotas:
    def __init__(self):
        self.notas={}

    def registrar(self,estudiante,nota):
        self.notas[estudiante]=nota

    def estudiantes_aprobados(self,nota_minima):
        aprobados=[]

        for estudiante,nota in self.notas.items():
            if nota>=nota_minima:
                aprobados.append(estudiante)

        return aprobados

    def mejor_estudiante(self):
        mejor=""
        mejor_nota=-1

        for estudiante,nota in self.notas.items():
            if nota>mejor_nota:
                mejor_nota=nota
                mejor=estudiante

        return (mejor,mejor_nota)


rn = RegistroNotas()
rn.registrar("Ana",95)
rn.registrar("Bob",70)

print(rn.estudiantes_aprobados(75))
print(rn.mejor_estudiante())

# PASO 5. PRUEBA DE ESCRITORIO

# Estudiante     Nota      Aprobado
# Ana            95        Sí
# Bob            70        No
# Mejor: ("Ana",95)

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 15 — Divisores de un número

# PASO 1. ENTENDER

# Entrada:
# Uno o varios números.

# Proceso:
# Encontrar divisores usando módulo.
# Verificar si un número es perfecto.

# Salida:
# Tupla de divisores, True/False y diccionario.

# PASO 2. BOSQUEJO

# 12:
# divisores = 1,2,3,4,6,12

# 6:
# divisores propios = 1,2,3
# suma = 6
# Es perfecto = True

# PASO 3. PATRÓN

# Si numero % i == 0, i es divisor.
# es_perfecto() reutiliza encontrar_divisores().
# encontrar_multiples_divisores() guarda número -> divisores.

# PASO 4. CÓDIGO

class DivisorFinder:
    def __init__(self):
        self.divisores={}

    def encontrar_divisores(self,numero):
        resultado=[]

        for i in range(1,numero+1):
            if numero%i==0:
                resultado.append(i)

        return tuple(resultado)

    def es_perfecto(self,numero):
        divisores=self.encontrar_divisores(numero)
        suma=0

        for divisor in divisores:
            if divisor!=numero:
                suma=suma+divisor

        if suma==numero:
            return True
        else:
            return False

    def encontrar_multiples_divisores(self,*numeros):
        self.divisores={}

        for numero in numeros:
            self.divisores[numero]=self.encontrar_divisores(numero)

        return self.divisores


df = DivisorFinder()

print(df.encontrar_divisores(12))
print(df.es_perfecto(6))
print(df.encontrar_multiples_divisores(6,12,15))

# PASO 5. PRUEBA DE ESCRITORIO

# encontrar_divisores(12) -> (1,2,3,4,6,12)
# es_perfecto(6)          -> True

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 16 — Codificador César

# PASO 1. ENTENDER

# Entrada:
# Letra o palabra y desplazamiento.

# Proceso:
# Convertir una letra a código, desplazarla y regresar a carácter.

# Salida:
# Palabra codificada e historial.

# PASO 2. BOSQUEJO

# "hola", desplazamiento 3

# h -> k
# o -> r
# l -> o
# a -> d

# Resultado: "krod"

# NOTA:
# La guía muestra "kroc" como ejemplo aproximado.
# Con César de desplazamiento 3, el resultado de "hola" es "krod".

# PASO 3. PATRÓN

# Cada letra se procesa igual.
# codificar_palabra() reutiliza codificar_letra().
# % 26 mantiene el resultado dentro del alfabeto.

# PASO 4. CÓDIGO

class CodificadorCesar:
    def __init__(self):
        self.historial={}

    def codificar_letra(self,letra,desplazamiento):

        if letra>="a" and letra<="z":
            codigo=ord(letra)-ord("a")
            codigo=(codigo+desplazamiento)%26
            return chr(codigo+ord("a"))

        elif letra>="A" and letra<="Z":
            codigo=ord(letra)-ord("A")
            codigo=(codigo+desplazamiento)%26
            return chr(codigo+ord("A"))

        else:
            return letra

    def codificar_palabra(self,palabra,desplazamiento):
        resultado=""

        for letra in palabra:
            resultado=resultado+self.codificar_letra(letra,desplazamiento)

        self.historial[palabra]=resultado

        return resultado


cc = CodificadorCesar()

print(cc.codificar_palabra("hola",3))
print(cc.historial)

# PASO 5. PRUEBA DE ESCRITORIO

# Letra      Desplazamiento      Resultado
# h          3                   k
# o          3                   r
# l          3                   o
# a          3                   d
# Palabra final: krod

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 17 — Grupo de edades

# PASO 1. ENTENDER

# Entrada:
# Varias edades.

# Proceso:
# Clasificar cada edad y guardarla en su categoría.

# Salida:
# Diccionario agrupado y promedio por categoría.

# IMPORTANTE:
# La guía no especifica los límites exactos de las categorías.
# Para que el ejercicio pueda ejecutarse se usa:
# menor de 12  -> niño
# 12 a 17      -> adolescente
# 18 a 64      -> adulto
# 65 o más     -> mayor

# Si el profesor dio otros límites, solo se cambian estos if/elif.

# PASO 2. BOSQUEJO

# 5  -> niño
# 15 -> adolescente
# 30 -> adulto
# 70 -> mayor

# PASO 3. PATRÓN

# clasificar_edad() usa if/elif/else.
# agrupar_por_categoria() reutiliza clasificar_edad().
# Cada categoría contiene una lista.

# PASO 4. CÓDIGO

class AgrupadorEdades:
    def __init__(self):
        self.grupos={"niño":[],"adolescente":[],"adulto":[],"mayor":[]}

    def clasificar_edad(self,edad):

        if edad<12:
            return "niño"

        elif edad<18:
            return "adolescente"

        elif edad<65:
            return "adulto"

        else:
            return "mayor"

    def agrupar_por_categoria(self,*edades):
        self.grupos={"niño":[],"adolescente":[],"adulto":[],"mayor":[]}

        for edad in edades:
            categoria=self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self,categoria):
        edades=self.grupos[categoria]
        return sum(edades)/len(edades)


ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(5,15,30,70))
print(ae.edad_promedio_categoria("adulto"))

# PASO 5. PRUEBA DE ESCRITORIO

# Edad      Categoría
# 5         niño
# 15        adolescente
# 30        adulto
# 70        mayor

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 18 — Matriz de distancias

# PASO 1. ENTENDER

# Entrada:
# Puntos como tuplas (x,y).

# Proceso:
# Calcular distancia euclidiana.
# Guardar las distancias.
# Comparar para obtener el punto más cercano.

# Salida:
# Distancia y punto más cercano.

# PASO 2. BOSQUEJO

# p1 = (0,0)
# p2 = (3,4)

# (3-0)^2 = 9
# (4-0)^2 = 16
# 9 + 16 = 25
# raíz = 5

# PASO 3. PATRÓN

# Cada punto tiene x en [0] e y en [1].
# punto_mas_cercano() reutiliza distancia_euclidiana().

# PASO 4. CÓDIGO

class CalculadorDistancia:
    def __init__(self):
        self.distancias=[]

    def distancia_euclidiana(self,p1,p2):
        x1=p1[0]
        y1=p1[1]

        x2=p2[0]
        y2=p2[1]

        distancia=((x2-x1)**2+(y2-y1)**2)**0.5

        self.distancias.append(distancia)

        return distancia

    def punto_mas_cercano(self,referencia,*puntos):
        cercano=None
        menor=None

        for punto in puntos:
            distancia=self.distancia_euclidiana(referencia,punto)

            if menor==None or distancia<menor:
                menor=distancia
                cercano=punto

        return cercano


cd = CalculadorDistancia()

print(cd.distancia_euclidiana((0,0),(3,4)))
print(cd.punto_mas_cercano((0,0),(5,5),(1,1),(10,10)))
print(cd.distancias)

# PASO 5. PRUEBA DE ESCRITORIO

# Punto                    Distancia aproximada
# (3,4)                    5.0
# (5,5)                    7.07
# (1,1)                    1.41
# (10,10)                  14.14
# Más cercano a (0,0): (1,1)

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 19 — Inventario de productos

# PASO 1. ENTENDER

# Entrada:
# Producto y cantidad.

# Proceso:
# Agregar stock, restar si existe suficiente y buscar bajo stock.

# Salida:
# True/False y lista de productos con bajo stock.

# PASO 2. BOSQUEJO

# pan = 50
# restar 30
# queda 20

# Si mínimo = 25:
# 20 < 25 -> pan está bajo stock.

# NOTA:
# En la guía aparece mínimo 15 y salida ["pan"] después de quedar 20.
# Matemáticamente 20 < 15 es falso.
# Por eso aquí se usa mínimo 25 para que el ejemplo sea coherente.

# PASO 3. PATRÓN

# Cada producto es una clave.
# La cantidad es el valor.
# Antes de restar se valida que exista suficiente stock.

# PASO 4. CÓDIGO

class Inventario:
    def __init__(self):
        self.productos={}

    def agregar_stock(self,producto,cantidad):

        if producto in self.productos:
            self.productos[producto]=self.productos[producto]+cantidad
        else:
            self.productos[producto]=cantidad

    def restar_stock(self,producto,cantidad):

        if producto in self.productos and self.productos[producto]>=cantidad:
            self.productos[producto]=self.productos[producto]-cantidad
            return True
        else:
            return False

    def productos_bajo_stock(self,minimo):
        bajos=[]

        for producto,cantidad in self.productos.items():
            if cantidad<minimo:
                bajos.append(producto)

        return bajos


inventario = Inventario()
inventario.agregar_stock("pan",50)

print(inventario.restar_stock("pan",30))
print(inventario.productos_bajo_stock(25))
print(inventario.productos)

# PASO 5. PRUEBA DE ESCRITORIO

# Acción               Stock       Salida
# agregar pan 50       50          -
# restar 30            20          True
# bajo stock 25        20          ["pan"]

#--------------------------------------------------------------------------------------------------------------

# EJERCICIO 20 — Analizador de patrones en textos

# PASO 1. ENTENDER

# Entrada:
# Texto y patrón.

# Proceso:
# Separar palabras, buscar las que empiezan con un patrón,
# agrupar por longitud y obtener palabras sin repetir.

# Salida:
# Lista, diccionario y conjunto.

# PASO 2. BOSQUEJO

# Texto: "casa carro perro camino"
# Patrón: "ca"

# casa   -> sí
# carro  -> sí
# perro  -> no
# camino -> sí

# Resultado:
# ["casa","carro","camino"]

# Para "el gato está aquí":
# el   -> longitud 2
# gato -> longitud 4
# está -> longitud 4
# aquí -> longitud 4

# Resultado correcto en Python:
# {2:["el"], 4:["gato","está","aquí"]}

# NOTA:
# La salida de ejemplo de la guía tiene claves repetidas y longitudes
# que no coinciden con len(). Un diccionario no puede tener dos claves
# iguales, por eso aquí se agrupan juntas las palabras de igual longitud.

# PASO 3. PATRÓN

# split() separa el texto.
# startswith() revisa el inicio de una palabra.
# len() obtiene la longitud.
# set() elimina duplicados.

# PASO 4. CÓDIGO

class AnalizadorPatrones:
    def __init__(self):
        self.palabras=[]

    def encontrar_palabras(self,texto,patron):
        encontradas=[]
        palabras=texto.split()

        for palabra in palabras:
            self.palabras.append(palabra)

            if palabra.startswith(patron):
                encontradas.append(palabra)

        return encontradas

    def agrupar_por_longitud(self,texto):
        grupos={}
        palabras=texto.split()

        for palabra in palabras:
            self.palabras.append(palabra)

            longitud=len(palabra)

            if longitud in grupos:
                grupos[longitud].append(palabra)
            else:
                grupos[longitud]=[palabra]

        return grupos

    def palabras_unicas(self):
        return set(self.palabras)


ap = AnalizadorPatrones()

print(ap.encontrar_palabras("casa carro perro camino","ca"))
print(ap.agrupar_por_longitud("el gato está aquí"))
print(ap.palabras_unicas())

# PASO 5. PRUEBA DE ESCRITORIO

# Acción                            Salida
# buscar patrón "ca"                ["casa","carro","camino"]
# agrupar "el gato está aquí"       {2:["el"],4:["gato","está","aquí"]}
# palabras_unicas()                 conjunto sin repetidos
