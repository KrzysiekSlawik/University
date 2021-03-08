from queue import Queue
from copy import deepcopy
class Vector2:
    def __init__(self, x:int, y:int):
        self.x:int = x
        self.y:int = y
    
    def __str__(self) -> str:
        return str(self.x)+str(self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)
'''
turn:bool #white = true, black = false
pieces order
white_rook [0]
white_king [1]
black_king [2]
state:{
    'turn' = bool
    'pieces' = list[Vector2]
    'prev_state' = key:str
}
'''
king_moves = [
    Vector2(1,1),
    Vector2(-1,-1),
    Vector2(1,-1),
    Vector2(-1,1),
    Vector2(1,0),
    Vector2(0,1),
    Vector2(-1,0),
    Vector2(0,-1),
]
def octile_distance(a:Vector2, b:Vector2) -> int:
    dx = abs(a.x - b.x)
    dy = abs(a.y - b.y)
    return (dx + dy) - min(dx, dy)
def on_board(pos:Vector2) -> bool:
    return pos.x >= 0 and pos.x < 8 and pos.y >= 0 and pos.y < 8

def is_empty(pos:Vector2, pieces:list[Vector2]) -> bool:
    return all(map(lambda other: other != pos, pieces))

def king_dist(pos1:Vector2, pos2:Vector2) -> bool:
    return octile_distance(pos1, pos2) > 1

def checked(pos:Vector2, pieces:list[Vector2]) -> bool:
    return pos.x == pieces[0].x or pos.y == pieces[0].y

def state_key(state) -> str:
    return str(state['turn'])+str(state['pieces'][0])+str(state['pieces'][1])+str(state['pieces'][2])

def white_king_moves(pieces:list[Vector2]) -> list[Vector2]:
    return [move+pieces[1] for move in king_moves if on_board(move+pieces[1]) and is_empty(move+pieces[1], pieces) 
                                                 and king_dist(move+pieces[1], pieces[2])]
def white_rook_moves(pieces:list[Vector2]) -> list[Vector2]:
    moves = []
    moves += [Vector2(x,pieces[0].y) for x in range(0,8) if on_board(Vector2(x,pieces[0].y))
                                                      and is_empty(Vector2(x,pieces[0].y), pieces)]
    moves += [Vector2(pieces[0].x, y) for y in range(0,8) if on_board(Vector2(pieces[0].x, y))
                                                      and is_empty(Vector2(pieces[0].x, y), pieces)]
    return moves

def black_king_moves(pieces:list[Vector2]) -> list[Vector2]:
    return [move+pieces[2] for move in king_moves if on_board(move+pieces[2]) and is_empty(move+pieces[2], pieces) 
                                                 and king_dist(move+pieces[2], pieces[1]) and not checked(move+pieces[2], pieces)]

def black_capture_rook(pieces:list[Vector2]) -> bool:
    return (abs(pieces[2].x-pieces[0].x) == 1 or abs(pieces[2].y-pieces[0].y) == 1) and king_dist(pieces[0], pieces[1])

def mate(state) -> bool:
    if state['turn']:
        return False
    if checked(state['pieces'][2], state['pieces']) and len(black_king_moves(state['pieces'])) == 0 and not black_capture_rook(state['pieces']):
        return True
    return False

def stalemate(state) -> bool:
    if state['turn']:
        return False
    moves = black_king_moves(state['pieces'])
    if not checked(state['pieces'][2], state['pieces']) and len(moves) == 0:
        
        return True
    if checked(state['pieces'][2], state['pieces']) and len(moves) == 0 and black_capture_rook(state['pieces']):
        
        return True
    return False

def state_from_move(prev_state, move:Vector2, piece:int):
    pieces = deepcopy(prev_state['pieces'])
    pieces[piece] = move
    return {
        'turn': not prev_state['turn'],
        'pieces': pieces,
        'prev_state': state_key(prev_state)
    }

'''
black c4 c8 h3
'''

def state_from_str(state:str):
    splited = state.split()
    w_king_pos = Vector2(ord(splited[1][0]) - 97, int(splited[1][1])-1)
    w_rook_pos = Vector2(ord(splited[2][0]) - 97, int(splited[2][1])-1)
    b_king_pos = Vector2(ord(splited[3][0]) - 97, int(splited[3][1])-1)
    return{
        'turn': splited[0] == 'white',
        'pieces': [
            w_rook_pos,
            w_king_pos,
            b_king_pos
        ],
        'prev_state': ''
    }

def legal_moves(state) -> list:
    if state['turn']:
        #white
        rook = white_rook_moves(state['pieces'])
        def inner(move):
            return state_from_move(state, move, 0)
        states_rook = list(map(inner, rook))
        king = white_king_moves(state['pieces'])
        def inner(move):
            return state_from_move(state, move, 1)
        states_king = list(map(inner, king))
        return states_rook + states_king
    #black
    king = black_king_moves(state['pieces'])
    def inner(move):
            return state_from_move(state, move, 2)
    return list(map(inner, king))



def BFS(root):
    Q:Queue = Queue()
    states = {state_key(root): root}
    Q.put(root)
    while Q.not_empty:
        state = Q.get()
        if mate(state):
            return [states, state]
        if stalemate(state):
            continue
        for next_state in legal_moves(state):
            key = state_key(next_state)
            if not key in states:
                Q.put(next_state)
                states[state_key(next_state)] = next_state

def state_depth(states, state) -> int:
    if state['prev_state'] == '':
        return 0
    return 1 + state_depth(states, states[state['prev_state']])

def state_steps(states, state) -> list:
    if state['prev_state'] == '':
        return [state]
    return state_steps(states, states[state['prev_state']]) + [state]

black_king = '\N{white chess king} '#white is more blackish in my console o_0
white_king = '\N{black chess king} '
white_rook = '\N{black chess rook} '
white_square = '\N{black square} '
black_square = '\N{white square} '

def print_steps(steps):
    for step in steps:
        print_state(step)

def print_state(state):
    board = ''
    white_rook_pos = state['pieces'][0]
    white_king_pos = state['pieces'][1]
    black_king_pos = state['pieces'][2]
    for y in reversed(range(0,8)):
        for x in range(0,8):
            pos = Vector2(x,y)
            if white_rook_pos == pos:
                board += white_rook
            elif white_king_pos == pos:
                board += white_king
            elif black_king_pos == pos:
                board += black_king
            else:
                if (x + y) % 2 == 0:
                    board += black_square
                else:
                    board += white_square
        board += '\n'
    print(board)


root = state_from_str('black c2 d2 a1')
state = BFS(root)
print('steps' + str(state_depth(*state)))
print_steps(state_steps(*state)) 

