from abc import ABC, abstractmethod
class Game(ABC):
    @abstractmethod
    def actions(self, state, player):
        """Identificar cuales son los movimientos o jugadas posibles de un jugador"""
        raise NotImplementedError

    @abstractmethod
    def result(self, state, move):
        """Ejecutar un movimiento o jugada y retornar el nuevo estado"""
        raise NotImplementedError

    @abstractmethod
    def utility(self, state, player):
        """Calcular la función de utilidad"""
        raise NotImplementedError

    @abstractmethod
    def terminal_test(self, state):
        """Retorna el valor de este estado final al jugador"""
        return not self.actions(state, 1)

    @abstractmethod
    def to_move(self, state):
        """Devuelve al jugador cuya jugada está en este estado."""
        return 1

    def display(self, state):
        """Imprime o muestra el estado."""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    @abstractmethod
    def play_game(self):
        """Realiza un movimiento alternativo de n personas."""
        raise NotImplementedError


