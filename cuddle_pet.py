from virtual_pet import Pet

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = 100
        self.hunger = hunger
        self.mopiness = 1
        
    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        other_pet.get_love()



daisy = CuddlyPet("Daisy", 50, 20, 20 ,1)
bobby = Pet("bobby", 50, 10, 30, 10)

print(bobby.happiness)

daisy.cuddle(bobby)

print(bobby.happiness)