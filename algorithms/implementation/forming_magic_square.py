class MagicSquare(object):
    valid_squares = [
            [8, 1, 6, 7, 2, 9, 4, 3],
            [4, 3, 8, 1, 6, 7, 2, 9],
            [2, 9, 4, 3, 8, 1, 6, 7],
            [6, 7, 2, 9, 4, 3, 8, 1],
            [8, 3, 4, 9, 2, 7, 6, 1],
            [6, 1, 8, 3, 4, 9, 2, 7],
            [2, 7, 6, 1, 8, 3, 4, 9],
            [4, 9, 2, 7, 6, 1, 8, 3]
        ]

    def __init__(self, square):
        """The implementation could also be done with a "regular"
        representation of the square, but in my opinion the current
        implementation gives clearer and better readable code in the
        actual computation function."""
        self.square = square
        self.alt_repr = self._alt_repr()

    def _alt_repr(self):
        # Represent the square without the middle element and walking
        # over the elements in order, i.e. starting in the top left
        # corner and going clockwise.
        tmp = self.square
        return [*tmp[0],
                tmp[1][2], tmp[2][2],
                tmp[2][1], tmp[2][0], tmp[1][0]]

    def minimum_distance(self):
        # 50 gives an upper bound, since all elements are within [1, 9].
        res = 50

        # Check what the minimal difference is between a valid sqaure
        # and the given square, by using the alternative representation.
        for valid_square in self.valid_squares:
            diff = sum([abs(x - y) for x, y in zip(valid_square, self.alt_repr)])

            res = min(res, diff)

        # Add the difference for the middle square.
        return res + abs(self.square[1][1] - 5)


if __name__ == '__main__':
    square = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
    print(MagicSquare(square).minimum_distance())
