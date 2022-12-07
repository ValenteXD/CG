#version 400

in float intensity;
out vec4 color;

void main(void) 
{
    color = intensity*vec4(1.0,0.0,0.0,1.0);
}