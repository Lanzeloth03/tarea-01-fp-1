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