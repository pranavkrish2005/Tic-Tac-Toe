
import numpy as np

class TicTcToe() :
  board = ["" for x in range(9)]
  turn = True

  def __init__(self):
    inp = input("Enter 1 if you want to go first or 0 if you want the computer to go first : ")
    if int(inp) == 1 :
      self.turn = not self.turn
    self.play();
  
  def play(self) :
    if not self.turn :
      self.display(self.board)
    while not self.ifwon(self.board) :
      if self.draw(self.board) :
        print("The game was a draw : ")
        self.display(self.board)
        return
      if self.turn :
        self.ActualAI(self.turn)
        self.display(self.board)
      else :
        self.playerMove()
      self.turn = not self.turn

    if not self.turn :
      print("the computer won")
    else :
      print("The player won")
    self.display(self.board)

  def draw(self, board) : 
    return board.count("") == 0

  def display(self, board) :
    board = self.Copy(board)
    print('_____ _____ _____')
    for i in range(0, 8, 3):
      if(board[i] == "") :
        board[i] = " "
      if(board[i + 1] == "") :
        board[i + 1] = " "
      if(board[i + 2] == "") :
        board[i + 2] = " "
      print("     |     |")
      print("  {}  |  {}  |  {}".format(board[i], board[i + 1], board[i + 2]))
      print('_____|_____|_____')

  def ifwon(self, board) :
    b1 = np.array(board).reshape(3, 3)
    b2 = np.array([b1[:, 0], b1[:, 1], b1[:, 2]]).tolist()
    b1 = b1.tolist()
    if b1.count(["X", "X", "X"]) > 0 or b1.count(["O", "O", "O"]) > 0 :
      return True
    elif b2.count(["X", "X", "X"]) > 0 or b2.count(["O", "O", "O"]) > 0 :
      return True
    elif b1[0][0] == b1[1][1] == b1[2][2] ==  "X" or b1[0][2] == b1[1][1] == b1[2][0] == "X" or b1[0][0] == b1[1][1] == b1[2][2] == "O" or b1[0][2] == b1[1][1] == b1[2][0] == "O" :
      return True
    return False

  def playerMove(self) :  
    playerChoice = input("Enter the number corresponding to the square : ")
    while self.board[int(playerChoice) - 1] != "" :
      print("The number that you entered is not empty, please enter again.")
      playerChoice = input("Enter the number corresponding to the square : ")
    self.board[int(playerChoice) - 1] = 'O'

  ind = 0
  def ActualAI(self, insideturn) :
    if self.board.count("") == 9 :
      self.board[4] = 'X'
    elif self.board.count("") == 8 and self.board[4] == "O" :
      self.board[0] = 'X'
    else :
      self.AI(insideturn, self.Copy(self.board), 0)
      self.board[self.ind] = 'X'

  def Copy(self, board) :
    temp = ['' for x in range(9)]
    for x in range(9) :
      temp[x] = board[x]
    return temp

  def AI(self, insideturn, board, depth) :
    arr = []
    i = 0
    depth += 1
    if insideturn :
      while board.count("") != 0 :
        num = np.where(np.array(board) == '')[0][i]
        board[num] = "X"
        if self.ifwon(board) :
          if depth == 1 :
            self.ind = num
          return 1 + board.count("");
        elif self.draw(board) :
          if depth == 1 :
            self.ind = num
          return 0
        else :
          arr.append(self.AI(not insideturn, self.Copy(board), depth))
          board[num] = ""
          self.ind = np.where(np.array(board) == '')[0][arr.index(max(arr))]
          if board.count("") - 1 != i :
            i += 1
          else :
            return max(arr)
    else : 
      while board.count("") != 0 :
        num = np.where(np.array(board) == '')[0][i]
        board[num] = "O"
        if self.ifwon(board) :
          if depth == 1 :
            self.ind = num
          return -1 * (1 + board.count(""));
        elif self.draw(board) :
          if depth == 1 :
            self.ind = num
          return 0
        else :
          arr.append(self.AI(not insideturn, self.Copy(board), depth))
          board[num] = ""
          self.ind = np.where(np.array(board) == '')[0][arr.index(min(arr))]
          if board.count("") - 1 != i :
            i += 1
          else :
            return min(arr)


one = TicTcToe()
