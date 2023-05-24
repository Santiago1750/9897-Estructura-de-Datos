primerNumero = input("Ingrese el primer número: ")

try:
    primero = int(primerNumero)
except:    
    primero = "Cadena"

segundoNumero = input("Ingrese el segundo número: ")

try:
    segundo= int(segundoNumero)
except:    
    segundo = "Cadena"

if primero == "Cadena" or segundo =="C adena":
    print("Ingreso mal un dato, pruebe una vez mas ingreando numeros")
else:
    print(primero + segundo)    
