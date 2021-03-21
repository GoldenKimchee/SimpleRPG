
""""""

class Area:
       def __init__(self, name: str, description: str, difficulty: int):
              self.name = name
              self.description = description
              self.difficulty = difficulty

       def display(self):
              print("#" * len(self.name) + 2)
              print("#" + self.name + "#")
              print("#" * len(self.name) + 2)


start = "##########################" \
        "####### SimpleRPG ########" \
        "##########################" \
        "        + Start           " \
        "        + Load            " \
        "        + Quit            "

# name        | the area's name will be always displayed while the player is there
# description | gives the player a basic description of the area
# observe     | an action the player can 
# events      |
a1 = {'name': 'Lake',
      'description': 'An open lake is in the middle of an ocean of trees.',
      'observe': 'Taking a closer look at the lake, you sense that the lake is far deeper than you expected.',
      'events': [6]}

story = {1: [''], 6: ["A woman stands in the corner "]}


map = [store, plaza, alley,
       garden, gates, home,
       a1, a2, a3,
       a4, a5, a6]
