from functools import reduce


class Matrix:

    def __init__(self, vals=None, rows=None, cols=None, val=0):
        if not vals:
            assert rows
            assert cols
            self.vals = [[val for _ in range(cols)] for _ in range(rows)]
        else:
            self.vals = vals

    @property
    def rows(self):
        return len(self.vals)

    @property
    def cols(self):
        return len(self.vals[0]) if type(self.vals[0]) is list else 1

    @property
    def shape(self):
        return self.rows, self.cols

    @property
    def T(self):
        return Matrix([[self[row][col] for row in range(self.rows)] for col in range(self.cols)])

    def __getitem__(self, idx):
        return self.vals[idx] if type(self.vals[idx]) is list else [self.vals[idx]]

    def __setitem__(self, idx, val):
        self.vals[idx] = val

    def __str__(self):
        out = '\n'
        for row in range(self.rows):
            out += '\t'
            for col in range(self.cols):
                out += str(self[row][col]) + ' '
            out += '\n'
        return out

    def __add__(self, other):
        if type(other) is int or type(other) is float:
            return Matrix([[self[row][col] + other for col in range(self.cols)] for row in range(self.rows)])
        elif type(other) is Matrix:
            assert self.shape == other.shape
            return Matrix([[self[row][col] + other[row][col] for col in range(self.cols)] for row in range(self.rows)])

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            return Matrix([[self[row][col] - other for col in range(self.cols)] for row in range(self.rows)])
        elif type(other) is Matrix:
            assert self.shape == other.shape
            return Matrix([[self[row][col] - other[row][col] for col in range(self.cols)] for row in range(self.rows)])

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Matrix([[self[row][col] * other for col in range(self.cols)] for row in range(self.rows)])
        elif type(other) is Matrix:
            assert self.cols == other.rows
            return Matrix([[reduce(lambda a, b: a + b, [self[row][i] * other[i][col] for i in range(self.cols)]) for col in range(other.cols)] for row in range(self.rows)])
