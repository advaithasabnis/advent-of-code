from .shared import TransparentPaper


def main(text):
    paper = TransparentPaper(text)
    paper.execute_instructions()
    X, Y = map(max, zip(*paper.grid))
    for y in range(Y + 1):
        print(*[' #'[(x, y) in paper.grid] for x in range(X + 1)])
