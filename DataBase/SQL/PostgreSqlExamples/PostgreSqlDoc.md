# Типы данных в PostgreSql
1. **Числовые типы**
- `smallint:` 2-байтовое целое число. `2^16` от `-32 768` до `32 768`
- `integer:` 4-байтовое целое число. `2^32` от `-2.14 млрд` до `2.14 млрд`
- `bigint:` 8-байтовое целое число. `2^64`
- `decimal(p, s):` Число с фиксированной точкой, где `p` — общее количество цифр, а
`s` — количество цифр после десятичной точки.
- `numeric(p, s):` То же, что и `decimal`, но более гибкий.
- `real:` 4-байтовое число с плавающей точкой.
- `double precision:` 8-байтовое число с плавающей точкой.
- `smallserial:` Автоматически увеличиваемое целое число (2 байта).
- `serial:` Автоматически увеличиваемое целое число (4 байта).
- `bigserial:` Автоматически увеличиваемое большое целое число (8 байт).

2. **Символьные типы**
- `char(n):` Строка фиксированной длины, `n` — количество символов.
- `varchar(n):` Строка переменной длины, максимальная длина `n`.
- `text:` Строка переменной длины без ограничения.

3. **Дата и время**
- `date:` Дата (год, месяц, день).
- `time:` Время (часы, минуты, секунды).
- `timestamp:` Дата и время (без часового пояса).
- `timestamptz:` Дата и время с часовым поясом.
- `interval:` Интервал времени.

4. **Логические типы**
- `boolean:` Логический тип, может принимать значения `true`, `false` или `null`.

5. **Геометрические типы**
- `point:` Точка в 2D пространстве.
- `line:` Линия.
- `lseg:` Отрезок линии.
- `box:` Прямоугольник.
- `path:` Путь (открытый или закрытый).
- `polygon:` Многоугольник.
- `circle:` Круг.

6. **Сетевые адреса**
- `cidr:` IPv4 или IPv6 адрес.
- `inet:` IPv4 или IPv6 адрес с возможностью указания маски.
- `macaddr:` MAC-адрес.

7. **UUID**
- `uuid:` Универсально уникальный идентификатор.

8. **JSON и XML**
- `json:` Данные в формате JSON.
- `jsonb:` Данные в бинарном формате JSON (более эффективный для обработки).
- `xml:` Данные в формате XML.

9. **Массивы**
- `PostgreSQL` поддерживает массивы для большинства типов данных, например:
- `integer[]`
- `text[]`

10. **Пользовательские типы**
Также можно создавать свои собственные типы данных, используя команду
`CREATE TYPE`


# Создание таблиц в PostgreSql
```sql
CREATE TABLE IF NOT EXISTS publisher (
	publisher_id serial,
	org_name varchar(128) NOT NULL,
	address text,
	CONSTRAINT pk_publisher PRIMARY KEY (publisher_id)
);
```
# Создание связи один к одному
```sql
CREATE TABLE IF NOT EXISTS persons (
    person_id SERIAL,
    first_name VARCHAR(64),
    last_name VARCHAR(64),
    CONSTRAINT pk_person PRIMARY KEY (person_id)
);
CREATE TABLE IF NOT EXISTS passport (
    passport_id SERIAL,
    serial_number INTEGER NOT NULL UNIQUE,
    person_id INTAGER NOT NULL,
    CONSTRAINT pk_passport PRIMARY KEY (passport_id),
    CONSTRAINT fk_person FOREIGN KEY (person_id) REFERENCES persons(person_id)
    ON DELETE CASCADE UNIQUE
);
```
# Создание связи один ко многим
```sql
CREATE TABLE IF NOT EXISTS publisher (
    publisher_id SERIAL,
    org_name varchar(128) NOT NULL,
    address TEXT,
    CONSTRAINT pk_publisher PRIMARY KEY (publisher_id)
);
CREATE TABLE IF NOT EXISTS book (
    book_id SERIAL,
    title TEXT NOT NULL,
    isbn VARCHAR(32) NOT NULL,
    publisher_id INTEGER,
    CONSTRAINT pk_book PRIMARY KEY (book_id),
    CONSTRAINT fk_publisher FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
    ON DELETE CASCADE
);
```
# Создание связи Многие ко многим
```sql
CREATE TABLE IF NOT EXISTS publisher (
    publisher_id SERIAL,
    org_name varchar(128) NOT NULL,
    address TEXT,
    CONSTRAINT pk_publisher PRIMARY KEY (publisher_id)
);

CREATE TABLE IF NOT EXISTS book (
    book_id SERIAL,
    title TEXT NOT NULL,
    isbn VARCHAR(32) NOT NULL,
    CONSTRAINT pk_book PRIMARY KEY (book_id)
);

CREATE TABLE IF NOT EXISTS publisher_book (
    publisher_id INTEGER,
    book_id INTEGER,
    CONSTRAINT fk_publisher FOREIGN KEY (publisher_id) REFERENCES publisher(publisher_id)
    ON DELETE CASCADE,
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES book(book_id)
    ON DELETE CASCADE,
    CONSTRAINT pk_publisher_book PRIMARY KEY (publisher_id, book_id)
)
```