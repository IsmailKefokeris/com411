from tech import Tech

class Laser(Tech):
    
    MAX_RANGE = 50

    def fire(self, range):
        if self.active == True:
            if range > Laser.MAX_RANGE:
                print ("The distance is too far move closer")
            else:
                print ("BoooOOoOOOOMMMMM!!!!")
        else:
            print("Power on Required....")