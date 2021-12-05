from time import perf_counter


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def update(self, binary_string, idx=0):
        if idx < len(binary_string):
            if binary_string[idx] == '0':
                if self.left is None:
                    self.left = Node(0)
                self.left.data += 1
                idx += 1
                self.left.update(binary_string, idx)
            elif binary_string[idx] == '1':
                if self.right is None:
                    self.right = Node(0)
                self.right.data += 1
                idx += 1
                self.right.update(binary_string, idx)

    def print_tree(self):
        print(self.data)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def traverse_oxy(self, path=''):
        if self.left and self.right:
            if self.left.data > self.right.data:
                path += '0'
                return self.left.traverse_oxy(path)
            else:
                path += '1'
                return self.right.traverse_oxy(path)
        elif self.left:
            path += '0'
            return self.left.traverse_oxy(path)
        elif self.right:
            path += '1'
            return self.right.traverse_oxy(path)
        else:
            return path

    def traverse_co2(self, path=''):
        if self.left and self.right:
            if self.left.data <= self.right.data:
                path += '0'
                return self.left.traverse_co2(path)
            else:
                path += '1'
                return self.right.traverse_co2(path)
        elif self.left:
            path += '0'
            return self.left.traverse_co2(path)
        elif self.right:
            path += '1'
            return self.right.traverse_co2(path)
        else:
            return path

    def life_support(self):
        oxygen_rating = self.traverse_oxy()
        co2_rating = self.traverse_co2()
        return int(oxygen_rating, 2) * int(co2_rating, 2)


def main(text):
    tree = Node('')
    ti = perf_counter()
    for line in text.splitlines():
        tree.update(line)
    tf = perf_counter()
    print(f'Time 2 : {(tf - ti)*1000:.3f}ms')
    return tree.life_support()


_input = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()
assert main(_input) == 230
