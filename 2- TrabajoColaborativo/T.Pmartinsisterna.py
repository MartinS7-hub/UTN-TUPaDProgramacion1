#TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN 
#Actividades  
#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.  

print("Hola Mundo")

#2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando 
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir 
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

nombre = input("Ingresa tu nombre: ")
print(f"Hola,{nombre}")

#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e 
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa 
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 #años y vivo en Argentina”.
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.  

nombre1 = input("Ingresa tu Nombre: ")
apellido = input("Ingresa tu Apellido: ")
edad = input("Ingresa tu Edad: ")
residencia = input("Ingresa tu lugar de Residencia: ")
print(f"Hola, yo soy {nombre1} {apellido}, tengo {edad} y soy de {residencia}")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 

radio = input("Ingresa el Radio: ")
radio2 = float(radio)

area = 3.14 * (radio2 ** 2)

perimetro= 2 * 3.14 * radio2

print(f"Usted ha ingresado el Radio de {radio2}, por lo tanto, su Área es de {area} Y su Perimetro es de {perimetro}")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 

segundos= int(input("Ingresa los segundos que desee: "))

minutos= segundos // 60

hora= segundos // 3600

print(f"Usted ah Ingresado {segundos}, por lo tanto serian {minutos} Minutos y {hora} Horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 

numeros = input("Ingresa un Numero: ")
numero2 = float(numeros)

print(f"Usted ha ingresado el Numero {numeros}")

for i in range (1,11):
    multiplicar = numero2 * i
    print(f"{numeros} X  {i} = {multiplicar}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por 
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

print("Ingresa 2 Numeros ")
numeroE = int(input("Ingresa el primer Numero: "))
numero11 = int(input("Ingresa el segundo Numero: "))

if numero <= 0 or numero1 <= 0:
    print("INGRESA UN NUMERO MAYOR A 0")
else:
    multiplicarr = numeroE * numero11
    resta = numeroE - numero11
    division = numeroE / numero11
    suma = numeroE + numero11
    
    print(f"Usted ah Ingresado el Numero {numeroE} y el Numero {numero11}, por lo tanto la suma de los 2 valores seria {suma}, la resta seria {resta}, la multiplicacion {multiplicarr} y la division {division}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice 
#de masa corporal. Tener en cuenta que el índice de masa corporal 

altura= float(input("Ingresa tu altura: "))
peso= float(input("Ingresa tu peso: "))

altura2 = altura ** 2
imc = peso / altura2

print(f"Segun su Altura de {altura} y su peso de {peso} tu indice de masa corporal seria de {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
#  Tener en cuenta la siguiente equivalencia

celcius= float(input("Ingresa la temperatura en grados celcius: "))

fahrenheit = (celcius * 9/5) + 32

print(f"Segun la temperatura de {celcius}°C eato equivaldria a {fahrenheit}°F")

#10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números. 

print("Ingresa 3 Numeros")
numer1 = float(input("Ingresa el primer Numero"))
numer2 = float(input("Ingresa el segundo Numero"))
numer3 = float(input("Ingresa el tercer Numero"))

sumar = numer1+numer2+numer3
promedios = sumar/3

print(f"Usted ah ingresado los numeros {numer1},{numer2} y {numer3} por lo que nos da un Promedio de {promedios}")