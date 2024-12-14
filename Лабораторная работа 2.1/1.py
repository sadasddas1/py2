import doctest
class Laptop:
    def __init__(self, brand: str, processor_speed: float):
        """
        Создание и подготовка к работе объекта "Ноутбук"

        :param brand: Бренд устройства.
        :type brand: str.
        :param processor_speed: Скорость процессора.
        :type processor_speed: float
        :raises ValueError: Если скорость процессора < 0.

        """
        if processor_speed <= 0:
            raise ValueError("Скорость процессора должна быть выше")
        self.brand = brand
        self.processor_speed = processor_speed

    def power_on(self) -> None:
        """
        Включает устройство.

        >>> device = Laptop("Intel", 2.5)
        >>> device.power_on()
        """
        ...

    def run_application(self, app_name: str) -> str:
        """
        Запускает приложение.

        :param app_name: Название приложения.
        :type app_name: str
        :returns: Сообщение о результате запуска.
        :rtype: str

        >>> device = Laptop("Intel", 2.5)
        >>> device.run_application("browser")
        """
        ...



class Apple:
    """
    Создание и подготовка к работе объекта "Яблоко"

    :color: Цвет фрукта.
    :ripeness: Степень зрелости (0.0 - незрелый, 1.0 - спелый).

    """
    def __init__(self, color: str, ripeness: float):
        if not 0.0 <= ripeness <= 1.0:
            raise ValueError("Зрелость должна быть между 0.0 и 1.0.")
        self.color = color
        self.ripeness = ripeness


    def eat(self) -> str:
        """
        Съесть фрукт.

        >>> fruit = Fruit("red", 1.0)
        >>> fruit.eat()
        """
        ...

    def check_ripeness(self) -> float:
        """
        Проверить степень зрелости.

        :returns: Степень зрелости.
        :rtype: float

        >>> fruit = Fruit("red", 1.0) #
        >>> fruit.check_ripeness()

        """
        ...



class String:
    """
    Создание и подготовка к работе объекта "Пружина"

    :param material: Материал детали.
    :type material: str
    :param size: Размер детали в см.
    :type size: float
    :raises ValueError: если размер ниже 0.

    """

    def __init__(self, material: str, size: float):
        if size <=0:
            raise ValueError("Размер должен быть больше 0.")
        self.material = material
        self.size = size

    def move(self, distance: float) -> None:
        """
        Переместить деталь.

        :param distance: Расстояние в см.
        :type distance: float
        :raises ValueError: если дистанция ниже 0.

        >>> part = String("steel", 10)
        >>> part.move(5)
        """
        ...
    def check_integrity(self) -> bool:
        """
        Проверить целостность детали.

        :returns: True, если деталь целая, False - иначе.
        :rtype: bool

        >>> part = String("steel", 10)
        >>> part.check_integrity()
        """
        ...
if __name__ == "__main__":
    doctest.testmod()
    pass
