
pets = []

main_menu = [
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "Hug Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do nothing",
]


class Pet():
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5, loneliness=50):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.loneliness = loneliness
        self.toys = []

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
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()

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



class Toy:
    def __init__(self, bonus=10, newness=10):
        self.bonus = 10
        self.newness = 10

    def use(self):
        if self.newness == 0:
            return 0
        else:
            self.newness -= 1
            return self.bonus




def print_menu_error():
    print("That was not a valid choice. Try again. \n\n\n")

def choices_to_string(choice_list):
    choice_string = ""
    num = 1
    for choice in choice_list:
        choice_string += "%d: %s\n" % (num, choice)
        num +- 1
    choice_string += "Please choose an option: "
    return choice_string

def get_user_choice(choice_list):
    choice = -1
    choice_string = choices_to_string(choice_list)
    while choice == -1:
        try:
            choice = int(input(choice_string))
            if choice <= 0 or choice > len(choice_list):
                raise ValueError
        except ValueError:
            print_menu_error()
    return choice

adoption_menu = [
    "Pet",
    "Cuddly Pet"
    # "Aggressive Pet"
]

def main():
    while True:
        choice = get_user_choice(main_menu)
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            print("Please choose the type of pet:")
            type_choice = get_user_choice(adoption_menu)
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print("You now have %d pets" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
        if choice == 3:
            for pet in pets:
                pet.eat_food()
        if choice ==4:
            for pet in pets:
                pet.get_attention()
        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        if choice == 6:
            for pet in pets:
                print(pet)
        if choice == 7:
            for pet in pets:
                pet.be_alive()
main()





bobby = Pet("Bobby")
print(bobby.name)
bobby.eat_food()
print(bobby.fullness)
print(bobby.happiness)

