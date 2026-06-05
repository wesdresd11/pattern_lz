class House:

    def __init__(self):
        self.walls = None
        self.doors = []
        self.windows = []
        self.roof = None
        self.garage = None

    def __str__(self):
        return (
            f"Дом: Стены ({self.walls}), Крыша ({self.roof}), "
            f"Окна ({len(self.windows)} шт.), Двери ({len(self.doors)} шт.), "
            f"Гараж ({'Есть' if self.garage else 'Нет'})"
        )


class HouseBuilder:

    def build_walls(self): 
        pass

    def build_doors(self): 
        pass

    def build_windows(self): 
        pass

    def build_roof(self): 
        pass

    def build_garage(self): 
        pass

    def get_result(self) -> House: 
        pass


class BrickHouseBuilder(HouseBuilder):

    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Кирпичные стены"

    def build_doors(self):
        self.house.doors.append("Деревянная дверь")

    def build_windows(self):
        self.house.windows.append("Пластиковое окно")

    def build_roof(self):
        self.house.roof = "Черепичная крыша"

    def build_garage(self):
        self.house.garage = "Кирпичный гараж"

    def get_result(self) -> House:
        return self.house


class Director:

    def __init__(self, builder: HouseBuilder = None):
        self.builder = builder

    def build_minimal_house(self):
        self.builder.build_walls()
        self.builder.build_roof()

    def build_full_featured_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_windows()
        self.builder.build_garage()


if __name__ == "__main__":
    builder1 = BrickHouseBuilder()
    director1 = Director(builder1)
    director1.build_minimal_house()
    print(builder1.get_result())

    builder2 = BrickHouseBuilder()
    director2 = Director(builder2)
    director2.build_full_featured_house()
    print(builder2.get_result())
