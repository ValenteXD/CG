from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm
import math

class SphereApp(GLAPP):

    def setup(self):
        # Window setup
        self.title("Globe")
        self.size(800,800)

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_CULL_FACE)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("SimpleTexture")
        GL.glUseProgram(self.pipeline)
        self.a = 0
        self.sphereArrayBufferId = None
        self.idTextureBuffer = None

        # Texture
        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("./textures/mapa.png")
        GL.glUniform1i(GL.glGetUniformLocation(self.pipeline, "textureSlot"),0)        

    def drawGlobe(self):
        n = 50
        if self.sphereArrayBufferId == None:
            position = array('f')
            for i in range(0,n):
                theta = i*2*math.pi/n
                theta2 = (i+1)*2*math.pi/n
                for j in range(0,n):
                    phi = j*math.pi/n-math.pi/2
                    phi2 = (j+1)*math.pi/n-math.pi/2
                    
                    position.append(math.cos(theta)*math.cos(phi2))
                    position.append(math.sin(phi2))
                    position.append(math.sin(theta)*math.cos(phi2))
                    
                    position.append(math.cos(theta2)*math.cos(phi))
                    position.append(math.sin(phi))
                    position.append(math.sin(theta2)*math.cos(phi))
                    
                    position.append(math.cos(theta)*math.cos(phi))
                    position.append(math.sin(phi))
                    position.append(math.sin(theta)*math.cos(phi))

                    position.append(math.cos(theta2)*math.cos(phi2))
                    position.append(math.sin(phi2))
                    position.append(math.sin(theta2)*math.cos(phi2))
                    
                    position.append(math.cos(theta2)*math.cos(phi))
                    position.append(math.sin(phi))
                    position.append(math.sin(theta2)*math.cos(phi))
                    
                    position.append(math.cos(theta)*math.cos(phi2))
                    position.append(math.sin(phi2))
                    position.append(math.sin(theta)*math.cos(phi2))
                    
        if self.idTextureBuffer == None:
            textureCoord = array('f')
            for i in range(0,n):
                for j in range(0,n):

                    textureCoord.append(1-i/n)
                    textureCoord.append((j+1)/n)

                    textureCoord.append(1-(i+1)/n)
                    textureCoord.append(j/n)

                    textureCoord.append(1-i/n)
                    textureCoord.append(j/n)

                    textureCoord.append(1-(i+1)/n)
                    textureCoord.append((j+1)/n)

                    textureCoord.append(1-(i+1)/n)
                    textureCoord.append(j/n)

                    textureCoord.append(1-i/n)
                    textureCoord.append((j+1)/n)

            self.sphereArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.sphereArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            self.idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, self.idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        
        GL.glBindVertexArray(self.sphereArrayBufferId)
        projection = glm.perspective(math.pi/4,self.width/self.height,0.1,100)
        camera = glm.lookAt(glm.vec3(0,0,5),glm.vec3(0),glm.vec3(0,1,0))
        model = glm.rotate(self.a,glm.vec3(0,0,1)) * glm.rotate(self.a,glm.vec3(0,1,0)) * glm.rotate(self.a,glm.vec3(1,0,0)) 
        mvp = projection * camera * model
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glDrawArrays(GL.GL_TRIANGLES,0,8*n**2)
        self.a += self.frameTime

    def draw(self):
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        # Draw a Globe
        self.drawGlobe()

SphereApp()
