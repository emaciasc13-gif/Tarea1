# EJERCICIO 1
# ENUNCIADO:
# Crear una clase ControlEdades que valide edades entre 0 y 120, cargue varias edades válidas y calcule el promedio.

class ControlEdades:
    def __init__(self):
        self.edades=[]

    def validar_edad(self,edad):
        if edad>=0 and edad<=120:
            return True
        else:
            return False

    def cargar_edades(self,*args):
        for edad in args:
            if self.validar_edad(edad):
                self.edades.append(edad)
        return self.edades

    def promedio(self):
        return sum(self.edades)/len(self.edades)


ce = ControlEdades()
print(ce.cargar_edades(18,25,-3,130,40))
print(ce.promedio())


# EJERCICIO 2
# ENUNCIADO:
# Crear una clase GestorColores que guarde colores en una lista y en un conjunto, cuente los colores únicos
# y permita agregar varios colores usando *args.

class GestorColores:
    def __init__(self):
        self.colores=[]
        self.unicos=set()

    def agregar_color(self,color):
        self.colores.append(color)
        self.unicos.add(color)

    def contar_unicos(self):
        return len(self.unicos)

    def agregar_varios(self,*args):
        for color in args:
            self.agregar_color(color)
        return self.colores


gc = GestorColores()
print(gc.agregar_varios("rojo","azul","rojo","verde"))
print(gc.contar_unicos())


# EJERCICIO 3
# ENUNCIADO:
# Crear una clase Tienda que guarde productos y precios en un diccionario, calcule el total
# y muestre los productos que cuesten menos de cierto valor.

class Tienda:
    def __init__(self):
        self.productos={}

    def agregar_producto(self,nombre,precio):
        self.productos[nombre]=precio

    def total_productos(self):
        total=0

        for precio in self.productos.values():
            total=total+precio

        return total

    def productos_baratos(self,precio_maximo):
        baratos=[]

        for nombre,precio in self.productos.items():
            if precio<=precio_maximo:
                baratos.append(nombre)

        return baratos


tienda = Tienda()
tienda.agregar_producto("cuaderno",2.50)
tienda.agregar_producto("mochila",20)
tienda.agregar_producto("lapiz",0.75)

print(tienda.total_productos())
print(tienda.productos_baratos(3))


# EJERCICIO 4
# ENUNCIADO:
# Crear una clase RotadorLista que mueva el primer elemento de una lista al final y que pueda hacerlo con varias listas.

class RotadorLista:
    def __init__(self):
        self.rotadas={}

    def rotar(self,lista):
        resultado=[]

        if len(lista)==0:
            return resultado

        i=1

        while i<len(lista):
            resultado.append(lista[i])
            i=i+1

        resultado.append(lista[0])

        return resultado

    def rotar_varias(self,*listas):
        self.rotadas={}

        for lista in listas:
            self.rotadas[tuple(lista)]=self.rotar(lista)

        return self.rotadas


rl = RotadorLista()
print(rl.rotar([1,2,3,4]))
print(rl.rotar_varias([1,2,3],[4,5,6]))


# EJERCICIO 5
# ENUNCIADO:
# Crear una clase ClasificadorNumeros que clasifique números en positivos, negativos y ceros.
# También debe devolver la cantidad de cada grupo.

class ClasificadorNumeros:
    def __init__(self):
        self.grupos={"positivos":[],"negativos":[],"ceros":[]}

    def tipo_numero(self,numero):
        if numero>0:
            return "positivo"

        elif numero<0:
            return "negativo"

        else:
            return "cero"

    def separar(self,*numeros):
        self.grupos={"positivos":[],"negativos":[],"ceros":[]}

        for numero in numeros:
            tipo=self.tipo_numero(numero)

            if tipo=="positivo":
                self.grupos["positivos"].append(numero)

            elif tipo=="negativo":
                self.grupos["negativos"].append(numero)

            else:
                self.grupos["ceros"].append(numero)

        return self.grupos

    def cantidades(self):
        positivos=len(self.grupos["positivos"])
        negativos=len(self.grupos["negativos"])
        ceros=len(self.grupos["ceros"])

        return (positivos,negativos,ceros)


cn = ClasificadorNumeros()
print(cn.separar(-3,0,5,8,-1,0))
print(cn.cantidades())


# EJERCICIO 6
# ENUNCIADO:
# Crear una clase RegistroLluvias que guarde cantidades de lluvia, calcule el valor mínimo, máximo y promedio
# y permita registrar varios valores con *args.

class RegistroLluvias:
    def __init__(self):
        self.lluvias=[]

    def registrar(self,cantidad):
        self.lluvias.append(cantidad)

    def minima(self):
        return min(self.lluvias)

    def maxima(self):
        return max(self.lluvias)

    def promedio(self):
        return sum(self.lluvias)/len(self.lluvias)

    def registrar_varias(self,*cantidades):
        for cantidad in cantidades:
            self.registrar(cantidad)

        return self.lluvias


