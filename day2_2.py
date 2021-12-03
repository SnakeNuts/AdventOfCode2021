with open("day2_1.txt") as data:
    horizontal_pos = 0
    depth = 0
    aim = 0
    for command_line in data.readlines():
        command = command_line.strip().split(" ")
        if command[0] == "forward":
            horizontal_pos += int(command[1])
            depth += (aim * int(command[1]))
        elif command[0] == "down":
            # depth += int(command[1])
            aim += int(command[1])
        elif command[0] == "up":
            # depth -= int(command[1])
            aim -= int(command[1])
        else:
            print("error!")
            exit(-1)
    result = horizontal_pos * depth
    print(result)
