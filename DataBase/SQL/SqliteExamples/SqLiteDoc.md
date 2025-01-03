# Важные особенности SQLite.
### Плюсы
1. `Транзакционная ACID`: Поддерживает транзакции, что гарантирует целостность
данных при одновременном доступе.
2. `JSON`: SqLite 3.30.0+ поддерживает работу с `json`, что позволяет хранить из
извлекать данные в формате `json` через встроенные функции.
3. `Расширения`: Поддерживает установку расширений для добовления расширенных
возможностей.
4. `Встроенные функции`: SqLite имеет набор встроенных функций для работы С
текстом, датами, и т.д.
5. `Файловая`: Нам не нужен отдельный сервер для самой БД. Поэтому ее можно
встроить в само приложение.
6. `Безопасность`: SqLite поддерживает шифрование базы данных.
7. `Поддержка триггеров`: SQLite позволяет создавать триггеры, которые
автоматически выполняются при выполнении определенных операций (например,
вставка, обновление или удаление).
8. `Поддержка виртуальных таблиц`: SQLite поддерживает виртуальные таблицы,
которые позволяют создавать таблицы, данные в которых извлекаются из других
источников.
9. `Поддержка временных таблиц`: SQLite поддерживает временные таблицы, которые
автоматически удаляются после завершения сессии.
10. `Поддержка полнотекстового поиска`: SQLite предлагает возможности
полнотекстового поиска через специальный модуль, что позволяет эффективно
искать текстовые данные.
11. `Инструменты для миграции`: SQLite предоставляет инструменты для экспорта и
импорта данных, что упрощает миграцию данных между различными форматами и
системами.

### Минусы
1. `Небольшие таблицы`: SqLite хорошо работает с небольшими таблицами. Однако,
при работе с очень большими объемами данных, может возникнуть проблема с
производительностью.
2. `Многопоточность`: Позволяет выполнять чтение данных в несколько потоков,
но запись всегда только одним потоком.
3. `Ограничения`: SqLite не подходит для высоконогруженных систем, где требуется
высокая пропускная способность и масштабируемость. SqLite не имеет встроенных
механизмов репликации или кластеризации. У SqLite нет концепции пользователей
и ролей, что может быть недостатком в сложных системах.
***

# Типы данных в Sqlite
## INTEGER
Хранит целые числа от `-2^63` до `2^63-1`.
SQLite автоматически выбирает размер, необходимый для хранения значения.
## REAL
Числовой тип с плавающей запятой. Это обычно 8-байтовое значение,
соответствующее стандарту `IEEE 754`.
## TEXT
Строковый тип данных. Текст может быть представлен в кодировке
`UTF-8`, `UTF-16BE` или `UTF-16LE`.
## BLOB
Тип данных для хранения `бинарных данных`.
BLOB может хранить данные любого размера.
## NULL
Специальный тип данных, представляющий отсутствие значения.
## BOOLEAN
Для хранения логических значений используются целые числа `0-1`
***

