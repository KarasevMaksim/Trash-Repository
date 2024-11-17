from typing import Final, Callable, Type, TypeVar


# Base TypeHint ===============================================================

PI: Final[float] = 3.14
MAX_COUNT: Final[int] = 100

name: str = 'Olga'
age: int = 10
mass: list[str] = ['Irina', 'Senko']
my_dict: dict[int, str] = {1: 'Kira'} # В словарях аннатируется ключ значение
cort: tuple[int, str] = (666, 'zero') # В кортежах аннатируется каждый элемент
elems: tuple[float, ...] = (1.1, 1.2, 1.3, 1.4)


def sum_two_numbers(x: int, y: int) -> int:
    return x + y

def example_two_types(
    x: int | float,
    y: int | float
    ) -> int | float:
    
    return x + y

# Если входные данные могут быть None
def process_item(item: str | None) -> None:
    if not item is None:
        print(item)
        
def hint_for_arg_func(
    func: Callable[[int], bool],
    mass: list[int]
    ) -> list[int] | None:
    # В callable[[int], bool] в вложеном списке указываются значения аргументов
    # передоваемой функции, далее возврощаемое значение.
    if mass:
        return mass[::].append(1)
    func(mass)
    



class FurFur:
    pass

T = TypeVar('T') # TypeHint для классов без ограничений
T = TypeVar('T', bound=FurFur) # TypeHint для одного класс и его наследников

    
def constract_object(class_obj: Type[T]) -> T:
    return class_obj()


# TypeHint with NamedTuple ====================================================
from typing import NamedTuple

class Coordinates(NamedTuple):
    latitude: float
    longitude: float
    
def get_gps_coord() -> Coordinates:
    result = Coordinates(
        latitude=10.0,
        longitude=20.0
    )
    return result

# TypeHint for Dicts with Literal =============================================
from typing import Literal

def get_gps_coord2() -> dict[Literal['latitude'] | Literal['longitude'], float]:
    res = {
        'latitude': 10.0,
        'longitude': 20.0
    }
    return res

# TypeHint with TypedDict =====================================================
from typing import TypedDict

class Coordinates2(TypedDict):
    longitude: float
    latitude: float
    
def get_gps_coord3() -> Coordinates2:
    res = Coordinates2(
        **{
            'latitude': 10.1,
            'longitude': 20.1
          }
    )
    return res

# TypeHint with @dataclass
# Создает эмуляцию обращения по атрибутам как в экземплярах класс, в отличии
# от именованных кортежей, является изменяемым типом данных.
from dataclasses import dataclass

@dataclass
class Coordinates4:
    longitude: float
    latitude: float
    
def get_gps_coord4() -> Coordinates4:
    res = Coordinates4(
        **{
            'latitude': 10.1,
            'longitude': 20.1
          }
    )
    # or
    # res = Coordinates4(latitude=10.1, longitude=20.1)
    return res

# TypeHint for Enum ===========================================================
# Используется для перечесления данных
from enum import Enum
from typing import NamedTuple
from datetime import datetime


class WeatherType(Enum):
    THUNDERSTORM = 'Гроза'
    RAIN = 'Дождь'
    SNOW = 'Снег'
    CLEAR = 'Ясно'

class Weather(NamedTuple):
    temerature: int
    weather_type: WeatherType
    city: str
    sunrise: datetime