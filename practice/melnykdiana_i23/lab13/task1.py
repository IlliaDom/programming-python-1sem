
import math
import sys

name = "Diana"
surname = "Melnyk"
group = "I-23"

ROOM_LENGTH = 3.0
ROOM_WIDTH = 4.0
ROOM_HEIGHT = 2.5

DOOR_WIDTH = 1.0
DOOR_HEIGHT = 1.8

WINDOW_WIDTH = 1.280
WINDOW_HEIGHT = 1.350

TILE_WIDTH = 0.15
TILE_HEIGHT = 0.15
TILE_PRICE = 289

floor_area = ROOM_LENGTH * ROOM_WIDTH
wall_area = 2 * (ROOM_LENGTH + ROOM_WIDTH) * ROOM_HEIGHT
door_area = DOOR_WIDTH * DOOR_HEIGHT
window_area = WINDOW_WIDTH * WINDOW_HEIGHT
paint_area = wall_area - door_area - window_area

floor_diagonal = math.hypot(ROOM_LENGTH, ROOM_WIDTH)
room_diagonal = math.dist(
    (0, 0, 0),
    (ROOM_LENGTH, ROOM_WIDTH, ROOM_HEIGHT)
)

tile_area = TILE_WIDTH * TILE_HEIGHT
exact_tiles = floor_area / tile_area
tiles_without_spare = math.ceil(exact_tiles)
tiles_with_spare = math.ceil(exact_tiles * 1.10)

paint_liters = paint_area / 10 * 2
paint_cans = math.ceil(paint_liters / 2.5)

cost_multiplication = tiles_with_spare * TILE_PRICE

cost_addition = 0
for _ in range(tiles_with_spare):
    cost_addition += TILE_PRICE

print(f"{name} {surname}, група {group}")
print("\n=== РОЗРАХУНОК РЕМОНТУ КІМНАТИ ===")
print(f"Площа підлоги: {floor_area:.2f} м²")
print(f"Площа стін: {wall_area:.2f} м²")
print(f"Площа дверей: {door_area:.2f} м²")
print(f"Площа вікна: {window_area:.2f} м²")
print(f"Площа для фарбування: {paint_area:.2f} м²")
print(f"Діагональ підлоги: {floor_diagonal:.2f} м")
print(f"Просторова діагональ кімнати: {room_diagonal:.2f} м")

print("\n=== ПЛИТКА ===")
print(f"Точна кількість плиток: {exact_tiles:.2f}")
print(f"Без запасу: {tiles_without_spare}")
print(f"З запасом 10%: {tiles_with_spare}")
print(f"Вартість множенням: {cost_multiplication} грн")
print(f"Вартість додаванням: {cost_addition} грн")
print(f"Результати рівні: {cost_multiplication == cost_addition}")
print(f"Результати близькі: {math.isclose(cost_multiplication, cost_addition)}")
print(f"Різниця: {abs(cost_multiplication - cost_addition)} грн")

print("\n=== ФАРБА ===")
print(f"Потрібно фарби: {paint_liters:.2f} л")
print(f"Банок по 2,5 л: {paint_cans}")
