import random

# # create 3 lists
# # l1 = descriptor i.e. 'Gorgeous'
# list1 = ["Cold", "Pulsing", "Superflous", "Angry",
#          "Scathing", "Puny", "Eerie", "Marvelous", "Eternal"]
# #l2 = adjective (room)
# list2 = ["Decaying", "Granite", "Wooden", "Drafty",
#          "Picturesque", "Failing", "Smoldering", "Forsaken"]
# # l3 = room type + description

# list3 = [{"name": "Palace", "desc": "An ornamental monstrosity"},
#          {"name": "Crypt", "desc": "Those buried here will never rest in peace"},
#          {"name": "Passage", "desc": "For a player on the go"},
#          {"name": "Stairwell", "desc": "Don't trip"},
#          {"name": "Burrows", "desc": "A field of danger"},
#          {"name": "Grotto", "desc": "A faeries light..."},
#          {"name": "NYT", "desc": "A lot of people say its failing"},
#          {"name": "Pits", "desc": "Deep in the muck"}]

# create class
# give class the attributes of the 3 lists
# when call class.generator(), return the list of combos


class ProceduralContent:
    def __init__(self):
        self.l1 = ["Cold", "Pulsing", "Superflous", "Angry",
                   "Scathing", "Puny", "Eerie", "Marvelous", "Eternal"]
        self.l2 = ["Decaying", "Granite", "Wooden", "Drafty",
                   "Picturesque", "Failing", "Smoldering", "Forsaken"]
        self.l3 = [{"name": "Palace", "desc": "An ornamental monstrosity"},
                   {"name": "Crypt", "desc": "Those buried here will never rest in peace"},
                   {"name": "Passage", "desc": "For a player on the go"},
                   {"name": "Stairwell", "desc": "Do not trip"},
                   {"name": "Burrows", "desc": "A field of danger"},
                   {"name": "Grotto", "desc": "A faeries light..."},
                   {"name": "NYT", "desc": "A lot of people say its failing"},
                   {"name": "Pits", "desc": "Deep in the muck"}]

    def generator(self):
        # total possible combinations
        combos = len(self.l1) * len(self.l2) * len(self.l3)
        iterations = []
        # create all possible combinations
        # triple nested for loop - yikes
        for i in self.l1:
            for j in self.l2:
                for k in range(len(self.l3)):
                    # append to list
                    str = f"{i} {j} {self.l3[k]['name']}"
                    rum = {"name": str, "desc": self.l3[k]['desc']}
                    iterations.append(rum)

        return iterations


# generator()
# print(generator(2))
# val = random.randint(0, 100)
# print(val)

# pc = ProceduralContent()
# listy = pc.generator()
# print(listy)
