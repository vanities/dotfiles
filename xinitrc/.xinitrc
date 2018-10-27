redshift -l 35.845621:-86.390270 &
./.config/polybar/launch.sh
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources &
feh --randomize --bg-fill ~/Downloads/pics/* &

exec bspwm
