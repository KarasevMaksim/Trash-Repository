pgrep -x sxhkd > /dev/null || sxhkd -f &

#sxhkd -c ~/.config/sxhkd/sxhkdrc &

$HOME/.config/polybar/launch.sh

# запуск приложений

firefox &

# правила для приложений

#bspc rule -a TelegramDesktop state=floating follow=off

bspc rule -a firefox state=floating rectangle=1600x900+160+90 desktop='^1'

bspc rule -a Lutris state=floating follow=off rectangle=1200x700+360+190 desktop='^6'

bspc rule -a mpv state=floating rectangle=800x450+560+315 follow=off

bspc rule -a dmenu rectangle=900x22+610+90

bspc rule -a Viewnior rectangle=1350x900+285+90 state=floating

bspc rule -a Inkscape desktop='^3'

#bspc rule -a Blender desktop='^2'

bspc monitor -d 1 2 3 4 5 6 7 8 9 []=

# ширина оконтовки

bspc config border_width         5

# расстояние между окнами

bspc config window_gap          10

bspc config normal_border_color "#2e3440"

bspc config active_border_color "#2e3440"

bspc config focused_border_color "#d8dee9"

bspc config presel_feedback_color "#2e3440"

bspc config split_ratio          0.5

bspc config focus_follows_pointer true

bspc config pointer_modifier    super

bspc config single_monocle           true

bspc config borderless_monocle   false

bspc config gapless_monocle      false

bspc config paddingless_monocle  true