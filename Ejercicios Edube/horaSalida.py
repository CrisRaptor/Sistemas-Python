hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

hourEnd = (((hour*60)+mins)+dura)//60%24
minsEnd = (((hour*60)+mins)+dura)%60
print(hourEnd,":",minsEnd,sep = "")
