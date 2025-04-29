#version 330 core

layout (location = 0) in vec3 in_position; // 3D 좌표 입력 (버텍스 위치)
layout (location = 1) in vec3 in_color; // 색상 입력 (RGB)

out vec3 color;  // 셰이더에서 계산된 색상값을 출력


void main() {
    color = in_color; // 입력 색상 값을 출력 색상으로 설정
    gl_Position = vec4(in_position, 1.0); // 3D 좌표를 4D로 변환 후, 화면 위치로 설정
}