

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
        if type(self.vals[0]) is list:
            return len(self.vals[0])
        else:
            return 1

    @property
    def shape(self):
        return self.rows, self.cols

    def __getitem__(self, idx):
        return self.vals[idx]

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
            assert self.rows == other.rows and self.cols == other.cols
            return Matrix([[self[row][col] + other[row][col] for col in range(self.cols)] for row in range(self.rows)])

    def __sub__(self, other):
        if type(other) is int or type(other) is float:
            return Matrix([[self[row][col] - other for col in range(self.cols)] for row in range(self.rows)])
        elif type(other) is Matrix:
            assert self.rows == other.rows and self.cols == other.cols
            return Matrix([[self[row][col] - other[row][col] for col in range(self.cols)] for row in range(self.rows)])

    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            return Matrix([[self[row][col] * other for col in range(self.cols)] for row in range(self.rows)])
        elif type(other) is Matrix:
            pass

if __name__ == '__main__':
    print(Matrix([[0, 1], [2, 3], [4, 5], [6, 7]]))
    print(Matrix(rows=2, cols=4))
    print(Matrix(rows=3, cols=5, val=1))
    print(Matrix([[10, 9], [8, 7]]) - Matrix([[5, 6], [7, 8]]))