import Gameboard
import Player
import random
import time



def start_Game() -> str:
    """ Starts the Game

    This Method starts the Game and decides on the Game-Mode played.
    The return value will define which Game-Mode will be started.

    Parameters
    ----------
    none
    
    Returns
    ------
    GameMode str
        return value A equals Co-Op
        return value B equals PC
        return value X equals quit

    """

    gamemode=""

    print("-- Hello Player!                                                  --")
    print("-- We welcome you to our 4Connect Game, made by Bojan and Adam!   --")
    print("-- select X at any Input, if you want to end the game             --")

    print("-- Please select which Game-Mode you want to play:                --")
    print("-- Co-Op = A                                                      --")
    print("-- PC = B                                                         --")
    

    while True:
        gamemode = input("-- Game-Mode:")
        if gamemode == "A" or gamemode == "B" or gamemode == "X":
            break
        else:
            print("-- You need to select A or B!                                     --")
            print("-- select X if you want to end the game                           --")

    return gamemode

def Check_Win(gameb: Gameboard, column: int, playerX: Player) -> bool:
    """ Checks for Win-Condition

    This Method checks if there is a Win, by checking if the last placed stone created a Win-Condition.
    Only the last placed stone will be checked!
    So always call this method after a stone was placed.

    Parameters
    ----------
    gameb: Gameboard
        'gameb' is the current gameboard, in which the Win-Condition needs to be found
    column: int
        'column' is the column, where the last stone was placed
    playerX: Player
        is the player who placed the last stone
    
    Returns
    ------
    Check_Win bool
        if the return value is True, there is a Win for playerX.

    """
    column = (int(column)-1)
    row = findRowWithO(gameb, column)
    win = False
    counter = 0

    # last Stone = gameb.Gameboard[row][column]

    if playerX == gameb.player1:
        # horizontal
        # 1,1,1,x - 1,1,x,1 - 1,x,1,1 - x,1,1,1
        if column >= 3:
            if gameb.Collection[row][column-1] == "\033[32mo\033[0m" and gameb.Collection[row][column-2] == "\033[32mo\033[0m" and gameb.Collection[row][column-3] == "\033[32mo\033[0m":
                return True
        if column <= 3:  
            if gameb.Collection[row][column+1] == "\033[32mo\033[0m" and gameb.Collection[row][column+2] == "\033[32mo\033[0m" and gameb.Collection[row][column+3] == "\033[32mo\033[0m":
                return True
        if column >= 1 and column <= 4:
            if gameb.Collection[row][column-1] == "\033[32mo\033[0m" and gameb.Collection[row][column+1] == "\033[32mo\033[0m" and gameb.Collection[row][column+2] == "\033[32mo\033[0m": 
                return True
        if column <= 5 and column >= 2:
            if gameb.Collection[row][column+1] == "\033[32mo\033[0m" and gameb.Collection[row][column-1] == "\033[32mo\033[0m" and gameb.Collection[row][column-2] == "\033[32mo\033[0m":
                return True
        
        # vertical
        # x ; 1 ; 1 ; 1
        # 1 ; x ; 1 ; 1
        # 1 ; 1 ; x ; 1
        # 1 ; 1 ; 1 ; x
        # actually a bit unnecessary -> only Scenario 1 is important, because Stones can only be placed at the Top of a Queue
        # no time for change
        if row <= 2:
            if gameb.Collection[row+1][column] == "\033[32mo\033[0m" and gameb.Collection[row+2][column] == "\033[32mo\033[0m" and gameb.Collection[row+3][column] == "\033[32mo\033[0m":
                return True 
        if row >= 3:
            if gameb.Collection[row-1][column] == "\033[32mo\033[0m" and gameb.Collection[row-2][column] == "\033[32mo\033[0m" and gameb.Collection[row-3][column] == "\033[32mo\033[0m":
                return True 
        if row >= 1 and row <=3:
            if gameb.Collection[row-1][column] == "\033[32mo\033[0m" and gameb.Collection[row+1][column] == "\033[32mo\033[0m" and gameb.Collection[row+2][column] == "\033[32mo\033[0m":
                return True 
        if row <= 4 and row >= 2:
            if gameb.Collection[row+1][column] == "\033[32mo\033[0m" and gameb.Collection[row-1][column] == "\033[32mo\033[0m" and gameb.Collection[row-2][column] == "\033[32mo\033[0m":
                return True 
            
        # diagonal
        # 1 ; 0 ; 0 ; 0 
        # 0 ; x ; 0 ; 0
        # 0 ; 0 ; 1 ; 0
        # 0 ; 0 ; 0 ; 1

        # diagonal left down -> right top
        if row <= 2 and column >= 3:  # Check, if there is enough space
            if gameb.Collection[row+1][column-1] == "\033[32mo\033[0m" and gameb.Collection[row+2][column-2] == "\033[32mo\033[0m" and gameb.Collection[row+3][column-3] == "\033[32mo\033[0m":
                return True

        # diagonal left top -> right bottom
        if row >= 3 and column >= 3: 
            if gameb.Collection[row-1][column-1] == "\033[32mo\033[0m" and gameb.Collection[row-2][column-2] == "\033[32mo\033[0m" and gameb.Collection[row-3][column-3] == "\033[32mo\033[0m":
                return True
    
        # diagonal left bottom -> right top
        if row <= 2 and column <= 3:  
            if gameb.Collection[row+1][column+1] == "\033[32mo\033[0m" and gameb.Collection[row+2][column+2] == "\033[32mo\033[0m" and gameb.Collection[row+3][column+3] == "\033[32mo\033[0m":
                return True
        
        # diagonal right bottom -> left top
        if row >= 3 and column <= 3:
            if gameb.Collection[row-1][column+1] == "\033[32mo\033[0m" and gameb.Collection[row-2][column+2] == "\033[32mo\033[0m" and gameb.Collection[row-3][column+3] == "\033[32mo\033[0m":
                return True

    
    elif playerX == gameb.player2:
        # horizontal
        # 1,1,1,x - 1,1,x,1 - 1,x,1,1 - x,1,1,1
        if column >= 3:
            if gameb.Collection[row][column-1] == "\033[31mo\033[0m" and gameb.Collection[row][column-2] == "\033[31mo\033[0m" and gameb.Collection[row][column-3] == "\033[31mo\033[0m":
                return True
        if column <= 3:  
            if gameb.Collection[row][column+1] == "\033[31mo\033[0m" and gameb.Collection[row][column+2] == "\033[31mo\033[0m" and gameb.Collection[row][column+3] == "\033[31mo\033[0m":
                return True
        if column >= 1 and column <= 4:
            if gameb.Collection[row][column-1] == "\033[31mo\033[0m" and gameb.Collection[row][column+1] == "\033[31mo\033[0m" and gameb.Collection[row][column+2] == "\033[31mo\033[0m": 
                return True
        if column <= 5 and column >= 2:
            if gameb.Collection[row][column+1] == "\033[31mo\033[0m" and gameb.Collection[row][column-1] == "\033[31mo\033[0m" and gameb.Collection[row][column-2] == "\033[31mo\033[0m":
                return True
        
        # vertical
        # x ; 1 ; 1 ; 1
        # 1 ; x ; 1 ; 1
        # 1 ; 1 ; x ; 1
        # 1 ; 1 ; 1 ; x
        # actually a bit unnecessary -> only Scenario 1 is important, because Stones can only be placed at the Top of a Queue
        # no time for change
        if row <= 2:
            if gameb.Collection[row+1][column] == "\033[31mo\033[0m" and gameb.Collection[row+2][column] == "\033[31mo\033[0m" and gameb.Collection[row+3][column] == "\033[31mo\033[0m":
                return True 
        if row >= 3:
            if gameb.Collection[row-1][column] == "\033[31mo\033[0m" and gameb.Collection[row-2][column] == "\033[31mo\033[0m" and gameb.Collection[row-3][column] == "\033[31mo\033[0m":
                return True 
        if row >= 1 and row <=3:
            if gameb.Collection[row-1][column] == "\033[31mo\033[0m" and gameb.Collection[row+1][column] == "\033[31mo\033[0m" and gameb.Collection[row+2][column] == "\033[31mo\033[0m":
                return True 
        if row <= 4 and row >= 2:
            if gameb.Collection[row+1][column] == "\033[31mo\033[0m" and gameb.Collection[row-1][column] == "\033[31mo\033[0m" and gameb.Collection[row-2][column] == "\033[31mo\033[0m":
                return True 
            

        # diagonal
        # 1 ; 0 ; 0 ; 0 
        # 0 ; x ; 0 ; 0
        # 0 ; 0 ; 1 ; 0
        # 0 ; 0 ; 0 ; 1
            
        # diagonal left bottom -> right top
        if row <= 2 and column >= 3: 
            if gameb.Collection[row+1][column-1] == "\033[31mo\033[0m" and gameb.Collection[row+2][column-2] == "\033[31mo\033[0m" and gameb.Collection[row+3][column-3] == "\033[31mo\033[0m":
                return True

        # diagonal left top -> right bottom
        if row >= 3 and column >= 3: 
            if gameb.Collection[row-1][column-1] == "\033[31mo\033[0m" and gameb.Collection[row-2][column-2] == "\033[31mo\033[0m" and gameb.Collection[row-3][column-3] == "\033[31mo\033[0m":
                return True
        
        # diagonal left bottom -> right top 
        if row <= 2 and column <= 3: 
            if gameb.Collection[row+1][column+1] == "\033[31mo\033[0m" and gameb.Collection[row+2][column+2] == "\033[31mo\033[0m" and gameb.Collection[row+3][column+3] == "\033[31mo\033[0m":
                return True
        
        # diagonal right bottom -> left top
        if row >= 3 and column <= 3:
            if gameb.Collection[row-1][column+1] == "\033[31mo\033[0m" and gameb.Collection[row-2][column+2] == "\033[31mo\033[0m" and gameb.Collection[row-3][column+3] == "\033[31mo\033[0m":
                return True

   
    return False

