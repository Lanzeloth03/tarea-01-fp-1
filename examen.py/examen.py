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