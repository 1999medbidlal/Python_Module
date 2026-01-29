import math


def calcule_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return d


def parsing_invalid_coordinates(coordinate):
    s = coordinate.split(",")
    coords = []
    try:
        for cord in s:
            coords += [int(cord)]
        return tuple(coords)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args:("{e}",)')


def info_coordinate_system():
    print("=== Game Coordinate System ===")
    p0 = (0, 0, 0)
    p1 = (10, 20, 5)
    p2 = "3,4,0"
    p3 = "abc,def,ghi"
    print(f"\nPosition created: {p1}")
    d = calcule_distance(p0, p1)
    print(f"Distance between {p0} and {p1}: {d:.2f}")
    print('\nParsing coordinates: "3,4,0"')
    position = parsing_invalid_coordinates(p2)
    print(f"Parsed position: {position}")
    d1 = calcule_distance(p0, position)
    print(f"Distance between {p0} and {position}: {d1:.1f}")
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    parsing_invalid_coordinates(p3)
    print("\nUnpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


info_coordinate_system()
