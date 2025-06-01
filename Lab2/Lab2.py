import time
import random
import os

def create_grid(rows, cols, random_fill=True):
    """Tworzy siatkę o zadanych wymiarach, opcjonalnie losowo wypełnioną."""
    return [[random.choice([0, 1]) if random_fill else 0 for _ in range(cols)] for _ in range(rows)]

def display_grid(grid):
    """Wyświetla siatkę w konsoli."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Czyści ekran konsoli
    for row in grid:
        print(" ".join("O" if cell else "." for cell in row))

def count_neighbors(grid, x, y):
    """Zlicza żywych sąsiadów komórki (x, y)."""
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny]:
            count += 1
    return count

def next_generation(grid):
    """Oblicza następną generację siatki."""
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1 and live_neighbors in [2, 3]:
                new_grid[x][y] = 1
            elif grid[x][y] == 0 and live_neighbors == 3:
                new_grid[x][y] = 1
    return new_grid

def game_of_life(rows=20, cols=20, generations=100, delay=1):
    """Uruchamia grę w życie."""
    grid = create_grid(rows, cols)
    for _ in range(generations):
        display_grid(grid)
        grid = next_generation(grid)
        time.sleep(delay)

if __name__ == "__main__":
    game_of_life()