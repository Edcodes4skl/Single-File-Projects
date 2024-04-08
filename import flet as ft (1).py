class Animal:
    def __init__(self, eyes, legs, tail, arms, size, species, sound, movement):
        self.eyes = eyes
        self.legs = legs
        self.tail = tail
        self.arms = arms
        self.size = size
        self.species = species
        self.sound = sound
        self.movement = movement
    def sounds(self):
        print("I  " + self.sound)
    def moves(self):
        print("And I  " + self.movement)

horse = Animal( 2,4,"Has a tail","Has no arms","Big","Horse","Neyhhhh","Gallop")

frog = Animal(2,2,"None",2,"Small","Frog","Ribbit","Hop")


horse.sounds()
horse.moves()
frog.sounds()
frog.moves()

del horse
del frog