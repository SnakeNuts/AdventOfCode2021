

if __name__ == "__main__":
    flat_data = []
    sliding_groups = {}

    data = open("day1.txt")
    for line in data.readlines():
        value = int(line.strip())
        flat_data.append(value)

    group_index = 0
    for index in range(0, len(flat_data)-2):
        group_sum = flat_data[index] + flat_data[index+1] + flat_data[index+2]
        sliding_groups[group_index] = group_sum
        group_index += 1

    print(len(sliding_groups))

    previous_sum = 0
    increases = 0
    for group_index in range(0, len(sliding_groups)):
        if sliding_groups[group_index] > previous_sum != 0:
            increases += 1
        previous_sum = sliding_groups[group_index]

    print(increases)