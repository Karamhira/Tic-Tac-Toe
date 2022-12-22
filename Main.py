class TicTacToe():  # Represents the board
    
    def __init__(self):
        #Initializing a new board.
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        #Initializing a new board so user can see positioning
        self.display = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        
        self.current_Player = "X"
        self.winner = ""
        self.player1_wins = 0
        self.player2_wins = 0
        self.gameRunning = True

    def demon_instructions(self): # Game introduction and instructions
        print("Welcome to TicTacToe")
        print("Enter Numbers based on postioning, shown below")
        top = "╔" + ("═══╦" * 2) + "═" * 3 + "╗\n"
        rows = "║"
        
        column_count = 0
        
        for row in self.display:
            
            for elements in row:
                rows += " " + str(elements) + " ║"
            
            while column_count < 2:
                rows += "\n╠" + ("═══╬" * 2) + "═══╣"
                rows += "\n"+"║"
                column_count += 1
                break
        
        bottom = "\n╚" + "═══╩" * 2 + "═" * 3 + "╝\n"
        print(top + rows + bottom)
        print("Player 1 is X\nPlayer 2 is O")
        return ""

    def printBoard(self): #Prints the board
        top = "╔" + ("═══╦" * 2) + "═" * 3 + "╗\n"
        rows = "║"

        column_count = 0

        for row in self.board:
            
            for elements in row:
                rows += " " + str(elements) + " ║"
            
            while column_count < 2:
                rows += "\n╠" + ("═══╬" * 2) + "═══╣"
                rows += "\n"+"║"
                column_count += 1
                break
        
        bottom = "\n╚" + "═══╩" * 2 + "═" * 3 + "╝\n"
        return top + rows + bottom

    def valid_move(self, move): #To check if the move is valid
      variable = ""
      if move < 1 or move > 9:
          return False
      if move >= 1 and move <= 3:
        variable = self.board[0][move-1]
      elif move >= 4 and move <= 6:
        variable = self.board[1][move-4]
      elif move >= 7 and move <= 9:
        variable = self.board[2][move-7]
      if variable == "-":
        return True
      else:
          False

    def update_board(self, move):#Updates the move after validating
      if self.valid_move(move) == True:
        if move >= 1 and move <= 3:
          self.board[0][move-1] = self.current_Player
        elif move >= 4 and move <= 6:
          self.board[1][move-4] = self.current_Player
        elif move >= 7 and move <= 9:
          self.board[2][move-7] = self.current_Player
        return True
      else:
        return False

    def player_input(self):#gets the player output
      updated = False
      while updated == False: #turn not over till user inputs a correct type
        if self.current_Player == "X":
            print("Player 1's Turn")
        else:
            print("Player 2's Turn")
        
        try: #make sure input is of type int
             move = int(input(f"Enter a number 1-9: "))
        except :
            print("Please only enter a number")
            move = int(input(f"Enter a number 1-9: "))
        
        if self.update_board(move) == True:
            updated = True
        else:
          updated = False
          print("\nInvalid Move, please go again")
      return ""

    def check_horizontal(self): #checks the rows
        for row in self.board:
          if row[0] == row[1] == row[2] == self.current_Player:
            return True
        else:
            False

    def check_vertical(self):  # checks the columns
      for columns in range(3):
        if self.board[0][columns] == self.board[1][columns] == self.board[2][columns] == self.current_Player:
            return True
      else:
          False

    def check_diaganol(self):#checks the diagonals
      if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_Player:
        return True
      elif self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_Player:
        return True
      return False
  
    def checkTie(self): #check if board is filled/ match is tied
      for row in self.board:
        if "-" in row:
          return False
      else:
        self.gameRunning = False
        return True

    def game_over(self): #Calls the other check methods to see if the game has finished
      if self.check_horizontal() or self.check_vertical() or self.check_diaganol():
        print(self.printBoard())
        self.winner = self.current_Player
        self.gameRunning = False
        return (self.current_Player, " wins!")
      elif self.checkTie():
        self.gameRunning = False
        return ("Tied!")
      return ""

    def switchPlay(self):#If game is not over and the player put a succesful input, player gets changed
      if self.current_Player == "X":
        self.current_Player = "O"
      else:
        self.current_Player = "X"
      return ""

    def restart(self): #Starts a new game
      self.gameRunning = True
      self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
      self.current_Player = "X"
      return ""

    def win_counter(self): #keeps track of wins if the players decide to play multiple games
        if self.current_Player == "X":
          self.player1_wins += 1
        else:
          self.player2_wins += 1
        return f"Player 1 Wins: {self.player1_wins} Player 2 Wins: {self.player2_wins}"


class game(TicTacToe): 
  game = TicTacToe()
  print(game.demon_instructions())
  play = True
  while play:
    while game.gameRunning:
      print(game.printBoard())
      print(game.player_input())
      print(game.game_over())
      game.switchPlay()
    print("Game Over!!!")
    restart = input("Would you like to play another game? (y/n): ")
    if restart == "y":
      print("\nRestarting...")
      print(game.restart())
      play = True
    else:
      play = False
      print(game.win_counter())
  print("Thanks for playing")

game()
