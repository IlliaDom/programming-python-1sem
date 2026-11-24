import math
room_length = 4
room_width = 3
room_height = 2.5

door_width = 1.2
door_height = 2
door_area = door_width * door_height

windows_width = 2
windows_height = 1.2
windows_area = windows_width * windows_height

floor_area = room_length * room_width
wall_area = 2*(room_width * room_height + room_length * room_height) - (door_area + windows_area)

floor_diag = math.hypot(room_width, room_length)
room_diag = math.hypot(room_width, room_height, room_length)
print("Hordiy Andriy IT-31")
print(f"room: {room_width} x {room_length} x {room_height}m")
print(f"floor area: {floor_area}")
print(f"wall area: {wall_area}")
print(f"floor diag: {floor_diag}")
print(f"room diag: {room_diag}")

tiles_length = 0.30
tiles_width = 0.30
tiles_area = tiles_length * tiles_width
tiles_exact = floor_area / tiles_area

print(f"tiles exact: {tiles_exact}")
print(f"    round: {round(tiles_exact)}")
print(f"    floor: {math.floor(tiles_exact)}")
print(f"    ceil: {math.ceil(tiles_exact)}")
print(f"tiles to buy: {math.ceil(tiles_exact*1.1)}")

paint = wall_area / 10
tin_paint = math.ceil(paint / 2.5)
print(f"paint: {paint}l; {tin_paint} of 2,5l per tin")

tiles_cost1 = math.ceil(tiles_exact*1.1) * 42.3
tiles_cost2 = 0
for i in range(math.ceil(tiles_exact*1.1)):
    tiles_cost2 += 42.3
print(f"tiles cost: {tiles_cost1}")
print(tiles_cost1==tiles_cost2)
print(math.isclose(tiles_cost1, tiles_cost2))
difference = tiles_cost1 - tiles_cost2
print(f"difference: {abs(difference)}")