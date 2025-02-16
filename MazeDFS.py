import matplotlib.pyplot as plt 
import numpy as np  
import random 

def create_maze(dim):
    maze = np.ones((dim * 2 + 1, dim * 2 + 1))

    x, y = (0, 0)
    maze[2 * x + 1, 2 * y + 1] = 0  

    stack = [(x, y)]  

    while stack:
        x, y = stack.pop()  
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        random.shuffle(directions) 
        for dx, dy in directions:
            nx, ny = x + dx, y + dy 
            if 0 <= nx < dim and 0 <= ny < dim and maze[2 * nx + 1, 2 * ny + 1] == 1:
                maze[2 * nx + 1, 2 * ny + 1] = 0  
                maze[2 * x + 1 + dx, 2 * y + 1 + dy] = 0  
                stack.append((x, y))  
                stack.append((nx, ny)) 
                break

    maze[1, 0] = 0  
    maze[-2, -1] = 0 
    return maze

def find_path_dfs(maze):
    """
    Använder depth-first search (DFS) för att hitta en väg från start till mål i labyrinten.
    Args:
        maze (np.array): Labyrinten som en 2D-array där 1:or är väggar och 0:or är vägar.
    Returns:
        list of tuples: En lista av koordinater (tupler) som representerar vägen från start till mål.
    """
    start = (1, 1)
    end = (maze.shape[0] - 2, maze.shape[1] - 2)
    stack = [(start, [start])]  
    visited = set() 

    # DFS 
    while stack:
        (node, path) = stack.pop()  
        if node in visited:
            continue 
        visited.add(node) 

        if node == end:
            return path  

    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            next_node = (node[0] + dx, node[1] + dy)  # Beräkna nästa position
            # Kontrollera att nästa position är inom labyrinten och inte är en vägg
            if 0 <= next_node[0] < maze.shape[0] and 0 <= next_node[1] < maze.shape[1] and maze[next_node] == 0 and next_node not in visited:
                stack.append((next_node, path + [next_node]))  # Lägg till nästa position och uppdaterad path i stacken

def draw_maze(maze, path=None):
    """
    Visualiserar labyrinten och den funna vägen om sådan finns.
    Args:
        maze (np.array): Labyrinten som en 2D-array.
        path (list of tuples, optional): Vägen som hittats genom labyrinten, om någon.
    """
    fig, ax = plt.subplots(figsize=(10, 10))  
    ax.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')  # Visa labyrinten som en bild

    if path:
        x_coords = [x[1] for x in path]  # X-koordinater för path
        y_coords = [y[0] for y in path]  # Y-koordinater för path
        ax.plot(x_coords, y_coords, 'r-', linewidth=2)  # Rita pathen som en röd linje

    ax.text(0.5, 1, 'S', color='green', fontsize=20, ha='center', va='center')  # 'S' för Start
    ax.text(maze.shape[1] - 1.5, maze.shape[0] - 2, 'E', color='blue', fontsize=20, ha='center', va='center')  # 'E' för End

    ax.set_xticks([]) 
    ax.set_yticks([]) 
    plt.show()  

if __name__ == "__main__":
    while True:
        try:
            dim = int(input("Ange dimensionen på labyrinten: "))  
            maze = create_maze(dim) 
            draw_maze(maze)  

            path = find_path_dfs(maze)  
            draw_maze(maze, path)  
            continue_playing = input("Vill du skapa en ny labyrint? Ange 'ja' för att fortsätta eller 'nej' för att stoppa: ")
            if continue_playing.lower() != 'ja':
                break 
        except ValueError:
            print("Felaktig inmatning. Ange ett heltal för dimensionen.")
            continue 




