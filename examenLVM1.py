def examenLVM1():
    #Definir variables
    exacono=float
    entreper=float
    testpsico=float
    a=float
    b=float
    c=float
    e=float
    mensaje=str
    #Datos de entrada 
    exacono=float(input("ingresar la nota del examen de conocimiento"))
    entreper=float(input("ingresar la nota de la entrevista personal"))
    testpsico=float(input("ingresar la nota del test psicologico"))
    #Proceso
    a=exacono*0.40
    b=entreper*0.35
    c=testpsico*0.25
    e=a+b+c
    if e>=17:
        mensaje=("su nivel es 4")
    elif e<17 and e>=14:
        mensaje=("su nivel es 3")
    elif e<14 and e>=11:
        mensaje=("su nivel es 2")
    else:
        mensaje=("no tiene vacante y es nivel 1")
    #Datos de salida
    print(mensaje)
def examenLVM2():
    #Definir variable
    descuento=float
    montopagar=float
    precio=float
    preciofin=float
    IGV=float 
    #Datos de entrada
    precio=float(input("ingrese el porecio"))
    #Proceso
    if precio>2000:
        descuento=precio*0.10
    elif precio<2000 and precio>=1000:
        descuento=precio*0.05
    elif precio>=500 and precio<1000:
        descuento=precio*0.02
    else:
        descuento=precio*0
    preciofin=precio-descuento
    IGV=preciofin*0.18
    montopagar=preciofin+IGV
    #Datos de salida
    print(f"el precio final es: {montopagar}")
    print(f"el IGV es: {IGV}")
    print(f"el descuento es: {descuento}")
def examenLVM3():
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
    print(f"RESULTADO :{total}")
def examenLVM4():
    #Definir variables
    años=float
    genero=str
    mensaje=str
    #Datos de entrada
    años=float(input("ingrese los años:"))
    print("genero:mujer;varon")
    genero=str(input("ingrese los tipos de generos"))    
    #Proceso
    if años>70:
        mensaje=("la vacuna es de tipo c")
    elif años>16 and años<=69 and genero=="mujer":
        mensaje=("la vacuna es de tipo b")
    elif años>16 and años<=69 and genero=="varon":  
        mesaje=("la vacuna es de tipo a") 
    else:
        mesaje=("la vacuna es de tipo a")
    #Datos de salida
    print(mensaje)
#PreguntaLVM5
#Definir variable
numero=float
#Datos de entrada
numero=float(input("ingrese el numero de la pregunta:"))
#Proceso
if numero==1:
    examenLVM1()
elif numero==2:
    examenLVM2()
elif numero==3:
    examenLVM3()
else :
    examenLVM4()
#Datos de salida
print("Gracias por el examen profe y por su paciencia <3")