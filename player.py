# Logic for controlling units

from random import randint

from game import Action


def get_actions(state):
    print('### ======================================================= ###')
    me = state.unit

    trg = {
        (me.x, me.y + 1): [Action('attack', 'down'), Action('move', 'up')],
        (me.x, me.y - 1): [Action('attack', 'up'), Action('move', 'down')],
        (me.x - 1, me.y): [Action('attack', 'left'), Action('move', 'right')],
        (me.x + 1, me.y): [Action('attack', 'right'), Action('move', 'left')],

        (me.x, me.y + 2): [Action('move', 'down'), Action('attack', 'down')],
        (me.x, me.y - 2): [Action('move', 'up'), Action('attack', 'up')],
        (me.x - 2, me.y): [Action('move', 'left'), Action('attack', 'left')],
        (me.x + 2, me.y): [Action('move', 'right'), Action('attack', 'right')],

        (me.x + 1, me.y - 1): [Action('move', 'right'), Action('attack', 'up')],
        (me.x - 1, me.y - 1): [Action('move', 'left'), Action('attack', 'up')],
        (me.x + 1, me.y + 1): [Action('move', 'right'), Action('attack', 'down')],
        (me.x - 1, me.y + 1): [Action('move', 'left'), Action('attack', 'down')]
    }

    me_pos = (me.x, me.y)
    print('My position %s' % str(me_pos))

    foes = [i for i in state.foes]
    foes_pos = list(map(lambda f: (f.x, f.y), foes))
    print('Foes position %s' % str(foes_pos))

    friends = [i for i in state.units]
    friends_pos = list(map(lambda f: (f.x, f.y), friends))
    print('Friends position %s' % str(friends_pos))

    for f in foes_pos:
        if f in trg:
            return trg.get(f)

    switcher = {
        0: [Action('move', 'left')],
        1: [Action('move', 'right')],
        2: [Action('move', 'down')],
        3: [Action('move', 'up')]
    }

    me_x = state.unit.x
    me_y = state.unit.y

    foes_x = list(map(lambda f: f.x, foes))
    foes_y = list(map(lambda f: f.y, foes))

    friends_x = list(map(lambda f: f.x, friends))
    friends_y = list(map(lambda f: f.y, friends))

    for x in foes_x:
        if x == me_x:
            return switcher.get(randint(0, 1))

    for y in foes_y:
        if y == me_y:
            return switcher.get(randint(2, 3))

    for x in friends_x:
        if x == me_x:
            return switcher.get(randint(0, 1))

    for y in friends_y:
        if y == me_y:
            return switcher.get(randint(2, 3))

    return switcher.get(randint(0, 3))


def get_player_info():
    return {
        "id": "Purple",
        "name": "Purple"
    }


def game_end():
    pass
