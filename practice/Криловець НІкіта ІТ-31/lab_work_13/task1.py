import math

name = "Nikita"
surname = "Krilovets"
group = "IT-31"

LENGTH = 4.5
WIDTH = 3.5
HEIGHT = 2.7

DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.0

WINDOW_WIDTH = 1.4
WINDOW_HEIGHT = 1.5

TILE_WIDTH = 0.3
TILE_HEIGHT = 0.3
TILE_PRICE = 42.30


print(f"{name} {surname}, {group}")
print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")

floor_area = LENGTH * WIDTH
wall_area = 2 * (LENGTH + WIDTH) * HEIGHT - DOOR_WIDTH * DOOR_HEIGHT - WINDOW_WIDTH * WINDOW_HEIGHT

floor_diagonal = math.hypot(LENGTH, WIDTH)
room_diagonal = math.dist((0, 0, 0), (LENGTH, WIDTH, HEIGHT))

tiles_exact = floor_area / (TILE_WIDTH * TILE_HEIGHT)

tiles_round = round(tiles_exact)
tiles_floor = math.floor(tiles_exact)
tiles_ceil = math.ceil(tiles_exact)

tiles_to_buy = math.ceil(tiles_exact * 1.1)

paint_liters = wall_area * 2 / 10
paint_cans = math.ceil(paint_liters / 2.5)

tiles_cost_mul = tiles_to_buy * TILE_PRICE

tiles_cost_sum = 0
for _ in range(tiles_to_buy):
    tiles_cost_sum += TILE_PRICE

print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2")
print(f"floor diag:    {floor_diagonal:.2f} m")
print(f"room diag:     {room_diagonal:.2f} m")

print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {tiles_round}")
print(f"  floor:       {tiles_floor}")
print(f"  ceil:        {tiles_ceil}")
print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")

print(f"paint:         {paint_liters:.2f} l -> {paint_cans} cans of 2.5 l")

print(f"tiles cost:    {tiles_cost_mul:.2f} UAH")
print(f"sum == mul:    {tiles_cost_sum == tiles_cost_mul}")
print(f"isclose:       {math.isclose(tiles_cost_sum, tiles_cost_mul)}")
print(f"difference:    {abs(tiles_cost_sum - tiles_cost_mul)}")