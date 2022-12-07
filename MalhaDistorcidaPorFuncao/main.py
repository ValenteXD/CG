import math
import sys
import time

import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *

def f(x,y):
  return x**2+y**2
def g(x,y):
  return x**2-y**2
def h(x,y):
    return x**2*y**3
def t(x,y):
    return(x+y)

cor=((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(0.5,0,0),(0,0.5,0),(0,0,0.5))
def Paraboloide(nx,ny,xo,yo,xf,yf):
    dx = (xf-xo)/nx
    dy = (yf-yo)/ny
    c=0
    counter = 0
    vertTable = [None]*nx*ny
    for i in range(0,nx):
        for j in range(0,ny):
            x = xo+i*dx
            y = yo+j*dy
            z = g(x,y)
            vertTable[counter]=(x, y, z)
            counter+=1
    counter = 0
    for i in range(0,nx-1):
        glBegin(GL_TRIANGLE_STRIP)
        for j in range(0,ny):
            glVertex3fv(vertTable[counter])
            glVertex3fv(vertTable[counter+ny])
            counter+=1
            glColor3fv(cor[c])
            if(c==8):
                c=0
            else:
                c+=1
        glEnd()

ar = 0
lastTime = 0

def desenha():
    global ar
    global lastTime
    frameTime=time.time()-lastTime
    lastTime=time.time()
    frameTime=max(frameTime,0.001)
    frameTime=min(frameTime,1)
    print("\033[H\033[J"+"%s fps"%str(1/frameTime))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    #glTranslatef(0,-1,0)
    glRotatef(ar, 0, 1, 1)
    Paraboloide(25,25,-1,1,1,-1)
    glPopMatrix()
    ar += 60*frameTime


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK, sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Paraboloide", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH,
                               WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)

running = True
event = sdl2.SDL_Event()
while running:
    while sdl2.SDL_PollEvent(ctypes.byref(event)) != 0:
        if event.type == sdl2.SDL_QUIT:
            running = False
        if event.type == sdl2.events.SDL_KEYDOWN:
            print("SDL_KEYDOWN")
            if event.key.keysym.sym == sdl2.SDLK_ESCAPE:
                running = False
    desenha()
    sdl2.SDL_GL_SwapWindow(window)
