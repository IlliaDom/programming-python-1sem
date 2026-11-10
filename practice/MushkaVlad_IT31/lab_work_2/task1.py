print("Mushka Vlad IT31")
import math

NAME = "Vlad Mushka"
GROUP = "IT31"

ROOM_LENGTH = 4.5
ROOM_WIDTH = 3.5
ROOM_HEIGHT = 2.7

DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0

WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

TILE_LENGTH = 0.30
TILE_WIDTH = 0.30
TILE_PRICE = 42.30

floor_area = ROOM_LENGTH * ROOM_WIDTH
wall_area = 2 * (ROOM_LENGTH + ROOM_WIDTH) * ROOM_HEIGHT
wall_area -= DOOR_WIDTH * DOOR_HEIGHT + WINDOW_WIDTH * WINDOW_HEIGHT

floor_diagonal = math.hypot(ROOM_LENGTH, ROOM_WIDTH)
room_diagonal = math.dist(
    (0, 0, 0),
    (ROOM_LENGTH, ROOM_WIDTH, ROOM_HEIGHT)
)

tile_area = TILE_LENGTH * TILE_WIDTH
tiles_exact = floor_area / tile_area

tiles_to_buy = math.ceil(tiles_exact * 1.10)

paint_liters = wall_area / 10 * 2
paint_cans = math.ceil(paint_liters / 2.5)

cost_mul = tiles_to_buy * TILE_PRICE

cost_sum = 0
for i in range(tiles_to_buy):
    cost_sum += TILE_PRICE

print(f"{NAME}, {GROUP}")
print(f"room:          {ROOM_LENGTH} x {ROOM_WIDTH} x {ROOM_HEIGHT} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diagonal:.2f} m")
print(f"room diag:     {room_diagonal:.2f} m")
print()

print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")
print(f"paint:         {paint_liters:.2f} l -> {paint_cans} cans of 2.5 l")
print()

print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")