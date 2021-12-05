from typing import List


def process_ratings(rating_list: List[str], bit_position: int, keep_most: bool) -> str:
    true_list = []
    false_list = []
    for rating in rating_list:
        if rating[bit_position] == '1':
            true_list.append(rating)
        else:
            false_list.append(rating)

    # end condition:
    if len(true_list) + len(false_list) == 1:
        if len(true_list) > 0:
            return true_list[0]
        else:
            return false_list[0]

    if keep_most:
        if len(true_list) == len(false_list):
            return process_ratings(true_list, bit_position+1, keep_most)
        if len(false_list) > len(true_list):
            return process_ratings(false_list, bit_position+1, keep_most)
        else:
            return process_ratings(true_list, bit_position+1, keep_most)
    else:
        if len(true_list) == len(false_list):
            return process_ratings(false_list, bit_position+1, keep_most)
        if len(true_list) > len(false_list):
            return process_ratings(false_list, bit_position+1, keep_most)
        else:
            return process_ratings(true_list, bit_position+1, keep_most)


if __name__ == "__main__":
    with open("day3.txt") as data:
        ratings = data.readlines()
        oxygen_rating_binary = process_ratings(ratings, 0, True)
        co2_rating_binary = process_ratings(ratings, 0, False)

        print(oxygen_rating_binary)
        print(co2_rating_binary)

        oxygen_rating = int(f"0b{oxygen_rating_binary}", 2)
        co2_rating = int(f"0b{co2_rating_binary}", 2)

        print(oxygen_rating)
        print(co2_rating)

        print(oxygen_rating * co2_rating)
