# confirm pos 400 600
# finish pos  400 1300

x11=(50 150 260 600 200 500 800 600 800 950 1050)
y11=(1500 1400 1500 1400 1800 1700 1500 1800 1700 1750 1680)
num=${#x11[*]}
while true; do
    for i in `seq 1 $num`;do
        input tap ${x11[$i-1]} ${y11[$i-1]}
        sleep 0.5;
        input tap 400 600
        sleep 0.5;
        input tap 400 600
    done
    sleep 185;
done
