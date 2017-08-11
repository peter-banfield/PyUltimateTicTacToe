# Ultimate tic tac toe in ascii art
# UTTTv1.py by PeterB, AbbyC, MatthewB, GordonM
# Future work: Graphics!!! (this version would be functional and work as a submission but it would be nice to have a GUI)

import time # IM NOT SURE IF THIS IS USED AGAIN
import random

# Defining the small boards
Board1BL = [1, 2, 3, 10, 11, 12, 19, 20, 21]
Board2BM = [4, 5, 6, 13, 14, 15, 22, 23, 24]
Board3BR = [7, 8, 9, 16, 17, 18, 25, 26, 27]
Board4CL = [28, 29, 30, 37, 38, 39, 46, 47, 48]
Board5CM = [31, 32, 33, 40, 41, 42, 49, 50, 51]
Board6CR = [34, 35, 36, 43, 44, 45, 52, 53, 54]
Board7UL = [55, 56, 57, 64, 65, 66, 73, 74, 75]
Board8UM = [58, 59, 60, 67, 68, 69, 76, 77, 78]
Board9UR = [61, 62, 63, 70, 71, 72, 79, 80, 81]
SMALLBLIST = [Board1BL, Board2BM, Board3BR, Board4CL, Board5CM, Board6CR, Board7UL, Board8UM, Board9UR]


def drawBoard(b, t):
    # This function prints out the board that it was passed.

    # "board" is a list of 81 strings representing the board (ignore index 0)
    print(t[7]+'           |'+t[8]+'            |'+t[9])
    print(' ' + b[73] + ' | ' + b[74] + ' | ' + b[75] + '  |  ' + b[76] + ' | ' + b[77] + ' | ' + b[78] + '  |  ' + b[79] + ' | ' + b[80] + ' | ' + b[81])
    print(' ---------  |  ---------  |  ---------')
    print(' ' + b[64] + ' | ' + b[65] + ' | ' + b[66] + '  |  ' + b[67] + ' | ' + b[68] + ' | ' + b[69] + '  |  ' + b[70] + ' | ' + b[71] + ' | ' + b[72])
    print(' ---------  |  ---------  |  ---------')
    print(' ' + b[55] + ' | ' + b[56] + ' | ' + b[57] + '  |  ' + b[58] + ' | ' + b[59] + ' | ' + b[60] + '  |  ' + b[61] + ' | ' + b[62] + ' | ' + b[63])
    print('7           |8            |9')
    print('---------------------------------------')
    print(t[4]+'           |'+t[5]+'            |'+t[6])
    print(' ' + b[46] + ' | ' + b[47] + ' | ' + b[48] + '  |  ' + b[49] + ' | ' + b[50] + ' | ' + b[51] + '  |  ' + b[52] + ' | ' + b[53] + ' | ' + b[54])
    print(' ---------  |  ---------  |  ---------')
    print(' ' + b[37] + ' | ' + b[38] + ' | ' + b[39] + '  |  ' + b[40] + ' | ' + b[41] + ' | ' + b[42] + '  |  ' + b[43] + ' | ' + b[44] + ' | ' + b[45])
    print(' ---------  |  ---------  |  ---------')
    print(' ' + b[28] + ' | ' + b[29] + ' | ' + b[30] + '  |  ' + b[31] + ' | ' + b[32] + ' | ' + b[33] + '  |  ' + b[34] + ' | ' + b[35] + ' | ' + b[36])
    print('4           |5            |6')
    print('---------------------------------------')
    print(t[1]+'           |'+t[2]+'            |'+t[3])
    print(' ' + b[19] + ' | ' + b[20] + ' | ' + b[21] + '  |  ' + b[22] + ' | ' + b[23] + ' | ' + b[24] + '  |  ' + b[25] + ' | ' + b[26] + ' | ' + b[27])
    print(' ---------  |  ---------  |  ---------')
    print(' ' + b[10] + ' | ' + b[11] + ' | ' + b[12] + '  |  ' + b[13] + ' | ' + b[14] + ' | ' + b[15] + '  |  ' + b[16] + ' | ' + b[17] + ' | ' + b[18])
    print(' ---------  |  ---------  |  ---------')
    print(' ' + b[1] + ' | ' + b[2] + ' | ' + b[3] + '  |  ' + b[4] + ' | ' + b[5] + ' | ' + b[6] + '  |  ' + b[7] + ' | ' + b[8] + ' | ' + b[9])
    print('1           |2            |3')
    
