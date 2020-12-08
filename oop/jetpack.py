from tech import Tech

class Jetpack(Tech):

    def __init__(self):
        super().__init__()

    def fly(self, speed):
        if self.active == True:
            print (f"ZoooOOOOOoooOOoMMMM!!!! at a speed of {speed}mph WOWW")
        else:
            print("Power on Required....")