import os, sys, inspect

# Pour inclure les fichiers de l'environnement, plot et stat
cmd_subfolder_grid = os.path.realpath(
    os.path.abspath(os.path.join(os.path.split(inspect.getfile(inspect.currentframe()))[0], "Grid")))
if cmd_subfolder_grid not in sys.path:
    sys.path.insert(0, cmd_subfolder_grid)

from envBuilder import *
from grid import Grid
import time
import random
from generator import Generator


def init_maze_task():

    # Load the environment called "maze"
    __ENVIRONMENT__ = "maze"

    # Print the GUI
    __GUI__ = True

    # Instanciation des builders
    envbuilder = EnvBuilder(__ENVIRONMENT__)
    gui, map, agents = envbuilder.build()

    # Creation de la grille
    env = Grid(gui, map, agents, __GUI__, __ENVIRONMENT__)

    return agents, env


'''
Actions
-------
0 - avancer
1 - toucher
2 - rotation gauche
3 - rotation droite
'''

def main():

    # Generate a new maze of size 9
    '''
    g = Generator(9)
    g.generate()
    g.save()
    '''

    agents, env = init_maze_task()
    
    i = 0
    result = 0

    while result != 3:
        result = env.step(agents[0], random.randint(0, 3))
    print("Salade trouvée !")
    while result != 0:
        result = env.step(agents[0], random.randint(0, 3))
    print("Position initiale trouvée !")
    print(env.getNbActions())
    while True:
        pass


if __name__ == '__main__':
    main()