def inputPlayerLetter():
    # Let's the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('\nWill Player 1 be X or O? (x/o)')
        letter = input().upper()

    # the first element in the tuple is the player's letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def difficulty():
    #Function changes difficulty
    print('\nHow difficult do you want the game to be? Easy, Medium, or Hard?')
    print('Each difficulty changes how the game handles ties on small boards.')
    print('In Easy(e): tie = board win X and O.')
    print('In Medium(m): tie = board reset.')
    print('In Hard(h): tie = board lost no win.')
    print('Please enter a difficulty.(e/m/h)')
    while True:
        level= input().lower()
        if level not in 'e h m easy medium hard'.split():
            print('Please choose difficulty. Easy, Medium, or Hard.(e/m/h)')
        else:
            break
    if level.startswith('e'):
        print('You have chosen Easy where a small board tied counts as a win for both players.')
        return 1
    elif level.startswith('m'):
        print('you have chosen Medium where a small board tied resets to an unplayed board.')
        return 2
    else:
        print('You have chosen Hard where a small board tied will never counnt as a win for either of the players.')
        return 3

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (y/n)')
    return input().lower().startswith('y')

def getPlayerMove(boardS, boardB):
    # Let the player type in their move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print('What is your next move? (1-9)') # The moves corrispond to the position of the numbers on a number pad
        move = input()
        if move in '1 2 3 4 5 6 7 8 9'.split():
            if boardB[boardS[int(move)-1]] == ' ':
                break
            else:
                print('Invalid move choice-Space full.')
                move = ' '
    move = int(move)-1
    return move

def makeMove(boardS, letter, move, boardB):# Makes move if space is empty
    if boardB[boardS[move]] == ' ':
        boardB[boardS[move]] = letter
        return True
    else:
        print('Invalid move choice-Space full.')
        return False

def getBoardChoice(move):
    # If a move has been made this puts the player in that board
    if (move==0 or move==1 or move==2 or move==3 or move==4 or move==5 or move==6 or move==7 or move==8) and (totalBoard[move+1] != 'X' and totalBoard[move+1] !='O' and totalBoard[move+1] != 'T' and totalBoard[move+1] !='L'):
        board = move
        print('You are playing in board '+str(board+1))
    # This part of the function has the user select which board to play on
    else:
        print('You can choose any board.')
        board = ' '
        while board not in '1 2 3 4 5 6 7 8 9'.split(): # The board corrispond to the position of the numbers on a number pad
            print('Which board do you want to play on? (1-9)')
            board = input()
            if board in '1 2 3 4 5 6 7 8 9'.split():
                if totalBoard[int(board)] == ' ':
                    break
                else:
                    print('Invalid board choice-Board full.')
                    board = ' '
        board = (int(board)-1)
    return board

def selectBoard(board): # Selects the board with player choice
    smallB = ' '
    if board == 0:
        smallB = Board1BL
    elif board == 1:
        smallB = Board2BM
    elif board == 2:
        smallB = Board3BR
    elif board == 3:
        smallB = Board4CL
    elif board == 4:
        smallB = Board5CM
    elif board == 5:
        smallB = Board6CR
    elif board == 6:
        smallB = Board7UL
    elif board == 7:
        smallB = Board8UM
    else:
        smallB = Board9UR
    return smallB

