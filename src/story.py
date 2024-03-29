import engine

"""Contains game's story content, and story reading function.
Sets up each area's information to display.
"""

class Travel:
    def __init__(self):



def read_story(story_point: int):
    global story
    read = story[story_point]
    for sentence in range(len(read) - 1):  # Print out all in the 'read' list except last item.
        engine.type(read[sentence])  # Print each sentence.

    end_point = read[-1]  # Last item is dict that can lead to another story point or resume traveling mode.
    if end_point is None:
        engine.enter_to_continue()
        engine.clear()
        return  # If None, we will end recursion.
    engine.clear()
    story_ind = engine.get_input(end_point['question'], end_point['responses'])  # Returns the index of the response chosen.
    engine.clear()
    story_ind -= 1  # Need to -1 to match up with index of the list, since get_input adds 1 to display choices properly.
    start_points = end_point['branch']  # Possible story points to resume at.
    if start_points is not None:  # If there is a list of story points to go to.
        go_to = start_points[story_ind]  # Match up response index to story point index to jump to.
        read_story(go_to)  # Recursively call function till we enter travel mode or reach end of story.


# area without enemies
class Area:
    def __init__(self, name: str, description: str, difficulty: float, observe: list):
        global story
        self.name = name
        self.description = description
        self.difficulty = difficulty
        self.observe = observe

    def display(self):
        print("=" * 60)
        spaces = int((60 - (len(self.name) + 2)) / 2)
        print("|" + (" " * spaces) + self.name + (" " * spaces)+ "|")
        print("=" * 60)
        engine.type(self.description, 60)

    def look_around(self):
        for i in range(len(self.observe) - 1):  # Type out 'observe' list's strings.
            engine.type(self.observe[i])

        go_to = self.observe[-1]  # Indicates what to do after reading all of the story point.
        if go_to != 0:
            read_story(go_to)

        return travel_mode()  # If go_to is 0 or story points are all read.

    def explore(self):
        if self.difficulty == 0:
            return

class Home_Area(Area):
    """Player can rest to full health."""
    def __init__(self, name: str, description: str, difficulty: float, observe: list):
        super().__init__(name, description, difficulty, observe)

    def recover(self, player):
        engine.type("You rested.")
        player.health = player.full_health


def antidote(player):
    player.health += 20
    if player.health > player.full_health:
        return player.full_health
    return player.health

def potion(player):
    if "Poison" in player.status:
        player.remove("Poison")
        print(player.name + " was cured of [Poisoned] status.")
        return
    print("You are not poisoned. You can't use the potion right now.")

class Shop_Area(Area):
    """Player can buy items."""
    def __init__(self, name: str, description: str, difficulty: float, observe: list):
        super().__init__(name, description, difficulty, observe)
        self.items = [["Antidote", antidote, "Recovers the status infliction [Poisoned]"],
                      ["Potion", potion, "Recovers 20 hp"]]

    def show_items(self):
        """Shows items of the shop."""
        print("Items")
        print("_" * 44)
        for item in self.items:
            print(item[0] + ": " + item[2])

    def buy_item(self, player, item):
        """When buying an item."""
        if item == "Potion":
            if player.wealth >= 3:
                player.wealth -= 3
            else:
                print("You don't have enough money.")
                return
        elif item == "Antidote":
            if player.wealth >= 2:
                player.wealth -= 2
            else:
                print("You don't have enough money.")
                return
        player.inventory.append(item)
        print("Bought the item, " + "[" + item + "]" + ".")


#area with enemies
class EnemiesArea(Area):
    def __init__(self, name: str, description: str, difficulty: int):
        super().__init__(name, description)
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

# name        | The area's name will be always displayed while the user is there.
# description | Gives the user a basic description of the area.
# difficulty  | A float to use to calculate enemy difficulty (easy: 0.5 ~ hard: 1. If 0, there are no enemies).
# observe     | An action the user can choose, gives more info about the area. Sometimes can trigger a story point,
#               indicated by having last item in the value be the number of the story point (0 = traveling mode).

a1 = {'name': 'Lake',
      'description': "An open lake is in the middle of an ocean of trees. As the waters move gently across, " +
                     "you think the glitter of sunlight reflected off the waves is quite pretty.",
      'difficulty': 0.8,
      'observe': ["Taking a closer look at the lake, you curiously peer down into the lake's blue...",
                  "Upon that brief inspection, you sense that the lake is far deeper than you expected.", 0]}

