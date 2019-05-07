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
        (me.x + 2, me.y): [Action('move', 'right'), Action('attack', 'right')]
    }

    me_pos = (me.x, me.y)
    print('My position %s' % str(me_pos))

    foes = [i for i in state.foes]
    foes_pos = list(map(lambda f: (f.x, f.y), foes))
    print('Foes position %s' % str(foes_pos))

    friends = [i for i in state.units]
    friends_pos = list(map(lambda f: (f.x, f.y), friends))
    print('Friends position %s' % str(friends_pos))

    print('Targets %s' % str(trg))
    for f in foes_pos:
        if f in trg:
            move = trg.get(f)
            print('Attack %s' % str(move))
            return move

    switcher = {
        0: [Action('move', 'left')],
        1: [Action('move', 'right')],
        2: [Action('move', 'down')],
        3: [Action('move', 'up')]
    }

    print('Unit %d , %d' % (state.unit.x, state.unit.y))
    print('FOE %d , %d' % (state.foes[0].x, state.foes[0].y))

    if (state.unit.x == state.units[0].x):
        return switcher.get(randint(2, 3))

    if (state.unit.y == state.units[0].y):
        return switcher.get(randint(0, 1))

    if (state.unit.x == state.units[1].x):
        return switcher.get(randint(2, 3))

    if (state.unit.y == state.units[1].y):
        return switcher.get(randint(0, 1))

    if (state.unit.x == state.units[2].x):
        return switcher.get(randint(2, 3))

    if (state.unit.y == state.units[2].y):
        return switcher.get(randint(0, 1))

    if (state.unit.x == state.foes[0].x):
        return switcher.get(randint(0, 1))

    if (state.unit.y == state.foes[0].y):
        return switcher.get(randint(2, 3))

    if (state.unit.x == state.foes[1].x):
        return switcher.get(randint(0, 1))

    if (state.unit.y == state.foes[1].y):
        return switcher.get(randint(2, 3))

    if (state.unit.x == state.foes[2].x):
        return switcher.get(randint(0, 1))

    if (state.unit.y == state.foes[2].y):
        return switcher.get(randint(2, 3))

    return switcher.get(randint(0, 3))


def get_player_info():
    return {
        "id": "Delphi",
        "name": "Delphi"
    }


def game_end():
    pass
