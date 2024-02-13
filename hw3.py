#Задача 3. 
#Вводится ширина, длина и высота комнаты.
#Рулон обоев 10 метров при ширине 0.5
#Сколько рулонов надо купить?
length=input("введите длину комнаты")
width=input("введите ширину комнаты")
height=input("введите высоту комнаты")
Hroll=10
Wroll=0,5

length_room=int(length)
width_room=int(width)
height_room=int(height)



Number_rolls=(length_room*2+width_room*2)*height_room/10*0,5

print ("Количество рулонов", Number_rolls, "шт" )