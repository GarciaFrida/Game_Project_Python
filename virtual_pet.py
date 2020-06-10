
class Pet():
    def __init__(self, name, fullness, happiness, loneliness):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.loneliness = loneliness
        
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