

class Matrix:

    def __init__(self, rows, cols, val=0):
        self.rows = rows
        self.cols = cols
        self.vals = [[val for _ in range(self.cols)] for _ in range(self.rows)]

    @property
    def shape(self):
        return (self.rows, self.cols)

    def __getitem__(self, idx):
        return self.vals[idx]

    def __setitem__(self, idx, val):
        self.vals[idx] = val

    def __str__(self):
        out = ''
        for row in range(self.rows):
            for col in range(self.cols):
                out += str(self[row][col]) + ' '
            out += '\n'
        return out