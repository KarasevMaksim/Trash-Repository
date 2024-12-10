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
#### Откат изменений
Откатить изменения к последнему коммиту. (если они небыли добавлены в `stage`)<br>
`git checkout <file.name> or <.>`<br>
Откатить изменения к последнему коммиту. (даже если они были добавлены в `stage`)<br>
`git checkout <file.name> or <.>`

#### Убираем файлы из `stage`
Убрать файл из `stage`.<br>
`git reset <file.name>`<br>
Убрать файл из `stage`, Для последующего его удаления. (После следующего
коммита файл будет удален).<br>
`git rm -r <file.name>

#### Удаление коммитов
Жесткий откат на один коммит вниз. С удаленим текущего коммита и удаленим изменений.<br>
`git reset --hard HEAD^1`<br>
Мягкий откат на один коммит вниз. С удалением текущего коммита, изменения остаются в `stage`.<br>
`git reset --soft HEAD^1`
