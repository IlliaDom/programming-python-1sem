import math
from turtle import window_height

name = "Bohdana"
surname = "Tsykhovych"
group = "IT-32"

length = 4.5
width = 3.0
height = 2.5

door_length = 2.0
door_width = 0.9
window_length = 1.5
window_width = 1.2

tile_side = 0.5
tile_price = 42.32

print(f"Студент: {name} {surname}, група: {group}")

floor_area = length * width
wall_area = 2 * (length + width) * height
wall_area -= door_width * door_length
wall_area -= window_width * window_length

floor_diagonal = math.hypot(length, width)
room_diagonal = math.dist((0, 0, 0), (length, width, height))

tiles_exact = floor_area / (tile_side ** 2)
tiles_rounded = round(tiles_exact)
tiles_floor = math.floor(tiles_exact)
tiles_ceil = math.ceil(tiles_exact)
tiles_buy = math.ceil(tiles_exact * 1.1)

paint = wall_area * 2 / 10
paint_cans = math.ceil(paint / 2.5)

cost_multiplication = tiles_buy * tile_price
cost_addition = 0

for _ in range(tiles_buy):
    cost_addition += tile_price

print(f"Площа підлоги: {floor_area:.2f} м²")
print(f"Площа стін без дверей і вікна: {wall_area:.2f} м²")
print(f"Діагональ підлоги: {floor_diagonal:.2f} м")
print(f"Діагональ кімнати: {room_diagonal:.2f} м")
print(f"Точна кількість плиток: {tiles_exact:.2f}")
print(f"Округлена кількість плиток (round): {tiles_rounded}")
print(f"Округлена кількість плиток (math.floor): {tiles_floor}")
print(f"Округлена кількість плиток (math.ceil): {tiles_ceil}")
print(f"Кількість плиток з запасом 10%: {tiles_buy}")
print(f"Кількість фарби (банки по 2.5 л): {paint_cans}")
print(f"Вартість плитки (множення): {cost_multiplication:.2f} грн")
print(f"Вартість плитки (додавання): {cost_addition:.2f} грн")
print(f"Порівняння через ==: {cost_multiplication == cost_addition}")
print(f"Порівняння через math.isclose: {math.isclose(cost_multiplication, cost_addition)}")
print(f"Різниця: {abs(cost_multiplication - cost_addition):.2f} грн")