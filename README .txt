NAME    :SIVA SUBRAMANINAN PARI ARIVAZHAGAN
UTA ID :1001644268

PROGRAMMING LANGUAGE USED : PYTHON

CODE STRUCTURE:

THERE ARE TWO PYTHON PROGRAMS 

1)sxp4268_maxConnect4.py
 	
 	result() 
 	input  : prev_Game, colVar
 	return : final result newgame

 	legalMovesfunc()
 	input  : board representation
 	return : list of possible legal moves

	to_decide_func()
	this handles the choosing of playing move by applying minmax	
 
	minVal()
 	input  : state, alpha, beta
 	return : minimum value

 
 	maxVal()
 	input  : state, alpha, beta
 	return : maximum value
	
	eval_utility()
	input : state
 	output : the calculated utility value calculated from the evaluation function

 	miscwork()
 	input : move
 	output : print game state and score after the move was played

 	oneMoveGame()
 	input : current game object ,depth
 	output :none, calls function within thats it and plays one move.

 	interactiveGame()
 	input : current game object ,depth
 	output :none, calls function within thats it and plays game interactively.

2)MaxConnect4Game.py

        This has the code for AI to play a "random" move.
	Also,
 	This python file handles the calculation of scores of each player.

TO COMPILE AND RUN :-
     INTERACTIVE MODE
		python sxp4268_maxConnect4.py interactive [computer-next/human-next] [depth]
	
     ONE MOVE MODE 
		python sxp4268_maxConnect4.py one-move [input-file] [output-file] [depth]
   
