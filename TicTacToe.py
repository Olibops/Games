def win_check(game):

    if game[0][0] == game[0][1] == game[0][2] and game[0][0] != 0:
        return game[0][0]

    if game[1][0] == game[1][1] == game[1][2] and game[1][0] != 0:
        return game[1][0]
    
    if game[2][0] == game[2][1] == game[2][2] and game[2][0] != 0:
        return game[2][0]

    if game[0][0] == game[1][0] == game[2][0] and game[0][0] != 0:
        return game[0][0]

    if game[0][1] == game[1][1] == game[2][1] and game[0][1] != 0:
        return game[0][1]

    if game[0][2] == game[1][2] == game[2][2] and game[0][2] != 0:
        return game[0][2]

    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0:
        return game[0][0]
    
    if game[2][0] == game[1][1] == game[0][2] and game[1][1] != 0:
        return game[0][0]

class Game:
    def __init__(self, game):
        self.game = game
    
    def add_move(self, y):

        game=self.game

        if win_check(game) == "X":
            print("X has already won")
            
        if win_check(game) == "O":
            print("0 has already won")

        else:

            X_count, O_count = game[0].count("X") + game[1].count("X") + game[2].count("X"), game[0].count("O") + game[1].count("O") + game[2].count("O")

            if X_count+O_count==9:
                print("No more moves, game is drawn")

            else:

                if X_count!=O_count:
                    scribble="X"
                else:
                    scribble="O"


                if game[y//3][y%3] == 0:
                    game[y//3][y%3] = scribble

                else:
                    print("Oi no cheating, thats very naughty")

                if win_check(game) =="X":
                    print("X has won")
                
                if win_check(game) =="0":
                    print("0 has won")

        return Game(game)

def new_game():

    return Game(game=[[0,0,0],[0,0,0],[0,0,0]])




        