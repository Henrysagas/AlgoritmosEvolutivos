import pandas as pd
#Sagastegui Balta Henry Arturo
#Datos en Pandas
datos = {
'Estudiante':["Ana","Luis","Maria","Juan","Carla"],
'Horas_usadas':[3,5,2,4,1]
}
df = pd.DataFrame(datos)

#Diccionario
df['Costo_total']=df["Horas_usadas"]*2

#costo total por estudiante
print(df.head())

#Estadisticas
estadisticias = df['Costo_total'].describe()

#Estudiantes con costo total mayor a 6
filtros= df[df['Costo_total']>6.0]

print ("\nEl gasto promedio fue de",estadisticias['mean'] ,"soles; los estudiantes que gastaron más de 6.00 son:")
print(filtros)
