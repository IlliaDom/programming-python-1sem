import math

name, surname, group = "Yaroslav", "Korolchuk", "IT-31"
L, W, H = 4.2, 3.5, 2.7
DOOR_W, DOOR_H = 0.9, 2.0
WIN_W, WIN_H = 1.4, 1.5
TILE = 0.3
PRICE = 42.30

print(f"{name} {surname}, {group}")
floor = L * W
walls = 2 * (L + W) * H - DOOR_W * DOOR_H - WIN_W * WIN_H
floor_diag = math.hypot(L, W)
room_diag = math.dist((0, 0, 0), (L, W, H))
tiles_exact = floor / (TILE * TILE)
tiles_buy = math.ceil(tiles_exact * 1.1)
paint = walls * 2 / 10
cans = math.ceil(paint / 2.5)

cost_mul = tiles_buy * PRICE
cost_sum = 0
for _ in range(tiles_buy):
    cost_sum += PRICE

print(f"room:          {L} x {W} x {H} m")
print(f"floor area:    {floor:.2f} m2")
print(f"wall area:     {walls:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")
print()
print(f"tiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")
print(f"tiles to buy:  {tiles_buy} (+10% spare)")
print(f"paint:         {paint:.2f} l -> {cans} cans of 2.5 l")
print()
print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")