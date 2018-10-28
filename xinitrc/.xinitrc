compton &
sxhkd &
$HOME/.config/polybar/launch.sh &

redshift -l 35.845621:-86.390270 &
[[ -f ~/.Xresources ]] && xrdb -merge ~/.Xresources &
feh --randomize --bg-fill ~/Downloads/pics/* &

exec bspwm
