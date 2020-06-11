
class Pet():
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5, loneliness=50):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.loneliness = loneliness

    def eat_food(self):
        self.fullness += 30
        
    def get_love(self):
        self.happiness += 30

    def be_alive(self, hunger, mopiness):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness

    def __str__(self):
        return """
        %s:
        Fullness: %d
        Happiness: %d
        """ % (self.name, self.fullness, self.happiness)

    class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        super().__init__(name,fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
        self.name = name
        self.fullness = fullness
        self.happiness = 100
        self.hunger = hunger
        self.mopiness = 1

    # class AggressivePet(Pet):
    #     __init__(self, name, fullness=10, happiness=15, hunger=1, mopiness=2):
    #     super().__init__(name,fullness, 20, hunger, 1)
    #     self.aggression_level =

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness/2

    def cuddle(self, other_pet):
        for i in range(self.cuddle_level):
            other_pet.get_love()    
        
    def get_attention(self):
        self.loneliness -= 20

    def pet_feed(pet):
        pet["fullness"] += 10
            
    def play_with_pet(pet):
        pet["happiness"] += 10
    
    def get_hungry_and_mopey(pet):
        pet["fullness"] -= 5
        pet["happiness"] -= 5
        while True:
            print("""
            %s's stats:
            Fullness: %d
            Happiness: %d
            """ % (puppy["name"], puppy["fullness"], pupp["happiness"]))
                 
            choice = int(input("""
            1. Feed puppy
            2. Play with puppy
            3. Do nothing
            """))
            if choice == 1:
                feed_pet(puppy)
            elif choice == 2:
                play_with_pet(puppy)
            else:
                pass           


bobby = Pet("Bobby")
print(bobby.name)
bobby.eat_food()
print(bobby.fullness)
print(bobby.happiness)

