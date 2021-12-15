from .shared import TransparentPaper


def main(text):
    paper = TransparentPaper(text)
    paper.execute_instructions(1)
    return len(paper.grid)


_input = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip()
assert main(_input) == 17
