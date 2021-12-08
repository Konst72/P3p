a = [[2, 4, 6], [3, 4, -7], [1, 2, 8]]
c = [[1, 5, 3], [9, -4, 5], [0, 2, 4]]


class Matrix:

    def __init__(self, kit):
        self.kit = kit

    def __str__(self):
        return '\n'.join('\t'.join([f"{itm}" for itm in line]) for line in self.kit)

    def __add__(self, other):
        b = []
        for i in range(len(self.kit)):
            b.append([])
            for j in range(len(self.kit)):
                b[i].append(self.kit[i][j] + other.kit[i][j])
        return '\n'.join('\t'.join([f"{itm}" for itm in line]) for line in b)


matr_a = Matrix(a)
matr_c = Matrix(c)
m_n = matr_c + matr_a

print(f"Матрица а\n{matr_a}\n{'♠'*15}")
print(f"Матрица c\n{matr_c}\n{'♠'*15}")
print(f"Сумма матриц а и c\n{m_n}\n{'♠'*15}")
