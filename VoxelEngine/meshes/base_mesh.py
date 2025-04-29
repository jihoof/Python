import numpy as np


class BaseMesh:
    def __init__(self):
        # OpenGL 컨텍스트 (그래픽 환경 설정 객체)
        self.ctx = None
        # 셰이더 프로그램 (vertex + fragment shader를 합친 것)
        self.program = None
        # 버텍스 버퍼 데이터 형식: "3f 3f" (예: 위치 3개 + 색상 3개)
        self.vbo_format = None
        # 데이터 형식에 따라 정해지는 속성 이름들: ("in_position", "in_color")
        self.attrs: tuple[str, ...] = None
        # 버텍스 배열 객체 (VAO: 버퍼와 셰이더 연결 설정)
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        # 버텍스(점) 데이터를 가져옴
        vertex_data = self.get_vertex_data()
        # 버텍스 데이터를 GPU에 올려서 버퍼(VBO)를 생성
        vbo = self.ctx.buffer(vertex_data)
        # 셰이더 프로그램과 버텍스 버퍼를 연결해서 VAO(버텍스 배열 객체) 생성
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)], skip_errors=True
        )
        # 만들어진 VAO를 반환
        return vao

    def render(self):
        # VAO를 이용해서 화면에 메시를 렌더링
        self.vao.render()
