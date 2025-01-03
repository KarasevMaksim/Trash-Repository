#linux #кастом #кастомный_линукс
# Конфиги
- [[Config Bspwm]]
- [[Config Polybar]]
- [[Config Sxhkd]]
***
# Bspwm
## Установка пакетов
```bash
sudo apt install xorg xorg-server xorg-xinit
sudo apt install bspwm sxhkd
sudo apt-get install pulseaudio-utils
```
## Утилиты
### Утилиты для звука:
pulseaudio
pulseaudio-utils
pactl - управление звуком в pulsaudio
`pactl list` - смотрим id устройства
`pactl set-sink-volume id +3%` - изменить громкость

### Утилиты для интернета и wifi:
NetworkManager - для wifi

### Утилиты для интерфейса:
picom - утилита для прозрачных окон
flameshot или scrot - утилита для скриншотов
Dunst - утилита для уведомлений
feh или nitrogen - обои на раб стол

### Утилиты для Архивации файлов:
Архиватор: `sudo apt install atool zip unzip p7zip tar`
Архивировать: `apack <name.zip> <name_file_or_dir>`
Разархивировать: `aunpack <name.zip>`
Посмотреть содержимое архива: `als <name.zip>`

### Утилиты для Музыки:
moc (Music On Console)
Обновить `.bashrc`

## Установка меняющихся обоев через `feh`:
Скрипт для установки обоев на 2 монитора:
`feh --no-fehbg --bg-center '/home/allan/wallpaper/1.jpg' '/home/allan/wallpaper/2.png'`
1) Создаем директорию куда будут помещены все обои. Путь к этой директории прописываем в скрипте выше.
2) Создаем Python программу которая будет рандомно выбирать обои `wallpaper_script.py`
3) Делаем данную программу исполняемой: `chmod +x wallpaper_script.py`
Код Python программы (Надо переработать)
```python
import os
from random import choice
from time import sleep


mass_file = tuple(os.listdir('/home/allan/wallpaper'))
bufer = list()

def wallpaper_update():
    while True:
      img1 = choice(mass_file)
      img2 = choice(mass_file)
      if img1 != img2 and img1 not in bufer and img2 not in bufer:
        bufer.append(img1)
        bufer.append(img2)
        break
      if len(bufer) > 2:
        del bufer[0]

    os.system(f"feh --no-fehbg --bg-center '/home/allan/wallpaper/{img1}' '/home/allan/wallpaper/{img2}'")

while True:
    wallpaper_update()
    sleep(600)
```
4) Добавляем в `xinitrc` путь к скрипту: `python3 $HOME/pypath/wallpaper_script.py &`

## Настройка мониторов
`xrandr` - показать конфигурацию мониторов
Настройка монитора: `xrandr --output DP-0 --mode 1600x900 --rate 60`
ключ `--primary` (Для выбора главного монитора)
Скрипт для настройки монитора:
`mkdir ~/.screenlayout`
```bash
echo "xrandr --output HDMI-0 --primary --mode 1920x1080 --rate 60 --output DP-0 --mode 1600x900 --rate 60 --right-of HDMI-0" >> .screenlayout/display.sh
```
`chmod +x .screenlayout/display.sh`
Добавляем путь к скрипту в `.xinitrc`

## Настройка Polybar:
Создаем файл конфигурации: `~/.config/polybar/config`
Создаем скрипт для запуска: `~/.config/polybar/launch.sh`
Даем скрипту права на исполнение: `chmod +x ~/.config/polybar/launch.sh`
Вставляем в файл скрипта данный код:
```bash
polybar-msg cmd quit

echo "---" | tee -a /tmp/polybar.log

polybar bar_name -c  ~/.config/polybar/config 2>&1 | tee -a /tmp/polybar.log & disown
```
Прописываем путь к скрипту в конфиге bspwm: `$HOME/.config/polybar/launch.sh`
`(Для создания бара на второй монитор, надо создать второй конфиг и второй скрипт)`

# Переменные окружения
## Переменные окружения для текущего сеанса:
`export PATH=$PATH:/dir/dir`
## Переменные окружения для текущего юзера:
изменяем файл `~/.bashrc`
## Переменные окружения для всей системы:
изменяем файл `/etc/environment`

# Алиасы
изменить файл:
https://gitlab.com/prolinux410/owl_dots/-/tree/main/bspwm/bspwm_nord?ref_type=heads
[rvaiya/warpd: A modal keyboard-driven virtual pointer (github.com)](https://github.com/rvaiya/warpd "https://github.com/rvaiya/warpd")
Command-not-found.com
[https://habr.com/ru/sandbox/211835/](https://habr.com/ru/sandbox/211835/ "https://habr.com/ru/sandbox/211835/")
https://github.com/lusakasa/saka-key
[https://wiki.archlinux.org/title/Bspwm_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)](https://wiki.archlinux.org/title/Bspwm_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9) "https://wiki.archlinux.org/title/Bspwm_(%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)")
[https://habr.com/ru/articles/721112/#habracut](https://habr.com/ru/articles/721112/#habracut "https://habr.com/ru/articles/721112/#habracut")
[qutebrowser](https://qutebrowser.org/ "https://qutebrowser.org/")

# Различные полезные линки:


# Вопросики
1) Подумать над другим дистрибутивом вместо Ubuntu server
2) Разобраться с `ntofetch` (добавить лисички на пикчу)
3) Разобраться с виджетами и оформлением `polybar`
4) Разобраться с `dmenu`
5) Разобраться с прозрачностью окон и анимациями
6) Разобраться с буфером обмена
7) Разобраться как открывать ссылки по клику из тг в браузер
8) Кастомизация `Ranger`
9) Автоматизированное окружение - завершение конфигов
10) Интеграция `NeoVim` как `IDE для Python`
11) Добавление юзера в группу (звук, питание и т.п.)
12) Решить проблему с потуханием монитора