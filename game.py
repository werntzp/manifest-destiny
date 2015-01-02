from manifestdestiny import *

def start():

    # create a game object
    md = ManifestDestiny()
    print("Welcome to Manifest Destiny!\n\n")

    # ask how many players
    inpnum = input("How many players? (2-4) [default is 2]")

    if inpnum == "":
        inpnum = "2"

    # loop through and create a player object
    for i in range(1, int(inpnum)+1):

        # default name to none
        name = None

        inptype = input("Is Player {0} (H)uman or (C)omputer? [default is C]".format(i))
        if inptype == "H":
            name = input("Enter name for Player {0}: ".format(i))
            ptype = Player.PLAYER_HUMAN
        else:
            ptype = Player.PLAYER_COMPUTER

        p = md.addplayer(ptype, name)

    # now that we have players, repeat them
    players = md.getplayers()
    for p in players:
        print(p)

    print("\n")

    # set up the initial map
    map = md.setupmap()

    for i in range(1, 21):

        line = ""

        for j in range(1, 21):
            l = map[i][j]

            if l.terrain == Location.TERRAIN_LAND:
                line += "*"
            elif l.terrain == Location.TERRAIN_SEA:
                line += "="
            else:
                line += "C"

        print(line)

if __name__ == "__main__":
    start()


