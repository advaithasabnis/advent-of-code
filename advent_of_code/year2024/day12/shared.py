from collections import defaultdict, deque


def calculate_score(text: str, part=1) -> int:
    """
    Calculates the sum of perimeters multiplied by the number of edges for orthogonal regions of letters
    in a given map.

    Parameters
    ----------
    text : str
        Multi-line string representing a grid of letters.

    Returns
    -------
    int
        Sum of the calculated region properties for all regions in the grid.
    """

    # Parse input into a grid map
    grid: defaultdict[tuple[int, int], str] = defaultdict(str)
    data = text.splitlines()
    for j, row in enumerate(data):
        for i, plant in enumerate(row):
            grid[(i, j)] = plant

    # Dimensions of the grid
    rows, cols = len(data), len(data[0])

    # Track visited postions
    visited: defaultdict[tuple[int, int], bool] = defaultdict(bool)

    # Orthogonal directions
    directions2D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def form_region(x: int, y: int) -> int:
        """Explores and forms a region around a given position (x, y)."""

        # Skip already visited positions
        if visited[(x, y)]:
            return 0

        # Initialize region
        plant = grid[(x, y)]
        plot_queue = deque([(x, y)])
        visited[(x, y)] = True
        area = 1
        perimeter = 0
        corners = 0

        # BFS to explore the region
        while plot_queue:
            cx, cy = plot_queue.popleft()
            local_perimeter = 4

            # Check neighbors
            for dx, dy in directions2D:
                nx, ny = cx + dx, cy + dy

                # If neighbor is part of the region, reduce perimeter and add it to the queue
                if grid[(nx, ny)] == plant:
                    local_perimeter -= 1
                    if not visited[(nx, ny)]:
                        plot_queue.append((nx, ny))
                        visited[(nx, ny)] = True
                        area += 1

                # Number of edges a region has is the same as the number of corners!
                if part == 2:
                    corners += is_corner(cx, cy, dx, dy, plant)

            perimeter += local_perimeter

        return area * (perimeter if part == 1 else corners)

    def is_corner(x: int, y: int, dx: int, dy: int, plant: str) -> int:
        """
        Check corners formed around (x, y) based on the given direction.
        """
        dx2, dy2 = -dy, dx  # Orthogonal to (dx, dy)
        left = grid[(x + dx, y + dy)]
        right = grid[(x + dx2, y + dy2)]
        mid = grid[(x + dx + dx2, y + dy + dy2)]

        # If outer corner or inner corner return 1
        if (left != plant and right != plant) or (
            left == plant and right == plant and mid != plant
        ):
            return 1
        return 0

    # Compute and return total score
    return sum(form_region(x, y) for y in range(rows) for x in range(cols))
