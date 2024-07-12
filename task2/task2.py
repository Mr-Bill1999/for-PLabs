import math
import argparse


def read_circle_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        circle_x, circle_y = map(float, lines[0].split())
        radius = float(lines[1])
    return circle_x, circle_y, radius


def read_points_data(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def point_position(x, y, circle_x, circle_y, radius):
    d = math.sqrt((circle_x - x) ** 2 + (circle_y - y) ** 2)
    if d < radius:
        return 1
    elif d == radius:
        return 0
    else:
        return 2


def main(circle_file_path, points_file_path):
    circle_x, circle_y, radius = read_circle_data(circle_file_path)
    points = read_points_data(points_file_path)

    for point in points:
        print(point_position(*point, circle_x, circle_y, radius))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check point positions relative to a circle.')
    parser.add_argument('circle_file_path', type=str)
    parser.add_argument('points_file_path', type=str)
    print('to use write in console: python task2.py path/to/circle.txt path/to/points.txt')
    args = parser.parse_args()

    main(args.circle_file_path, args.points_file_path)




