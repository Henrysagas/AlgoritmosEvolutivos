import numpy as np


#Sagastegui Balta Henry Arturo
#presupuesto
presupuesto = 10

#precios
precios = np.array([2.5,3.0,1.75,2.20])

#Cafes en base a precio y presupuesto
max_cafes = np.floor(presupuesto/precios)

#Metodo para definir cafeteria en base a nombre
def nombre(i):
    if i==0:
        return "A"
    elif i==1:
        return "B"
    elif i==2:
        return "C"
    else:
        return "D"


for i,precio in enumerate(precios):
    print("Se pueden comprar", int(max_cafes[i]), "Cafes con un precio de", precios[i]  )


print("\nCon S/", presupuesto,"puedo comprar como maximo ", int(max_cafes.max())," cafés en la cafeteria" , nombre(int(max_cafes.argmax())),
      "(precio minimo S/",precios.min(),")\n")

print("Con S/", presupuesto,"puedo comprar como minimo ", int(max_cafes.min())," cafés en la cafeteria" , nombre(int(max_cafes.argmin())),
      "(precio maximo S/",precios.max(),")")

