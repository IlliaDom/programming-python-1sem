import math
import sys

NAME_SURNAME = "Oleksandra Romanich"
GROUP = "IT-32"

L, W, H = 4.2, 3.5, 2.7  
DOOR_W, DOOR_H = 0.9, 2.0
WIN_W, WIN_H = 1.4, 1.5
TILE_W, TILE_H = 0.3, 0.3
TILE_PRICE = 42.30
PAINT_LAYERS = 2
PAINT_CONSUMPTION = 10  
PAINT_CAN_VOL = 2.5

def main():
    print(f"{NAME_SURNAME}, {GROUP}")
    print(f"room:          {L} x {W} x {H} m")

    floor_area = L * W
    wall_area = 2 * (L + W) * H - (DOOR_W * DOOR_H) - (WIN_W * WIN_H)
    floor_diag = math.hypot(L, W)
    room_diag = math.dist((0, 0, 0), (L, W, H))

    print(f"floor area:    {floor_area:.2f} m2")
    print(f"wall area:     {wall_area:.2f} m2 (without door and window)")
    print(f"floor diag:    {floor_diag:.2f} m")
    print(f"room diag:     {room_diag:.2f} m")
    print()

    tile_area = TILE_W * TILE_H
    tiles_exact = floor_area / tile_area

    print(f"tiles exact:   {tiles_exact:.2f}")
    print(f"  round:       {round(tiles_exact)}")
    print(f"  floor:       {math.floor(tiles_exact)}")
    print(f"  ceil:        {math.ceil(tiles_exact)}")

    tiles_to_buy = math.ceil(tiles_exact * 1.10)
    print(f"tiles to buy:  {tiles_to_buy} (+10% spare)")

    paint_liters = (wall_area / PAINT_CONSUMPTION) * PAINT_LAYERS
    paint_cans = math.ceil(paint_liters / PAINT_CAN_VOL)
    print(f"paint:         {paint_liters:.2f} l -> {paint_cans} cans of {PAINT_CAN_VOL} l")
    print()

    tiles_cost_mul = tiles_to_buy * TILE_PRICE
    tiles_cost_sum = 0.0
    for _ in range(tiles_to_buy):
        tiles_cost_sum += TILE_PRICE

    print(f"tiles cost:    {tiles_cost_mul:.2f} UAH")
    print(f"sum == mul:    {tiles_cost_sum == tiles_cost_mul}")
    print(f"isclose:       {math.isclose(tiles_cost_sum, tiles_cost_mul)}")
    print(f"difference:    {abs(tiles_cost_sum - tiles_cost_mul)}")

if __name__ == "__main__":
    main()