# Cоздание таблиц со связью
## Создание таблиц со связью Один ко Многим
```sql
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS anime_titles (
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   genre TEXT NOT NULL,
   raiting TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS persons (
   id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   special TEXT NOT NULL,
   anime_title_id INTEGER,
   FOREIGN KEY (anime_title_id) REFERENCES anime_titles(id)
);
```
***
## Создание таблиц со связью Один к Одному
### Вариант 1
```sql
PRAGMA foreign_keys = ON;

-- Таблица "Users"
CREATE TABLE Users (
  id INTEGER PRIMARY KEY,
  name TEXT
);

-- Таблица "Profiles"
CREATE TABLE Profiles (
  id INTEGER PRIMARY KEY,
  user_id INTEGER UNIQUE,  -- Более классический подход
  bio TEXT,
  FOREIGN KEY (user_id) REFERENCES Users(id)
);
```
### Вариант2
```sql
PRAGMA foreign_keys = ON;

-- Таблица "Users"
CREATE TABLE Users (
  id INTEGER PRIMARY KEY,
  name TEXT
);

-- Таблица "Profiles"
CREATE TABLE Profiles (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  bio TEXT,
  CHECK (user_id IN (SELECT id FROM Users)) -- более гибкий подход для
-- использования других типов данных
);
```
***
## Создание таблиц со связью Многие ко Многим
```sql
PRAGMA foreign_keys = ON;

CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE courses (
  id INTEGER PRIMARY KEY,
  name TEXT
);

CREATE TABLE students_to_courses (
  id INTEGER PRIMARY KEY,
  student_id INTEGER,
  course_id INTEGER,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id),
  UNIQUE (student_id, course_id) --Добавлен UNIQUE для комбинированного индекса
);

CREATE INDEX idx_student_id ON students_to_courses (student_id);
-- Индекс для student_id
CREATE INDEX idx_course_id ON students_to_courses (course_id);
-- Индекс для course_id
```
***
# Удаление таблиц
## Удаление таблицы у которой нет зависимостей
```sql
DROP TABLE <table_name>;
```
***
## Проверка на существование таблицы, перед ее удалением
```sql
DROP TABLE IF EXISTS <table_name>;
```
***
## Удаление таблицы с зависимостями в виде внешних ключей
### Вариант1:
Перед удалением таблицы, можно отключить проверку зависимых ключей.
```sql
PRAGMA foreign_keys = OFF;
DROP TABLE <table_name>;
```
### Вариант2:
Таблица `orders` ссылается на таблицу `users`. Чтобы удалить таблицу `users`, надо
сначала удалить таблицу `orders`, которая на нее ссылается.
```sql
DROP TABLE orders;
DROP TABLE users;
```
### Вариант3:
При проектировании таблицы, можно задать автоматическое удаление записей, в
зависимой таблице, при удаление записи в основной таблице или удалении этой
таблицы. При помощи конструкции `ON DELETE CASCADE`.
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);
DROP TABLE users;
```
***
# Добавление новых полей в таблицу
Нельзя добавить несколько полей за один запрос, только по одному запросу.
```sql
ALTER TABLE <table_name> ADD COLUMN <column_name> INTAGER;
```
***
# Управление Sqlite через терминал
1. Установить Sqlite:
**Windows** - Скачать распаковать и добавить путь к папке в `PATH`
**Linux** - `sudo apt-get install sqlite3`
2. **Запуск в терминале**: `sqlite3 путь/к/базе_данных.db` (Если путь к базе данных
не существует, то `SqLite` создаст новый файл с базой данных)
3. **Специальные команды для управления и просмотра**:
- `.tables` - просмотр всех таблиц
- `.schema` имя_таблицы - просмотр структуры определенной таблицы
- `.schema` - покажет структуры всех таблиц
- `.quit` - выход из режима работы с базами данных
- `.exit`
- `.close` - закрывает текущую базу данных.
- `.open data.db` - открывате новый файл с базой даннх для работы
- `.headers on|off` - Включает или отключает вывод заголовков столбцов при
выполнении запросов.
- `.mode csv|column|...` - Устанавливает режим вывода данных. Некоторые режимы:
- `csv` - вывод в формате CSV
- `column` - вывод в формате таблицы
- `line` - вывод по строкам
- `list` - вывод в формате списка
- `.width 10 20 5` - устанавливает ширину для каждого столбца.
- `.save backup.db` - сохраняет текущее состояние базы данных в новый файл
- `.load my_extension` - загружает расширение для SqLite
- `.databases` - показывает список всех открытых баз данных
- `.indices name_table` - показывает все индексы, созданные для данной таблицы
- `.fullschema` - показывает полную схему базы данных, включая триггеры и индексы
- `.system` - выполняет команду операционной системы
***
# Разные фичи
## `Триггеры`: Автоматически выполняются при определенных действиях.
```sql
CREATE TRIGGER user_age_update 
AFTER UPDATE ON users 
FOR EACH ROW 
BEGIN 
    UPDATE logs SET updated_at = CURRENT_TIMESTAMP WHERE user_id = NEW.id; 
END;
```
***
## `Представления`: Виртуальные таблицы, которые могут упрощать сложные запросы.
```sql
CREATE VIEW active_users AS 
SELECT * FROM users WHERE active = 1;  -- Представление активных пользователей
```
***
## Экспорт и импорт данных
Используйте `.import` и `.export` в командной строке `SQLite` для работы с `CSV`.
```sql
-- Экспорт в CSV`
.mode csv
.headers on
.output users.csv
SELECT * FROM users;
.output stdout
-- Импорт из CSV
.mode csv
.import путь_к_файлу.csv имя_таблицы
```
***
## Миграция данных
SQL-скрипты для миграции данных между различными системами.
### `Python`: Используйте библиотеку sqlite3
```python
import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM users')
```
***
## Работа с бд через транзакции
**Сохранение изменений:** `SQLite` автоматически сохраняет изменения после каждой
команды. Если вы хотите использовать транзакции, вы можете использовать:
```sql
BEGIN;
-- ваши команды
COMMIT;
```
***
