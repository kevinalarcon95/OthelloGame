from Game import Game
class Othello(Game):

    def __init__(self):
        self.points_board = [[100, -10, 5, 2, 2, 5, -10, 100],
                             [-10, -30, -2, -2, -2, -2, -30, -10],
                             [5, 2, 10, 10, 10, 10, 2, 5],
                             [3, 2, 10, 0, 0, 10, 2, 3],
                             [3, 2, 10, 0, 0, 10, 2, 3],
                             [5, 2, 10, 10, 10, 10, 2, 5],
                             [-10, -30, -2, -2, -2, -2, -30, -10],
                             [100, -10, 5, 2, 2, 5, -10, 100]]
        self.n_columns = 8
        self.n_rows = 8

    def to_move(self, state):
        white = self.count(state, 2)
        black = self.count(state, 1)
        sm = white + black
        if sm % 2 == 0:
            return 1
        else:
            return 2

    def actions(self, state):
        player = self.to_move(state)
        actions = []
        positions_player = self.positions_of_player(state, player)
        for index in positions_player:
            legal_movs = self.legal_moves(state, index, player)
            actions.extend(legal_movs)

        for i in range(len(actions) - 1):
            sub = actions[i + 1: len(actions)]
            while len(sub) > 0:
                act = sub.pop()
                if actions[i][0] == act[0] and actions[i][1] == act[1]:
                    pos_opponents = act[3]
                    actions[i][3].extend(pos_opponents)
                    actions.remove(act)
        return actions

    def result(self, state, move):
        aux_state = state
        aux_state[move[0]][move[1]] = move[2]
        for pos in move[3]:
            aux_state[pos[0]][pos[1]] = move[2]
        return aux_state

    def utility(self, state, player):
        fichas = self.count(state, player) - self.count(state, 2)
        points_black = 0
        points_white = 0

        for x in range(8):
            for y in range(8):
                # player is black
                if state[x][y] == 1:
                    points_black += self.points_board[x][y]
                # player is white
                elif state[x][y] == 2:
                    points_white += self.points_board[x][y]

        suma = (points_black - points_white)
        return suma

    def terminal_test(self, state):
        # Si hay ganador o si no hay casillas vacias (tablero lleno)
        if not self.actions(state) or self.count(state, 0) == 0:
            return True
        return False

    def play_game(self):
        raise NotImplementedError

    def positions_of_player(self, state, player):
        listPlayer = []
        for i in range(len(state)):
            for j in range(len(state)):
                if player == state[i][j]:
                    listPlayer.append([i, j])
        return listPlayer

    def legal_moves(self, state, position, player):
        column = [c[position[1]] for c in state]
        row = state[position[0]]
        actions = []

        if player == 1:
            opponent = 2
        else:
            opponent = 1

        action = self.up(column, position, player, opponent)
        if action is not None:
            actions.append(action)

        action = self.down(column, position, player, opponent)
        if action is not None:
            actions.append(action)
            # print("DO", action[0], " ", action[1])

        action = self.right(row, position, player, opponent)
        if action is not None:
            actions.append(action)

        action = self.left(row, position, player, opponent)
        if action is not None:
            actions.append(action)

        action = self.semiDiagonalUpRight(state, position, player, opponent)
        if action is not None:
            actions.append(action)

        action = self.semiDiagonalDownRight(state, position, player, opponent)
        if action is not None:
            actions.append(action)

        action = self.semiDiagonalUpLeft(state, position, player, opponent)
        if action is not None:
            actions.append(action)

        action = self.semiDiagonalDownLeft(state, position, player, opponent)
        if action is not None:
            actions.append(action)

        return actions

    def up(self, column, position, player, opponent):
        x = position[0]
        y = position[1]
        if x > 1:
            sub_column = column[0:x]
            if opponent == sub_column[x - 1]:
                pos_opponents = [[x - 1, y]]
                for i in range(len(sub_column) - 2, -1, -1):
                    if sub_column[i] == 0:
                        return [i, y, player, pos_opponents]
                    elif sub_column[i] == player:
                        return None
                    pos_opponents.append([i, y])
                return None
            return None
        return None

    def down(self, column, position, player, opponent):
        x = position[0]
        y = position[1]
        if x < len(column) - 2:
            sub_column = column[x + 1:len(column)]
            if opponent == column[x + 1]:
                pos_opponents = [[x + 1, y]]
                for i in range(1, len(sub_column)):
                    if sub_column[i] == 0:
                        return [i + x + 1, y, player, pos_opponents]
                    elif sub_column[i] == player:
                        return None
                    pos_opponents.append([i + x + 1, y])
                return None
            return None
        return None

    def left(self, row, position, player, opponent):
        x = position[0]
        y = position[1]
        if y > 1:
            sub_row = row[0:y]
            if opponent == sub_row[y - 1]:
                pos_opponents = [[x, y - 1]]
                for i in range(len(sub_row) - 2, -1, -1):
                    if sub_row[i] == 0:
                        return [x, i, player, pos_opponents]
                    elif sub_row[i] == player:
                        return None
                    pos_opponents.append([x, i])
                return None
            return None
        return None

    def right(self, row, position, player, opponent):
        x = position[0]
        y = position[1]
        if y < len(row) - 2:
            sub_row = row[y + 1:len(row)]
            if opponent == row[y + 1]:
                pos_opponents = [[x, y + 1]]
                for i in range(len(sub_row)):
                    if sub_row[i] == 0:
                        return [x, i + y + 1, player, pos_opponents]
                    elif sub_row[i] == player:
                        return None
                    pos_opponents.append([x, i + y + 1])
                return None
            return None
        return None

    def semiDiagonalUpRight(self, state, position, player, opponent):
        x = position[0]
        y = position[1]
        if y < self.n_columns - 2 and x > 1:
            x -= 1
            y += 1
            if state[x][y] == opponent:
                pos_opponents = [[x, y]]
                while x > 0 and y < self.n_columns - 1:
                    x -= 1
                    y += 1
                    if state[x][y] == 0:
                        return [x, y, player, pos_opponents]
                    elif state[x][y] == player:
                        return None
                    pos_opponents.append([x, y])
                return None
            return None
        return None

    def semiDiagonalDownLeft(self, state, position, player, opponent):
        x = position[0]
        y = position[1]
        if y > 1 and x < self.n_rows - 2:
            x += 1
            y -= 1
            if state[x][y] == opponent:
                pos_opponents = [[x, y]]
                while x < self.n_rows - 1 and y > 0:
                    x += 1
                    y -= 1
                    if state[x][y] == 0:
                        return [x, y, player, pos_opponents]
                    elif state[x][y] == player:
                        return None
                    pos_opponents.append([x, y])
                return None
            return None
        return None

    def semiDiagonalDownRight(self, state, position, player, opponent):
        x = position[0]
        y = position[1]
        if y < 6 and x < 6:
            x += 1
            y += 1
            if state[x][y] == opponent:
                pos_opponents = [[x, y]]
                while x < self.n_columns - 1 and y < self.n_columns - 1:
                    x += 1
                    y += 1
                    if state[x][y] == 0:
                        return [x, y, player, pos_opponents]
                    elif state[x][y] == player:
                        return None
                    pos_opponents.append([x, y])
                return None
            return None
        return None

    def semiDiagonalUpLeft(self, state, position, player, opponent):
        x = position[0]
        y = position[1]
        if y > 1 and x > 1:
            x -= 1
            y -= 1
            if state[x][y] == opponent:
                pos_opponents = [[x, y]]
                while x > 0 and y > 0:
                    x -= 1
                    y -= 1
                    if state[x][y] == 0:
                        return [x, y, player, pos_opponents]
                    elif state[x][y] == player:
                        return None
                    pos_opponents.append([x, y])
                return None
            return None
        return None

    def count(self, state, chip):
        cont = 0
        for i in state:
            cont += i.count(chip)
        return cont