lluvia = RegistroLluvias()
print(lluvia.registrar_varias(12,5,20,8))
print(lluvia.minima())
print(lluvia.maxima())
print(lluvia.promedio())


# EJERCICIO 7
# ENUNCIADO:
# Crear una clase AgendaContactos que guarde nombres y teléfonos en un diccionario.
# Debe buscar un teléfono por nombre y encontrar nombres que comiencen con una letra.

class AgendaContactos:
    def __init__(self):
        self.contactos={}

    def agregar_contacto(self,nombre,telefono):
        self.contactos[nombre]=telefono

    def buscar_telefono(self,nombre):
        if nombre in self.contactos:
            return self.contactos[nombre]
        else:
            return None

    def nombres_por_letra(self,letra):
        resultado=[]

        for nombre in self.contactos.keys():
            if nombre.startswith(letra):
                resultado.append(nombre)

        return resultado


agenda = AgendaContactos()
agenda.agregar_contacto("Ana","0991111111")
agenda.agregar_contacto("Carlos","0982222222")
agenda.agregar_contacto("Andres","0973333333")

print(agenda.buscar_telefono("Ana"))
print(agenda.nombres_por_letra("A"))


# EJERCICIO 8
# ENUNCIADO:
# Crear una clase Cursos que permita crear cursos, agregar estudiantes y encontrar el curso que tenga menos estudiantes.

class Cursos:
    def __init__(self):
        self.cursos={}

    def crear_curso(self,nombre):
        self.cursos[nombre]=[]

    def agregar_estudiante(self,curso,estudiante):
        if curso in self.cursos:
            self.cursos[curso].append(estudiante)

    def curso_menor_integrantes(self):
        menor=""
        cantidad=None

        for curso,estudiantes in self.cursos.items():

            if cantidad==None or len(estudiantes)<cantidad:
                cantidad=len(estudiantes)
                menor=curso

        return menor


cursos = Cursos()
cursos.crear_curso("A")
cursos.crear_curso("B")

cursos.agregar_estudiante("A","Luis")
cursos.agregar_estudiante("A","Maria")
cursos.agregar_estudiante("B","Pedro")

print(cursos.cursos)
print(cursos.curso_menor_integrantes())


# EJERCICIO 9
# ENUNCIADO:
# Crear una clase AnalizadorCaracteres que determine si una letra es mayúscula y cuente mayúsculas, minúsculas y dígitos de un texto.

class AnalizadorCaracteres:
    def __init__(self):
        self.ultimo_texto=""

    def es_mayuscula(self,letra):
        if letra.isalpha() and letra==letra.upper():
            return True
        else:
            return False

    def contar(self,texto):
        resultado={"mayusculas":0,"minusculas":0,"digitos":0}

        self.ultimo_texto=texto

        for caracter in texto:

            if caracter.isdigit():
                resultado["digitos"]=resultado["digitos"]+1

            elif caracter.isalpha():

                if self.es_mayuscula(caracter):
                    resultado["mayusculas"]=resultado["mayusculas"]+1

                else:
                    resultado["minusculas"]=resultado["minusculas"]+1

        return resultado


ac = AnalizadorCaracteres()
print(ac.contar("HolaMundo2026"))
print(ac.ultimo_texto)


# EJERCICIO 10
# ENUNCIADO:
# Crear una clase Recordatorios que guarde recordatorios como tuplas de texto y estado.
# Debe mostrar los pendientes y permitir eliminar uno.

class Recordatorios:
    def __init__(self):
        self.recordatorios=[]

    def agregar(self,texto,estado):
        self.recordatorios.append((texto,estado))

    def pendientes(self):
        resultado=[]

        for recordatorio in self.recordatorios:

            if recordatorio[1]=="pendiente":
                resultado.append(recordatorio)

        return resultado

    def eliminar(self,texto):
        for recordatorio in self.recordatorios:

            if recordatorio[0]==texto:
                self.recordatorios.remove(recordatorio)
                return True

        return False


r = Recordatorios()

r.agregar("Comprar pan","pendiente")
r.agregar("Enviar tarea","completado")

print(r.pendientes())
print(r.eliminar("Enviar tarea"))
print(r.recordatorios)


# EJERCICIO 11
# ENUNCIADO:
# Crear una clase ContadorVisitas que registre cuántas veces se visita cada página.
# Debe devolver la página más visitada y la cantidad de visitas de una página.

