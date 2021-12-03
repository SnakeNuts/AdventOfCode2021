true_bit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open("day3_1.txt") as data:
    for data_line in data.readlines():
        bit_index = 0
        for bit in data_line:
            if bit == "1":
                true_bit_count[bit_index] += 1
            bit_index += 1
    print(true_bit_count)

    gamma_bits = "0b"
    epsilon_bits = "0b"
    for count in true_bit_count:
        if count > 500:
            gamma_bits = gamma_bits + "1"
            epsilon_bits = epsilon_bits + "0"
        else:
            gamma_bits = gamma_bits + "0"
            epsilon_bits = epsilon_bits + "1"

    print(gamma_bits)
    print(epsilon_bits)

    gamma = int(gamma_bits, 2)
    epsilon = int(epsilon_bits, 2)

    print(gamma)
    print(epsilon)

    print(gamma * epsilon)