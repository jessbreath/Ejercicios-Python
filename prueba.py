print ("Se va calcular la cantidad de segundos que estan incluidos en el número de hroas,minutos y segundos ingresados por el usuario:")
print("Escribe las horas")
horas=input()
horas=int(horas)
print("Escribe los minutos")
minutos=input()
minutos=int(minutos)
print("Escribe los segundos")
segundos=input()
segundos=int(segundos)

horasSeg=horas*3600
minutosSeg=minutos*60

sumaDeto=horasSeg+minutosSeg+segundos

print("Elequivalente de horas, minutos, segundos son de el total de segundos:")
print("Horas: ", horasSeg)
print("Minutos: ",minutosSeg)
print("Segundos: ", segundos)
print("La suma de Horas+Minutos+Segundos: ", sumaDeto)



input('Press ENTER to exit')
