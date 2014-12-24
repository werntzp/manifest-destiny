class Unit():

    UNIT_INFANTRY = 0
    UNIT_MECHANIZED = 1
    UNIT_FIGHTER = 2
    UNIT_BOMBER = 3
    UNIT_TRANSPORT = 4
    UNIT_DESTROYER = 5
    UNIT_CARRIER = 6


    def __init__(self, type, x, y, owner):
        self._type = type
        self._x = x
        self._y = y
        self._owner = owner
        self.initvalues()

    # initialize variables based on unit type
    def initvalues(self):
        # fighters and bombers have a range before they must land and refuel
        self._range = -1
        if self._type in (self.UNIT_FIGHTER, self.UNIT_BOMBER):
            self._range = 10

        # transports and carriers have no attack value by themselves
        self._attack = 1
        if self._type in (self.UNIT_TRANSPORT, self.UNIT_CARRIER):
            self._attack = 0

        # start off with no transported unit
        self._transportedunit = None

    @property
    def cantransport(self, type):
        # transports can carry inf and mech, carriers can hold fighters ... everything else returns false
        if type in (self.UNIT_INFANTRY, self.UNIT_MECHANIZED) and self._type == self.UNIT_TRANSPORT:
            return True
        elif type == self.UNIT_FIGHTER and self._type == self.UNIT_CARRIER:
            return True
        else:
            return False

    @property
    def transportedunit(self):
        return self._transportedunit

    @transportedunit.setter
    def transportedunit(self, unit):
        if self._type == self.UNIT_TRANSPORT and unit in (self.UNIT_INFANTRY, self.UNIT_MECHANIZED):
            self._transportedunit = unit
        elif self._type == self.UNIT_CARRIER and unit == self.UNIT_FIGHTER:
            self._transportedunit = unit
        else:
            raise ValueError("Cannot load this type of unit!")
