pedestrian_speed = 4
travel_time = 2
car_time = 10
car_speed_ms = 30

car_speed_kmch = 30*3600/1000
# Рассчитываем пусть от точки А до точки Б
way = car_speed_kmch*car_time
# Рассчитываем время, за которое проходит пешеход
time = way/pedestrian_speed/60 - 2

print('Пешеходу осталось идти', time, 'часа')
