if __name__ == "__main__":
    from typing import Union


    class Shape:
        """
        Базовый класс для геометрических фигур.
        """

        def __init__(self, color: str = "black"):
            """
            Конструктор класса Shape.

            Args:
                color: Цвет фигуры (по умолчанию: "black").
            """
            self.color = color
            self._area = None
        def get_area(self) -> Union[float, None]:
            """
            Возвращает площадь фигуры.

            Подклассы должны переопределить этот метод, чтобы вычислить фактическую площадь.

            Returns:
                Площадь фигуры или None, если площадь не определена.
            """
            return self._area

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Shape.
            """
            return f"Shape (color: {self.color}, area: {self.get_area()})"

        def __repr__(self) -> str:
            """
            Возвращает представление объекта Shape в виде строки, пригодной для отладки.
            """
            return f"Shape(color='{self.color}')"

        def describe(self) -> str:
            """
            Общее описание фигуры.  Может быть переопределено в подклассах для большей конкретики.
            """
            return f"Это геометрическая фигура."


    class Circle(Shape):
        """
        Класс, представляющий круг.
        """

        def __init__(self, radius: float, color: str = "blue"):
            """
            Конструктор класса Circle.  Расширяет конструктор базового класса Shape.

            Args:
                radius: Радиус круга.
                color: Цвет круга (по умолчанию: "blue").
            """
            super().__init__(color)
            self.radius = radius
            self._area = self.calculate_area()

        def calculate_area(self) -> float:
            """
            Вычисляет площадь круга.

            Returns:
                Площадь круга.
            """
            return 3.14159 * self.radius * self.radius

        def get_area(self) -> float:
            """
            Переопределенный метод get_area для возврата площади круга.

            Этот метод переопределен, так как вычисление площади круга отличается от общей формулы для площади Shape.
            """
            return self._area

        def __str__(self) -> str:
            """
            Переопределенный метод __str__ для класса Circle.
            """
            return f"Circle (radius: {self.radius}, color: {self.color}, area: {self.get_area()})"

        def __repr__(self) -> str:
            """
            Переопределенный метод __repr__ для класса Circle.
            """
            return f"Circle(radius={self.radius}, color='{self.color}')"

        def describe(self) -> str:
            """
            Переопределенный метод describe для класса Circle.
            """
            return f"Это круг радиусом {self.radius} и цветом {self.color}."
    pass
