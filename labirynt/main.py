import labGen

height = int(input('wprowadź wysokość labiryntu (jeśli parzysta dodam 1): '))
if height % 2 == 0:
    height = height+1
if height < 3:
    height = 3
width = int(input('wprowadź szerokość labiryntu (jeśli parzysta dodam 1): '))
if width % 2 == 0:
    width = width+1
if width < 3:
    width = 3

maze = labGen.generate_maze(width, height)
labGen.print_maze(maze)






