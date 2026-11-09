import math
import sys

# Персональні дані
print("Батура Каріна Віталіївна, ІТ-31")

# Константи кімнати, дверей, вікна та плитки
ROOM_L, ROOM_W, ROOM_H = 4.2, 3.5, 2.7
DOOR_W, DOOR_H = 0.9, 2.0
WINDOW_W, WINDOW_H = 1.4, 1.5
TILE_SIZE = 0.3 
TILE_PRICE = 42.30

# 1. Площі
floor_area = ROOM_L * ROOM_W
perimeter = 2 * (ROOM_L + ROOM_W)
walls_total_area = perimeter * ROOM_H
door_area = DOOR_W * DOOR_H
window_area = WINDOW_W * WINDOW_H
wall_area_net = walls_total_area - door_area - window_area

# 2. Діагоналі
floor_diag = math.hypot(ROOM_L, ROOM_W)
room_diag = math.dist((0, 0, 0), (ROOM_L, ROOM_W, ROOM_H))

# 3. Плитка
tile_area = TILE_SIZE * TILE_SIZE
tiles_exact = floor_area / tile_area
tiles_round = round(tiles_exact)
tiles_floor = math.floor(tiles_exact)
tiles_ceil = math.ceil(tiles_exact)

# Купуємо з запасом 10% (цілими плитками)
tiles_to_buy = math.ceil(tiles_exact * 1.1)

# 4. Фарба: 1 л на 10 м² за один шар, шарів два. Банки по 2.5 л.
paint_liters = (wall_area_net * 2) / 10
paint_cans = math.ceil(paint_liters / 2.5)

# 5. Вартість плитки 
cost_mul = tiles_to_buy * TILE_PRICE
cost_sum = sum(TILE_PRICE for _ in range(tiles_to_buy))

is_equal = (cost_sum == cost_mul)
close = math.isclose(cost_sum, cost_mul)
diff = abs(cost_sum - cost_mul)

# Вивід результатів
print(f"room:          {ROOM_L} x {ROOM_W} x {ROOM_H} m")
print(f"floor area:    {floor_area:.2f} m2")
print(
    f"wall area:     {wall_area_net:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m\n")

print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {tiles_round}")
print(f"  floor:       {tiles_floor}")
print(f"  ceil:        {tiles_ceil}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")
print(
    f"paint:         {paint_liters:.2f} l -> {paint_cans} cans of 2.5 l\n")

print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {is_equal}")
print(f"isclose:       {close}")
print(f"difference:    {diff}")