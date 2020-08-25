class Game:
    player_side = []
    player_goal = 0
    computer_side = []
    computer_goal = 0
    turn = 0

    def __init__(self, ps, pg, cs, cg, turn):     
        self.player_side = ps
        self.player_goal = pg
        self.computer_side = cs
        self.computer_goal = cg
        self.turn = turn  #turn = 0 --> computer plays first, turn = 1 --> player plays first

    # typical board setup:
    # 0,1,2,3,4,5 cg
    # pg 5,4,3,2,1,0
        
    def take_turn(self, index):
        if self.turn == 0:
            numStones = self.computer_side[index]
            side = 0
            Game_Actions.move(self, self.turn, side, index, numStones)

        else:
            numStones = self.player_side[index]
            side = 1
            Game_Actions.move(self, self.turn, side, index, numStones)

    def move(self, turn, side, index, numStones):   #returns the turn --> can get two turns in a row
        while numStones != 0:
            index += 1
            if index >= len(self.player_side):
                if side == 0 and turn == 0:
                    self.computer_goal += 1
                    numStones -= 1
                    side = 1
                    index = -1
                elif side == 1 and turn == 1:
                    self.player_goal += 1
                    numStones -= 1
                    side = 0
                    index = -1
                elif side == 0 and turn == 1:
                    side = 1
                    index = 0
                    numStones -= 1
                    self.player_side[index] += 1

                elif side == 1 and turn == 0:
                    side = 0
                    index = 0
                    numStones -= 1
                    self.computer_side[index] += 1

            else:
                numStones -= 1
                if side == 0:
                    self.computer_side[index] += 1
                else:
                    self.player_side[index] += 1

        if turn == side:
            if turn == 0:
                if self.computer_side[index] == 1:
                    Game_Actions.capture(self, index, turn)
            else:
                if self.player_side[index] == 1:
                    Game_Actions.capture(self, index, turn)

        if index != -1:
            if turn == 0:
                turn = 1
            else:
                turn = 0

        return turn
 

    def capture(self, index, turn):
        totalCaptured = self.computer_side[index] + self.player_side[index]
        self.computer_side[index] = 0
        self.player_side[index] = 0
        if turn == 0:
            self.computer_goal += totalCaptured
        else:
            self.player_goal += totalCaptured


    def isOver(self):
        player_side_sum = 0
        computer_side_sum = 0
        for i in range(len(self.player_side)):
            player_side_sum += self.player_side[i]
            computer_side_sum += self.computer_side[i]
        if player_side_sum == 0 or computer_side_sum == 0:
            return True
        else:
            return False

    def finalScore(self):  #returns in form of tuple with (computer_score, player_score)
        player_side_sum = 0
        computer_side_sum = 0
        for i in range(len(self.player_side)):
            player_side_sum += self.player_side[i]
            computer_side_sum += self.computer_side[i]
        player_score = player_side_sum + self.player_goal
        computer_score = computer_side_sum + self.computer_goal
        return (computer_score, player_score)

    def printBoard(self):
        for i in range(len(self.player_side)):
            print("|", end='')
            print(self.player_side[i], end = "")
            print("|", end = "")
        print(" (goal:" + str(self.player_goal) + ")")
        print(" (goal:" + str(self.computer_goal) + ")", end = "")
        for i in range(len(self.computer_side)):
            print("|", end='')
            print(self.computer_side[i], end = "")
            print("|", end = "")
        print()
    







