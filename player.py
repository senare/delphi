# Logic for controlling units

from game import Action, is_empty, Unit, GameState, build_distance_map
from random import randint

def get_actions(state):
  switcher = {
    0: [ Action('move', 'left'), Action('attack', 'left')   ]  ,  
    1: [ Action('move', 'right'), Action('attack', 'right')   ]  ,  
    2: [ Action('move', 'down'), Action('attack', 'down')   ]   ,
    3: [ Action('move', 'up'), Action('attack', 'up')   ]  ,
    4: [ Action('move', 'left'), Action('attack', 'left')   ]  ,  
    5: [ Action('move', 'down'), Action('attack', 'down')   ]   ,
    6: [ Action('move', 'right'), Action('attack', 'right')   ]  ,  
    7: [ Action('move', 'up'), Action('attack', 'up')   ]    
  }

  print('Unit %d , %d' % (state.unit.x, state.unit.y))
  print('FOE %d , %d' % (state.foes[0].x, state.foes[0].y))

  if(state.unit.x == state.units[0].x):
    return switcher.get(randint(2,3)) 
    
  if(state.unit.y == state.units[0].y):
    return switcher.get(randint(0,1)) 

  if(state.unit.x == state.units[1].x):
    return switcher.get(randint(2,3)) 
    
  if(state.unit.y == state.units[1].y):
    return switcher.get(randint(0,1)) 

  if(state.unit.x == state.units[2].x):
    return switcher.get(randint(2,3)) 
    
  if(state.unit.y == state.units[2].y):
    return switcher.get(randint(0,1)) 

  if(state.unit.x == state.foes[0].x):
    return switcher.get(randint(0,1)) 
    
  if(state.unit.y == state.foes[0].y):
    return switcher.get(randint(2,3)) 

  if(state.unit.x == state.foes[1].x):
    return switcher.get(randint(0,1)) 
    
  if(state.unit.y == state.foes[1].y):
    return switcher.get(randint(2,3)) 

  if(state.unit.x == state.foes[2].x):
    return switcher.get(randint(0,1)) 
    
  if(state.unit.y == state.foes[2].y):
    return switcher.get(randint(2,3)) 

  return switcher.get(randint(0,3)) 

def get_player_info():
  return {
    "id": "Delphi",
    "name": "Delphi"
  }

def game_end():
  pass