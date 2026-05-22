import math


def get_player_pos():
    while True:
        coordinates_str = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates_list = coordinates_str.split(",")
        if len(coordinates_list) != 3:
            print("Invalid syntax")
            continue
        try:
            coords = []
            for x in coordinates_list:
                coords.append(float(x))
            return (coords[0], coords[1], coords[2])
        except ValueError as e:
            print(f"Error on parameter '{x}': {e}")
            continue

def main() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    first_tuple = get_player_pos()
    print(f"Got a first tuple: {first_tuple}")
    x1 = first_tuple[0]
    y1 = first_tuple[1]
    z1 = first_tuple[2]
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist_center = math.sqrt((0-x1)**2 + (0-y1)**2 + (0-z1)**2)
    print(f"Distance to center: {round(dist_center, 4)}\n")

    print("Get a second set of coordinates")
    second_tuple = get_player_pos()
    print(f"Got a second tuple: {second_tuple}")
    x2 = second_tuple[0]
    y2 = second_tuple[1]
    z2 = second_tuple[2]
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist, 4)}")


if __name__ == "__main__":
    main()