import math

NAME = "Anastasia"
SURNAME = "Zakharchuk"
GROUP = "IT-32"

ROOM_L = 8.8
ROOM_W = 3.0
ROOM_H = 3.6
DOOR_W, DOOR_H = 0.8, 2.0
WINDOW_W, WINDOW_H = 1.3, 1.4
TILE_SIDE = 0.30
TILE_PRICE = 38.50

SPARE = 1.10
PAINT_PER_M2 = 0.1
LAYERS = 2
CAN_SIZE = 2.5

print(f"{NAME} {SURNAME}, {GROUP}")

floor_area = ROOM_L * ROOM_W
walls_full = 2 * (ROOM_L + ROOM_W) * ROOM_H
wall_area = walls_full - DOOR_W * DOOR_H - WINDOW_W * WINDOW_H

floor_diag = math.hypot(ROOM_L, ROOM_W)
room_diag = math.dist((0, 0, 0), (ROOM_L, ROOM_W, ROOM_H))

tiles_exact = floor_area / (TILE_SIDE * TILE_SIDE)
tiles_to_buy = math.ceil(tiles_exact * SPARE)

paint_l = wall_area * PAINT_PER_M2 * LAYERS
cans = math.ceil(paint_l / CAN_SIZE)

cost_mul = tiles_to_buy * TILE_PRICE
cost_sum = 0.0
for _ in range(tiles_to_buy):
    cost_sum += TILE_PRICE

print(f"room:          {ROOM_L} x {ROOM_W} x {ROOM_H} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")
print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")
print(f"paint:         {paint_l:.2f} l -> {cans} cans of {CAN_SIZE} l")
print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")
#Відповідь на питання до звіту
#round не підходить, бо округлює до найближчого числа.
# Для плиток і банок треба завжди вгору, інакше не вистачить матеріалу.
