import sdl2
from OpenGL.GL import *
from OpenGL.GLU import *
import time
import math
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def interpola(init, final, prog):
    return init*(1-prog)+(final*prog)

def loopCor(i):
    while i>7:
        i-=7
    glColor(cores[max(0,i)])

def base(n,r,y):
    glBegin(GL_TRIANGLES)
    ang = interpola(0,math.pi*2,0)
    x0 = math.cos(ang)*r
    z0 = math.sin(ang)*r
    for i in range(1,n-1):
        ang = interpola(0,math.pi*2,i/n)
        nextAng = interpola(0,math.pi*2,(i+1)/n)
        x1 = math.cos(ang)*r
        z1 = math.sin(ang)*r
        x2 = math.cos(nextAng)*r
        z2 = math.sin(nextAng)*r
        loopCor(i)
        glVertex(x0,y,z0)
        loopCor(i+1)
        glVertex(x1,y,z1)
        loopCor(i+2)
        glVertex(x2,y,z2)
    glEnd()

def paredes(n,r,h):
    for i in range(n):
        ang = interpola(0,math.pi*2,i/n)
        nextAng = interpola(0,math.pi*2,(i+1)/n)
        x1 = math.cos(ang)*r
        z1 = math.sin(ang)*r
        x2 = math.cos(nextAng)*r
        z2 = math.sin(nextAng)*r
        glBegin(GL_TRIANGLE_STRIP)
        loopCor(i)
        glVertex(x1,h/2,z1)
        loopCor(i+1)
        glVertex(x2,h/2,z2)
        loopCor(i+2)
        glVertex(x1,-h/2,z1)
        loopCor(i+3)
        glVertex(x2,-h/2,z2)
        glEnd()

def prisma(n,r,h):
    base(n,r,-h/2)
    base(n,r,h/2)
    paredes(n,r,h)

def cone(n,r,h):
    for i in range(n):
        ang = interpola(0,math.pi*2,i/n)
        nextAng = interpola(0,math.pi*2,(i+1)/n)
        x1 = math.cos(ang)*r
        z1 = math.sin(ang)*r
        x2 = math.cos(nextAng)*r
        z2 = math.sin(nextAng)*r
        glBegin(GL_TRIANGLES)
        loopCor(i)
        glVertex(0,h/2,0)
        loopCor(i+1)
        glVertex(x1,-h/2,z1)
        loopCor(i+2)
        glVertex(x2,-h/2,z2)
        glEnd()

def piramide(n,r,h):
    base(n,r,-h/2)
    cone(n,r,h)

a = 0

def desenhaPiramidePrisma(n,r,h):
    # Piramide da Esquerda
    glPushMatrix()
    glTranslatef(-5,0,0)
    glRotatef(a,0,1,0)
    glRotatef(a,0,0,1)
    piramide(n,r,h)
    glPopMatrix()
    # Prisma da Direita
    glPushMatrix()
    glTranslatef(5,0,0)
    glRotatef(-a,1,0,0)
    glRotatef(-a,0,1,0)
    prisma(n,r,h)
    glPopMatrix()


def desenha():
    global a
    global frameTime
    global lastTime
    frameTime = (time.time()-lastTime)
    frameTime=max(frameTime,0.001)
    frameTime=min(frameTime,1)
    lastTime = time.time()
    print("\033[H\033[J"+"%s fps"%str(1/frameTime))
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glTranslatef(0,-5,0)
    desenhaPiramidePrisma(5,2,3)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(0,5,0)
    desenhaPiramidePrisma(5,2,3)
    glPopMatrix()
    a+=60*frameTime

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

sdl2.SDL_Init(sdl2.SDL_INIT_EVERYTHING)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MAJOR_VERSION, 2)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_MINOR_VERSION, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_CONTEXT_PROFILE_MASK,sdl2.SDL_GL_CONTEXT_PROFILE_CORE)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DOUBLEBUFFER, 1)
sdl2.SDL_GL_SetAttribute(sdl2.SDL_GL_DEPTH_SIZE, 24)
sdl2.SDL_GL_SetSwapInterval(1)
window = sdl2.SDL_CreateWindow(b"Prisma e piramide", sdl2.SDL_WINDOWPOS_CENTERED, sdl2.SDL_WINDOWPOS_CENTERED, WINDOW_WIDTH, WINDOW_HEIGHT, sdl2.SDL_WINDOW_OPENGL | sdl2.SDL_WINDOW_SHOWN)
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
lastTime = time.time()
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

