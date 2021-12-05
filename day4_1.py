from typing import TextIO, Dict, Optional, Tuple, List


class Bingo_card:
    def __init__(self, numbers: Dict[Tuple[int, int], int]):
        self.numbers = numbers
        self.marked: Dict[Tuple[int, int], int] = dict()

        for x in range(0, 5):
            for y in range(0, 5):
                self.marked[(x, y)] = False

    def mark(self, number: int) -> Optional[int]:
        # shortcut: if number not in the card, don't bother marking or checking

        found_coordinate = None

        if number in self.numbers.values():
            for coordinate in self.numbers.keys():
                if self.numbers[coordinate] == number:
                    self.marked[coordinate] = 1
                    found_coordinate = coordinate

            # check row/column
            x = found_coordinate[0]
            y = found_coordinate[1]
            row_sum = self.marked[x, 0] + self.marked[x, 1] + self.marked[x, 2] + self.marked[x, 3] + self.marked[x, 4]
            col_sum = self.marked[0, y] + self.marked[1, y] + self.marked[2, y] + self.marked[3, y] + self.marked[4, y]

            if row_sum == 5 or col_sum == 5:
                # BINGO!
                unmarked_sum = 0
                for coordinate in self.numbers.keys():
                    if self.marked[coordinate] == 0:
                        unmarked_sum += self.numbers[coordinate]

                return unmarked_sum * number

        else:
            return None


def read_bingo_card(input_file: TextIO) -> Optional[Dict[Tuple[int, int], int]]:
    x: int = 0
    y: int = 0
    result: Dict[Tuple[int, int], int] = dict()

    # read empty line (or fail at end of file)
    try:
        input_file.readline()

        for y in range(0, 5):
            card_line = input_file.readline().strip().split()
            for x in range(0, 5):
                result[(x, y)] = int(card_line[x])

        return result

    except:
        return None


if __name__ == "__main__":
    with open("day4.txt") as data:
        bingo_calls = data.readline().split(",")
        bingo_cards: List[Bingo_card] = list()
        while True:
            bingo_card = read_bingo_card(data)
            if bingo_card is None:
                break
            bingo_cards.append(Bingo_card(bingo_card))

        for call in bingo_calls:
            call_int = int(call)
            for bingo_card in bingo_cards:
                result = bingo_card.mark(call_int)
                if result is not None:
                    print(result)
                    exit()
