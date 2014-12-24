class Location():

    TERRAIN_LAND = 0
    TERRAIN_SEA = 1
    TERRAIN_CITY = 2

    def __init__(self, terrain, x, y, cityname = None):
        self._terrain = terrain
        self._x = x
        self._y = y
        self._cityname = cityname
        self._cityowner = None

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def terrain(self):
        return self._terrain

    @property
    def cityname(self):
        return self._cityname

    @property
    def owner(self):
        return self._cityowner

    @owner.setter
    def owner(self, rhs):
        if self._terrain == self.TERRAIN_CITY:
            self._owner = rhs
        else:
            raise ValueError("Cannot set an owner on anything but a city!")
