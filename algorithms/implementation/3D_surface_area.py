from functools import reduce


class Board(object):
    def __init__(self, board):
        self.board = board

        if board:
            self.num_rows = len(board)
            self.num_cols = len(board[0])
        else:
            self.num_rows = 0
            self.num_cols = 0

    def _is_valid(self, i, j):
        """Return whether the given index is contained in the board."""
        return 0 <= i < self.num_rows and 0 <= j < self.num_cols

    def _get_height(self, i, j):
        """Return the height of the box on index (i, j)."""
        if self._is_valid(i, j):
            return self.board[i][j]
        else:
            return 0

    def _get_neighbours(self, i, j):
        """Return the heights of the neighbors of index (i, j)."""
        neighbours = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

        return [self._get_height(*pair) for pair in neighbours]

    def get_surface_area(self):
        """Return the surface area of the given board of heights."""
        area = 0
        reduce_func = lambda x, y: x + (height - y) if y < height else x

        # For each block look at its four direct neighbours and compute
        # the difference in height if the blocks height is greater than
        # its neighbours (this gives an ordering). In case the blocks is
        # on the boundary, consider its neighbor to have height zero.
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                neighbours = self._get_neighbours(i, j)
                height = self._get_height(i, j)

                area += reduce(reduce_func, neighbours, 0)

                # If the block exists then it automatically has an area
                # of at least two (its bottom and top).
                if height:
                    area += 2

        return area


if __name__ == '__main__':
    board = [[1, 3, 4], [2, 2, 3], [1, 2, 4]]
    print(Board(board).get_surface_area())

    board = [[1]]
    print(Board(board).get_surface_area())
