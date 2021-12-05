from collections import defaultdict

if __name__ == "__main__":
    with open("day5.txt") as data:

        sea_floor = defaultdict(int)

        for vents in data:
            (from_vent, to_vent) = vents.split(" -> ")
            (x1_str, y1_str) = from_vent.split(",")
            (x2_str, y2_str) = to_vent.split(",")

            x1 = int(x1_str)
            y1 = int(y1_str)

            x2 = int(x2_str)
            y2 = int(y2_str)

            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2+1):
                        sea_floor[(x1, y)] += 1
                elif y2 < y1:
                    for y in range(y2, y1+1):
                        sea_floor[(x1, y)] += 1
                else:
                    print("trouble")

            elif y1 == y2:
                if x1 < x2:
                    for x in range(x1, x2+1):
                        sea_floor[(x, y1)] += 1
                elif x2 < x1:
                    for x in range(x2, x1+1):
                        sea_floor[(x, y1)] += 1
                else:
                    print("uh-oh")
            else:
                x_direction = 0
                y_direction = 0

                if x1 < x2:
                    x_direction = 1
                else:
                    x_direction = -1

                if y1 < y2:
                    y_direction = 1
                else:
                    y_direction = -1

                y = y1
                for x in range(x1, x2+x_direction, x_direction):
                    sea_floor[(x, y)] += 1
                    y += y_direction


        print(len(sea_floor))

        cross_count = 0

        for vent_value in sea_floor.values():
            if vent_value > 1:
                cross_count += 1

        print(cross_count)
