class Stack(object):
    def __init__(self, lst):
        self.lst = lst

    def peek(self):
        return self.lst[-1]

    def pop(self):
        return self.lst.pop()

    def push(self, elt):
        self.lst.append(elt)

    def __len__(self):
        return len(self.lst)


class UniqueStack(Stack):
    def __init__(self, lst):
        self.lst = self._make_unique(lst)

    @staticmethod
    def _make_unique(lst):
        """Remove dublicated from a decreasingly sorted list."""
        # By removing the duplicates the length of the stack implies the
        # ranking.
        res = []
        for elt in lst:
            if not res or res[-1] != elt:
                res.append(elt)

        return res


def get_rankings(leaderboard, scores):
    l = UniqueStack(leaderboard)

    # Set a default ranking of 1, since once alice ranking exceeds the
    # number one ranking she will always be first for the consecutive
    # scores.
    rankings = len(scores) * [1]
    for i, score in enumerate(scores):
        while l and score > l.peek():
            l.pop()

        if not l:
            break
        elif score < l.peek():
            rankings[i] = len(l) + 1
        else:
            rankings[i] = len(l)

    return rankings


if __name__ == '__main__':
    leaderboard = [100, 90, 90, 80, 75, 60]
    scores = [50, 65, 77, 90, 102]
    print(get_rankings(leaderboard, scores))

    leaderboard = [100, 100, 50, 40, 40, 20, 10]
    scores = [5, 25, 50, 120]
    print(get_rankings(leaderboard, scores))
