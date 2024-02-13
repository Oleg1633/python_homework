#Задача 2.
#Вводится количество минут до урока и расстояние в километрах.
#Какая должна быть средняя скорость,чтобы успеть на урок?
minute=input("введите количество минут")
distance=input("введите расстояние в километрах")
minute_lesson=int(minute)
distance_lesson=int(distance)
minute_lesson_h=minute_lesson/60
av_speed=distance_lesson/minute_lesson_h
print ("Средняя скорость", av_speed, "км/ч" )