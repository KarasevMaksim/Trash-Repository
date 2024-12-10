# Работа с `Git`
## Быстрый старт
```bash
git init # инициализируем новый репазиторий
# or
git clone <link to repositories> # клонируем удаленный репозиторий

# Создаем локального git user. Ключ --global добавит в конфиг юзера
git config --global user.name "Name"
git congig --global user.email "example@gmail.com"

git branch -M main # Переименовываем ветку master в main

# Связываем локальный репазиторий с удаленным
git remote add origin https://github.com/username/my-project.git

# Создаем файл README.md коммитми и пушим в удаленный репозиторий
git add README.md
git commit -m "init commit"
git push -u origin main
```

## Доступ к удаленномоу репозиторию по `SSH` ключу.
1. Создаем ssh-key на локальном компьютере. Команда: `ssh-keygen`.
2. Копируем публичный ключ и сохраняем в настройках `GitHub`.
3. Теперь для клонирования репозитория и т.п. используем ssh ссылки.

## Отмена изменений в коде и отмена коммитов
Откатить изменения к последнему коммиту. (если они небыли добавлены в `stage`)
`git checkout <file.name> or <.>`
Убрать файл из `stage`.
`git reset <file.name>`
Убрать файл из `stage`, Для последующего его удаления. (После следующего
коммита файл будет удален). 
