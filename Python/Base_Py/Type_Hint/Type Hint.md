#python #type_hint
# Аннотация типов для python
## Base Type Hint
```python
name: str = 'Olga'
age: int = 10
array: list[str] = ['Irina', 'Senko']
my_dict: dict[int, str] = {1: 'Kira'} # В словорях аннатируется ключ: значение
my_tuple: tuple[int, str] = (666, 'zero') # В кортежах аннатируется каждый элемент пары
elems: tuple[float, ...] = (1.1, 1.2, 1.3, 1.4)
```
***
## Type Hint для констант
```python
from typing import Final
PI: Final[float] = 3.14
MAX_COUNT: Final[int] = 100
```
***
## Type Hint для простой функции
```python
def sum_two_numbers(x: int, y:int) -> int:
	return x + y


def example_two_types(
	x: int | float,
	y: int | float
) -> int | float:
	return x + y

# если входные данные могут быть None
def process_item(item: str | None) -> None:
	if not item is None:
		print(item)
```
***
## Type Hint если аргумент является функцией или вызываемым объектом
### Описание:
В `callable[[int], bool]` в вложенном списке указываются значения аргументов передаваемой функции, далее возвращаемое значение передаваемой функции.
```python
from typing import Callable

def hint_for_arg_func(
	func: Callable[[int], bool],
	mass: list[int]
) -> list[int] | None:
	if mass:
		return mass[::].append(1)
	func(mass)
```
***
## Type Hint для классов
```python
from typing import TypeVar, Type

class FurFur:
	pass

T = TypeVar('T') # Type Hint для классов без ограничений
T = TypeVar('T', bound=FurFur) # Type Hint для одного класса и его наследников

def constract_object(class_obj: Type[T]) -> T:
	return class_obj()
```
***
## Type Hint with NamedTuple
```python
from typing import NamedTuple

class Coordinates(NamedTuple):
	latitude: float
	longitude: float

def get_gps_coord() -> Coordinates:
	result = Coordinates(
		latitude=10.0
		longitude=20.0
	)
	return result
```
***
## Type Hint for Dicts with Literal
```python
from typing import Literal

def get_gps_coord() -> dict[Literal['latitude'] | ['longitude'], float]:
	res = {
		'latitude': 10.0,
		'longitude': 20.0
	}
	return res
```
***
## Type Hint with Type Dict
```python
from typing import TypeDict

class Coordinates(TypeDict):
	longitude: float
	latitude: float

def get_gps_coord() -> Coordinates:
	res = Coordinates(
		**{
			'latitude': 10.1,
			'longitude': 20.1
		}
	)
	return res
```
***
## Type Hint with @dataclass
### Описание:
Создает эмуляцию обращения по атрибутам как в экземплярах класса, в отличие от именованных кортежей `NamedTuple`, являются изменяемым типом данных.
```python
from dataclasses import dataclass

@dataclass
class Coordinates:
	longitude: float
	latitude: float

def get_gps_coord() -> Coordinates:
	res = Coordinates(
		**{
			'latitude': 10.1
			'longitude': 20.1
		}
	)
	# or
	# res = Coordinates(latitude=10.1, longitude=20.1)
	return res
```
***
## Type Hint for Enum
### Описание:
Используется для перечисления данных
```python
from enum import Enum
from typing import NamedTuple
from datetime import datetime


class WeatherType(Enum):
	THUNDERSTORM = 'Гроза'
	RAIN = 'Дождь'
	SNOW = 'Снег'
	CLEAR = 'Ясно'

class Weather(NamedTuple):
	temperature: int
	weather_type: WeatherType
	city: str
	sunrice: datetime
```
***