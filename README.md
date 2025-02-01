# En este repo veremos el uso de excepciones.
# Reto_6!

## Principalmente vamos a poner excepciones en las diferentes tareas.

#### La primera nos da unas caracteristicas que cumplir.

Aqui solo pude detectar dos posibles lugares donde podria poner el try y except.
#### El primero fue con el ejercicio A
```python
   def operador (x1: float, y1 : float, z):
    if z == "+":
        return x1 + y1
    elif z == "-":
        return x1 - y1
    elif z == "/":
        if y1 == 0:
            raise ZeroDivisionError("No se puedee usar el 0 de denominador")
        return x1 / y1
    elif z == "*":
        return x1 * y1

# primer ejercicio division entre cero no se puede 
  try:
    elemento = operador(1, 0, "/")
    print(f"El Resultado es : {elemento}")
  except ZeroDivisionError as error:
    print(f"Error: {error}")
```
### El segundo fue con el Ejercicio D
Aquí nos pidieron una lista que diera como resultado la sumatoria succesiva, sin embargo, si solo hay un dato esta no podra dar un resultado ya que no habra sumatoria.
```python
   def sumatoria_sucesiva(a):       
      if int(len(a))< 2:
          raise IndexError ("indice fuera de rango")
      if int(len(a))>=2:             
          max=a[0]+a[1]          
          Lista=int (len(a))     
          for i in range (1,Lista):  
              int(a[i])             
              int(a[i-1])          
              x=a[i]+ a[i-1]        
              if x> max:             
                  max=x             
          total= (f"La sumatoria Maxima es {max}") 
      else:
          total= "No se encontraron parejas validas en la lista"     
      return total
# cuarto ejercicio, este no puede tener una lista de un dato o sino no funciona
  try:
    elemento = sumatoria_sucesiva([1])
    print(f"El resultado es: {elemento}")
  except IndexError as error:
    print(f"Error: {error}")

```

## El Segundo Punto de este Reto es hacer lo mismo pero con shape.
Poner excepts en lugares donde uno los vea utiles.
```python
  class Shape...
    try          :  
    
      triangulos = Triangulo ((0,0),(6,0),(3,5))    # Obligatorio dar solo 3 datos con tuplas de dos numeros
      rectangulos= Rectangulo((2,0),(0,0),(0,3),(2,3))     # Aquí son 4 datos y dos numeros en tuplas 
      cuadrados = Cuadrado((2,0),(0,0),(0,2),(2,2))
      print (rectangulos.aristas())
      print (triangulos.vertices())
      print (cuadrados.calculara_area())
      print (triangulos.calcular_perimetro())
      print (rectangulos.ang_inter())
    
    except ValueError as error1:
      print(f"Error: {error1}, \nIntente dar solo dos puntos de x and y")
    except TypeError as error :
      print (f"Error : {error }\nNo cumple con el requerimiento de las figuras")
```
Aquí, puse valueError y TypeError, pues en caso de que los datos no sean "__x__" y "__y__ "estos daran como resultado donde esta el error y dirá que ponga solo puntos de "__x__" y "__y__"
y TypeError si los argumentos estan incompletos o no cumplen con lo requerido.
adjunte todo el codigo de ambos, pero en general los que yo muestro son los puntos donde estan las excepciones.

## conclusión:
Si soy sincero, me gusto repetir el Reto_1! y darme cuenta que he mejorado un poco más, además con el tema dado me senti muy comodo poniendo excepciones,
me parecio (eso sí) un poco difícil cuando la excepcion es en una clase tan grande y todo esta tan conectado (como en shape) , así que lo mejor fue poner al final los excepts.

Me gusto mucho mi trabajo y la verdad, aúnque el incio fue sencillo y gratificante, y el final fue un poco estresante, me gusto aún así poder controlar los errores que se pueden dar 
por parte externa y así poder guiar a como hacerlo correctamente. 
hasta el proximo reto bai (bye)!... _¿no es curioso que cada véz es mas corto estos repos?_
