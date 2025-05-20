from meshes.base_mesh import BaseMesh


class ChunkMesh(BaseMesh):
    def __init__(self, chunk):
        self.app = chunk.app
        self.chunk = chunk