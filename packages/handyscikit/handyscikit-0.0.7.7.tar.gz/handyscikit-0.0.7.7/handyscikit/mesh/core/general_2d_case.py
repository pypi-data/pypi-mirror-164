from .gmsh_encapsulation import GmshEncapsulation
from .mesh_2d import Mesh2D
from .mesh_base import meshing_time_recorder
import gmsh


class General2DCase(Mesh2D, GmshEncapsulation):
    def __init__(self):
        Mesh2D.__init__(self)

        if not gmsh.is_initialized(): gmsh.initialize()

        self._dim = 2
        self._node_per_face = 2

        self._gmsh_element_type = 2  # 2 means triangle.
        self._face_per_cell = 3
        self._node_per_cell = 3

    @meshing_time_recorder
    def generate_unstructured(self, show_mesh=False):

        gmsh.model.mesh.generate(2)
        if self._gmsh_element_type == 3: gmsh.model.mesh.recombine()
        if show_mesh: gmsh.fltk.run()

        self._generate_topology()
        gmsh.clear()