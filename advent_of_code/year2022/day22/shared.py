import re
from collections import defaultdict
from math import sqrt


Pose = tuple[complex, complex]
Step = tuple[complex, int]


def parse_input(text: str) -> tuple[set[complex], set[complex], list[Step]]:
    puzzle, instructions = text.split("\n\n")

    # Patternt to parse the steps
    # R is added in the beginning to make the first step a right turn
    pattern = re.compile(r'([RL])(\d+)')
    instructions = 'R' + instructions

    steps: list[tuple[complex, int]] = []
    for p in pattern.finditer(instructions):
        steps.append((1j if p.group(1) == 'R' else -1j, int(p.group(2))))

    # Parse the puzzle, store all grid points in `bounds` and all walls in `walls`
    bounds = set()
    walls = set()
    rows = puzzle.split('\n')
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char == '#':
                bounds.add(complex(x, y))
                walls.add(complex(x, y))
            elif char == '.':
                bounds.add(complex(x, y))

    return bounds, walls, steps


def neighbors(pos: complex) -> list[complex]:
    return [pos + 1, pos - 1, pos + 1j, pos - 1j]


def diag_neighbors(pos: complex) -> list[complex]:
    return [pos + 1 + 1j, pos - 1 + 1j, pos + 1 - 1j, pos - 1 - 1j]