def Check_Draw(gameb: Gameboard) -> bool:
    """ Checks for Draw-Condition

    This Method checks if there is a draw, by checking if there is any Places left without a stone

    Parameters
    ----------
    gameb: Gameboard
        'gameb' is the current gameboard, in which the right row index needs to be found
    

    Returns
    ------
    Check_Draw bool
        if the return value is False, there is no draw.

    """
    xFound = False
    for row in gameb.Collection:
        for column in row:
            if column == "x":
                xFound = True

    return not(xFound)

def findRowWithO(gameb: Gameboard, column: int) -> int:
    """ Finds the highes row in a specific column, where a Stone is placed

    This Method returns the value of highest row-index in a column, where a Stone is already placed.

    Parameters
    ----------
    gameb: Gameboard
        'gameb' is the current gameboard, in which the right row index needs to be found
    
    column: int
        'column' is the column index, where the highest row index needs to be found

    Returns
    ------
    row-index
        the index of the searched row

    """
    for i in range(0, 6): #5, -1, -1
        if gameb.Collection[i][column] != "x":
            return i

    return 5
    


def run_CO_OP_Mode():
    """ Starts and Runs the Co-Op-Mode of the game

    2 Players play against each other.
    "Multi-Player"-Mode

    Parameters
    ----------
    none

    Returns
    ------
    none

    """
    print("-- Co-OP Mode is activated                                        --")
    player1_name = input("-- Please enter the Name of Player 1: ")
    if player1_name == "X": StopGame() 
    player2_name = input("-- Please enter the Name of Player2: ")
    if player2_name == "X": StopGame()
    player1 = Player.Player(player1_name,0,False)
    player2 = Player.Player(player2_name,0,False)
    gameb = Gameboard.Gameboard(player1,player2)

    print("-- !Let's Start!                                                  --")
    gameb.Show_Board()

    while True:
        column = input(f'-- {player1.name}, please select a column-number: ')
        if column == "X": StopGame() 
        try:
            if int(column) >= 1 and int(column) <= 7:
                gameb.Place_Stone(int(column), player1)
                player1.increase_Turn_Counter()
                gameb.Show_Board()
                if player1.current_turn >= 4 and Check_Win(gameb, column, player1) == True:
                    print("------ WINNER WINNER CHICKEN DINNER           ------")
                    print(f"------ {player1.name.upper()} IS THE WINNER!                      ------")
                    print(f"------ {player2.name.upper()} IS THE DINNER...                   ------")
                    break
                if Check_Draw(gameb):
                    StopGame()
        except ValueError:
            print("------ Input not OK ------")

        column = input(f'-- {player2.name}, please select a column: ')
        if column == "X": StopGame() 
        try:
            if int(column) >= 1 and int(column) <= 7:
                gameb.Place_Stone(int(column), player2)
                player2.increase_Turn_Counter()
                gameb.Show_Board()
                if player2.current_turn >= 4 and Check_Win(gameb, column, player2) == True:
                    print("------ WINNER WINNER CHICKEN DINNER           ------")
                    print(f"------ {player2.name.upper()} IS THE WINNER!                     ------")
                    print(f"------ {player1.name.upper()} IS THE DINNER...                   ------")
                    break
                if Check_Draw(gameb):
                    StopGame()

        except ValueError:
            print("------ Input not OK ------")


