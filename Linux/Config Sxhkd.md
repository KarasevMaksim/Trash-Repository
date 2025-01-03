super + d

        dmenu

super + {_,shift + }Return

        {alacritty --config-file ~/.config/bspwm/themes/bspwm_nord/alacritty/alacritty.yml, bspc node -s biggest.local}

@Print

        scrot

shift + @Print

        scrot -d 5

super + n

        cool-retro-term

super + v

        virt-manager

super + b

        blender

super + i

        inkscape

super + l

        lutris

super + o

        obs

#ПЕРЕЗАГРУЗИТЬ КОНФИГ SXHKD

super + e

        pkill -USR1 -x sxhkd

#ВЫЙТИ/ПЕРЕЗАГРУЗИТЬ BSPWM

super + shift + {q,r}

        bspc {quit,wm -r}

#ПЕРЕЗАГРУЗКА

super + ctrl + r

        sudo shutdown -r now

#ВЫКЛЮЧЕНИЕ

super + ctrl + p

        sudo shutdown -h now

#ПОМЕНЯТЬ СТАТУС ОКНА НА /ТАЙЛОВОЕ/ПСЕВДО ТАЙЛОВОЕ/ПЛАВАЮЩЕЕ/ПОЛНОЭКРАННОЕ

super + {t,shift + t,s,f}

        bspc node -t {tiled,pseudo_tiled,floating,fullscreen}

        bspc node -g {marked,locked,sticky,private}

#ВЫБРАТЬ НАПРАВЛЕНИЕ В КОТОРОМ ОТКРОЕТСЯ НОВОЕ ОКНО

super + alt + {Left,Down,Up,Right}

        bspc node -p {west,south,north,east}

#ОТМЕНИТЬ НАПРАВЛЕНИЕ В КОТОРОМ ОТКРОЕТСЯ НОВОЕ ОКНО

super + alt + space

#ПЕРЕКЛЮЧИТСЯ НА ВОРКСПЕЙС ИЛИ ПЕРЕТАЩИТЬ НА НЕГО АКТИВНОЕ ОКНО

super + {_,shift + }{1-9,0}

        bspc {desktop -f,node -d} '^{1-9,10}'

#ЗАКРЫТЬ ОКНО ИЛИ УБИТЬ ЕГО

super + {_, shift + }c

        bspc node -{c}

#ПЕРЕМЕЩЕНИЕ ТАЙЛИНГОВЫХ ОКОН

super + {_,shift + }{Left,Down,Up,Right}

        bspc node -{f,s} {west,south,north,east}

#РЕСАЙЗ ТАЙЛИНГОВЫХ ОКОН

super + ctrl + {Left,Down,Up,Right}

        {bspc node -z left -20 0; bspc node -z right -20 0, \

        bspc node -z bottom 0 20; bspc node -z top 0 20, \

        bspc node -z bottom 0 -20; bspc node -z top 0 -20, \

        bspc node -z left 20 0; bspc node -z right 20 0}

#РЕСАЙЗА ПЛАВАЮЩИХ ОКОН

alt + ctrl + {Left,Down,Up,Right}

        {bspc node -z right -20 20, \

        bspc node -z bottom 20 20, \

        bspc node -z bottom 20 -20, \

        bspc node -z right 20 20}

#ПЕРЕМЕЩЕНИЕ ПЛАВАЮЩИХ ОКОН

ctrl + shift + {Left,Down,Up,Right}

        bspc node -v {-20 0,0 20,0 -20,20 0}