#      3   4  7
#      2   5  8
#      1   6  9
#Forritið keyrir while loopu þangað til við komumst í tile_9. Staðsetningin er geymd í int breytu kölluð tile_int. 
#Forritið keyrir í gegnum if setningar til þess að finna hvort staðsetningin er gild. 

tile_int = 1
direction_str = ""
print("You can travel: (N)orth.")
while tile_int < 9:
    if tile_int == 1:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "N":
            tile_int = 2
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")

    elif tile_int == 2:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "N":
            tile_int = 3
            print("You can travel: (E)ast or (S)outh.")
        elif direction_str == "E":
            tile_int = 5
            print("You can travel: (S)outh or (W)est.")
        elif direction_str == "S":
            tile_int = 1
            print("You can travel: (N)orth.")
        else:
            print("Not a valid direction!")
    elif tile_int == 3:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "E":
            tile_int = 4
            print("You can travel: (E)ast or (W)est.")
        elif direction_str == "S":
            tile_int = 2
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    elif tile_int == 4:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "E":
            tile_int = 7
            print("You can travel: (S)outh or (W)est.")
        elif direction_str == "W":
            tile_int = 3
            print("You can travel: (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    elif tile_int == 5:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "S":
            tile_int = 6
            print("You can travel: (N)orth.")
        elif direction_str == "W":
            tile_int = 2
            print("You can travel: (N)orth or (E)ast or (S)outh.")
        else:
            print("Not a valid direction!")
    elif tile_int == 6:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "N":
            tile_int = 5
            print("You can travel: (S)outh or (W)est.")
        else:
            print("Not a valid direction!")
    elif tile_int == 7:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "S":
            tile_int = 8
            print("You can travel: (N)orth or (S)outh.")
        elif direction_str == "W":
            tile_int = 4
            print("You can travel: (E)ast or (W)est.")
        else:
            print("Not a valid direction!")
    elif tile_int == 8:
        direction_str = str(input("Direction: "))
        direction_str = direction_str.upper()
        if direction_str == "N":
            tile_int = 7
            print("You can travel: (S)outh or (W)est.")
        elif direction_str == "S":
            tile_int = 9
            print("Victory!")
        else:
            print("Not a valid direction!")

        



