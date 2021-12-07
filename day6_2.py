fish_by_age = {0: 0,
               1: 0,
               2: 0,
               3: 0,
               4: 0,
               5: 0,
               6: 0,
               7: 0,
               8: 0}

with open("day6.txt") as data:
    starting_fish = map(int, data.readline().split(','))
    for fish in starting_fish:
        fish_by_age[fish] += 1

    print(fish_by_age)

    for t in range(1, 256):
        next_day = {0: fish_by_age[1], 1: fish_by_age[2], 2: fish_by_age[3], 3: fish_by_age[4], 4: fish_by_age[5],
                    5: fish_by_age[6], 6: fish_by_age[7] + fish_by_age[0], 7: fish_by_age[8], 8: fish_by_age[0]}

        total_fish = (next_day[0] * 2) + next_day[1] + next_day[2] + next_day[3] + next_day[4] + next_day[5] + next_day[6] + next_day[7] + next_day[8]

        print(total_fish)

        fish_by_age[0] = next_day[0]
        fish_by_age[1] = next_day[1]
        fish_by_age[2] = next_day[2]
        fish_by_age[3] = next_day[3]
        fish_by_age[4] = next_day[4]
        fish_by_age[5] = next_day[5]
        fish_by_age[6] = next_day[6]
        fish_by_age[7] = next_day[7]
        fish_by_age[8] = next_day[8]


