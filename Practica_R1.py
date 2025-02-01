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


def palindromo (x1):
    x  = x1.replace(" ", "")
    for i in range (len(x)):
        der =(x[i])
        izq = (x[-1-(i-(len(x)))])
        # print (der, izq)
        if der == izq :
            p = ("¡Es Palindromo!")
        else:
            p =("No es Palindromo")
            break
    return p
    

def lista_primos(a):
    c=[]                      
    for j in range (len(a)):   
        numero= int(a[j])         
        if numero>2:                
            for i in range (2,numero):
                sol= numero % i
                if sol == 0:
                    p= "no es primo" 
                    break
                else :          
                    p= "es primo"
        elif numero==1 or numero==0:
            p= "no es primo"
        elif numero==2:
            p= "es primo"
        else:
            p= "es negativo"

        if p == "es primo":
            p=numero
            c.append (p)
    return c 


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


def lista_letras_iguales(x): 
    a=[a.lower() for a in x]
    b=[]                               
    for i in range (len (a)):            
        a1= str(a[i])
        for j in range (i+1, len(a)):   
            a2= str(a[j])              
            print (a1,a2)  
            d= sorted (a1)               
            d1= sorted (a2)             
            if d== d1 :                  
                print ("son iguales ", a1, a2)
                b.append(a1)
                b.append (a2)          

                break
    return (list(set(b)))                


# primer ejercicio division entre cero no se puede 
try:
  elemento = operador(1, 0, "/")
  print(f"El Resultado es : {elemento}")
except ZeroDivisionError as error:
  print(f"Error: {error}")
# cuarto ejercicio, este no puede tener una lista de un dato o sino no funciona
try:
  elemento = sumatoria_sucesiva([1])
  print(f"El elemento en la posición 4 es: {elemento}")
except IndexError as error:
  print(f"Error: {error}")


