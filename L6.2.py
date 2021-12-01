class Road:
    def __init__(self, len, wid):
        self._len = len
        self._wid = wid

    def calc(self, wiqht=30, thickness=5):
        print(f"Требуемая масса асфальта - {self._len * self._wid * wiqht * thickness / 1000} тонн ")


def main():
    while True:
        try:
            road_1 = Road(int(input("Введите ширину дороги в метрах: ")), int(input("Введите длину дороги в метрах: ")))
            road_1.calc()
            break
        except ValueError:
            print("Только целое!")

main()

