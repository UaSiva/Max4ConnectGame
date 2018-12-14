import sys
from MaxConnect4Game import *
import copy
        
def final_cal_result(prev_Game, colVar):
    newGame = maxConnect4Game()

    try:
        newGame.nodeDepth = prev_Game.nodeDepth + 1
    except AttributeError:
        newGame.nodeDepth = 1

    newGame.pieceCount = prev_Game.pieceCount
    newGame.gameBoard = copy.deepcopy(prev_Game.gameBoard)
    if not newGame.gameBoard[0][colVar]:
        for i in range(5, -1, -1):
            if not newGame.gameBoard[i][colVar]:
                newGame.gameBoard[i][colVar] = prev_Game.currentTurn
                newGame.pieceCount += 1
                break
    if prev_Game.currentTurn == 1:
        newGame.currentTurn = 2
    elif prev_Game.currentTurn == 2:
        newGame.currentTurn = 1

    newGame.checkPieceCount()
    newGame.countScore()

    return newGame

def legalMovesfunc(brepres):
    legalMovesvar1 = []
    for col, var_col in enumerate(brepres[0]):
        if var_col == 0:
            legalMovesvar1.append(col)
    return legalMovesvar1

class Minimax:
    def __init__(self, game, depth):
        self.currentTurn = game.currentTurn
        self.game = game
        self.maxPossibleDepth = int(depth)
        
    def to_decide_func(self):

        values_from_min = []
        legalMovesvar2 = legalMovesfunc(self.game.gameBoard)

        for move in legalMovesvar2:

            our_result = final_cal_result(self.game,move)
            values_from_min.append( self.minVal(our_result,99999,-99999) )


        chosen = legalMovesvar2[values_from_min.index( max( values_from_min ) )]
        return chosen

    def minVal(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxPossibleDepth:
            return self.eval_utility(state)
        meh1 = 99999

        for move in legalMovesfunc(state.gameBoard):
            anew1 = final_cal_result(state,move)

            meh1 = min(meh1,self.maxVal( anew1,alpha,beta ))
            if meh1 <= alpha:
                return meh1
            beta = min(beta, meh1)
        return meh1
        
    def maxVal(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxPossibleDepth:
            return self.eval_utility(state)
        meh2 = -99999

        for move in legalMovesfunc(state.gameBoard):
            anew2 = final_cal_result(state,move)

            meh2 = max(meh2,self.minVal( anew2,alpha,beta ))
            if meh2 >= beta:
                return meh2
            alpha = max(alpha, meh2)
        return meh2

    def eval_utility(self,state):
        if self.currentTurn == 1:
            util = state.player1Score * state.player1Score - state.player2Score * state.player2Score
        elif self.currentTurn == 2:
            util = state.player2Score * state.player2Score - state.player1Score * state.player2Score

        return util


def miscwork(currentGame,move):
    
    print('\n\nMove no. %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, move+1))
    if currentGame.currentTurn == 1:
        currentGame.currentTurn = 2
    elif currentGame.currentTurn == 2:
        currentGame.currentTurn = 1

    print 'Game state after move:'
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()

def oneMoveGame(currentGame,depth):
    if currentGame.pieceCount == 42:    
        print 'BOARD FULL\n\nGame Over!\n'
        sys.exit(0)

    
    search_tree_arr_var = Minimax(currentGame,depth)
    move = search_tree_arr_var.to_decide_func()
    effect = currentGame.playPiece(move)
    miscwork(currentGame,move)
    currentGame.gameFile.close()


def interactiveGame(currentGame,depth):
    

    while not currentGame.pieceCount == 42:
        if currentGame.currentTurn == 1:
            userMove = input("ENTER THE COLUMN NUMBER THAT YOU WANT TO PLAY. VALUES ACCEPTED [1-7] ")
            if not 0 < userMove < 8:
                print "Invalid column number!"
                continue
            if not currentGame.playPiece(userMove-1):
                print "This column is full!"
                continue
            try:
                currentGame.gameFile = open("human.txt", 'w')
            except:
                sys.exit('THERE WAS AN ERROR OPENING THE OUTPUT FILE')
            miscwork(currentGame,userMove-1)

        elif not currentGame.pieceCount == 42:
            search_tree_arr_var = Minimax(currentGame,depth)
            move = search_tree_arr_var.to_decide_func()
            effect = currentGame.playPiece(move)
            try:
                currentGame.gameFile = open("comupter.txt", 'w')
            except:
                sys.exit('THERE WAS AN ERROR OPENING THE OUTPUT FILE')
            miscwork(currentGame,move)

    currentGame.gameFile.close()

    if currentGame.player1Score > currentGame.player2Score:
        print "Player 1 wins"
    elif currentGame.player2Score > currentGame.player1Score:
        print "Computer wins"
    else:
        print "It's a draw"
    print "THANK YOU FOR PLAYING MAXCONNECT4 !!! FEEL FREE TO PLAY AGAIN :)"

def main(argv):
    
    if len(argv) != 5:
        print 'Four command-line arguments are needed:'
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() 

    
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print '\nMaxConnect-4 game\n'
    print 'Game state before move:'
    currentGame.printGameBoard()

    
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == 'computer-next': 
            currentGame.currentTurn = 2
        else: 
            currentGame.currentTurn = 1
        interactiveGame(currentGame,argv[4]) 
    else: 
        
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('THERE WAS AN ERROR OPENING THE OUTPUT FILE')
        oneMoveGame(currentGame,argv[4]) 

if __name__ == '__main__':
    main(sys.argv)



