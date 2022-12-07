import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import math

vertices = (
    ( 1, -1,-1),
    (-1, -1,-1),
    ( 1, -1, 1),
    (-1, -1, 1),
    (0, 0.5, 0),
    )



#cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
def interpola(init, final, prog):
    return init*(1-prog)+(final*prog)

def circulo(n,r,x):
    for i in range(n):
        ang = interpola(0,math.pi*2,i/n)
        y = math.cos(ang)*r
        z = math.sin(ang)*r
        glPushMatrix()
        glBegin(GL_POINTS)
        glVertex(x,y,z)
        glEnd()
        glPopMatrix()

def esfera(n,r):
    for i in range(n):
        ang = interpola(-math.pi/2,math.pi/2,i/n)
        x = math.cos(ang)*r
        y = math.sin(ang)*r
        circulo(n,x,y)

def desenha():
    global frameTime
    global lastTime
    global a
    frameTime = (time.time()-lastTime)
    lastTime = time.time()
    a+=1
    print("%s fps"%(1/frameTime))
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a,0,1,0)
    esfera(50,5)
    glPopMatrix()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Esfera", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
if not window:
    sys.stderr.write("Error: Could not create window\n")
    exit(1)
glcontext = sdl2.SDL_GL_CreateContext(window)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,100.0)
glTranslatef(0.0,0.0,-20)

running = True
event = sdl2.SDL_Event()
a = 0
lastTime = 0
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