class Net:
    """
    Net represents a 2D pattern that can be folded into a cube.
    """

    def __init__(self, bounds: set[complex], is_cube: bool = True):
        self.bounds = bounds
        self.face_length = int(sqrt(len(bounds) / 6))
        # Find the starting position (leftmost point in top row)
        self.start_pos = min((x for x in self.bounds if x.imag == 0), key=lambda x: x.real)

        # Start with pointing up because we added 'R' to the instructions in parse_input
        self.start_direction = complex(0, -1)

        # Generate wrap map
        self.wrap_map: dict[Pose, Pose] = dict()
        if is_cube:
            self.generate_cube_wrap_map()
        else:
            self.generate_2d_wrap_map()

    def is_interior_corner(self, pos: complex) -> bool:
        """Checks if the given position is an interior corner of the 2D pattern."""
        # A point is an interior corner if it is on the board,
        # all its neighbors are on the board, and at least one of its diagonal neighbors is not on the board.
        if (
            pos in self.bounds
            and all(neighbor in self.bounds for neighbor in neighbors(pos))
            and any(neighbor not in self.bounds for neighbor in diag_neighbors(pos))
        ):
            return True
        else:
            return False

    def interior_corner_vector(self, interior_corner: complex):
        """Computes the outward pointing vector from the given interior corner."""
        for d in [1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j]:
            if interior_corner + d not in self.bounds:
                return d

    def is_exterior_corner(self, pos: complex) -> bool:
        """Checks if the given position is an exterior corner of the 2D pattern."""
        if sum(neighbor in self.bounds for neighbor in neighbors(pos)) == 2:
            return True
        else:
            return False

    # Move one step from the given position in the given direction along the perimeter.
    # If next pos is out of bounds, then it is an exterior corner, and we need to round the corner.
    # If next pos is an interior corner, then we need to turn in the correct direction.
    def perimeter_step(self, pos: complex, direction: complex) -> Pose:
        """
        Calculates the next position and direction along the perimeter of the 2D pattern.
        """

        next_pos = pos + direction

        # If next_pos is out of bounds, then it is an exterior corner
        if next_pos not in self.bounds:
            # Find the valid direction to turn in (either left or right of the current direction)
            directionL = direction * -1j
            next_posL = pos + directionL

            directionR = direction * 1j
            next_posR = pos + directionR

            # Keep the current coordinates, and just change the direction
            if next_posL in self.bounds:
                return pos, directionL

            if next_posR in self.bounds:
                return pos, directionR

        # If next_pos is an interior corner,
        # the outward pointing vector of the interior corner is added to the current direction.
        elif self.is_interior_corner(next_pos):
            corner_vector = self.interior_corner_vector(next_pos)
            return next_pos, direction + corner_vector

        return next_pos, direction

    # Generates part of the mapping of points on the outer edges of the shape to the corresponding
    # points on the cube starting from an interior corner.
    def zip_up(self, pos: complex, vector: complex):
        """
        Updates the wrap map starting from an interior corner.

        Parameters
        ----------
        pos : complex
            The starting position of the interior corner
        vector : complex
            The outward pointing vector of the interior corner
        """
        # Determines which direction is clockwise and anti-clockwise
        # and provides the rotation factor to get the outward normal vector.
        if vector.real == vector.imag:
            rot0, rot1 = 1j, -1j
        else:
            rot0, rot1 = -1j, 1j

        d0, d1 = complex(vector.real, 0), complex(0, vector.imag)
        d0_prev, d1_prev = d0, d1
        pos0, pos1 = pos + d0, pos + d1

        # Terminate the zip process if we round two corners simultaneously
        # since this means we have reached the end of the shape that wraps together.
        while d0_prev == d0 or d1_prev == d1:
            d0_prev, d1_prev = d0, d1
            norm0, norm1 = d0 * rot0, d1 * rot1

            # Add the mappings for the points in both directions
            self.wrap_map[(pos0, norm0)] = (pos1, -norm1)
            self.wrap_map[(pos1, norm1)] = (pos0, -norm0)

            # Move one step in each direction
            pos0, d0 = self.perimeter_step(pos0, d0)
            pos1, d1 = self.perimeter_step(pos1, d1)

    # For 4 out of 11, the zip up process from interior corners does not cover all the edges.
    # This function zips up the remaining edges starting from an interior corner and
    # moving till both directions reach an exterior corner and start zipping up again.
    def zip_up_exterior(self, pos: complex, vector: complex):
        """
        Updates the wrap map by zipping up the remaining edges.

        Parameters
        ----------
        pos : complex
            The starting position of the interior corner
        vector : complex
            The outward pointing vector of the interior corner
        """
        if vector.real == vector.imag:
            rot0, rot1 = 1j, -1j
        else:
            rot0, rot1 = -1j, 1j

        d0, d1 = complex(vector.real, 0), complex(0, vector.imag)
        pos0, pos1 = pos + d0, pos + d1
        norm0, norm1 = d0 * rot0, d1 * rot1

        # Keep moving in each direction until we reach a Pose which does not have a map
        # Interior corners don't have a map, so skip them
        while (pos0, norm0) in self.wrap_map or self.is_interior_corner(pos0):
            pos0, d0 = self.perimeter_step(pos0, d0)
            norm0 = d0 * rot0

        while (pos1, norm1) in self.wrap_map or self.is_interior_corner(pos1):
            pos1, d1 = self.perimeter_step(pos1, d1)
            norm1 = d1 * rot1

        # Keep moving in each direction until we reach a Pose which has a map
        # Zip up the remaining edges
        while (pos0, norm0) not in self.wrap_map and (pos1, norm1) not in self.wrap_map:
            self.wrap_map[(pos0, norm0)] = (pos1, -norm1)
            self.wrap_map[(pos1, norm1)] = (pos0, -norm0)

            pos0, d0 = self.perimeter_step(pos0, d0)
            pos1, d1 = self.perimeter_step(pos1, d1)
            norm0, norm1 = d0 * rot0, d1 * rot1

    # Generates a map connecting points on the outer edges of the board for a cube shape.
    # The process starts by walking along the permimeter of the shape.
    # For every interior corner, the zip up process is performed.
    # For 4 out of 11 nets of a cube, the zip up process from interior corners is not complete.
    # Further zip ups are performed to map remaining edges.
    def generate_cube_wrap_map(self):
        interior_corner = None
        pos, direction = self.perimeter_step(self.start_pos, complex(1, 0))

        # Start updating the map from the start position and move one step along the permimeter
        # Until we return to the start position
        while pos != self.start_pos:
            # If point is an interior corner, perform the zip up operation and update the map
            if self.is_interior_corner(pos):
                self.zip_up(pos, self.interior_corner_vector(pos))

                # Store the first interior corner to perform further zip ups later
                if interior_corner is None:
                    interior_corner = pos

            pos, direction = self.perimeter_step(pos, direction)

        # If wrap map is not complete, perform further zip ups
        # The number of mappings should be equal to the 14 * edge length
        # All nets of a cube always have 14 outer edges, 6 squares or faces
        if len(self.wrap_map) / 14 != self.face_length:
            # One zip up process is always enough to complete the map
            self.zip_up_exterior(interior_corner, self.interior_corner_vector(interior_corner))

    # Generates a map connecting points on the outer edges of the board for a 2D shape.
    # The map is created by finding the leftmost and rightmost points for each row
    # and the topmost and bottommost points for each column.
    # Map connects the leftmost point in a row to the rightmost point in the same row and vice versa.
    # It does the same for the topmost and bottommost points in each column.
    def generate_2d_wrap_map(self):
        wrap_map_col = defaultdict(lambda: {'min_y': float('inf'), 'max_y': float('-inf')})
        wrap_map_row = defaultdict(lambda: {'min_x': float('inf'), 'max_x': float('-inf')})

        for z in self.bounds:
            x, y = z.real, z.imag

            wrap_map_col[x]['min_y'] = min(wrap_map_col[x]['min_y'], y)
            wrap_map_col[x]['max_y'] = max(wrap_map_col[x]['max_y'], y)

            wrap_map_row[y]['min_x'] = min(wrap_map_row[y]['min_x'], x)
            wrap_map_row[y]['max_x'] = max(wrap_map_row[y]['max_x'], x)

        # Combine the two final loops into a single loop
        for col, ends in wrap_map_col.items():
            self.wrap_map[(complex(col, ends['min_y']), -1j)] = (complex(col, ends['max_y']), -1j)
            self.wrap_map[(complex(col, ends['max_y']), 1j)] = (complex(col, ends['min_y']), 1j)

        for row, ends in wrap_map_row.items():
            self.wrap_map[(complex(ends['min_x'], row), -1 + 0j)] = (
                complex(ends['max_x'], row),
                -1 + 0j,
            )
            self.wrap_map[(complex(ends['max_x'], row), 1 + 0j)] = (
                complex(ends['min_x'], row),
                1 + 0j,
            )

    def move(self, pos, direction):
        next_pos = pos + direction
        next_direction = direction

        # If the resulting position is not on the board, wrap no the cube
        if next_pos not in self.bounds:
            next_pos, next_direction = self.wrap_map[(pos, direction)]

        return next_pos, next_direction


def facing(direction: complex) -> int:
    match direction:
        case 1 + 0j:
            return 0
        case 0 + 1j:
            return 1
        case -1 + 0j:
            return 2
        case 0 - 1j:
            return 3
        case _:
            raise ValueError(f"Invalid direction: {direction}")


def password(pos, direction):
    return int(1000 * (pos.imag + 1) + 4 * (pos.real + 1) + facing(direction))