def smallWinner(bo, le, player):
    # check if small board won
    count = 0
    for i in (SMALLBLIST):
        count = count + 1
        if totalBoard[count] != 'X' and totalBoard[count] != 'O' and totalBoard[count] != 'T' and totalBoard[count] != 'L':
            if (# check vertical
                (bo[i[0]] == le and bo[i[3]] == le and bo[i[6]] == le)or
                (bo[i[1]] == le and bo[i[4]] == le and bo[i[7]] == le)or
                (bo[i[2]] == le and bo[i[5]] == le and bo[i[8]] == le)or
                #check horizontal
                (bo[i[0]] == le and bo[i[1]] == le and bo[i[2]] == le)or
                (bo[i[3]] == le and bo[i[4]] == le and bo[i[5]] == le)or
                (bo[i[6]] == le and bo[i[7]] == le and bo[i[8]] == le)or
                # check / diagonal spaces
                (bo[i[8]] == le and bo[i[4]] == le and bo[i[0]] == le)or
                # check \ diagonal spaces
                (bo[i[6]] == le and bo[i[4]] == le and bo[i[2]] == le)):
                    winnerBoard(le, i)
                    print(player + ' has won a small board!') # Prints out a message saying that the player has won a small board

def winnerBoard(le, bo): # sets won board to player letter
    for i in (0, 1, 2, 3, 4, 5, 6, 7, 8): 
        theBoard[bo[i]] = le 
    if bo == Board1BL:
        totalBoard[1] = le
    elif bo == Board2BM:
        totalBoard[2] = le
    elif bo == Board3BR:
        totalBoard[3] = le
    elif bo == Board4CL:
        totalBoard[4] = le
    elif bo == Board5CM:
        totalBoard[5] = le
    elif bo == Board6CR:
        totalBoard[6] = le
    elif bo == Board7UL:
        totalBoard[7] = le
    elif bo == Board8UM:
        totalBoard[8] = le
    else:
        totalBoard[9] = le
                   
def isWinner(bo, le): # Checks for a winner small board
    if (# check vertical
        (((bo[1]==le)or(bo[1]=='T'))and((bo[4]==le)or(bo[4]=='T'))and((bo[7]==le)or(bo[7]=='T')))or
        (((bo[2]==le)or(bo[2]=='T'))and((bo[5]==le)or(bo[5]=='T'))and((bo[8]==le)or(bo[8]=='T')))or
        (((bo[3]==le)or(bo[3]=='T'))and((bo[6]==le)or(bo[6]=='T'))and((bo[9]==le)or(bo[9]=='T')))or
        #check horizontal
        (((bo[1]==le)or(bo[1]=='T'))and((bo[2]==le)or(bo[2]=='T'))and((bo[3]==le)or(bo[3]=='T')))or
        (((bo[4]==le)or(bo[4]=='T'))and((bo[5]==le)or(bo[5]=='T'))and((bo[6]==le)or(bo[6]=='T')))or
        (((bo[7]==le)or(bo[7]=='T'))and((bo[8]==le)or(bo[8]=='T'))and((bo[9]==le)or(bo[9]=='T')))or
        # check / diagonal spaces
        (((bo[9]==le)or(bo[9]=='T'))and((bo[5]==le)or(bo[5]=='T'))and((bo[1]==le)or(bo[1]=='T')))or
        # check \ diagonal spaces
        (((bo[7]==le)or(bo[7]=='T'))and((bo[5]==le)or(bo[5]=='T'))and((bo[3]==le)or(bo[3]=='T')))):
        return True
    else:
        return False

