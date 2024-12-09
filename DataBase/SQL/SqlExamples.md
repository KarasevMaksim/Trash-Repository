# Порядок выполнения в запросе
1. **FROM** выбирается таблица для получения записей
2. **WHERE** из этой таблицы отбираются записи, подходящие под условие
3. **GROUP BY** эти записи агригируются в группы
4. **HAVING** из агригированных записей, выбираются подходящие под условие
5. **SELECT** формируются результирующие данные как они указаны в селекте
6. **ORDER BY** сортируется результатирующая выборка

# ЗАПРОСЫ К БД
## Получить все данные из таблицы
```sql
SELECT * FROM anime_titles;
```
## Получить только уникальные данные из таблицы
```sql
SELECT DISTINCT id, name FROM anime_titles;
```
## Получить все данные соответствующие условию
```sql
SELECT * FROM anime_titles WHERE id=2;
```
## Получить новую колонку с расчетом значения
```sql
SELECT
    title,
    amount,
    amount * 1.65 AS pack
FROM 
    book;
```
## Условия при расчете значений `IF(условие, true, false)`
```sql
SELECT
    author,
    title,
    IF(author = 'Булгаков М.А.',
        price + (price * 0.10),
        IF(author = 'Есенин С.А.',
            price + (price * 0.05),
            price)
    ) AS new_price
FROM
    book;
```
## Запрос с отношением по ключам к нескольким таблицам
```sql
SELECT
    anime_titles.name AS title_name,
    genre,
    persons.name AS person_name,
    special
FROM
    anime_titles,
    persons
WHERE
    anime_titles.id = persons.anime_title_id;
```
## Запрос к нескольким таблицам через `JOIN`
```sql
SELECT
    anime_titles.name AS anime,
    anime_titles.raiting,
    persons.name,
    persons.special
FROM
    anime_titles
JOIN persons
    ON anime_titles.id = persons.anime_title_id
WHERE
    persons.special = 'Tail Fluf';
```
## Найти все Аниме, у которых нет записей о персонажах
```sql
SELECT anime_titles.id, anime_titles.name, anime_titles.genre
FROM anime_titles
LEFT JOIN persons
    ON anime_titles.id = persons.anime_title_id
WHERE persons.name IS NULL;
```
# ЗАПРОСЫ К БД С СОРТИРОВКОЙ
## Сортировка по колонке в порядке возрастания `ASC` и убывания `DESC`
```sql
SELECT * FROM anime_titles ORDER BY id ASC;
SELECT * FROM anime_titles ORDER BY id DESC;
```
## Сортировка по нескольким колонкам
```sql
SELECT * FROM anime_titles ORDER BY id DESC, name ASC;
```
## Сортировка с Лимитом по записям
```sql
SELECT * FROM anime_titles ORDER BY id DESC LIMIT 2;
SELECT * FROM anime_titles ORDER BY id DESC LIMIT 2 OFFSET 1;
```
## Сортировка и вычисляемым значением
```sql
SELECT id * 2 AS double_id, name FROM anime_titles ORDER BY double_id DESC;
```
# ЗАПРОСЫ К БД С ГРУППИРОВКОЙ
## Вывести количество тайтлов с группированных по рейтингу и если этих тайтлов больше одного
```sql
SELECT
    raiting, COUNT(name) as cnt_title
FROM
    anime_titles
GROUP BY
    raiting
HAVING
    COUNT(name) > 1
ORDER BY
    cnt_title DESC;
```
# ДОБАВЛЕНИЕ ЗАПИСЕЙ В БД
## Добавить запись в таблицу
```sql
INSERT INTO anime_titles (name, genre, raiting)
VALUES ('Маг цилитель', 'Hentai', '18+');
```
# ОБНОВЛЕНИЕ ДАННЫХ В БД
## Обновить данные по `id`
Если не указать условие на конкретную запись, то обновятся все записи в колонке
```sql
UPDATE anime_titles SET raiting = '18+' WHERE id=2;
```
# УДАЛЕНИЕ ЗАПИСЕЙ В БД
## Удалить запись по `id`
Если не указать условие на конкретную запись, то удалятся все записи из таблицы
```sql
DELETE FROM anime_titles WHERE id=3;
```
# Условия WHERE с ветвлением `AND`, `OR`, `NOT`, `IN`
## Получить данные по нескольким условиям
```sql
SELECT id, name FROM anime_titles WHERE raiting='18+' OR raiting='16+';
SELECT id, name, raiting FROM anime_titles WHERE raiting IN ('18+', '16+');
```
## Более сложное условие со скобками
```sql
SELECT * FROM anime_titles WHERE (id >= 2 OR id < 5)
AND raiting IN ('18+', '16+');
```
# ОПЕРАТОРЫ ДЛЯ СОСТАВЛЕНИЯ ЗАПРОСОВ
- `=` это оператор сравнения, а не присваивания.
- `<>` не равно (в некоторых БД `!=`).
- `BETWEEN` — «между», для проверки значения в диапазоне. Например: `birth_year BETWEEN 1850 AND 1900`.
- `LIKE`, `ILIKE` — поиск строки по шаблону и поиск строки по шаблону без учёта регистра. Пример: `city LIKE 'Днепр%'`, символ `%` заменяет любой набор символов: такой маске будут соответствовать значения поля ДнепроГЭС, Днепр или Днепровский.
- `IN` — вхождение в список. Пример использования `city IN ('Москва', 'Днепр')`.

