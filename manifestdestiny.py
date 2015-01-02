import random

class Unit():

    UNIT_INFANTRY = 0
    UNIT_MECHANIZED = 1
    UNIT_FIGHTER = 2
    UNIT_BOMBER = 3
    UNIT_TRANSPORT = 4
    UNIT_DESTROYER = 5
    UNIT_CARRIER = 6
    MOVE_MANUAL = 0
    MOVE_RANDOM = 1
    MOVE_PATROL = 2

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

        # start with manual move (player decides)
        self._movetype = self.MOVE_MANUAL

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

    @property
    def movetype(self):
        return self._movetype

    @movetype.setter
    def movetype(self, type):
        self._movetype = type



class Player():

    PLAYER_HUMAN = 0
    PLAYER_COMPUTER = 1

    def __init__(self, number, type, name = None):

        # load up player name options
        f = open("players.txt")
        names = f.readlines()
        playernames = names
        f.close()

        self._number = number
        self._type = type
        if type == self.PLAYER_COMPUTER:
            self._name = playernames[number-1].strip()
        else:
            self._name = name
        self._citiesowned = 0

    @property
    def type(self):
        return self._type

    @property
    def typename(self):
        if self._type == self.PLAYER_HUMAN:
            return "Human"
        else:
            return "Computer"

    @property
    def name(self):
        return self._name

    @property
    def cities(self):
        return self._citiesowned

    @cities.setter
    def cities(self, cities):
        self._citiesowned = cities

    def __str__(self):
        return "Player {0} is a {1}.".format(self.name, self.typename)


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

class ManifestDestiny():

    def __init__(self):
        """
        init - setup internal data structures
        """
        # init players array
        self._players = []
        # init 20x20 array to hold the board
        self._map = [[0 for x in range(1, 22)] for x in range(1, 22)]
        # load all the city names into a list
        f = open("cities.txt")
        names = f.readlines()
        self._citynames = names
        f.close()

    def getcityname(self, pos):
        """
        getcityname - return the corresponding city name
        """
        return self._citynames[pos].strip()

    def getterraintype(self):
        """
        getterraintype - randomly decide whether spot on map is land, sea or a city
        """
        x = random.randrange(1,30+1)
        if x < 12:
            return Location.TERRAIN_LAND
        elif x < 29:
            return Location.TERRAIN_SEA
        else:
            return Location.TERRAIN_CITY

    def getmap(self):
        return self._map


    def setupmap(self):
        """
        setupmap -organize a random map board
        """
        # track cities, since we don't want more than 45
        ctr = 0

        # board is 20x20 grid
        for i in range(1, 21):
            for j in range(1, 21):

                # get random terrain type
                cname = None
                terrain = self.getterraintype()
                if terrain == Location.TERRAIN_CITY:
                    # if too many cities, just make the rest land
                    if ctr <= 44:
                        cname = self.getcityname(ctr)
                    else:
                        terrain = Location.TERRAIN_LAND
                    ctr += 1

                #print("terrain: {0}".format(terrain))
                #print("city: {0}".format(cname))
                l = Location(terrain, i, j, cname)
                self._map[i][j] = l

        # return the initial map back out
        return self._map

    def addplayer(self, type, name = None):
        """
        addplayer - add a new player (either human or computer)
        """
        p = Player(len(self._players)+1, type, name)
        # add it to the internal array
        self._players.append(p)

    def getplayers(self):
        return self._players

