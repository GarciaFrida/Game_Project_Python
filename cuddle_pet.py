from virtual_pet import Pet

class CuddlyPet(Pet):
    def cuddle(self, other_pet):
        other_pet.get_love()



daisy = CuddlyPet("Daisy", 50, 20, 20 ,1)
bobby = Pet("bobby", 50, 10, 30, 10)

print(bobby.happiness)

daisy.cuddle(bobby)

print(bobby.happiness)