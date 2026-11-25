import math

NAME, SURNAME, GROUP = "Sofiia", "Zakharchuk", "IT-32"

# TODO: свої виміри (м)
ROOM_L, ROOM_W, ROOM_H = 4.0, 3.2, 2.6
DOOR_W, DOOR_H = 0.9, 2.0
WIN_W, WIN_H = 1.4, 1.5
TILE_SIDE = 0.30          # м
TILE_PRICE = 42.30        # грн
SPARE = 0.10
PAINT_PER_M2 = 1 / 10     # л на м2 за шар
COATS = 2
CAN = 2.5                 # л

print(f"{NAME} {SURNAME}, {GROUP}")

floor = ROOM_L * ROOM_W
walls = 2 * (ROOM_L + ROOM_W) * ROOM_H - DOOR_W * DOOR_H - WIN_W * WIN_H
floor_diag = math.hypot(ROOM_L, ROOM_W)
room_diag = math.dist((0, 0, 0), (ROOM_L, ROOM_W, ROOM_H))

tiles = floor / TILE_SIDE ** 2
to_buy = math.ceil(tiles * (1 + SPARE))

paint = walls * PAINT_PER_M2 * COATS
cans = math.ceil(paint / CAN)

cost_mul = to_buy * TILE_PRICE
cost_sum = 0.0
for _ in range(to_buy):
    cost_sum += TILE_PRICE

print(f"room:          {ROOM_L} x {ROOM_W} x {ROOM_H} m")
print(f"floor area:    {floor:.2f} m2")
print(f"wall area:     {walls:.2f} m2 (without door and window)")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")
print()
print(f"tiles exact:   {tiles:.2f}")
print(f"  round:       {round(tiles)}")
print(f"  floor:       {math.floor(tiles)}")
print(f"  ceil:        {math.ceil(tiles)}")
print(f"tiles to buy:  {to_buy} (+{SPARE:.0%} spare)")
print(f"paint:         {paint:.2f} l -> {cans} cans of {CAN} l")
print()
print(f"tiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")
