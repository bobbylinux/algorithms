class QueensProblem:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for _ in range(n)] for _ in range(n)]

    def print_queens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_table[i][j] == 1:
                    print('Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')

    def solve_n_queens(self):
        if self.solve(0):
            self.print_queens()
        else:
            print('there is no solution to the problem...')

    # stesso indice della regina
    def solve(self, col_index):

        # caso base
        if col_index == self.n:
            return True
        # proviamo a trovare una posizione per la regina nella col_index
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                self.chess_table[row_index][col_index] = 1

                if self.solve(col_index + 1):
                    return True
                # backtrack
                self.chess_table[row_index][col_index] = 0
        # quando abbiamo considerato tutte le posizioni di una colonna senza trovare una valida cella per la regina
        return False

    def is_place_valid(self, row_index, col_index):
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False

        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        j = col_index

        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        return True


if __name__ == '__main__':
    queens = QueensProblem(4)
    queens.print_queens()
