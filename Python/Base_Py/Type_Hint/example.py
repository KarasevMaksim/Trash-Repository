from typing import Final, Callable, Type, TypeVar


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
