from time import sleep
import itertools

class TrafficLight:
    __color = [["красный", [7, 31]], ["желтый", [2, 33]], ["зеленый", [10, 32]], ["желтый", [2, 33]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
            sleep(light[1][0])

traffic_light_1 = TrafficLight()
traffic_light_1.running()
