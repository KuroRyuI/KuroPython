import random


def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]  # wstaw ścianę

    def create_path(x, y):
        # zaznacz komórkę jako część ścieżki
        maze[y][x] = " "

        # kierunek ruchu (góra, dół, lewo, prawo)
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        # przetasuj
        random.shuffle(directions)

        for dx, dy in directions:
            new_x, new_y = x + dx * 2, y + dy * 2  # nowa współrzędna

            # sprawdź czy nie poza granicą labiryntu i czy jeszcze tam nie byłem
            if 0 <= new_x < width and 0 <= new_y < height and maze[new_y][new_x] == "#":
                # usuń ścianę pomiędzy nową i starą komórką
                maze[y + dy][x + dx] = " "
                # rekurencyjnie twórz ścieżkę
                create_path(new_x, new_y)

    create_path(1, 1)  # Utwórz labirynt zaczynając od komórki (1,1)

    maze[1][0] = 'X' # punkt startowy 'X' drugi rząd pierwsza kolumna

    #DO POPRAWY
    maze[-2][-1] = 'E' # punkt końcowy 'E'

    return maze


def print_maze(maze):
    for row in maze:
        print(' '.join(cell for cell in row))