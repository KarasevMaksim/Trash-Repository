import sqlite3


base_data = {
    'anime_title1': {
        'name': 'Konosuba',
        'genre': 'isekai',
        'raiting': '16+',
        'persons': {
            'person1': {
                'name': 'Megumin',
                'special': 'Explousen',
                'anime_title_id': 1
            },
            'person2': {
                'name': 'Aqua',
                'special': 'Wother',
                'anime_title_id': 1
            }
        }
    },
    'anime_title2': {
        'name': 'SenkoSun',
        'genre': 'life',
        'raiting': '12+',
        'persons': {
            'person1': {
                'name': 'Senko',
                'special': 'Tail Fluf',
                'anime_title_id': 2
            }
        }
    }
}

def init_db():
    # подключаемся к бд, если нет бд она будет создана
    with sqlite3.connect('example.db') as conn:
        # создаем курсор для работы с бд    
        cursor = conn.cursor()
        # Включение внешних ключей для проверки целостности бд
        cursor.execute('PRAGMA foreign_keys = ON;')

        # создаем таблицы в бд
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS anime_titles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                genre TEXT NOT NULL,
                raiting TEXT NOT NULL
            );
            '''
        )
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS persons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                special TEXT NOT NULL,
                anime_title_id INTEGER,
                FOREIGN KEY (anime_title_id) REFERENCES anime_titles (id)
            );
            '''
        )

        # Заполняем таблицу начальными данными
        for item in base_data:
            anime_title = base_data[item]
        
            name = anime_title['name']
            genre = anime_title['genre']
            raiting = anime_title['raiting']
            cursor.execute(
                '''
                INSERT INTO anime_titles (name, genre, raiting)
                VALUES (?, ?, ?);
                ''', (name, genre, raiting)
            )

        for item in base_data:
            anime_title = base_data[item]  
            anime_person = anime_title['persons']
            for person in anime_person:
                person_item = anime_person[person]
                name = person_item['name']
                special = person_item['special']
                anime_title_id = person_item['anime_title_id']
                cursor.execute(
                    '''
                    INSERT INTO persons (name, special, anime_title_id)
                    VALUES (?, ?, ?);
                    ''', (name, special, anime_title_id)
                )

        # Сохраняем изменения
        conn.commit()
    

if __name__ == '__main__':
    init_db()
