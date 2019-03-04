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
    f= f.read().split('\n')#infile now a list of lines
    for i in range(len(f)):
        if f[i]== "line": # adds a line to edge matrix
            pars= f[i+1] #parameters for line
            splt= pars.split(' ') #pars in a list now
            x0=int(splt[0])
            y0=int(splt[1])
            z0=int(splt[2])
            x1=int(splt[3])
            y1=int(splt[4])
            z1=int(splt[5])
            add_edge(points,x0,y0,z0,x1,y1,z1)
        elif f[i]== "ident": #transform to identity
            ident(transform)
        elif f[i]== "scale": #transform * scale matrix
            pars= f[i+1]
            splt=pars.split(' ')
            sx=int(splt[0])
            sy=int(splt[1])
            sz=int(splt[2])
            scale= make_scale(sx,sy,sz)
            matrix_mult(scale,points)
        elif f[i]== "translate":
            pars= f[i+1]
            splt=pars.split(' ')
            tx=int(splt[0])
            ty=int(splt[1])
            tz=int(splt[2])
            trans= make_translate(tx,ty,tz)
            matrix_mult(trans,points)
        elif f[i]== "rotate":
            pars= f[i+1]
            splt=pars.split(' ')
            axis=splt[0]
            theta = int(splt[1])
            theta= math.radians(theta)
            if axis== "x":
                rotate= make_rotX(theta)
                matrix_mult(rotate,points)
            elif axis== "y":
                rotate= make_rotY(theta)
                matrix_mult(rotate,points)
            else:
                rotate= make_rotZ(theta)
                matrix_mult(rotate,points)
        elif f[i]== "apply":
            matrix_mult(transform,points)
        elif f[i]== "display":
            clear_screen(screen)
            draw_lines(points,screen,color)
            display(screen)
        elif f[i]== "save":
            clear_screen(screen)
            draw_lines(points,screen,color)
            fname= f[i+1]
            save_extension(screen,fname)
        elif f[i]== "quit":
            break
