from termcolor import colored, cprint
import json
from qiskit import *
from qiskit.tools.monitor import job_monitor

def resetBoard():
  return {'1': [' ', 0] , '2': [' ', 0], '3': [' ', 0],
          '4': [' ', 0], '5': [' ', 0], '6': [' ', 0],
          '7': [' ', 0], '8': [' ', 0], '9': [' ', 0]}

def printBoard(board):
  print()
  colour = 0
  for i in range (1,10):
    if board[str(i)][1] == 0:
      cprint(board[str(i)][0], end='')
    else:
      if (colour == 0 or colour == 1):
        cprint(board[str(i)][0], 'red', end='')
        colour = colour + 1
      elif (colour == 2 or colour == 3):
        cprint(board[str(i)][0], 'green', end='')
        colour = colour + 1
      elif (colour == 4 or colour == 5):
        cprint(board[str(i)][0], 'blue', end='')
        colour = colour + 1
      elif (colour == 6 or colour == 7):
        cprint(board[str(i)][0], 'yellow', end='')
        colour = colour + 1

    if i % 3 == 0:
      print()
      if i != 9: 
        print('-+-+-')
    else:
      cprint('|', end='') 

def make_classic_move(theBoard, turn, count, circuit):

  valid_move = 0
  valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  
  while (not valid_move):
    print()
    print("Which location? (1-9) ", end='')
    location = input()

    if location in valid_moves:
        
      if theBoard[location][0] == ' ':
        valid_move = 1
        # set the location's marker
        theBoard[location][0] = turn
        # increment counter (total markers on board) *when this = 9, collapse the board, also called measurement
        count += 1
        # set marker's state (classical or quantum)
        theBoard[location][1] = 0 # classical (not flashing on screen)

        # set qubit[location] to ON, 100% = 1
        # one pauli X gate
        circuit.x(int(location)-1)

        print(circuit.draw())
      else: 
        print()
        print("That place is already filled.")
    else:
      print("Please select a square from 1-9")

  return theBoard, turn, count, circuit

def make_quantum_move(theBoard, count, circuit, turn):

  valid_move = False
  valid_moves = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

  while (not valid_move):
      
    print()
    print("Which location? (1-9) ")
    location1 = input()
    print("Which location? (1-9) ")
    location2 = input()

    if theBoard[location1][0] == ' ' and theBoard[location2][0] == ' ' and location1 != location2:
        # set the location's marker
        theBoard[location1][0] = turn
        theBoard[location2][0] = turn
        # increment counter (total markers on board) *when this = 9, collapse the board, also called measurement
        count += 2
        # set marker's state (classical or quantum)
        theBoard[location1][1] = 1 # quantum (flashing on screen)
        theBoard[location2][1] = 1 # quantum (flashing on screen)


        # set qubit[location1], qubit[location2] to superposition/entangled

        # hadamard gates
        circuit.h(int(location1)-1)

        # x gate
        circuit.x(int(location2)-1)

        # cnot gate
        circuit.cx(int(location1)-1,int(location2)-1)

        print(circuit.draw())
        valid_move = True
    else:
        print()
        print("You have selected an invalid position/s")
    

  return theBoard, count, circuit, turn

def measure(circuit, theBoard, count):
  # trigger collapse
  printBoard(theBoard)
  print()
  print("Trigger collapse.")
  print()

  # Use Aer's qasm_simulator
  simulator = qiskit.Aer.get_backend('qasm_simulator')

  circuit.measure(0,0)
  circuit.measure(1,1)
  circuit.measure(2,2)
  circuit.measure(3,3)
  circuit.measure(4,4)
  circuit.measure(5,5)
  circuit.measure(6,6)
  circuit.measure(7,7)
  circuit.measure(8,8)

  print(circuit.draw())

  # Execute the circuit on quantum simulator
  job = qiskit.execute(circuit, simulator, shots=1)

  # Grab results from the job
  result = job.result()

  out = json.dumps(result.get_counts()) #Converts the result.get_counts() into a string
  string = out[2:11] #Removes unnecessary data from string, leaving us with board

  # update board
  for i in range(9):
      if string[i] == '1':
          # cement value in the board
          theBoard[str(9-i)][1] = 0
      else:
          # make square empty
          theBoard[str(9-i)][1] = 0
          theBoard[str(9-i)][0] = ' '

  # update count (total number of markers on the board)
  count = 0
  for i in range(9):
      theBoard[str(i+1)][1] = 0
      if theBoard[str(i+1)][0] != ' ':
          count += 1

  # reset qubits
  circuit.reset(0)
  circuit.reset(1)
  circuit.reset(2)
  circuit.reset(3)
  circuit.reset(4)
  circuit.reset(5)
  circuit.reset(6)
  circuit.reset(7)
  circuit.reset(8)

  for i in range(9):
      if string[8-i] == '1':
          # add pauli x gate
          circuit.x(i)

  return circuit, string, theBoard, count

