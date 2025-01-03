[colors]

background = #222

background-alt = #444

foreground = #dfdfdf

foreground-alt = #f0f0f0

primary = #646464

secondary = #646464

alert = #646464

underline = #c0c0c0

[bar/lolicon]

#monitor = ${env:MONITOR:HDMI-0}

#Размеры

monitor = HDMI-0

width = 100%

height = 27

;offset-x = 1%

;offset-y = 1%

radius = 8.0

fixed-center = true

#Цвета

background = ${colors.background}

foreground = ${colors.foreground}

#Настройка линии

line-size = 2

line-color = #f00

#Настройка рамки

border-size = 4

border-color = #00000000

#Шрифты

font-0 = fixed:pixelsize=10;1

font-1 = unifont:fontformat=truetype:size=8:antialias=false;0

font-2 = siji:pixelsize=10;1

#Отступы

padding-left = 0

padding-right = 5

module-margin-left = 1

module-margin-right = 2

#Расположение модулей

modules-left = bspwm

modules-center = time

modules-right = date

#Активация кастомного модуля. (не забываем сделать скрипт исполняемым)

#[module/{ИМЯ}]

#type = custom/script

#exec = ~/.config/polybar/script.sh

[module/date]

type = internal/date

date = %Y-%m-%d%

[module/bspwm]

type = internal/bspwm

pin-workspaces = true

inline-mode = true

enable-click = true

enable-scroll = true

reverse-scroll = false

format = <label-state>

ws-icon-0 = 1;%{F#F9DE8F}1

ws-icon-1 = 2;%{F#ff9b93}2

ws-icon-2 = 3;%{F#95e1d3}3

ws-icon-3 = 4;%{F#81A1C1}4

ws-icon-4 = 5;%{F#A3BE8C}5

ws-icon-5 = 6;%{F#F9DE8F}6

ws-icon-6 = 7;%{F#ff9b93}7

label-separator = ""

label-separator-background = #2b2f37

label-focused =  %icon%

label-focused-foreground = ${colors.foreground}

label-focused-underline =  #565c64

label-focused-padding = 1

label-focused-background = #2b2f37

label-occupied = %icon%

label-occupied-foreground = #646870

label-occupied-background = #2b2f37

label-occupied-padding = 1

label-empty = %icon%

label-empty-foreground =   ${colors.foreground}

label-empty-padding = 1

label-empty-background = #2b2f37

label-urgent = %icon%

label-urgent-foreground = #88C0D0

label-urgent-background = #2b2f37

label-urgent-padding = 1

[module/time]

type = internal/date

interval = 60

format = <label>

format-background = #2b2f37

date = %{F#888e96}  %H:%M %p%{F-}

time-alt = %{F#61afef}  %a, %d %b %Y%{F-}

label = %date%%time%