#definir variables
v1=float
v2=float
signo=str
total=float
#datos de entrada
v1=float(input("ingrese el primer numero :"))
v2=float(input("ingrese el segundo numero:"))
print("+=suma")
print("-=resta")
print("/=division")
print("*=multiplicacion")
print("^=potencia")
print("R = RAIZ")
print("%=modulo de 2")
signo=str(input("ingrese el signo:"))
#proceso
if signo=="+":
    total=v1+v2
elif signo=="-":
    total=v1-v2
elif signo=="/":
    total=v1/v2
elif signo=="*":
    total==v1*v2
elif signo=="^":
    total=v1^v2
elif signo=="R":
    total=v1**0.5
else:
    total=v1-v1
#datos de salida
print(f"resultado :{total}")