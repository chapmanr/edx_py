#Week 2 homework
import numpy as numpy
import random


random.seed(1)


def create_board():
    return numpy.zeros((3,3), dtype=int)

def place(board, player, position):
    #print("set ", position)
    board[position[0]][position[1]]=player
    #print(board)


def possibilities(board):
    result = [tuple(coord) for coord in numpy.argwhere(numpy.array(board) == 0).tolist()]
    return result

def random_place(board, player):
    poss = possibilities(board)
    if len(poss) > 0:
        selected = random.choice(poss)
        #print("Selected=",selected)
        place(board,player,selected)
        return True
    return False

def row_win(board, player):
    for y in board:
        if all(x == player for  x in y):
            return True
    return False
        
def col_win(board, player):
    new_board = numpy.transpose(board)
    return row_win(new_board, player)

def test_diagr(board, player):
    diag = [(0,0), (1,1), (2,2) ]
    count = 0
    for diag_pos in diag:
        if(board[diag_pos]==player):
            count = count + 1
    if(count == 3):
        return True
    return False

def test_diagl(board, player):
    diag = [(2,0), (1,1), (0,2) ]
    count = 0
    for diag_pos in diag:
        if(board[diag_pos]==player):
            count = count + 1
    if(count == 3):
        return True
    return False

def diag_win(board, player):
    if test_diagr(board, player):
        return True
    elif test_diagl(board, player):
        return True
    return False

def evaluate(board, players):
    winner = 0
    for player in players:
        if(row_win(board, player) or col_win(board, player) or diag_win(board, player)):
            winner = player    
    if numpy.all(board != 0 ) and winner == 0:
        winner = -1
    return winner


def test_range():
    for i in range(10, 0, -1):
        print(i)


player1 = int(1)
player2 = int(2)

def play_game():
    ttt = create_board()    
    result = 0
    players = [player1, player2]
    count = 0
    while result == 0:
            index = count % 2
            #print(index)
            if(count==0):
                ttt[1,1]=player1
            else:
                random_place(ttt, players[index])
            result = evaluate(ttt, players)
            count = count + 1
    print("count = ", count, " result = ", result)
    return result

def run_test_game():
    results = []
    for i in range(1000):
        results.append(play_game())
    num_player1 = numpy.sum([i==player1 for i in results])
    print(num_player1)
    num_player2 = numpy.sum([i==player2 for i in results])
    print(num_player2)
    no_wins = numpy.sum([i==-1 for i in results])
    print(no_wins)
    #print(results)




def test_diag():
    ttt = create_board() 
    ttt[0,0]=2
    ttt[1,1]=2
    ttt[2,2]=2
    print(ttt)
    print(test_diagr(ttt, 2))
    print(test_diagr(ttt, 1))
    
    ttt[2,0]=1
    ttt[1,1]=1
    ttt[0,2]=1
    print(ttt)
    print(test_diagl(ttt, 2))
    print(test_diagl(ttt, 1))
    

#test_diag()
run_test_game()