class ContadorVisitas:
    def __init__(self):
        self.visitas={}

    def registrar_visita(self,pagina):

        if pagina in self.visitas:
            self.visitas[pagina]=self.visitas[pagina]+1

        else:
            self.visitas[pagina]=1

    def pagina_mas_visitada(self):
        pagina_mayor=None
        cantidad_mayor=0

        for pagina,cantidad in self.visitas.items():

            if cantidad>cantidad_mayor:
                cantidad_mayor=cantidad
                pagina_mayor=pagina

        return pagina_mayor

    def visitas_pagina(self,pagina):

        if pagina in self.visitas:
            return self.visitas[pagina]

        else:
            return 0


cv = ContadorVisitas()

cv.registrar_visita("inicio")
cv.registrar_visita("productos")
cv.registrar_visita("inicio")

print(cv.visitas)
print(cv.pagina_mas_visitada())
print(cv.visitas_pagina("inicio"))


# EJERCICIO 12
# ENUNCIADO:
# Crear una clase RangosPares que construya una tupla con los números pares de un rango y combine varios rangos sin repetir números.

class RangosPares:
    def __init__(self):
        self.numeros=set()

    def crear_pares(self,inicio,fin):
        pares=[]

        for numero in range(inicio,fin+1):

            if numero%2==0:
                pares.append(numero)

        return tuple(pares)

    def combinar_rangos(self,*rangos):
        self.numeros=set()
        resultado=[]

        for rango in rangos:

            pares=self.crear_pares(rango[0],rango[1])

            for numero in pares:

                if numero not in self.numeros:
                    self.numeros.add(numero)
                    resultado.append(numero)

        return resultado


rpares = RangosPares()
print(rpares.crear_pares(1,10))
print(rpares.combinar_rangos((1,6),(4,10)))


# EJERCICIO 13
# ENUNCIADO:
# Crear una clase UnionListas que una dos listas sin repetir elementos y permita unir varias listas reutilizando el mismo método.

class UnionListas:
    def __init__(self):
        self.resultado=[]

    def unir(self,lista1,lista2):
        self.resultado=[]

        for elemento in lista1:

            if elemento not in self.resultado:
                self.resultado.append(elemento)

        for elemento in lista2:

            if elemento not in self.resultado:
                self.resultado.append(elemento)

        return self.resultado

    def unir_varias(self,*listas):

        if len(listas)==0:
            return []

        resultado=listas[0]
        i=1

        while i<len(listas):

            resultado=self.unir(resultado,listas[i])
            i=i+1

        return resultado


ul = UnionListas()
print(ul.unir([1,2,3],[3,4,5]))
print(ul.unir_varias([1,2],[2,3],[3,4]))


# EJERCICIO 14
# ENUNCIADO:
# Crear una clase RegistroPuntajes que guarde jugadores y puntajes.
# Debe encontrar jugadores que superen un mínimo y encontrar al jugador con menor puntaje.

class RegistroPuntajes:
    def __init__(self):
        self.puntajes={}

    def registrar(self,jugador,puntaje):
        self.puntajes[jugador]=puntaje

    def jugadores_superiores(self,minimo):
        resultado=[]

        for jugador,puntaje in self.puntajes.items():

            if puntaje>=minimo:
                resultado.append(jugador)

        return resultado

    def menor_puntaje(self):
        jugador_menor=""
        puntaje_menor=None

        for jugador,puntaje in self.puntajes.items():

            if puntaje_menor==None or puntaje<puntaje_menor:
                puntaje_menor=puntaje
                jugador_menor=jugador

        return (jugador_menor,puntaje_menor)


rp = RegistroPuntajes()

rp.registrar("Luis",80)
rp.registrar("Ana",95)
rp.registrar("Pedro",60)

print(rp.jugadores_superiores(75))
print(rp.menor_puntaje())


# EJERCICIO 15
# ENUNCIADO:
# Crear una clase MultiploFinder que encuentre los múltiplos de un número hasta un límite, compruebe si un valor es múltiplo
# y procese varios números.

class MultiploFinder:
    def __init__(self):
        self.multiplos={}

    def encontrar_multiplos(self,numero,limite):
        resultado=[]
        valor=numero

        while valor<=limite:

            resultado.append(valor)
            valor=valor+numero

        return tuple(resultado)

    def es_multiplo(self,numero,valor):

        if valor%numero==0:
            return True

        else:
            return False

    def multiples_varios(self,limite,*numeros):
        self.multiplos={}

        for numero in numeros:

            self.multiplos[numero]=self.encontrar_multiplos(numero,limite)

        return self.multiplos


mf = MultiploFinder()

print(mf.encontrar_multiplos(3,15))
print(mf.es_multiplo(3,12))
print(mf.multiples_varios(12,2,3,4))


# EJERCICIO 16
# ENUNCIADO:
# Crear una clase ReemplazadorVocales que cambie cada vocal por un símbolo *.
# Debe transformar palabras completas y guardar un historial.

