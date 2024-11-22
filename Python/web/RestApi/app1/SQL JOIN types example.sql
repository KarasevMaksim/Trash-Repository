-- inner, left, right, full outer используятся для того, чтобы задать какая
-- таблица будет главной, а какая будет добавляться.


-- INNER JOIN используется по умолчанию =======================================
-- SELECT * FROM TableA
-- дополнительно запросить данные из таблицы TableB
-- INNER JOIN TableB
    -- и возвращать записи, в которых 
    -- для значения TableA.costume найдено такое же в TableB.costume
--     ON TableA.costume = TableB.costume;

-- Ответ:

-- id costume    id  costume
   -- --------   --  ---------
-- 1  Пират      2   Пират
-- 3  Котик      4   Котик


-- FULL OUTER JOIN ============================================================
-- SELECT * FROM TableA
-- FULL OUTER JOIN 
--     TableB
-- ON 
--     TableA.costume = TableB.costume;

-- Ответ:

-- id    costume    id    costume
   ----  --------   ----  ---------
-- 1     Пират      2     Пират
-- 2     Снежинка   null  null
-- null  null       1     Жучка
-- 3     Котик      4     Котик
-- null  null       3     Принцесса
-- 4     Буратино   null  null


-- LEFT JOIN ==================================================================
-- SELECT * FROM TableA
-- LEFT JOIN 
--     TableB
-- ON 
--     TableA.costume = TableB.costume;

-- Ответ:

-- id costume    id    costume
   -- --------   ----  ---------
-- 1  Пират      2     Пират
-- 2  Снежинка   null  null
-- 3  Котик      4     Котик
-- 4  Буратино   null  null


-- RIGHT JOIN =================================================================
-- SELECT * FROM TableA
-- RIGHT JOIN 
--     TableB
-- ON 
--     TableA.costume = TableB.costume;

-- Ответ:

-- id   costume    id    costume
   ---- --------   ----  ---------
-- null  null       1    Жучка
-- 1     Пират      2    Пират
-- null  null       3    Принцесса
-- 3     Котик      4    Котик
