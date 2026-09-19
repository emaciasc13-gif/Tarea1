# EJERCICIO 1

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


# EJERCICIO 2

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


# EJERCICIO 3

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


# EJERCICIO 4

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


# EJERCICIO 5

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


# EJERCICIO 6

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


# EJERCICIO 7

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


# EJERCICIO 8

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


# EJERCICIO 9

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


# EJERCICIO 10

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


# EJERCICIO 11

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


# EJERCICIO 12

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


# EJERCICIO 13

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


# EJERCICIO 14

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


# EJERCICIO 15

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


# EJERCICIO 16

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


# EJERCICIO 17

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


# EJERCICIO 18

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


# EJERCICIO 19

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


# EJERCICIO 20

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
