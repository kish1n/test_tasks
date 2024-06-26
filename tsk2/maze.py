import argparse
import random
from collections import deque

class Maze:
    def __init__(self, width, height):
        if width % 2 == 0 or height % 2 == 0:
            raise ValueError("Width and height must be odd numbers")

        self.width = width
        self.height = height
        self.maze = [['#'] * width for _ in range(height)]
        self.entrance = None
        self.exit = None
        self.visited = set()
        self.treasure = None
        self.traps = []
        self._generate_maze(1, 1)
        self.create_entrance_and_exit()
        self.place_treasure()
        self.place_traps()
        self.ensure_valid_path()

    def _generate_maze(self, x, y):
        self.maze[y][x] = ' '
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < self.width and 0 < ny < self.height and self.maze[ny][nx] == '#':
                self.maze[ny][nx] = ' '
                self.maze[y + dy // 2][x + dx // 2] = ' '
                self._generate_maze(nx, ny)

    def create_entrance_and_exit(self):
        entrance_x = random.choice(range(1, self.width, 2))
        self.entrance = (0, entrance_x)
        self.maze[0][entrance_x] = 'E'

        exit_x = random.choice(range(1, self.width, 2))
        self.exit = (self.height - 1, exit_x)
        self.maze[self.height - 1][exit_x] = 'X'

    def is_valid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height and self.maze[y][x] == ' '

    def create_road(self, x1, y1, x2, y2):
        self.visited.clear()
        stack = [(x1, y1)]
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]

        while stack:
            x, y = stack[-1]
            self.visited.add((x, y))

            if (x, y) == (x2, y2):
                break

            random.shuffle(directions)
            moved = False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if self.is_valid(nx, ny) and (nx, ny) not in self.visited:
                    stack.append((nx, ny))
                    self.maze[ny][nx] = ' '
                    self.maze[y + dy // 2][x + dx // 2] = ' '
                    moved = True
                    break

            if not moved:
                stack.pop()

    def bfs_find_path(self, start, end):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([start])
        parent = {start: None}

        while queue:
            x, y = queue.popleft()
            if (x, y) == end:
                path = []
                while (x, y) is not None:
                    path.append((x, y))
                    x, y = parent[(x, y)]
                return path[::-1]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (0 <= nx < self.width and 0 <= ny < self.height and (nx, ny) not in parent and self.maze[ny][nx] in (' ', '3', 'T')):
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

        return None

    def count_traps_on_path(self, path):
        return sum(1 for x, y in path if self.maze[y][x] == 'T')

    def place_treasure(self):
        if random.choice([True, False]):
            while True:
                tx, ty = random.randint(1, self.width - 2), random.randint(1, self.height - 2)
                if self.maze[ty][tx] == ' ':
                    self.maze[ty][tx] = '3'
                    self.treasure = (ty, tx)
                    break

    def place_traps(self):
        trap_count = random.randint(0, 5)
        placed_traps = 0

        while placed_traps < trap_count:
            tx, ty = random.randint(1, self.width - 2), random.randint(1, self.height - 2)
            if self.maze[ty][tx] == ' ':
                self.maze[ty][tx] = 'T'
                self.traps.append((ty, tx))
                placed_traps += 1

    def ensure_valid_path(self):
        path = self.bfs_find_path(self.entrance, self.exit)
        if path and self.count_traps_on_path(path) > 2:
            self.remove_excess_traps_from_path(path)
        elif not path:
            self.create_road(self.entrance[1], self.entrance[0], self.exit[1], self.exit[0])

    def remove_excess_traps_from_path(self, path):
        trap_positions = [(x, y) for x, y in path if self.maze[y][x] == 'T']
        excess_traps = len(trap_positions) - 2

        for i in range(excess_traps):
            tx, ty = trap_positions[i]
            self.maze[ty][tx] = ' '

    def display(self):
        for row in self.maze:
            print(''.join(row))


def main():
    parser = argparse.ArgumentParser(description='Generate a maze with specified dimensions.')
    parser.add_argument('width', type=int, help='Width of the maze (must be an odd number)')
    parser.add_argument('height', type=int, help='Height of the maze (must be an odd number)')
    args = parser.parse_args()

    try:
        maze = Maze(args.width, args.height)
        maze.display()
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()