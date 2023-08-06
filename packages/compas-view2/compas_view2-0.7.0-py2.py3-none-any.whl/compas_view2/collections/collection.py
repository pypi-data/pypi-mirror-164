class Collection:
    """A collection of COMPAS items like meshes or shapes.
    """

    def __init__(self, items=None):
        super().__init__()
        self.items = items or []
