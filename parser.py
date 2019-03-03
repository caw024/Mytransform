from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname,'r')
    #list of things
    lines = f.read().split('\n')
    size = len(lines)-1
    curr = 0
    while curr <= size:
        if lines[curr] == 'line':
            args = lines[curr+1].split(' ')
            argint = [int(x) for x in args]
            add_edge(points,argint[0],argint[1],argint[2],argint[3],argint[4],argint[5])
            curr += 2
        elif lines[curr] == 'ident':
            ident(transform)
            curr+=1
        elif lines[curr] == 'scale':
            args = lines[curr+1].split(' ')
            argint = [int(x) for x in args]
            smatrix = make_scale(argint[0],argint[1],argint[2])
            matrix_mult(smatrix,transform)
            curr += 2
        elif lines[curr] == 'translate':
            args = lines[curr+1].split(' ')
            argint = [int(x) for x in args]
            tmatrix = make_translate(argint[0],argint[1],argint[2])
            matrix_mult(tmatrix,transform)
            curr += 2
        elif lines[curr] == 'rotate':
            args = lines[curr+1].split(' ')
            if args[0] == 'x':
                rmatrix = make_rotX( int(args[1]) )
            elif args[0] == 'y':
                rmatrix = make_rotY( int(args[1]) )
            elif args[0] == 'z':
                rmatrix = make_rotZ( int(args[1]) )
            matrix_mult(rmatrix,transform)
            curr += 2
        elif lines[curr] == 'apply':
            matrix_mult(transform,points)
            curr+=1
        elif lines[curr] == 'display':
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
            curr+=1
        elif lines[curr] == 'save':
            clear_screen(screen)
            draw_lines(points,screen,color)
            save_extension(screen,lines[curr+1])
            curr+=2
        elif lines[curr] == 'quit':
            f.close()
            curr = size+1
        else:
            curr+=1
    f.close()
