import engine

""""""

class Area:
    def __init__(self, name: str, description: str, difficulty: int):
        self.name = name
        self.description = description
        self.difficulty = difficulty

    def display(self):
        print("=" * 44)
        spaces = int((44 - (len(self.name) + 2)) / 2)
        print("|" + (" " * spaces) + self.name + (" " * spaces)+ "|")
        print("=" * 44)
        engine.type(self.description, 44)

start = "#############################################\n" \
        "+                 SimpleRPG                 +\n" \
        "#############################################\n" \
        "                   + Start                   \n" \
        "                   + Load                    \n" \
        "                   + Quit                    \n"

# name        | the area's name will be always displayed while the player is there
# description | gives the player a basic description of the area
# observe     | an action the player can choose, gives more info about the area

a1 = {'name': 'Lake',
      'description': "An open lake is in the middle of an ocean of trees. As the waters move gently across, " +
                     "you think the glitter of sunlight reflected off the waves is quite pretty.",
      'observe': ["Taking a closer look at the lake, you curiously peer down into the lake's blue...",
                  "Upon that brief inspection, you sense that the lake is far deeper than you expected."],
      'events': [6]}

story = {1: [''], }

available_events = []
triggered_events = []
"""
map = [store, plaza, alley,
       garden, gates, home,
       a1, a2, a3,
       a4, a5, a6]
"""