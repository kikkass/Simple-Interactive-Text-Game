class Creatures:
    class_name = ""
    desc = ""
    creatures = {}

    def __init__(self,name):
        self.name = name
        Creatures.creatures[self.name] = self

    def get_desc(self):
            return self.class_name + '\n' + self.desc

class Dragon(Creatures):
    class_name = 'Dragon'
    _desc = 'An incredible creature that can blow fire from mouth'
    health = 5

    def desc(self):
        healthmeter = {0:'is Dead',1:'is severly injured',2:'has lost both legs',3:'has got wound on head',4:'has got wond on knee'}
        if self.health == 5:
            return self.name + '\n Description --> ' + self._desc
        else:
            return self.name + '\n Description --> ' + self._desc + '\n   Healh -->  {}'.format(healthmeter[self.health])

class Rakshas(Creatures):
    class_name = 'Rakshas'
    _desc = 'A human like evil creature'
    health = 10

    def desc(self):
        healthmeter = {0:'is Dead',1:'is severly injured',2:'s severly injured',3:'has lost both legs',4:'has lost both legs',5:'has lost left leg',6:'has got wound on head',7:'has got wound on head',8:'has got wond on both knees',9:'has got one knee'}
        if self.health == 10:
            return self.name + '\n Description --> ' + self._desc
        else:
            return self.name + '\n Description --> ' + self._desc + '\n  Healh -->  {}'.format(healthmeter[self.health])

def show(noun):
    if noun in Creatures.creatures:
        return '{}\n'.format(noun) + Creatures.creatures[noun]._desc
    else:
        return '--Creature {0} Not found--'.format(noun)

def evaluate(noun):
    if noun in Creatures.creatures:
        return Creatures.creatures[noun].desc()
    else:
        return '--Creature {0} Not found--'.format(noun)

def say(noun):
    return 'You --> {0}'.format(noun)

def hit(noun):
    if noun in Creatures.creatures:
        thing = Creatures.creatures[noun]
        if thing.health > 0:
            thing.health -= 1
            if thing.health == 0:
                return '** You kiled {} **'.format(noun)
            else:
                return ' * You hit {} *'.format(noun)
        else:
            return '-- {} is dead --'.format(noun)
    else:
        return '--Creature {0} Not found--'.format(noun)

redfly = Dragon('Redfly')
kataka = Rakshas('Kataka')
neecha = Rakshas('Neecha')

def get_input():
    command = input(':').split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    else:
        print('-- Undefined action {} --'.format(verb_word))
        return

    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print ('-- Nothing --')

verb_dict = {'say':say,'show':show,'hit':hit,'eval':evaluate}

while True:
    get_input()