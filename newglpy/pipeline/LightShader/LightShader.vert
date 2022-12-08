#version 400

layout (location=0) in vec3 attr_position;
layout (location=1) in vec2 attr_textureCoord;
layout (location=2) in vec3 normal;
uniform mat4 MVP;
uniform mat3 normalMatrix;
out float intensity;
out vec2 textureCoord;

void main(void) 
{
    vec3 lightDir = normalize(vec3(0.0,0.0,10.0));
    vec3 Vnormal = normalMatrix*normal;
    intensity = dot(lightDir,normalize(Vnormal));
    gl_Position = MVP * vec4(attr_position,1.0);
    textureCoord = attr_textureCoord;
}
