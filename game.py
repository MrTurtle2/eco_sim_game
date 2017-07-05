'''
Economic Simulation Game
David Buick & Leo Calder-Knight
2017
'''


def start_game():
    '''initialises game'''
    size = int(input('Input map size (nxn):'))
    _map = create_map(size)
    return _map


def create_map(size):
    '''makes map'''
    i = 0
    j = 0
    the_map = []
    while i < size:
        the_map.append([])
        i += 1
    return the_map
    
    
the_map = start_game()
print(the_map)


