from settings import *
from meshes.chunk_mesh import ChunkMesh


class Chunk:
    def __inti__(self,app):
        self.app = app
        self.voxels: np.array = self.build_voxels()

    def build_voxels():
        # empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        # fill chunk
        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                for y in range(CHUNK_SIZE):
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = 1
        return voxels