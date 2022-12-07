from GLAPP import GLAPP
from OpenGL import GL
from array import array
import ctypes
import glm

class SquareWithTextureApp(GLAPP):

    def setup(self):
        # Window setup
        self.title("Square With Texture")
        self.size(800,800)

        # OpenGL Initialization
        GL.glClearColor(0.2, 0.2, 0.2, 0.0)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glEnable(GL.GL_MULTISAMPLE)

        # Pipeline (shaders)
        self.pipeline = self.loadPipeline("SimpleTexture")
        GL.glUseProgram(self.pipeline)

        # Texture
        GL.glActiveTexture(GL.GL_TEXTURE0)
        self.loadTexture("./textures/uv_grid_opengl.png")
        GL.glUniform1i(GL.glGetUniformLocation(self.pipeline, "textureSlot"),0)

        self.squareArrayBufferId = None

    def drawSquare(self):
        if self.squareArrayBufferId == None:
            position = array('f',[
                 0.8, -0.8, 0.0,
                -0.8, -0.8, 0.0,
                 0.8,  0.8, 0.0,
                -0.8,  0.8, 0.0
            ])

            textureCoord = array('f',[
                1.0, 0.0,
                0.0, 0.0,
                1.0, 1.0,
                0.0, 1.0
            ])

            self.squareArrayBufferId = GL.glGenVertexArrays(1)
            GL.glBindVertexArray(self.squareArrayBufferId)
            GL.glEnableVertexAttribArray(0)
            GL.glEnableVertexAttribArray(1)
            
            idVertexBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idVertexBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(position)*position.itemsize, ctypes.c_void_p(position.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(0,3,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))

            idTextureBuffer = GL.glGenBuffers(1)
            GL.glBindBuffer(GL.GL_ARRAY_BUFFER, idTextureBuffer)
            GL.glBufferData(GL.GL_ARRAY_BUFFER, len(textureCoord)*textureCoord.itemsize, ctypes.c_void_p(textureCoord.buffer_info()[0]), GL.GL_STATIC_DRAW)
            GL.glVertexAttribPointer(1,2,GL.GL_FLOAT,GL.GL_FALSE,0,ctypes.c_void_p(0))
        
        mvp = glm.mat4(1.0)
        GL.glUniformMatrix4fv(GL.glGetUniformLocation(self.pipeline, "MVP"),1,GL.GL_FALSE,glm.value_ptr(mvp))
        GL.glBindVertexArray(self.squareArrayBufferId)
        GL.glDrawArrays(GL.GL_TRIANGLE_STRIP,0,4)

    def draw(self):
        # clear screen and depth buffer
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)

        # Draw a Triangle
        self.drawSquare()

SquareWithTextureApp()
