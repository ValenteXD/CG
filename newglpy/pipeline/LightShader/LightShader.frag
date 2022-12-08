#version 400

in vec2 textureCoord;
in float intensity;
uniform sampler2D textureSlot;
out vec4 color;

void main(void) 
{
    color = intensity*vec4(1.0,1.0,1.0,1.0)*texture(textureSlot,textureCoord);
}