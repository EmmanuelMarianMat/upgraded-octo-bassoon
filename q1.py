from random import randint,choice
from typing import SupportsComplex
class Environment:
    def __init__(self, a_dirty: bool, b_dirty: bool) -> None:
        self.room_dict = { 'A':a_dirty, 'B':b_dirty }
    
class SimpleReflexAgent:
    def __init__(self) -> None:
        pass
    
    def suck(self, env: Environment, loc: str):
        env.room_dict[loc] = False
    
    def left(self):
        self.vacuum_loc = 'A'
    
    def right(self):
        self.vacuum_loc = 'B'

    def clean(self, env: Environment, iniital_position: str):
        self.vacuum_loc = iniital_position
        self.score = 0
        self.positions = []
        for _ in range(1000):
            self.positions.append(self.vacuum_loc)
            print('Position:', self.vacuum_loc, end=" ")
            if env.room_dict[self.vacuum_loc]:
                print('Action: SUCK')
                self.suck(env, self.vacuum_loc)
            else:
                if self.vacuum_loc == 'A':
                    print('Action: RIGHT')
                    self.right()
                else:
                    print('Action: LEFT')
                    self.left()
            self.score += sum(not env.room_dict[key] for key in env.room_dict)
        print('Score =',self.score)
        print('State space search path:', '->'.join(self.positions))
        
vacuum_cleaner = SimpleReflexAgent()

i = 1
for a_dirty, b_dirty, initial_position in [
    (True,True,'A'),(True,True,'B'),(True,False,'A'),(True,False,'B'),
    (False,True,'A'),(False,True,'B'),(False,False,'A'),(False,False,'B')]:
    print('Configuration', i)

    if a_dirty:
        print('A is dirty')
    else:
        print('A is clean')

    if b_dirty:
        print('B is dirty')
    else:
        print('B is clean')

    print('Initial Location of the vacuum cleaner is', initial_position)
    env = Environment(a_dirty,b_dirty)
    vacuum_cleaner.clean(env, initial_position)
    print()
    i+=1



