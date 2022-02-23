from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=1):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError


    def move(self, distance):

        max_distance = self.fuel // self.fuel_consumption
        if max_distance == 0 or distance > max_distance:
            raise exceptions.NotEnoughFuel
        else:
            self.fuel -= distance * self.fuel_consumption

