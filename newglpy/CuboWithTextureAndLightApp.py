from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math

class CuboWithTextureAndLightApp(GLAPP):

    def setup(self):
        global a
        # Window setup
        self.title("Cube With Texture And Light")
        self.size(800,800)
        self.FPSlimit = 120

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)
        GL.glEnable(GL.GL_CULL_FACE)

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("Phong")#"LightShader")
        GL.glUseProgram(self.pipeline)

        # Texture
        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("./textures/dado.png")
        GL.glUniform1i(GL.glGetUniformLocation(self.pipeline, "textureSlot"),0)

        self.squareArrayBufferId = None
        self.pi = math.pi
        a = self.pi/10

    def drawDado(self):
        global a
        #GL.glCullFace(GL.GL_FRONT)
        if self.squareArrayBufferId == None:
            position = array('f',[
                 1.0,  1.0, 1.0, # C
                -1.0, -1.0, 1.0, # B
                 1.0, -1.0, 1.0, # A

                 1.0,  1.0, 1.0, # C
                -1.0,  1.0, 1.0, # D
                -1.0, -1.0, 1.0, # B

                 1.0,  -1.0, -1.0,# F
                 1.0,  1.0,  1.0, # C
                 1.0, -1.0,  1.0, # A

                 1.0,  -1.0, -1.0,# F
                 1.0,  1.0, -1.0, # E
                 1.0,  1.0,  1.0, # C

                 1.0,  1.0, -1.0, # E
                 1.0,  -1.0, -1.0,# F
                -1.0, -1.0, -1.0, # H                

                 1.0,  1.0, -1.0, # E
                -1.0, -1.0, -1.0, # H
                -1.0,  1.0, -1.0, # G

                -1.0, -1.0, -1.0, # H
                -1.0, -1.0, 1.0,  # B
                -1.0,  1.0, -1.0, # G

                -1.0,  1.0, -1.0, # I
                -1.0, -1.0, 1.0,  # B
                -1.0,  1.0, 1.0,  # D

                 1.0,  1.0,  1.0, # C
                 1.0,  1.0, -1.0, # E
                -1.0,  1.0, -1.0, # G

                 1.0,  1.0,  1.0, # C
                -1.0,  1.0, -1.0, # G
                -1.0,  1.0, 1.0,  # D

                 1.0, -1.0,  1.0, # A
                -1.0, -1.0, 1.0,  # B
                -1.0, -1.0, -1.0, # H

                -1.0, -1.0, -1.0, # H
                 1.0,  -1.0, -1.0,# F
                 1.0, -1.0,  1.0  # A
            ])

            textureCoord = array('f',[
                1/3, 1.0, # C
                0.0, 0.5, # B
                1/3, 0.5, # A
                1/3, 1.0, # C
                0.0, 1.0, # D
                0.0, 0.5, # B

                2/3, 0.5, # F
                1/3, 1.0, # C
                1/3, 0.5, # A
                2/3, 0.5, # F
                2/3, 1.0, # E
                1/3, 1.0, # C
                
                2/3, 0.5, # E
                2/3, 0.0, # F
                1.0, 0.0, # H
                2/3, 0.5, # E
                1.0, 0.0, # H
                1.0, 0.5, # G

                1/3, 0.0, # H
                2/3, 0.0, # B
                1/3, 0.5, # G
                1/3, 0.5, # G
                2/3, 0.0, # B
                2/3, 0.5, # D

                1/3, 0.0, # C
                1/3, 0.5, # E
                0.0, 0.5, # G
                1/3, 0.0, # C
                0.0, 0.5, # G
                0.0, 0.0, # D

                1.0, 0.5, # A
                2/3, 0.5, # B
                2/3, 1.0, # H
                2/3, 1.0, # H
                1.0, 1.0, # F
                1.0, 0.5  # A
            ])
            normal = array('f',[
                1.0,1.0,1.0,#C
                -1.0,-1.0,1.0,#B
                1.0,-1.0,1.0,#A
                1.0,1.0,1.0,#C
                -1.0,1.0,1.0,#D
                -1.0,-1.0,1.0,#B

                1.0,-1.0,-1.0,#F
                1.0,1.0,1.0,#C
                1.0,-1.0,1.0,#A
                1.0,-1.0,-1.0,#F
                1.0,1.0,-1.0,#E
                1.0,1.0,1.0,#C

                1.0,1.0,-1.0,#E
                1.0,-1.0,-1.0,#F
                -1.0,-1.0,-1.0,#H
                1.0,1.0,-1.0,#E
                -1.0,-1.0,-1.0,#H
                -1.0,1.0,-1.0,#G

                -1.0,-1.0,-1.0,#H
                -1.0,-1.0,1.0,#B
                -1.0,1.0,-1.0,#G
                -1.0,1.0,-1.0,#G
                -1.0,-1.0,1.0,#B
                -1.0,1.0,1.0,#D

                1.0,1.0,1.0,#C
                1.0,1.0,-1.0,#E
                -1.0,1.0,-1.0,#G
                1.0,1.0,1.0,#C
                -1.0,1.0,-1.0,#G
                -1.0,1.0,1.0,#D

                1.0,-1.0,1.0,#A
                -1.0,-1.0,1.0,#B
                -1.0,-1.0,-1.0,#H
                -1.0,-1.0,-1.0,#H
                1.0,-1.0,-1.0,#F
                1.0,-1.0,1.0 #A
            ])

            self.squareArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.squareArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            GL.glEnableVertexAttribArray(2)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idNormalBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idNormalBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(normal)*normal.itemsize, ctypes.c_void_p(normal.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(2,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

        
        projection = glm.perspective(self.pi/4,self.width/self.height,0.1,100)
        camera = glm.lookAt(glm.vec3(6,0,6),glm.vec3(0,0,0),glm.vec3(0,1,0))
        model = glm.rotate(a,glm.vec3(0,1,0))*glm.rotate(self.pi/4,glm.vec3(0,0,1))*glm.rotate(self.pi/4,glm.vec3(1,0,0))#*glm.rotate(a,glm.vec3(0,1,0))*glm.rotate(a,glm.vec3(0,0,1))
        mvp = projection * camera * model
        normalMatrix = glm.transpose(glm.inverse(glm.mat3(camera*model)))
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glUniformMatrix3fv(GL.glGetUniformLocation(self.pipeline, "normalMatrix"),1,GL.GL_FALSE,glm.value_ptr(normalMatrix))
        GL.glBindVertexArray(self.squareArrayBufferId)
        GL.glDrawArrays(GL.GL_TRIANGLES,0,36)

    def draw(self):
        global a
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        # Draw a Triangle
        self.drawDado()
        a+=self.pi*self.frameTime

CuboWithTextureAndLightApp()
