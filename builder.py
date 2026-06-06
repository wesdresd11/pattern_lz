#Вариант 4
class House:  #взял для примера строителя создание дома из лекции, в этом классе взе возможные параметры дома и информация о нем

    def __init__(self):
        self.walls = None
        self.doors = []
        self.windows = []
        self.roof = None
        self.garage = None
        self.shashlik_mangal = None

    def __str__(self):
        return (
            f"Дом: Стены ({self.walls}), Крыша ({self.roof}),\n"
            f"Окна ({len(self.windows)} шт.), Двери ({len(self.doors)} шт.),\n"
            f"Гараж ({'Есть' if self.garage else 'Нет'})\n"
            f"Шашлычная зона ({'Есть' if self.shashlik_mangal else 'Нет'})\n"
        )


class HouseBuilder: #Что должен уметь каждый строитель

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

    def build_shashlik_mangal(self):
        pass

    def get_result(self) -> House: 
        pass


class BrickHouseBuilder(HouseBuilder): #Конкретный строитель кирпичного дома, и то, каким он может сделать наш домик

    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.walls = "Кирпичные стены"

    def build_doors(self):
        self.house.doors.append("Железная дверь")

    def build_windows(self):
        self.house.windows.append("Пластиковое окно")

    def build_roof(self):
        self.house.roof = "Черепичная крыша"

    def build_garage(self):
        self.house.garage = "Кирпичный гараж"
    
    def build_shashlik_mangal(self):
        self.house.shashlik_mangal = "Шашлычная зона"

    def get_result(self) -> House:
        return self.house


class Director: #Директор, упрявляет строителями, создал домик в минимальной комплектации, и супер крутой домик со всем, что только возможно

    def __init__(self, builder: HouseBuilder = None):
        self.builder = builder

    def build_minimal_house(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_doors()
        self.builder.build_windows()

    def build_super_mansion(self):
        self.builder.build_walls()
        self.builder.build_roof()
        self.builder.build_doors()
        self.builder.build_windows()
        self.builder.build_windows()
        self.builder.build_garage()
        self.builder.build_shashlik_mangal()

