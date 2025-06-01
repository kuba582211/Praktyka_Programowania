import time;
import random;

def create_grid(rows,cols,rand):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            if rand == True:row.append(random.choice([0,1]))
            else:row.append(0)
        grid.append(row)
    return grid

def display_grid(grid):
    print("\n")
    for row in grid:
        for cell in row:
            if cell == 1:
                print("O",end=" ")
            else:
                print("",end=" ")
        print("")

def count_neighbors(grid,x,y):
    neighbors = [(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
    rows = len(grid)
    cols = len(grid[0])
    count = 0;
    for dx, dy in neighbors:
        nx = dx + x
        ny = dy + y
        if 0<=nx<rows and 0<=ny<cols and grid[nx][ny]==1:
            count +=1
    return count

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = create_grid(rows,cols,False) 

    for x in range(rows):
        for y in range(cols):
            live_neighbors = count_neighbors(grid,x,y)
            if grid[x][y]==1 and 2<=live_neighbors<=3:
                new_grid[x][y]=1;
            elif grid[x][y]==0 and live_neighbors==3:
                new_grid[x][y]=1
    return new_grid

def game_of_life(rows=10,cols=10,generations=10,delay=1):
    grid = create_grid(rows,cols,True)
    for i in range(generations):
        display_grid(grid)
        grid = next_generation(grid)
        time.sleep(delay)

game_of_life()
