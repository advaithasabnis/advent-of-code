from .shared import Board, parse_text


def find_loser(draws, boards):
    new = boards.copy()
    drawn = set()
    for n in draws:
        drawn.add(n)
        valid_boards = new.copy()
        new = []
        for board in valid_boards:
            for line in board.rows + board.cols:
                if line <= drawn:
                    break
            else:
                new.append(board)
        if len(new) == 0:
            return valid_boards[0], drawn, n


def main(text):
    draws, boards = parse_text(text)
    winning_board, drawn, last_draw = find_loser(draws, boards)
    return winning_board.final_score(drawn, last_draw)


_input = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
 """.strip()
assert main(_input) == 1924
