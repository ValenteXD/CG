#version 400

in vec2 textureCoord;
in float intensity;
uniform sampler2D textureSlot;
out vec4 color;

void main(void) 
{
    vec4 pallette[2];
    pallette[0]=vec4(0.5,0.3,0.0,0.5);
    pallette[1]=vec4(0.7,0.5,0.0,0.5);
    float threshold = min(100.0*(intensity-min(intensity,0.3)),1.0);
    int index = int(threshold);
    color = pallette[index]*texture(textureSlot,textureCoord);
}