def smallTie(difficulty): # Checks for a tie on small board
    # check if small board tie
    count = 0
    for i in (SMALLBLIST):
        count = count + 1
        if totalBoard[count] != 'X' and totalBoard[count] != 'O' and totalBoard[count] != 'T' and totalBoard[count] != 'L':
            if isBoardFull(i) and difficulty == 1:
                totalBoard[count] = 'T'
                for k in range(0, 9): 
                    theBoard[i[k]] = 'T'
                print('A board has been tied.')
            elif isBoardFull(i) and difficulty == 2:
                for k in range(0, 9): 
                    theBoard[i[k]] = ' '
                print('A board has been tied.')
                print('Board Reset To Empty.')
            elif isBoardFull(i) and difficulty == 3:
                totalBoard[count] = 'L'
                for k in range(0, 9): 
                    theBoard[i[k]] = 'L'
                print('A board has been tied.')
                print('Board Locked.')
            else:
                return False

def largeTie(bo, le1, le2): # Checks for win
    if bo[1]==' 'or bo[2]==' 'or bo[3]==' 'or bo[4]==' 'or bo[5]==' 'or bo[6]==' 'or bo[7]==' 'or bo[8]==' 'or bo[9]==' ':
        return False
    elif((# check vertical
        (((bo[1]==le1)or(bo[1]=='T'))and((bo[4]==le1)or(bo[4]=='T'))and((bo[7]==le1)or(bo[7]=='T')))or
        (((bo[2]==le1)or(bo[2]=='T'))and((bo[5]==le1)or(bo[5]=='T'))and((bo[8]==le1)or(bo[8]=='T')))or
        (((bo[3]==le1)or(bo[3]=='T'))and((bo[6]==le1)or(bo[6]=='T'))and((bo[9]==le1)or(bo[9]=='T')))or
        #check horizontal
        (((bo[1]==le1)or(bo[1]=='T'))and((bo[2]==le1)or(bo[2]=='T'))and((bo[3]==le1)or(bo[3]=='T')))or
        (((bo[4]==le1)or(bo[4]=='T'))and((bo[5]==le1)or(bo[5]=='T'))and((bo[6]==le1)or(bo[6]=='T')))or
        (((bo[7]==le1)or(bo[7]=='T'))and((bo[8]==le1)or(bo[8]=='T'))and((bo[9]==le1)or(bo[9]=='T')))or
        # check / diagonal spaces
        (((bo[9]==le1)or(bo[9]=='T'))and((bo[5]==le1)or(bo[5]=='T'))and((bo[1]==le1)or(bo[1]=='T')))or
        # check \ diagonal spaces
        (((bo[7]==le1)or(bo[7]=='T'))and((bo[5]==le1)or(bo[5]=='T'))and((bo[3]==le1)or(bo[3]=='T'))))and
        (# check vertical
        (((bo[1]==le2)or(bo[1]=='T'))and((bo[4]==le2)or(bo[4]=='T'))and((bo[7]==le2)or(bo[7]=='T')))or
        (((bo[2]==le2)or(bo[2]=='T'))and((bo[5]==le2)or(bo[5]=='T'))and((bo[8]==le2)or(bo[8]=='T')))or
        (((bo[3]==le2)or(bo[3]=='T'))and((bo[6]==le2)or(bo[6]=='T'))and((bo[9]==le2)or(bo[9]=='T')))or
        #check horizontal
        (((bo[1]==le2)or(bo[1]=='T'))and((bo[2]==le2)or(bo[2]=='T'))and((bo[3]==le2)or(bo[3]=='T')))or
        (((bo[4]==le2)or(bo[4]=='T'))and((bo[5]==le2)or(bo[5]=='T'))and((bo[6]==le2)or(bo[6]=='T')))or
        (((bo[7]==le2)or(bo[7]=='T'))and((bo[8]==le2)or(bo[8]=='T'))and((bo[9]==le2)or(bo[9]=='T')))or
        # check / diagonal spaces
        (((bo[9]==le2)or(bo[9]=='T'))and((bo[5]==le2)or(bo[5]=='T'))and((bo[1]==le2)or(bo[1]=='T')))or
        # check \ diagonal spaces
        (((bo[7]==le2)or(bo[7]=='T'))and((bo[5]==le2)or(bo[5]=='T'))and((bo[3]==le2)or(bo[3]=='T'))))):
        return True
    else:
        return True
    
 
