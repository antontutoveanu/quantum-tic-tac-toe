A 'quantum' version of tic tac toe that can run on IBM's quantum computer (or simulated on your local machine).

Requires 9 qubits.

Done as part of [Chris Ferrie](https://profiles.uts.edu.au/Christopher.Ferrie)'s [Introduction to Quantum Computing](https://handbook.uts.edu.au/subjects/41170.html) course at [UTS](https://www.uts.edu.au/).

![](./poster.png)

To run simulated version:
```bash
python3 simulated.py
```
To run on IBM's quantum computer:
```bash
python3 IBM.py
```

Example output of a game:
```

    ###########################
    ### Quantum Tic-Tac-Toe ###
    ###########################
    

    Start Menu:

    1. Start Game
    2. How to Play
    3. Quit
    
What would you like to do? 1

 | | 
-+-+-
 | | 
-+-+-
 | | 

It's your turn X. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
1

Which location? (1-9) 1
     ┌───┐
q_0: ┤ X ├
     └───┘
q_1: ─────
          
q_2: ─────
          
q_3: ─────
          
q_4: ─────
          
q_5: ─────
          
q_6: ─────
          
q_7: ─────
          
q_8: ─────
          
c: 9/═════
          

X| | 
-+-+-
 | | 
-+-+-
 | | 

It's your turn O. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
2

Which location? (1-9) 
2
Which location? (1-9) 
3
     ┌───┐     
q_0: ┤ X ├─────
     ├───┤     
q_1: ┤ H ├──■──
     ├───┤┌─┴─┐
q_2: ┤ X ├┤ X ├
     └───┘└───┘
q_3: ──────────
               
q_4: ──────────
               
q_5: ──────────
               
q_6: ──────────
               
q_7: ──────────
               
q_8: ──────────
               
c: 9/══════════
               

X|O|O
-+-+-
 | | 
-+-+-
 | | 

It's your turn X. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
2

Which location? (1-9) 
4
Which location? (1-9) 
5
     ┌───┐     
q_0: ┤ X ├─────
     ├───┤     
q_1: ┤ H ├──■──
     ├───┤┌─┴─┐
q_2: ┤ X ├┤ X ├
     ├───┤└───┘
q_3: ┤ H ├──■──
     ├───┤┌─┴─┐
q_4: ┤ X ├┤ X ├
     └───┘└───┘
q_5: ──────────
               
q_6: ──────────
               
q_7: ──────────
               
q_8: ──────────
               
c: 9/══════════
               

X|O|O
-+-+-
X|X| 
-+-+-
 | | 

It's your turn O. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
2

Which location? (1-9) 
6
Which location? (1-9) 
7
     ┌───┐     
q_0: ┤ X ├─────
     ├───┤     
q_1: ┤ H ├──■──
     ├───┤┌─┴─┐
q_2: ┤ X ├┤ X ├
     ├───┤└───┘
q_3: ┤ H ├──■──
     ├───┤┌─┴─┐
q_4: ┤ X ├┤ X ├
     ├───┤└───┘
q_5: ┤ H ├──■──
     ├───┤┌─┴─┐
q_6: ┤ X ├┤ X ├
     └───┘└───┘
q_7: ──────────
               
q_8: ──────────
               
c: 9/══════════
               

X|O|O
-+-+-
X|X|O
-+-+-
O| | 

It's your turn X. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
2

Which location? (1-9) 
8
Which location? (1-9) 
9
     ┌───┐     
q_0: ┤ X ├─────
     ├───┤     
q_1: ┤ H ├──■──
     ├───┤┌─┴─┐
q_2: ┤ X ├┤ X ├
     ├───┤└───┘
q_3: ┤ H ├──■──
     ├───┤┌─┴─┐
q_4: ┤ X ├┤ X ├
     ├───┤└───┘
q_5: ┤ H ├──■──
     ├───┤┌─┴─┐
q_6: ┤ X ├┤ X ├
     ├───┤└───┘
q_7: ┤ H ├──■──
     ├───┤┌─┴─┐
q_8: ┤ X ├┤ X ├
     └───┘└───┘
c: 9/══════════
               

X|O|O
-+-+-
X|X|O
-+-+-
O|X|X

Trigger collapse.

     ┌───┐     ┌─┐                        
q_0: ┤ X ├─────┤M├────────────────────────
     ├───┤     └╥┘┌─┐                     
q_1: ┤ H ├──■───╫─┤M├─────────────────────
     ├───┤┌─┴─┐ ║ └╥┘┌─┐                  
q_2: ┤ X ├┤ X ├─╫──╫─┤M├──────────────────
     ├───┤└───┘ ║  ║ └╥┘┌─┐               
q_3: ┤ H ├──■───╫──╫──╫─┤M├───────────────
     ├───┤┌─┴─┐ ║  ║  ║ └╥┘┌─┐            
q_4: ┤ X ├┤ X ├─╫──╫──╫──╫─┤M├────────────
     ├───┤└───┘ ║  ║  ║  ║ └╥┘┌─┐         
q_5: ┤ H ├──■───╫──╫──╫──╫──╫─┤M├─────────
     ├───┤┌─┴─┐ ║  ║  ║  ║  ║ └╥┘┌─┐      
q_6: ┤ X ├┤ X ├─╫──╫──╫──╫──╫──╫─┤M├──────
     ├───┤└───┘ ║  ║  ║  ║  ║  ║ └╥┘┌─┐   
q_7: ┤ H ├──■───╫──╫──╫──╫──╫──╫──╫─┤M├───
     ├───┤┌─┴─┐ ║  ║  ║  ║  ║  ║  ║ └╥┘┌─┐
q_8: ┤ X ├┤ X ├─╫──╫──╫──╫──╫──╫──╫──╫─┤M├
     └───┘└───┘ ║  ║  ║  ║  ║  ║  ║  ║ └╥┘
c: 9/═══════════╩══╩══╩══╩══╩══╩══╩══╩══╩═
                0  1  2  3  4  5  6  7  8 

X| |O
-+-+-
X| | 
-+-+-
O|X| 

It's your turn O. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
1

Which location? (1-9) 2
     ┌───┐     ┌─┐     ┌───┐                                   
q_0: ┤ X ├─────┤M├─|0>─┤ X ├───────────────────────────────────
     ├───┤     └╥┘ ┌─┐ └───┘┌───┐                              
q_1: ┤ H ├──■───╫──┤M├──|0>─┤ X ├──────────────────────────────
     ├───┤┌─┴─┐ ║  └╥┘  ┌─┐ └───┘┌───┐                         
q_2: ┤ X ├┤ X ├─╫───╫───┤M├──|0>─┤ X ├─────────────────────────
     ├───┤└───┘ ║   ║   └╥┘  ┌─┐ └───┘┌───┐                    
q_3: ┤ H ├──■───╫───╫────╫───┤M├──|0>─┤ X ├────────────────────
     ├───┤┌─┴─┐ ║   ║    ║   └╥┘  ┌─┐ └───┘                    
q_4: ┤ X ├┤ X ├─╫───╫────╫────╫───┤M├──|0>─────────────────────
     ├───┤└───┘ ║   ║    ║    ║   └╥┘  ┌─┐                     
q_5: ┤ H ├──■───╫───╫────╫────╫────╫───┤M├──|0>────────────────
     ├───┤┌─┴─┐ ║   ║    ║    ║    ║   └╥┘  ┌─┐      ┌───┐     
q_6: ┤ X ├┤ X ├─╫───╫────╫────╫────╫────╫───┤M├──|0>─┤ X ├─────
     ├───┤└───┘ ║   ║    ║    ║    ║    ║   └╥┘  ┌─┐ └───┘┌───┐
q_7: ┤ H ├──■───╫───╫────╫────╫────╫────╫────╫───┤M├──|0>─┤ X ├
     ├───┤┌─┴─┐ ║   ║    ║    ║    ║    ║    ║   └╥┘  ┌─┐ └───┘
q_8: ┤ X ├┤ X ├─╫───╫────╫────╫────╫────╫────╫────╫───┤M├──|0>─
     └───┘└───┘ ║   ║    ║    ║    ║    ║    ║    ║   └╥┘      
c: 9/═══════════╩═══╩════╩════╩════╩════╩════╩════╩════╩═══════
                0   1    2    3    4    5    6    7    8       

X|O|O
-+-+-
X| | 
-+-+-
O|X| 

It's your turn X. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
1

Which location? (1-9) 6
     ┌───┐     ┌─┐     ┌───┐                                   
q_0: ┤ X ├─────┤M├─|0>─┤ X ├───────────────────────────────────
     ├───┤     └╥┘ ┌─┐ └───┘┌───┐                              
q_1: ┤ H ├──■───╫──┤M├──|0>─┤ X ├──────────────────────────────
     ├───┤┌─┴─┐ ║  └╥┘  ┌─┐ └───┘┌───┐                         
q_2: ┤ X ├┤ X ├─╫───╫───┤M├──|0>─┤ X ├─────────────────────────
     ├───┤└───┘ ║   ║   └╥┘  ┌─┐ └───┘┌───┐                    
q_3: ┤ H ├──■───╫───╫────╫───┤M├──|0>─┤ X ├────────────────────
     ├───┤┌─┴─┐ ║   ║    ║   └╥┘  ┌─┐ └───┘                    
q_4: ┤ X ├┤ X ├─╫───╫────╫────╫───┤M├──|0>─────────────────────
     ├───┤└───┘ ║   ║    ║    ║   └╥┘  ┌─┐      ┌───┐          
q_5: ┤ H ├──■───╫───╫────╫────╫────╫───┤M├──|0>─┤ X ├──────────
     ├───┤┌─┴─┐ ║   ║    ║    ║    ║   └╥┘  ┌─┐ └───┘┌───┐     
q_6: ┤ X ├┤ X ├─╫───╫────╫────╫────╫────╫───┤M├──|0>─┤ X ├─────
     ├───┤└───┘ ║   ║    ║    ║    ║    ║   └╥┘  ┌─┐ └───┘┌───┐
q_7: ┤ H ├──■───╫───╫────╫────╫────╫────╫────╫───┤M├──|0>─┤ X ├
     ├───┤┌─┴─┐ ║   ║    ║    ║    ║    ║    ║   └╥┘  ┌─┐ └───┘
q_8: ┤ X ├┤ X ├─╫───╫────╫────╫────╫────╫────╫────╫───┤M├──|0>─
     └───┘└───┘ ║   ║    ║    ║    ║    ║    ║    ║   └╥┘      
c: 9/═══════════╩═══╩════╩════╩════╩════╩════╩════╩════╩═══════
                0   1    2    3    4    5    6    7    8       

X|O|O
-+-+-
X| |X
-+-+-
O|X| 

It's your turn O. 
Do you want to make a (1) classical move, (2) quantum move, (3) collapse?, or (4) quit?
1

Which location? (1-9) 5
     ┌───┐     ┌─┐     ┌───┐                                   
q_0: ┤ X ├─────┤M├─|0>─┤ X ├───────────────────────────────────
     ├───┤     └╥┘ ┌─┐ └───┘┌───┐                              
q_1: ┤ H ├──■───╫──┤M├──|0>─┤ X ├──────────────────────────────
     ├───┤┌─┴─┐ ║  └╥┘  ┌─┐ └───┘┌───┐                         
q_2: ┤ X ├┤ X ├─╫───╫───┤M├──|0>─┤ X ├─────────────────────────
     ├───┤└───┘ ║   ║   └╥┘  ┌─┐ └───┘┌───┐                    
q_3: ┤ H ├──■───╫───╫────╫───┤M├──|0>─┤ X ├────────────────────
     ├───┤┌─┴─┐ ║   ║    ║   └╥┘  ┌─┐ └───┘┌───┐               
q_4: ┤ X ├┤ X ├─╫───╫────╫────╫───┤M├──|0>─┤ X ├───────────────
     ├───┤└───┘ ║   ║    ║    ║   └╥┘  ┌─┐ └───┘┌───┐          
q_5: ┤ H ├──■───╫───╫────╫────╫────╫───┤M├──|0>─┤ X ├──────────
     ├───┤┌─┴─┐ ║   ║    ║    ║    ║   └╥┘  ┌─┐ └───┘┌───┐     
q_6: ┤ X ├┤ X ├─╫───╫────╫────╫────╫────╫───┤M├──|0>─┤ X ├─────
     ├───┤└───┘ ║   ║    ║    ║    ║    ║   └╥┘  ┌─┐ └───┘┌───┐
q_7: ┤ H ├──■───╫───╫────╫────╫────╫────╫────╫───┤M├──|0>─┤ X ├
     ├───┤┌─┴─┐ ║   ║    ║    ║    ║    ║    ║   └╥┘  ┌─┐ └───┘
q_8: ┤ X ├┤ X ├─╫───╫────╫────╫────╫────╫────╫────╫───┤M├──|0>─
     └───┘└───┘ ║   ║    ║    ║    ║    ║    ║    ║   └╥┘      
c: 9/═══════════╩═══╩════╩════╩════╩════╩════╩════╩════╩═══════
                0   1    2    3    4    5    6    7    8       

X|O|O
-+-+-
X|O|X
-+-+-
O|X| 

Game Over.

 **** O won ****

Play Again?(y/n) 
```