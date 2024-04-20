import matplotlib.pyplot as plt  # Importera matplotlib.pyplot för att skapa visualiseringar
import numpy as np  # Importera numpy för att få stöd för stora, flerdimensionella matriser och arrayer
import random  # Importera random för att generera slumpmässiga tal

def create_maze(dim):
    """
    Skapar en labyrint genom att använda en depth-first search (DFS) algoritm.
    Args:
        dim (int): Dimensionen på labyrinten som anger hur stor den ska vara.
    Returns:
        np.array: En 2D-array som representerar labyrinten där 1:or är väggar och 0:or är öppna vägar.
    """
    # Initiera en kvadratisk labyrint med alla celler som väggar (representerade av ettor)
    maze = np.ones((dim * 2 + 1, dim * 2 + 1))

    # Startpunkt i labyrinten
    x, y = (0, 0)
    maze[2 * x + 1, 2 * y + 1] = 0  # Öppnar startcellen

    stack = [(x, y)]  # Stack för att hålla reda på positioner för DFS

    # Använder DFS för att generera labyrinten
    while stack:
        x, y = stack.pop()  # Hämta senaste positionen från stacken
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Möjliga rörelseriktningar
        random.shuffle(directions)  # Blanda riktningarna för att skapa en mer slumpmässig labyrint

        # Prova alla riktningar från nuvarande position
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # Beräkna nästa position
            # Kontrollera att nästa position är inom gränserna och att det är en vägg
            if 0 <= nx < dim and 0 <= ny < dim and maze[2 * nx + 1, 2 * ny + 1] == 1:
                maze[2 * nx + 1, 2 * ny + 1] = 0  # Öppna nästa cell
                maze[2 * x + 1 + dx, 2 * y + 1 + dy] = 0  # Öppna cellen mellan nuvarande och nästa
                stack.append((x, y))  # Lägg tillbaka nuvarande position i stacken för backtracking
                stack.append((nx, ny))  # Lägg till nästa position i stacken
                break

    # Skapa en ingång och en utgång
    maze[1, 0] = 0  # Ingång i övre vänstra hörnet
    maze[-2, -1] = 0  # Utgång i nedre högra hörnet
    return maze

def find_path_dfs(maze):
    """
    Använder depth-first search (DFS) för att hitta en väg från start till mål i labyrinten.
    Args:
        maze (np.array): Labyrinten som en 2D-array där 1:or är väggar och 0:or är vägar.
    Returns:
        list of tuples: En lista av koordinater (tupler) som representerar vägen från start till mål.
    """
    # Start- och slutpunkter för vägsökningen
    start = (1, 1)
    end = (maze.shape[0] - 2, maze.shape[1] - 2)
    stack = [(start, [start])]  # Stack för att hålla reda på vägsökningspath och positioner
    visited = set()  # Set för att hålla reda på besökta positioner

    # DFS för att hitta en väg genom labyrinten
    while stack:
        (node, path) = stack.pop()  # Ta fram den senaste positionen och path
        if node in visited:
            continue  # Hoppa över om noden redan är besökt
        visited.add(node)  # Markera noden som besökt

        if node == end:
            return path  # Returnera path om slutpunkten är nådd

        # Prova alla möjliga riktningar från nuvarande position
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
    fig, ax = plt.subplots(figsize=(10, 10))  # Skapa en figur och axel för visualisering
    ax.imshow(maze, cmap=plt.cm.binary, interpolation='nearest')  # Visa labyrinten som en bild

    # Om en path finns, rita ut den
    if path:
        x_coords = [x[1] for x in path]  # X-koordinater för path
        y_coords = [y[0] for y in path]  # Y-koordinater för path
        ax.plot(x_coords, y_coords, 'r-', linewidth=2)  # Rita pathen som en röd linje

    # Markera start och slut med text
    ax.text(0.5, 1, 'S', color='green', fontsize=20, ha='center', va='center')  # 'S' för Start
    ax.text(maze.shape[1] - 1.5, maze.shape[0] - 2, 'E', color='blue', fontsize=20, ha='center', va='center')  # 'E' för End

    ax.set_xticks([])  # Ta bort x-axelns markeringar
    ax.set_yticks([])  # Ta bort y-axelns markeringar
    plt.show()  # Visa visualiseringen

if __name__ == "__main__":
    while True:
        try:
            dim = int(input("Ange dimensionen på labyrinten: "))  # Få dimensionen av labyrinten från användaren
            maze = create_maze(dim)  # Skapa labyrinten med angiven dimension
            draw_maze(maze)  # Rita labyrinten med vägen

            path = find_path_dfs(maze)  # Hitta en väg genom labyrinten
            draw_maze(maze, path)  # Rita labyrinten med vägen

            # Fråga användaren om de vill skapa en ny labyrint
            continue_playing = input("Vill du skapa en ny labyrint? Ange 'ja' för att fortsätta eller 'nej' för att stoppa: ")
            if continue_playing.lower() != 'ja':
                break  # Avbryt loopen om användaren inte anger 'ja'
        except ValueError:
            print("Felaktig inmatning. Ange ett heltal för dimensionen.")
            continue  # Fortsätt loopen, och be användaren mata in igen






"""

import matplotlib.pyplot as plt: Importera matplotlib.pyplot för att använda dess funktioner för att skapa visualiseringar.
import numpy as np: Importera numpy för att använda dess stöd för stora, flerdimensionella matriser och arrayer.
import random: Importera random för att kunna generera slumpmässiga tal.
def create_maze(dim):: Definiera en funktion create_maze som skapar en labyrint med en given dimension genom att använda en depth-first search (DFS) algoritm.
maze = np.ones((dim * 2 + 1, dim * 2 + 1)): Skapa en kvadratisk labyrint med alla celler som väggar (representerade av ettor).
x, y = (0, 0): Ange startpunkten i labyrinten.
maze[2 * x + 1, 2 * y + 1] = 0: Öppna startcellen i labyrinten.
stack = [(x, y)]: Skapa en stack för att hålla reda på positioner för DFS.
while stack:: Utför DFS för att generera labyrinten.
if path:: Kontrollera om en väg (path) har hittats i labyrinten.
ax.text(0.5, 1, 'S', color='green', fontsize=20, ha='center', va='center'): Placera en större textmarkör 'S' för startpunkt i labyrinten.
ax.text(maze.shape[1] - 1.5, maze.shape[0] - 2, 'E', color='blue', fontsize=20, ha='center', va='center'): Placera en större textmarkör 'E' för slutpunkt i labyrinten.
while True:: Skapa en oändlig loop för att kontinuerligt skapa nya labyrinter.
dim = int(input("Ange dimensionen på labyrinten: ")): Fråga användaren efter dimensionen på labyrinten.
except ValueError:: Hantera undantaget om användaren matar in något som inte är ett heltal för dimensionen.
print("Felaktig inmatning. Ange ett heltal för dimensionen."): Meddela användaren om felaktig inmatning av dimensionen.
continue_playing = input("Vill du skapa en ny labyrint? Ange 'ja' för att fortsätta eller 'nej' för att stoppa: "): Fråga användaren om de vill skapa en ny labyrint eller avsluta programmet.


"""