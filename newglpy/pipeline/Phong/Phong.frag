#version 400

in vec2 textureCoord;
in float intensity;
uniform sampler2D textureSlot;
out vec4 color;

void main(void) 
{
    float specular = 3.0*(intensity-min(intensity,0.85));
    float shadow = (-0.6)*(intensity-max(intensity,-0.7));
    float ambient = 0.3;
    color = max(ambient,intensity)*vec4(1.0,1.0,1.0,1.0)*texture(textureSlot,textureCoord)+specular;//-shadow;
}