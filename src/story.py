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

    def explore(self):
        engine.slow_type("Exploring...")

start = "#############################################\n" \
        "+                 SimpleRPG                 +\n" \
        "#############################################\n" \
        "                   + Start                   \n" \
        "                   + Load                    \n" \
        "                   + Quit                    \n"

name = "Rachel"

# name        | the area's name will be always displayed while the user is there
# description | gives the user a basic description of the area
# difficulty  | a float to use to calculate enemy difficulty (easy: 0.5 ~ hard: 1)
# observe     | an action the user can choose, gives more info about the area

a1 = {'name': 'Lake',
      'description': "An open lake is in the middle of an ocean of trees. As the waters move gently across, " +
                     "you think the glitter of sunlight reflected off the waves is quite pretty.",
      'difficulty': 0.5,
      'observe': ["Taking a closer look at the lake, you curiously peer down into the lake's blue...",
                  "Upon that brief inspection, you sense that the lake is far deeper than you expected."],
      }

# story | a dict containing story to be presented as the player progresses
# key = int (represents a story point),  value = list (story content to print out)
#                                        ^ last item is dict with
#                                        question  | a prompt for the user to respond to
#                                        responses | list of choices the user can respond with (if None, means
#                                        it takes any input)
#                                        branch    | leads to another story point (index of each point matches up with
#                                        index of the response chosen)

story = {1: ["In the fair lands of Estriam, you are a traveler set on helping out your small town deal with the " +
             "problems its been having.", "From constant monster invasions to mysterious incidents, the town " +
             "desperately needs your help!", "You waste no time, and decide to utilize your talents and skills to " +
             "help your town out.", {'question': "Humble traveler, what is your name?", 'responses': [None],
                                     'branch': [2]}],
         2: [f"Well, its nice meeting you, {name}."]}

available_events = []
triggered_events = []
"""
map = [store, plaza, alley,
       garden, gates, home,
       a1, a2, a3,
       a4, a5, a6]
"""