# Simple clouser for counter ==================================================
def counter():
    count = 0
    def inner():
        nonlocal count
        count +=1
        return count
    return inner

# count = counter()

# if __name__ == '__main__':
#     for i in range(10):
#         print(count())

# Clouser with arguments ======================================================
# Также можно использовать для создания функций с предустановленными праметрами

def word_creator(word):
    def inner(name):
        return f'{word}: ...{name}'
    return inner

# if __name__ == '__main__':
#     generate = word_creator('Я очень сильно люблю котиков')
#     print(generate('Мое имя Анаями Рей'))

# __closure__ =================================================================

def inner_clouser(arg):
    name = 'Holo'
    num = 5
    def inner():
        print(arg)
        print(name)
    return inner

# if __name__ == '__main__':
#     f = inner_clouser(10)
#     for value in f.__closure__:
#         # Возвращает только те значения которые были захвачены в inner
#         print(value.cell_contents)

# closure for ivent ===========================================================
def create_button(lable):
    def on_click():
        print(f'Кнопка "{lable}" нажата')
    return on_click

# if __name__ == '__main__':
#     button1 = create_button('Сохранить')
#     button2 = create_button('Отмена')
#     button1()
#     button2()