# Агрегирующие функции: функции `COUNT`, `MIN`, `MAX`.
## Посчитать количество записей в таблице
```sql
SELECT COUNT(*) AS cnt FROM persons;
```
## Найти самый новый и самый старый аниме тайтел
```sql
SELECT MAX(id) AS new_row, name FROM persons;
SELECT MIN(id) AS old_row, name FROM persons;
```
# Разные агрегирующие функции
- `AVG(column)` возвращает среднее значение по столбцу column
- `SUM(column)` возвращает сумму по столбцу column
- `CAST(column AS INTEGER)` преобразует колонку к новому типу данных в запросе
# Функции для работы с ДАТАМИ
## Функция `EXTRACT` извлекает из даты нужную ее часть
- `century` — век;
- `day` — день;
- `doy` (от англ. day of the year) — день года: от 1 до 365/366;
- `isodow` (от англ. day of the week и ISO 8601, международного стандарта даты и времени) — день недели: понедельник — 1, воскресенье — 7.
- `hour` — час;
- `milliseconds` — миллисекунда;
- `minute` — минута;
- `second` — секунда;
- `month` — месяц;
- `quarter` — квартал;
- `week` — неделя в году;
- `year` — год.
### Шаблон
```sql
SELECT 
    id_user,
    EXTRACT(MONTH FROM log_on) AS month_activity,
    EXTRACT(DAY FROM log_on) AS day_activity
FROM 
    user_activity;
```
## Функция `DATE_TRUNC` усекает дату до часа, дня или месяца
- `microseconds` — микросекунды;
- `milliseconds` — миллисекунды;
- `second` — секунда;
- `minute` — минута;
- `hour` — час;
- `day` — день;
- `week` — неделя;
- `month` — месяц;
- `quarter` — квартал;
- `year` — год;
- `decade` — декада года;
- `century` — век.
### Шаблон из `2019-03-01 23:34:55` получаем `2019-03-01 23:00:00`
```sql
SELECT 
    DATE_TRUNC('hour', log_on) as date_log_on
FROM 
   user_activity;
```
# ПОДЗАПРОСЫ
В `SQL` нельзя использовать вложенные агригирующие функции.
`SELECT AVG(COUNT(raiting))` для этого нужно использовать подзапросы.

### Шаблон
```sql
SELECT 
    AVG(Sub.count_rating) AS avg_count_rating
FROM
    (SELECT 
       COUNT(rating) AS count_rating
    FROM 
        books
    GROUP BY genre) AS Sub;
```