def check_win(theBoard, turn):
  if theBoard['7'][0] == theBoard['8'][0] == theBoard['9'][0] != ' ': # across the top
      if theBoard['7'][1] == theBoard['8'][1] == theBoard['9'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['8'][0], end='')
          print(" won ****")
          print() 
          return True

  elif theBoard['4'][0] == theBoard['5'][0] == theBoard['6'][0] != ' ': # across the middle
      if theBoard['4'][1] == theBoard['5'][1] == theBoard['6'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['5'][0], end='')
          print(" won ****")
          print()
          return True

  elif theBoard['1'][0] == theBoard['2'][0] == theBoard['3'][0] != ' ': # across the bottom
      if theBoard['1'][1] == theBoard['2'][1] == theBoard['3'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['2'][0], end='')
          print(" won ****")
          print()
          return True

  elif theBoard['1'][0] == theBoard['4'][0] == theBoard['7'][0] != ' ': # down the left side
      if theBoard['1'][1] == theBoard['4'][1] == theBoard['7'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['4'][0], end='')
          print(" won ****")
          print()
          return True

  elif theBoard['2'][0] == theBoard['5'][0] == theBoard['8'][0] != ' ': # down the middle
      if theBoard['2'][1] == theBoard['5'][1] == theBoard['8'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['5'][0], end='')
          print(" won ****")
          print()
          return True

  elif theBoard['3'][0] == theBoard['6'][0] == theBoard['9'][0] != ' ': # down the right side
      if theBoard['3'][1] == theBoard['6'][1] == theBoard['9'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['6'][0], end='')
          print(" won ****")
          print()
          return True

  elif theBoard['7'][0] == theBoard['5'][0] == theBoard['3'][0] != ' ': # diagonal
      if theBoard['7'][1] == theBoard['5'][1] == theBoard['3'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['5'][0], end='')
          print(" won ****")
          print()
          return True

  elif theBoard['1'][0] == theBoard['5'][0] == theBoard['9'][0] != ' ': # diagonal
      if theBoard['1'][1] == theBoard['5'][1] == theBoard['9'][1] == 0: # only cemented markers
          printBoard(theBoard)
          print("\nGame Over.\n")                
          print(" **** ", end='')
          print(theBoard['5'][0], end='')
          print(" won ****")
          print()
          return True

#Implementation of Two Player Tic-Tac-Toe game in Python.
# start game function
# Now we'll write the main function which has all the gameplay functionality.


def game():

    turn = 'X'
    count = 0
    win = False
    x_collapse = 1
    y_collapse = 1

    # initialise quantum circuit with 9 qubits (all on OFF = 0)
    circuit = qiskit.QuantumCircuit(9, 9)

    while (not win):

        # ============================= ROUND START ============================ 
        global theBoard
        printBoard(theBoard)

        print()
        print("It's your turn " + turn + ". Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?")

        move = input()

        # ============================= CLASSIC MOVE ===========================

        if int(move) == 1:
            theBoard, turn, count, circuit = make_classic_move(theBoard, turn, count, circuit)
            madeMove = True

        # ============================= QUANTUM MOVE ===========================

        elif int(move) == 2 and count > 8:
          # cant do a quantum move if there's only 1 empty square left
          print()
          print("There aren't enough empty spaces for that!")

        elif int(move) == 2 and count < 8:
          theBoard, count, circuit, turn = make_quantum_move(theBoard, count, circuit, turn)
          madeMove = True
        
        # ============================= COLLAPSE/MEASURE =======================

        elif int(move) == 3:

          if (turn == 'X' and x_collapse== 1 ):
            circuit, string, theBoard, count = measure(circuit, theBoard, count)
            x_collapse = 0
          elif (turn == 'O' and y_collapse == 1):
            circuit, string, theBoard, count = measure(circuit, theBoard, count)
            y_collapse = 0
          else:
            print("You have already used your collapse this game!")

        # ============================= QUIT ===================================

        elif int(move) == 4:
            break
        
        # ============================= CHECK FOR WIN ==========================

        # Now we will check if player X or O has won,for every move  
        if count >= 5:
          win = check_win(theBoard, turn)
          if (win):
            break



        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
          circuit, string, theBoard, count = measure(circuit, theBoard, count)
          win = check_win(theBoard, turn)
          if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie !")
            print()
            win = True
          


        # Now we have to change the player after every move.
        if  (madeMove):  
          madeMove = False
          if turn =='X':
              turn = 'O'
          else:
              turn = 'X'        
    

    # Now we will ask if player wants to restart the game or not.
    restart = input("Play Again?(y/n) ")
    if restart == "y" or restart == "Y":

        theBoard = resetBoard()
        game()

def start_menu():
    start_menu = """
    Start Menu:

    1. Start Game
    2. How to Play
    3. Quit
    """ 
    
    print("""
    ###########################
    ### Quantum Tic-Tac-Toe ###
    ###########################
    """)
    print(start_menu)
    choice = 0
    while (choice != '1'):
      print("What would you like to do? ", end='')
      choice = input()

      if (choice == '2'):
        How_To = """ 
        In Quantum Tic-Tac-Toe, each square starts empty and your goal is to create a line of three of your naughts/crosses. 
        Playing a classical move will result in setting a square permanently as your piece.
        Playing a quantum move will create a superposition between two squares of your choosing. You may only complete a quantum move in two empty squares.
        The board will collapse when the board is full. At collapse, each superposition is viewed and only 1 piece of the superposition will remain. 
        *Powerup* Each player can decide to collapse the board prematurely, they may do this once per round each.
        """
        print(How_To)

      if (choice == '3'):
        print("Goodbye")
        break
      
    return choice

#Reset the board at start
theBoard = resetBoard()

#Set no moves made yet
if (start_menu() == '1'):  
  madeMove = False
  game()