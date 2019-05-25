xwin=1
owin=-1
draw=0
x='x'
o='o'
b='_'
import copy

#x always goes first

def static_evaluation(pos):
    #check the rows
    for row in pos:
        if row[0]==row[1]==row[2] and row[0]!=b:
            return xwin if row[0]==x else owin
    #check columns
    for i in range(3):
        if pos[0][i]==pos[1][i]==pos[2][i] and pos[0][i]!=b:
            return xwin if pos[0][i]==x else owin
    #check both diagonals
    if pos[0][0]==pos[1][1]==pos[2][2] and pos[0][0]!=b:
        return xwin if pos[0][0]==x else owin
    if pos[2][0]==pos[1][1]==pos[0][2] and pos[2][0]!=b:
        return xwin if pos[2][0]==x else owin
    return draw

##returns True if the board is full, otherwise False            
def isboardfull(pos):
    for i in range(3):
        for j in range(3):
            if pos[i][j]==b:
                return False
    return True

#defines the depth of the board, which is the number of empty spaces
def depth(pos):
    empty=0
    for i in range(3):
        for j in range(3):
            if pos[i][j]==b:
                empty+=1
    return empty

#return True if it's xturn (x always goes first), otherwise false
def xturn(pos):
    x_count=0
    for row in pos:
        x_count+=row.count(x)
        x_count-=row.count(o)
    return x_count==0

#returns the possible moves from a board and whose turn
def child(pos,xturn):
    symbol=x if xturn else o
    branches=[]
    for i in range(3):
        for j in range(3):
            if pos[i][j]==b:
                branches.append(copy.deepcopy(pos))
                branches[-1][i][j]=symbol
    return branches

#minimax algorithm based on wikipedia pseudocode
def minimax(pos,depth,xturn):
    if static_evaluation!=draw:
        return static_evaluation(pos)
    elif isboardfull(pos):
        return draw
    if xturn(pos):
        value=float('-inf')
        for branch in child(pos,True):
            value=max(value,minimax(branch,depth-1,True))
        return value
    else:
        value=float('inf')
        for branch in child(pos,False):
            value=min(value,minimax(branch,depth-1,False))
        return value

##example of my failure
board=[[x,o,x],
       [x,o,b],
       [b,b,b]]
# in this example, its o's turn and it should obviously play the bottom center square to win
print(minimax(board,depth(board),xturn(board)))
