import datetime, bday_messages
"""
#Esta es para saber cuanto falta para tu cumpleaños
today = datetime.date.today()
birthday = datetime.date(2024, 2, 28)
daysAway = birthday - today
#Si hoy es tu cumpleaños imprime un mensaje aleatorio de felicitaciones
if today == birthday:
    print(bday_messages.randomMessage)
#Si no imprime cuantos dias faltan para tu cumpleaños
else:
    print(f"My next birthday is {daysAway} days away!")
    """
today=datetime.date.today()
diaImportante=datetime.date(2024,2,14)
daysPast=today-diaImportante
#Si hoy es el dia importante te dice que hoy es ese dia
if diaImportante==today:
    print("Hoy es ese dia")
#Si no te dice cuantos dias han pasado desde el dia importante
else:
    print(f"El dia importante fue hace {daysPast} dias")