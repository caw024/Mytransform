from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )

edges = []
transform = new_matrix()

parse_file( 'myscript', edges, transform, screen, color )
