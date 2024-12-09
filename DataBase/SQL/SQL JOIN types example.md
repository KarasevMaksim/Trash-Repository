# SQL JOIN Операции

В данном документе описаны различные типы JOIN операций в SQL, которые используются для
объединения данных из двух таблиц.

## INNER JOIN

`INNER JOIN` используется по умолчанию и возвращает записи, для которых есть совпадения
в обеих таблицах.

### Запрос

```sql
SELECT * FROM TableA
INNER JOIN TableB
ON TableA.costume = TableB.costume;
```
### Описание
Запрос возвращает записи, в которых для значения TableA.costume найдено такое же в TableB.costume.

`Ответ`
|id |costume|id |costume|
|:-:|:-----:|:-:|:-----:|
|1	|Пират	|2  |Пират  |
|3	|Котик	|4  |Котик  |


## FULL OUTER JOIN
`FULL OUTER JOIN` возвращает все записи из обеих таблиц, включая те, для которых нет совпадений.

### Запрос

```sql
SELECT * FROM TableA
FULL OUTER JOIN TableB
ON TableA.costume = TableB.costume;
```

`Ответ`
| id    | costume    | id    | costume    |
|:-----:|:----------:|:-----:|:----------:|
|  1    |   Пират   |  2    |   Пират   |
|  2    | Снежинка  | null  |   null     |
| null  |   null     |  1    |   Жучка   |
|  3    |   Котик   |  4    |   Котик   |
| null  |   null     |  3    | Принцесса  |
|  4    | Буратино  | null  |   null     |


## LEFT JOIN
`LEFT JOIN` возвращает все записи из левой таблицы (TableA) и совпадающие записи из
правой таблицы (TableB). Если совпадений нет, то в полях правой таблицы будут значения NULL.

### Запрос

```sql
SELECT * FROM TableA
LEFT JOIN TableB
ON TableA.costume = TableB.costume;
```

`Ответ`
| id    | costume    | id    | costume    |
|:-----:|:----------:|:-----:|:----------:|
|  1    |   Пират   |  2    |   Пират   |
|  2    | Снежинка  | null  |   null     |
|  3    |   Котик   |  4    |   Котик   |
|  4    | Буратино  | null  |   null     |



## RIGHT JOIN
`RIGHT JOIN` возвращает все записи из правой таблицы (TableB) и совпадающие записи из
левой таблицы (TableA). Если совпадений нет, то в полях левой таблицы будут значения NULL.

### Запрос

```sql
SELECT * FROM TableA
RIGHT JOIN TableB
ON TableA.costume = TableB.costume;
```

`Ответ`
| id    | costume    | id    | costume    |
|:-----:|:----------:|:-----:|:----------:|
| null  |   null     |  1    |   Жучка    |
|  1    |   Пират   |  2    |   Пират    |
| null  |   null     |  3    | Принцесса  |
|  3    |   Котик   |  4    |   Котик    |
