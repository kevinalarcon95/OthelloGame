class Board():

    def __init__(self):
        self.grid_column = 8
        self.grid_row = 8
        self.model = [[0 for x in range(self.grid_column)] for y in range(self.grid_row)]
        self.player = 1
        self.pos = (0, 0)
        self.game = Othello()
        self.initialState()
        self.drawBoard()

    def drawChips(self):
        for i in range(len(self.model)):
            row=self.model[i]
            for j in range(len(row)):
                val = self.model[i][j]
                if(val == 1):
                    self.model[i][j] = 1
                elif(val == 2):
                    self.model[i][j] = 2

    def star_Game(self, x, y):
        self.player = 2
        if self.play_opponent(x, y):
            self.player = 1
            self.call_alpha_beta()

        player = self.game.count(self.model, 2)
        pc = self.game.count(self.model, 1)
        print("----------------------------------")
        print("\t\t\tMarcador")
        print("Player: " + str(pc))
        print("PC: " + str(player))
        print("----------------------------------")

    def initialState(self):
        idx1 = int(len(self.model) / 2 - 1)
        idx2 = int(len(self.model) / 2)
        self.model[idx1][idx1] = 2
        self.model[idx1][idx2] = 1
        self.model[idx2][idx1] = 1
        self.model[idx2][idx2] = 2

    def drawBoard(self):
        print("***********************************")
        print("  | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
        print("***********************************")
        for i in range(self.grid_row):
            print(i, end=' | ')
            for j in range(self.grid_column):
                if(self.model[i][j] == 0):
                    print(' ', end=' | ')
                elif(self.model[i][j] == 1):
                    print('X', end=' | ')
                else:
                    print('O', end=' | ')
                    #print(self.model[i][j], end=' | ')
            print('\n')

    def validate_play(self, i, j):
        flag = False
        state = copy.deepcopy(self.model)

        if state[i][j] == 0:
            state[i][j] = self.player
            # acciones legales del oponente
            state2 = copy.deepcopy(self.model)
            actions = self.game.actions(state2)
            for action in actions:
                if action[0] == i and action[1] == j:
                    self.model = self.game.result(state, action)
                    flag = True
                    break
            if flag is False:
                print("¡ERROR!", "Movimiento inválido")
        return flag

    def call_alpha_beta(self):
        state = copy.deepcopy(self.model)
        state2 = copy.deepcopy(self.model)
        action = alphabeta_search(state, self.game, 6)

        if action is not None:
            self.model = self.game.result(state2, action)
        print('\n')
        print("----------------------------------")
        print('Turno del PC')
        self.drawBoard()

    def play_opponent(self, x, y):
        self.pos = (x, y)
        flag = self.validate_play(x, y)
        self.drawBoard()
        return flag