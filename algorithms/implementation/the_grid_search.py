def get_occurrences(seq, string):
    """Return a list indeces on which the sequence starts."""
    n = len(seq)
    return [i for i, v in enumerate(string) if string[i:i+n] == seq]


def is_seq_in_grid(seq, grid):
    for i, row in enumerate(grid):
        # Get possible starting positions for the sequence.
        start_positions = get_occurrences(seq[0], row)

        # For each occurence of the first string of the seq, check each
        # subsequent row whether it holds the next string of the seq
        # starting at the same position as the first string.
        for sp in start_positions:
            for j in range(1, len(seq)):
                if grid[i+j][sp:sp + len(seq[0])] != seq[j]:
                    break
            else:
                return True

        # When the sequence would fit in the grid anymore, break.
        if i == len(grid) - len(seq):
            break

    return False


if __name__ == '__main__':
    seq = 'World!'
    string = 'Hello World! World!'
    print(get_occurrences(seq, string))

    seq = ['876543',
           '111111',
           '111111']
    grid = ['1234567890',
            '0987654321',
            '1111111111',
            '1111111111',
            '2222222222']
    print(is_seq_in_grid(seq, grid))
