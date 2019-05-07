# Logic for controlling units

from random import randint

from game import Action


def get_actions(state):
    me = state.unit
    foes = [f for f in state.foes if f.health > 0]
    friends = [f for f in state.units if f.health > 0]

    trg = {
        (me.x, me.y + 1): [Action('attack', 'down'), Action('move', 'up')],
        (me.x, me.y - 1): [Action('attack', 'up'), Action('move', 'left')],
        (me.x - 1, me.y): [Action('attack', 'left'), Action('move', 'up')],
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

    for f in foes:
        if (f.x, f.y) in trg:
            return trg.get((f.x, f.y))

    for f in foes:
        if f.x == me.x:
            return [Action('move', 'left')]

    for f in foes:
        if f.y == me.y:
            return [Action('move', 'up')]

    for f in friends:
        if f.x == me.x:
            return [Action('move', 'up')]

    for f in friends:
        if f.y == me.y:
            return [Action('move', 'left')]

    move = {
        1: [Action('move', 'up')],
        2: [Action('move', 'left')]
    }

    pos = {
        1: (me.x, me.y + 1),
        2: (me.x - 1, me.y)
    }

    default = randint(1, 2)
    default_pos = pos.get(default)

    if state.empty_map[default_pos[0]][default_pos[1]]:
        return move.get(default)

    if default == 1:
        return move.get(2)
    else:
        return move.get(1)


def get_player_info():
    return {
        "id": "Delphi",
        "name": "Delphi"
    }


def game_end():
    pass
