class Lanternfish:

    all_fish = []

    def __init__(self, start_value, fresh_fish=False):
        self.timer = start_value
        self.fresh_fish = fresh_fish

    def tick(self):
        if self.fresh_fish:
            self.fresh_fish = False
            return

        if self.timer == 0:
            self.timer = 6

            spawn = Lanternfish(8, True)

            Lanternfish.all_fish.append(spawn)

            return

        self.timer -= 1

    def __str__(self):
        return str(self.timer)


if __name__ == "__main__":
    with open("day6.txt") as data:
        list_of_fish = data.readline().split(',')
        for fish in list_of_fish:
            initial_fish = Lanternfish(int(fish))
            Lanternfish.all_fish.append(initial_fish)

    print(",".join([str(fish) for fish in Lanternfish.all_fish]))

    for t in range(0, 80):
        for fish in Lanternfish.all_fish:
            fish.tick()
        print(f"{t}: {len(Lanternfish.all_fish)}")
