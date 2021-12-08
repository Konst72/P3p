class Cell:
    def __init__(self, square):
        self.square = int(square)

    def make_order(self, stro):
        return '\n'.join(['\a' * stro for _ in range(self.square // stro)]) + '\n' + '\a' * (self.square %stro)

    def __add__(self, other):
        return f"Cумма клеток равна: {self.square + other.square}"

    def __sub__(self, other):
        raz = self.square - other.square
        return f"Осталось{raz} клеток " if raz > 0 else "Все пропало..."

    def __truediv__(self, other):
        return self.square // other.square

    def __mul__(self, other):
        return self.square * other.square




cell_1 = Cell(40)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_2.make_order(7))