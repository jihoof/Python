from settings import *  # 설정 불러오기
from meshes.base_mesh import BaseMesh  # BaseMesh 클래스 불러오기


class QuadMesh(BaseMesh):
    def __init__(self, app):
        super().__init__()  # 부모 클래스 초기화

        self.app = app  # 앱 객체 저장
        self.ctx = app.ctx  # OpenGL 컨텍스트 저장
        self.program = app.shader_program.quad  # 셰이더 프로그램 선택

        self.vbo_format = '3f 3f'
        self.attrs = ('in_position', 'in_color')
        self.vao = self.get_vao()

    def get_vertex_data(self):
        # 사각형을 그리기 위한 버텍스와 색상 데이터 정의
        vertices = [
            (0.5, 0.5, 0.0), (-0.5, 0.5, 0.0), (-0.5, -0.5, 0.0),
            (0.5, 0.5, 0.0), (-0.5, -0.5, 0.0), (0.5, -0.5, 0.0)
        ]
        colors = [
            (0, 1, 0), (1, 0, 0), (1, 1, 0),
            (0, 1, 0), (1, 1, 0), (0, 0, 1)
        ]
        # 버텍스와 색상 합쳐서 반환
        vertex_data = np.hstack([vertices, colors], dtype='float32')
        return vertex_data
