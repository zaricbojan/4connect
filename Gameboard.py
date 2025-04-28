

import Player

class Gameboard:
    """ Creates a Gameboard

    This Class creates a gameboard - 6x7.
    Can be used for a 4connect game.

    Parameters
    ----------
    Collection: collection
        its Collection in a Collection which represents the gameboard.
        first level equals rows
        second level equals columns
    
    Methods
    -------
    display_board(self):
        Prints the current state of the board.
    
    place_piece(self, column, player):
        Places a player's stone ('o' in a specific color) in the given column, if possible.

    """
    #ChatGPT
    # ANSI Escape-Codes for Colors
    __RED = '\033[31m'    # Rot
    __GREEN = '\033[32m'  # Grün
    __RESET = '\033[0m'   # Zurücksetzen auf Standardfarbe
    # Output with different Colors
    # print(f"{GREEN}O{RESET} {RED}o{RESET}")

    #'\033[32mo\033[0m Grün
    # \033[31mo\033[0m Rot

    def __init__(self, player1: Player, player2: Player):
        self.Collection = [['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],
                           ['x','x', 'x', 'x', 'x', 'x', 'x'],]
        self.player1 = player1
        self.player2 = player2
        
        


    def __repr__(self):
        return f'{self.Collection}'
    
    # Here the Gameboard will be printed
    # it will show the current score
    def Show_Board(self):
        """ Prints the Gameboard.

        Prints the current state of the Gameboard

        Parameters
        ----------
        none
        
        Returns
        -------
        none

        """
        string_4_print = ""
        for row in self.Collection:
            for column in row:
                string_4_print += column + "   "
            print(string_4_print)
            string_4_print = ""


    # Here a Stone is thrown into a column
    # the return value describes, if the Stone placing was successfull or not
    # it wont be successfull, if the column is already full
    # print(f"{GREEN}O{RESET} {RED}o{RESET}")
    def Place_Stone(self, column: int, player: Player) -> bool:
        """ Places a player's stone

        Places a player's stone ('o' in a specific color, depending on the player) in the given column, if possible.

        Parameters
        ----------
        column: int
            defines in which column the stone needs to be thrown
        player: Player
            defines which player (and which color) is placing the stone
        
        Returns
        -------
        Place_Stone: bool
            returns if a stone placing was succesfull
            if false, the column is already full

        """
        column = column-1
        if self.Collection[0][column] == "o":
            return False
        
        for i in range(5, -1, -1):
            if self.Collection[i][column] == "x":
                if player == self.player1:
                    self.Collection[i][column] = f'{self.__GREEN}o{self.__RESET}'
                elif player == self.player2:
                    self.Collection[i][column] = f'{self.__RED}o{self.__RESET}'
                return True
        
            




if __name__ == '__main__':
    player1 = Player.Player("Bojan",0,False)
    player2 = Player.Player("Adam",0,False)
    s = Gameboard(player1,player2)
    s.Show_Board()

    s.Place_Stone(1,player1)
    s.Place_Stone(1,player1)
    s.Place_Stone(1,player2)

    s.Place_Stone(2,player1)
    s.Place_Stone(2,player2)

    s.Place_Stone(3,player2)

    s.Place_Stone(7,player1)

    print("------------------------------------------------")
    s.Show_Board()

    print(s.Collection[5][0])

    if "\033[32mo\033[0m" in s.Collection[5][0]:
        print("OK")
