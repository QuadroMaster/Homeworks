"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=0):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)

        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, added_cargo):
        if self.cargo + added_cargo <= self.max_cargo:
            self.cargo += added_cargo

        else:
            raise CargoOverload

    def remove_all_cargo(self):
        cargo_value = self.cargo
        self.cargo = 0
        return cargo_value
