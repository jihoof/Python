#version 330 core  // GLSL 버전 3.30 사용


layout (location = 0) out vec4 fragColor;  // 출력: 픽셀 색상 (vec4는 R, G, B, A)

in vec3 color;  // 입력: 버텍스 셰이더에서 넘겨받은 색상 (RGB)


void main() {
    fragColor = vec4(color, 1.0);  // RGB 색상에 알파(투명도) 1.0을 추가해서 최종 픽셀 색상으로 출력
}