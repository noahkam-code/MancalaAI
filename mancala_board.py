from mancala_game import Game

#inital setup for mancala game
player_side = [4,4,4,4,4,4]
player_goal = 0
computer_side = [4,4,4,4,4,4]
computer_goal = 0
turn = 0

def playMancala(ps, pg, cs, cg, turn):
    game = Game(ps, pg, cs, cg, turn)
    game.printBoard()


playMancala(player_side, player_goal, computer_side, computer_goal, turn)
