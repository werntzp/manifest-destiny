import random
from location import Location

class ManifestDestiny():

    def __init__(self):
        # init 20x20 array to hold the board
        self._map = [[0 for x in range(1, 21)] for x in range(1, 21)]
        # load all the city names into a list
        f = open("cities.txt")
        names = f.readlines()
        self._citynames = names
        f.close()

    def getcityname(self, pos):
        # return a name from the list we read in
        return self._citynames[pos].strip()

    def getterraintype(self):
        # randomly decide whether spot on map is land, sea or a city
        x = random.randrange(1,30+1)
        if x < 12:
            return Location.TERRAIN_LAND
        elif x < 29:
            return Location.TERRAIN_SEA
        else:
            return Location.TERRAIN_CITY

    def setupmap(self):
        # track cities, since we don't want more than 45
        ctr = 0

        # board is 20x20 grid
        for i in range(1, 20):
            for j in range(1, 20):

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
                #l = Location(terrain, i, j, cname)
                #self._map[i][j] = l

        # return the full map
        #return self._map






