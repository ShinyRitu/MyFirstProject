# Tic_Tac_Toe Game: using some AI concepts

from random import randrange


def insertLetter(le, pos):
    board[pos] = le


def spaceIsFree(pos):
    return board[pos] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(bo, le):
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (
                bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (
                       bo[2] == le and bo[5] == le and bo[8] == le) or (
                       bo[3] == le and bo[6] == le and bo[9] == le) or (
                       bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True

    while (run):
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    insertLetter("X", move)
                    run = False
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')

        except:
            print('Please type a number!')


def compMove():
    # Create a list of possible moves
    possible_moves = [i for i, letter in enumerate(board) if board[i] == ' ' and i != 0]
    move = 0

    # 1st logic: Check for possible winning move to take or to block opponents winning move
    for let in ['O', 'X']:
        for i in possible_moves:
            boardcpy = board[:]
            boardcpy[i] = let
            if isWinner(boardcpy, let):
                move = i
                return move

    # 2nd logic: Try to take one of the corners
    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = selectRandom(corners_open)
        return move

    # 3rd logic: Try to take the center
    if 5 in possible_moves:
        move = 5
        return move

    # 4th logic: Take any edge
    edge_open = []
    for i in possible_moves:
        if i in [2, 4, 8, 6]:
            edge_open.append(i)

    if len(edge_open) > 0:
        move = selectRandom(edge_open)

    return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():

    printBoard(board)

    while not (isBoardFull(board)):
        if not (isWinner(board, 'O')):
            playerMove()
            #printBoard(board)
        else:
            print('Sorry!, ' + name + ' computer\'s won this match :(')
            #com_score+=1
            break

        if not (isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')

                printBoard(board)

        else:
            print('You won this match:)..Good job ' + name)
            #your_score+=1
            break

    if isBoardFull(board):
        print('Tie Game!!')


a = True
name = input('Type your name here: ')


while (a):

    answer = input('Are you ready for the game? yes/ no: ')

    if answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('WELCOME TO TIC TAC TOE GAME!!!')
        main()
        
    else:

        print('Hope you are enjoying it a lot....See you again ' + name + ':)')
        quit()