def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    if theBoard[board[0]]==' 'or theBoard[board[1]]==' 'or theBoard[board[2]]==' 'or theBoard[board[3]]==' 'or theBoard[board[4]]==' 'or theBoard[board[5]]==' 'or theBoard[board[6]]==' 'or theBoard[board[7]]==' 'or theBoard[board[8]]==' ':
        return False
    else:
        return True

def playerTurn(playerLetter, Lastmove, otherPlayer, turn): # carries out the players turn
    MoveCheck = False
    while MoveCheck == False:
        drawBoard(theBoard, totalBoard)
        print(turn+'('+playerLetter+'\'s) it is your turn.')
        board = selectBoard(getBoardChoice(Lastmove))
        move = getPlayerMove(board, theBoard)
        MoveCheck = makeMove(board, playerLetter, move, theBoard)
    return move
  
def menu(): # Main menu and rules
    print('Welcome to Ultimate Tic-Tac-Toe!\n')
    print('XOXOXOXOXOXOXOXOXOXOXO')
    print ("M A I N - M E N U") 
    print('XOXOXOXOXOXOXOXOXOXOXO\n')
    print("Would you like to see the rules (y/n)?")
    choice = input().lower()
    if choice.startswith('y'):
        print('''
In Ultimate Tic-Tac-Toe the goal is to win three
small Tic-Tac-Toe boards in a row set in a
larger Tic-Tac-Toe grid. Players will take turns
selecting a location to play on the board. The
first player to play will select which board on
the larger board to play on and then select a
position on that board. Every move after the first
board selection will be in the larger board location
corresponding to the location selected by the
previous player.\n''')
        input('Press enter to continue')
        print('''
If the board location the player
is supposed to play in has already been won the
player will instead be allowed to choose any
available location on the larger board. In the
case of a tie on a small board the difficulty
level will dictate what happens. In easy mode
a tie will result in the small board counting as
a win for both players. In medium mode ties wipe
the board as if no one had played in the board.
In hard a tied board will be locked as unable
to be won by any player.
''')
        print()
        print("X O X O X O X O X O X O X O X O X O X O X O")
        print()
    

menu()# Calls the menu function

while True:
    # Reset the board
    theBoard = [' '] * 82
    totalBoard = [' '] * 10
    player1Letter, player2Letter = inputPlayerLetter()
    turn = whoGoesFirst()
    move = 'x'
    print( turn + ' will go first.')
    diff = difficulty()
    gameIsPlaying = True


    
    while gameIsPlaying:
        if turn == 'Player 1':
            # Player1 turn.
            # player move
            move = playerTurn(player1Letter, move, player2Letter, turn)

            # Win/tie checks
            smallTie(diff)
            smallWinner(theBoard, player1Letter, turn)                       
            if largeTie(totalBoard, player1Letter, player2Letter):
                drawBoard(theBoard, totalBoard)
                print('The game is a tie!')
                break
            else:
                if isWinner(totalBoard, player1Letter):
                    drawBoard(theBoard, totalBoard)
                    print('Hooray! Player 1 has won the game!')
                    gameIsPlaying = False
                else:
                    turn = 'Player 2'

        else:
            # Player2 turn.
            # player move
            move = playerTurn(player2Letter, move, player2Letter, turn)

            # Win/tie checks
            smallTie(diff)
            smallWinner(theBoard, player2Letter, turn)
            if largeTie(totalBoard, player1Letter, player2Letter):
                drawBoard(theBoard, totalBoard)
                print('The game is a tie!')
                break
            else:
                if isWinner(totalBoard, player2Letter):
                    drawBoard(theBoard, totalBoard)
                    print('Hooray! Player 2 has won the game!')
                    gameIsPlaying = False 
                else:
                    turn = 'Player 1'

    if not playAgain(): # Play again loop
        break