class ReemplazadorVocales:
    def __init__(self):
        self.historial={}

    def reemplazar_letra(self,letra):
        letra_minuscula=letra.lower()

        if letra_minuscula=="a" or letra_minuscula=="e" or letra_minuscula=="i" or letra_minuscula=="o" or letra_minuscula=="u":
            return "*"

        else:
            return letra

    def reemplazar_palabra(self,palabra):
        resultado=""

        for letra in palabra:

            resultado=resultado+self.reemplazar_letra(letra)

        self.historial[palabra]=resultado

        return resultado


rv = ReemplazadorVocales()

print(rv.reemplazar_palabra("programacion"))
print(rv.historial)


# EJERCICIO 17
# ENUNCIADO:
# Crear una clase ClasificadorAlturas que clasifique alturas como baja, media o alta.
# Debe agrupar varias alturas y calcular el promedio de una categoría.

class ClasificadorAlturas:
    def __init__(self):
        self.grupos={"baja":[],"media":[],"alta":[]}

    def clasificar(self,altura):

        if altura<150:
            return "baja"

        elif altura<180:
            return "media"

        else:
            return "alta"

    def agrupar(self,*alturas):
        self.grupos={"baja":[],"media":[],"alta":[]}

        for altura in alturas:

            categoria=self.clasificar(altura)
            self.grupos[categoria].append(altura)

        return self.grupos

    def promedio_categoria(self,categoria):
        alturas=self.grupos[categoria]

        return sum(alturas)/len(alturas)


ca = ClasificadorAlturas()

print(ca.agrupar(145,160,175,182,190))
print(ca.promedio_categoria("media"))


# EJERCICIO 18
# ENUNCIADO:
# Crear una clase CalculadorPerimetro que reciba rectángulos representados por tuplas (base,altura),
# calcule su perímetro y encuentre el rectángulo con menor perímetro.

class CalculadorPerimetro:
    def __init__(self):
        self.perimetros=[]

    def calcular(self,rectangulo):
        base=rectangulo[0]
        altura=rectangulo[1]

        perimetro=2*(base+altura)

        self.perimetros.append(perimetro)

        return perimetro

    def menor_perimetro(self,*rectangulos):
        menor_rectangulo=None
        menor=None

        for rectangulo in rectangulos:

            perimetro=self.calcular(rectangulo)

            if menor==None or perimetro<menor:
                menor=perimetro
                menor_rectangulo=rectangulo

        return menor_rectangulo


cp = CalculadorPerimetro()

print(cp.calcular((3,4)))
print(cp.menor_perimetro((5,5),(2,3),(10,2)))
print(cp.perimetros)


# EJERCICIO 19
# ENUNCIADO:
# Crear una clase Biblioteca que guarde libros y cantidad de copias.
# Debe agregar copias, prestar un libro y mostrar los libros con pocas copias.

class Biblioteca:
    def __init__(self):
        self.libros={}

    def agregar_copias(self,libro,cantidad):

        if libro in self.libros:
            self.libros[libro]=self.libros[libro]+cantidad

        else:
            self.libros[libro]=cantidad

    def prestar(self,libro):

        if libro in self.libros and self.libros[libro]>0:
            self.libros[libro]=self.libros[libro]-1
            return True

        else:
            return False

    def pocas_copias(self,minimo):
        resultado=[]

        for libro,cantidad in self.libros.items():

            if cantidad<minimo:
                resultado.append(libro)

        return resultado


b = Biblioteca()

b.agregar_copias("Python",3)
b.agregar_copias("Matematicas",1)

print(b.prestar("Python"))
print(b.pocas_copias(2))
print(b.libros)


# EJERCICIO 20
# ENUNCIADO:
# Crear una clase BuscadorPalabras que encuentre palabras que terminen con un patrón, agrupe palabras por su primera letra
# y devuelva las palabras únicas.

class BuscadorPalabras:
    def __init__(self):
        self.palabras=[]

    def palabras_que_terminan(self,texto,patron):
        encontradas=[]
        palabras=texto.split()

        for palabra in palabras:

            self.palabras.append(palabra)

            if palabra.endswith(patron):
                encontradas.append(palabra)

        return encontradas

    def agrupar_por_inicial(self,texto):
        grupos={}
        palabras=texto.split()

        for palabra in palabras:

            self.palabras.append(palabra)

            inicial=palabra[0]

            if inicial in grupos:
                grupos[inicial].append(palabra)

            else:
                grupos[inicial]=[palabra]

        return grupos

    def palabras_unicas(self):
        return set(self.palabras)


bp = BuscadorPalabras()

print(bp.palabras_que_terminan("casa mesa perro ventana","a"))
print(bp.agrupar_por_inicial("sol silla luna libro"))
print(bp.palabras_unicas())
