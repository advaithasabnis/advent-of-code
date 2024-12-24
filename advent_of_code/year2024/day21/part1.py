from advent_of_code.year2024.day21.shared import find_shortest_paths, shortest_seq


def main(text: str, num_intermediate_robots: int = 2) -> int:
    complexity = 0
    num_paths = find_shortest_paths('numpad')

    for _input in text.splitlines():
        # The arm of the robot is intially on 'A'
        code = 'A' + _input  # e.g. from '029A' to 'A029A'

        # For each pair of keys, find the length of the shortest path
        final_len = 0
        for i in range(len(code) - 1):
            src, target = code[i], code[i + 1]
            # Get all shortest paths between two keys
            paths = num_paths[src][target]
            # Find the length of the shortest path and add it to the total length
            l = min(shortest_seq(path + 'A', num_intermediate_robots) for path in paths)
            final_len += l

        # The puzzle's "complexity" measure
        num_value = int(_input.strip('A'))  # e.g. '029A' -> '029' -> int(29)
        complexity += final_len * num_value

    return complexity


_input = """
029A
980A
179A
456A
379A
""".strip()

assert main(_input) == 126384