def run_PC_Mode():
    """ Starts and Runs the PC-Mode of the game

    1 Player plays against the PC.
    "Single-Player"-Mode

    Parameters
    ----------
    none

    Returns
    ------
    none

    """
    print("-- PC Mode is activated                                        --")
    player_name = input("-- Please enter your Name: ")
    if player_name == "X": StopGame()
    player1 = Player.Player(player_name,0,False)
    playerPC = Player.Player("PC",0,False)
    gameb = Gameboard.Gameboard(player1,playerPC)

    print("-- !Let's Start!                                                  --")
    gameb.Show_Board()
    
    while True:
        column = input(f'{player1.name}, please select a column-number: ')
        if column == "X": StopGame() 
        try:
            if int(column) >= 1 and int(column) <= 7:
                gameb.Place_Stone(int(column), player1)
                player1.increase_Turn_Counter()
                gameb.Show_Board()

                if player1.current_turn >= 4 and Check_Win(gameb, column, player1) == True:
                    print("------ WINNER WINNER CHICKEN DINNER                   ------")
                    print(f"------ {player1.name.upper()} IS THE WINNER!                  ------")
                    print(f"------ {playerPC.name.upper()} IS THE DINNER...                   ------")
                    break
                if Check_Draw(gameb):
                    StopGame()
            
        except ValueError:
            print("------ Input not OK ------")

        boolPlaceStone = True
        counterPlaceStone = 0
        print(f'{playerPC.name}, please select a column-number: ')
        time.sleep(1)

        while boolPlaceStone:
            random_column = random.randint(1, 7)
            counterPlaceStone += 1
            if gameb.Place_Stone(int(random_column), playerPC):
                print(f'{playerPC.name}, please select a column-number: {random_column}')
                boolPlaceStone = False
            elif counterPlaceStone > 20:
                break
            
        if boolPlaceStone:
            print("Es konnte leider keine freie Spalte gefunden werden!")
            StopGame()
        
        playerPC.increase_Turn_Counter()
        gameb.Show_Board()
        
        if playerPC.current_turn >= 4 and Check_Win(gameb, column, playerPC) == True:
            print("------ WINNER WINNER CHICKEN DINNER                   ------")
            print(f"------ {playerPC.name.upper()} IS THE WINNER!                  ------")
            print(f"------ {player1.name.upper()} IS THE DINNER...                   ------")
            break
        if Check_Draw(gameb):
            StopGame()
            
        


    print("")


def StopGame():
    """ Stops and Exits the Game

    This Method is for stopping and exiting the Game.

    Parameters
    ----------
    none

    Returns
    ------
    none

    """
    print("-- Game Over! Thank You!                                          --")
    exit()
    



if __name__ == '__main__':
    gamemode = start_Game()

    if gamemode == "A":
        run_CO_OP_Mode()
    elif gamemode=="B":
        run_PC_Mode()
    else:
        print("-- Game Over! Thank You!                                          --")





