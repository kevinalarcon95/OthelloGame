from Board import Board
def main():
    print('\n')
    print("----------------------------------")
    print('\t\tWelcome to Othello Game')
    board = Board()

    while not board.game.terminal_test(board.model):
        print('\n')
        print("----------------------------------")
        print('Turno del Jugador: ')
        x = int(input("Posicion X: "))
        y = int(input("Posicion Y: "))
        board.star_Game(x, y)

        playerChips = board.game.count(board.model,1)
        pcChips = board.game.count(board.model,2)

        if (playerChips > 32):
            print('El ganador es el Jugador 1')
            break
        elif (pcChips > 32):
            print('El ganador es el Jugador 2')
            break
main()