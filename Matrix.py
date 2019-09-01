

class Matrix:

    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.values = [[]]
        for row in rows:
            for col in cols:
                self.values[row][col] = value

    @property
    def shape(self):
        return (self.rows, self.cols)
