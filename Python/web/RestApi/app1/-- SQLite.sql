-- Типы данных в Sqlite =======================================================
-- INTEGER
-- Хранит целые числа от -2^63 до 2^63-1.
-- SQLite автоматически выбирает размер, необходимый для хранения значения.
-- REAL
-- Числовой тип с плавающей запятой. Это обычно 8-байтовое значение,
-- соответствующее стандарту IEEE 754.
-- TEXT
-- Строковый тип данных. Текст может быть представлен в кодировке
-- UTF-8, UTF-16BE или UTF-16LE.
-- BLOB
-- Тип данных для хранения бинарных данных.
-- BLOB может хранить данные любого размера.
-- NULL
-- Специальный тип данных, представляющий отсутствие значения.
-- BOOLEAN
-- Для хранения логических значений используются целые числа 0-1


-- Cоздание таблиц со связью один ко многим ==================================
-- CREATE TABLE IF NOT EXISTS anime_titles (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    name TEXT NOT NULL,
--    genre TEXT NOT NULL,
--    raiting TEXT NOT NULL
-- );
-- CREATE TABLE IF NOT EXISTS persons (
--    id INTEGER PRIMARY KEY AUTOINCREMENT,
--    name TEXT NOT NULL,
--    special TEXT NOT NULL,
--    anime_title_id INTEGER,
--    FOREIGN KEY (anime_title_id) REFERENCES anime_titles(id)
-- );


-- ЗАПРОСЫ К БД ===============================================================
-- Получить все данные из таблицы ---------------------------------------------
-- SELECT * FROM anime_titles;

-- Получить только уникальные данные из таблицы -------------------------------
-- SELECT DISTINCT id, name FROM anime_titles;

-- Получить все данные соответствующие условию --------------------------------
-- SELECT * FROM anime_titles WHERE id=2;

-- Запрос с отношением по ключам к нескольким таблицам ------------------------
-- SELECT
--     anime_titles.name AS title_name,
--     genre,
--     persons.name AS person_name,
--     special
-- FROM
--     anime_titles,
--     persons
-- WHERE
--     anime_titles.id = persons.anime_title_id;

-- Запрос к нескольким таблицам черз JOIN -------------------------------------
-- SELECT
--     anime_titles.name AS anime,
--     anime_titles.raiting,
--     persons.name,
--     persons.special
-- FROM
--     anime_titles
-- JOIN persons
--     ON anime_titles.id = persons.anime_title_id
-- WHERE
--     persons.special = 'Tail Fluf';

-- Найти все Аниме, у которых нет записей о персонажах ------------------------
-- SELECT anime_titles.id, anime_titles.name, anime_titles.genre
-- FROM anime_titles
-- LEFT JOIN persons
-- ON anime_titles.id = persons.anime_title_id
-- WHERE persons.name IS NULL;


-- ДОБОВЛЕНИЕ ЗАПИСЕЙ В БД ====================================================
-- Добавить запись в таблицу --------------------------------------------------
-- INSERT INTO anime_titles (name, genre, raiting)
-- VALUES ('Маг цилитель', 'Hentai', '18+');


-- ОБНОВЛЕНИЕ ДАННЫХ В БД =====================================================
-- Обновить данные по id. Если не указать условиe на конкретную запись, то
-- обновятся все записи в колонке ---------------------------------------------
-- UPDATE anime_titles SET raiting = '18+' WHERE id=2;


-- УДАЛЕНИЕ ЗАПИСЕЙ В БД ======================================================
-- Удалить запись по id. Если не указать условие на конеретную запись, то
-- удаляться все записи из таблицы --------------------------------------------
-- DELETE FROM anime_titles WHERE id=3;


-- Условия WHERE с ветвлением AND, OR, NOT, IN ================================
-- Получить данные по нескольким условиям--------------------------------------
-- SELECT id, name FROM anime_titles WHERE raiting='18+' OR raiting='16+';
-- SELECT id, name, raiting FROM anime_titles WHERE raiting IN ('18+', '16+');

-- Более сложное условие со скобками ------------------------------------------
-- SELECT * FROM anime_titles WHERE (id >= 2 OR id < 5)
-- AND raiting IN ('18+', '16+');


-- ОПЕРАТОРЫ ДЛЯ СОСТАВЛЕНИЯ ЗАПРОСОВ =========================================
-- = это оператор сравнения, а не присваивания.

-- <> не равноо (в некоторых бд !=)

-- BETWEEN — «между», для проверки значения в диапазоне
-- Например: birth_year BETWEEN 1850 AND 1900

-- LIKE, ILIKE — поиск строки по шаблону и поиск строки по шаблону без учёта
-- регистра.
-- Пример: city LIKE 'Днепр%', символ % заменяет любой набор символов: такой
-- маске будут соответствовать значения поля ДнепроГЭС, Днепр или Днепровский

-- IN — вхождение в список. Пример использования city IN ('Москва', 'Днепр')


-- Агрегирующие функции. Функция COUNT, MIN, MAX===============================
-- Посчитать количество записей в таблице
-- SELECT COUNT(*) AS cnt FROM persons;

-- Найти самый новый и самый старый аниме тайтел
-- SELECT MAX(id) AS new_row, name FROM persons;
-- SELECT MIN(id) AS old_row, name FROM persons;


-- Разные агрегирующие функции ================================================
-- AVG (column) возвращает среднее значение по столбцу column
-- SUM(column) возвращает сумму по столбцу column