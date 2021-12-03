

if __name__ == "__main__":
    depth = 0
    larger_count = 0

    data = open("day1_1.txt")
    for line in data.readlines():
        value = int(line.strip())
        if value > depth != 0:
            larger_count += 1
        depth = value
    print(larger_count)