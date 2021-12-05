class Board:
    def __init__(self, data):
        self.board = [list(map(int, line.split())) for line in data.splitlines()]
        self.cols = list(map(set, map(list, zip(*self.board))))
        self.rows = list(map(set, self.board))

    def final_score(self, drawn, last_draw):
        return sum(sum(row - drawn) for row in self.rows) * last_draw


def parse_text(text):
    draws, *board_data = text.split('\n\n')
    draws = list(map(int, draws.split(',')))
    boards = []
    for board in board_data:
        boards.append(Board(board))
    return draws, boards
