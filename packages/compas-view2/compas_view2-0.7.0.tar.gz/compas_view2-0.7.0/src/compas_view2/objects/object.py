import abc
import numpy as np
import inspect

from compas.geometry import Transformation
from compas.geometry import Translation
from compas.geometry import Rotation
from compas.geometry import Scale
from compas.geometry import decompose_matrix
from compas.geometry import identity_matrix


ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})

DATA_OBJECT = {}


def _get_object_cls(data):
    dtype = type(data)
    cls = None

    for type_ in inspect.getmro(dtype):
        cls = DATA_OBJECT.get(type_, None)
        if cls is not None:
            break

    if cls is None:
        raise Exception('No object is registered for this data type: {}'.format(dtype))

    return cls


class Object(ABC):
    """Base object for compas_view2

    Attributes
    ----------
    name : str
        The name of the object.
    is_selected : bool
        Whether the object is selected.
    translation : list
        The translation vector of the object.
    rotation : list
        The Euler rotation of the object in XYZ order.
    scale : list
        The scale factor of the object.
    matrix: list
        The 4x4 transformation matrix that is composed from translation, rotation and scale.
    """

    @staticmethod
    def register(dtype, otype):
        """Register an object class to its corrensponding data type"""
        DATA_OBJECT[dtype] = otype

    @staticmethod
    def build(data, **kwargs):
        """Build an object class according to its corrensponding data type"""
        try:
            obj = _get_object_cls(data)(data, **kwargs)
        except KeyError:
            raise TypeError("Type {} is not supported by the viewer.".format(type(data)))
        return obj

    def __init__(self, data, name=None, is_selected=False, is_visible=True):
        self._data = data
        self.name = name or str(self)
        self.is_selected = is_selected
        self.is_visible = is_visible
        self.parent = None
        self._children = set()
        self._instance_color = None
        self._translation = [0., 0., 0.]
        self._rotation = [0., 0., 0.]
        self._scale = [1., 1., 1.]
        self._transformation = Transformation()
        self._matrix_buffer = None
        self._app = None

    @property
    def otype(self):
        return DATA_OBJECT[self._data.__class__]

    @property
    def DATA_OBJECT(self):
        return DATA_OBJECT

    @abc.abstractmethod
    def init(self):
        pass

    @abc.abstractmethod
    def draw(self, shader):
        pass

    def create(self):
        pass

    @property
    def properties(self):
        return None

    @property
    def children(self):
        return self._children

    def add(self, item, **kwargs):
        if isinstance(item, Object):
            obj = item
        else:
            obj = self._app.add(item, **kwargs)
        self._children.add(obj)
        obj.parent = self

        if self._app.dock_slots['sceneform'] and self._app.view.isValid():
            self._app.dock_slots['sceneform'].update()
        return obj

    def remove(self, obj):
        obj.parent = None
        self._children.remove(obj)

    @property
    def translation(self):
        return self._translation

    @translation.setter
    def translation(self, vector):
        self._translation[0] = vector[0]
        self._translation[1] = vector[1]
        self._translation[2] = vector[2]

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, angles):
        self._rotation[0] = angles[0]
        self._rotation[1] = angles[1]
        self._rotation[2] = angles[2]

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, factors):
        self._scale[0] = factors[0]
        self._scale[1] = factors[1]
        self._scale[2] = factors[2]

    def _update_matrix(self):
        """Update the matrix from object's translation, rotation and scale"""
        if (not self.parent or self.parent._matrix_buffer is None) and (self.translation == [0, 0, 0] and self.rotation == [0, 0, 0] and self.scale == [1, 1, 1]):
            self._transformation.matrix = identity_matrix(4)
            self._matrix_buffer = None
        else:
            T1 = Translation.from_vector(self.translation)
            R1 = Rotation.from_euler_angles(self.rotation)
            S1 = Scale.from_factors(self.scale)
            M = T1 * R1 * S1
            self._transformation.matrix = M.matrix
            self._matrix_buffer = np.array(self.matrix_world).flatten()

        if self.children:
            for child in self.children:
                child._update_matrix()

    @property
    def matrix(self):
        """Get the updated matrix from object's translation, rotation and scale"""
        return self._transformation.matrix

    @property
    def matrix_world(self):
        """Get the updated matrix from object's translation, rotation and scale"""
        if self.parent:
            return (self.parent._transformation * self._transformation).matrix
        else:
            return self.matrix

    @matrix.setter
    def matrix(self, matrix):
        """Set the object's translation, rotation and scale from given matrix, and update object's matrix"""
        scale, _, rotation, tranlation, _ = decompose_matrix(matrix)
        self.translation = tranlation
        self.rotation = rotation
        self.scale = scale
        self._update_matrix()