a2 = {'name': 'Forest',
      'description': "There is green as far as your eyes can see. You don't know what the names of any of the trees " +
                     "are, but you can tell there is a diverse variety of trees here.",
      'difficulty': 0.6,
      'observe': ["As you focus on your surroundings, you notice the presence of monsters. This much is to be " +
                  "expected. You grip your lance firmly, ready for any danger that might pounce out of the trees.", 0]}

a3 = {'name': 'Den',
      'description': "Damp and dark, the den seems to ooze death. It may not be a good idea to explore here until " +
                     "properly equipped...",
      'difficulty': 1.0,
      'observe': ["With the heightened senses you gained through your life as a traveler, you realize that this is " +
                  "where all the monsters are spawning from.", 0]}

home = {'name': 'Home',
      'description': "Home, sweet home. You've spent most of your years in this homely shack. It's a great place to " +
                     "rest up before continuing your journey.",
      'difficulty': 0,
      'observe': ["For some reason, you feel a bit melancholy as you gaze upon your humble abode.",
                  "You smile as you think back on past memories.", 0]}

alley = {'name': 'Alley',
      'description': "The dark alleyway gives you the goosebumps. The brick walls surrounding the alley seem to be " +
                     "ready to crumble down any minute. You can't fathom staying at this place for long.",
      'difficulty': 0,
      'observe': ["Your've experienced scarier things than this, but somehow this place manages to unnerve you " +
                  "everytime.", "As you walk deeper into the alleyway, near the end of the alley... You can barely " +
                  "make out a cloaked figure.", 3]}

shop = {'name': 'Store',
      'description': "A small store that sells many items you've used as a wandering traveler. It is a bit run-" +
                     "down, but its still your same old reliable go-to.",
      'difficulty': 0,
      'observe': ["You look at the store that you know just as well as your own house. Instead of waiting around, " +
                  "maybe I should go in?", 0]}

gates = {'name': 'Gates',
      'description': "The town gates stand tall. However, there are some noticable cracks in the gates from monsters " +
                     "trying to get in. You wave to the guard, and the guard waves back.",
      'difficulty': 0,
      'observe': ["You take a closer look at the condition of the gates. You notice there is quite a lot more " +
                  "damage on these gates than you thought. You feel a bit more determined to protect your town.", 0]}

# story | A dict containing story to be presented as the player progresses
# key = int (represents a story point),  value = list (story content to print out)
#                                        ^ last item is dict with
#                                        question  | A prompt for the user to respond to
#                                        responses | List of choices the user can respond with (if None, means
#                                                    it takes any input)
#                                        branch    | Leads to another story point (index of each point matches up with
#                                                    index of the response chosen)
#                                                    *(If last item is None, activate travel mode)

story = {1: ["In the fair lands of Estriam, you are a traveler set on helping out your small town deal with the " +
             "troubles it has been having.", "From constant monster invasions to mysterious incidents, the town " +
             "desperately needs your help!", "You waste no time, and decide to utilize your talents and skills to " +
             "help your town out.", {'question': "Humble traveler, what is your name?", 'responses': [None],
                                     'branch': [2,]}],
         2: [f"Well, its nice meeting you, {name}.", "Well now, I won't delay things any longer! Get out and help " +
             "your town!", None],
         3: ["You approach the cloaked figure, even though you think that might not be a good idea.", "Getting " +
             "closer, the figure looks up to you.", "You can't help but let out slight gasp as you see a face " +
             "made of skin and bones. In the midst of your shock, the figure speaks.", {'question': '"Young lad, if ' +
             'you would do this old man a favor..."', 'responses': ['"What is it?"', '''"I'm busy."'''], 'branch':
             [4, 5]}],
         4: ['"Haha... thank you." The old man gently nods his head.', '"There is something I dropped while I was ' +
             'at the lake. Is it possible for you to retrieve it for me?" The man asks.', '"What am I looking for?" ' +
             'I ask.', '"A silver necklace with an enchanted stone. It may be in the lake, or a monster may have ' +
             'taken it... But I have a feeling you will find it." he replies.', '''"Alright. I'll search for it. ''' +
             'Rest easy, old man."', None],
         5: ['"Hmph." The old man turns away, and his thinly cloaked figure shrinks into the darkness.', None]
        }

map = [
    [shop, home, alley],
    [None, gates, None],
    [a1, a2, a3]
]

Alley = Area(**alley)
Shop = Shop_Area(**shop)
Home = Home_Area(**home)

