# confirm pos 400 600
# finish pos  400 1300

x11=(50 150)
y11=(1500 1400)
num=${#x11[*]}
for i in `seq 1 $num`;do
    input tap ${x11[$i-1]} ${y11[$i-1]}
    sleep 0.5;
    input tap 400 600
    sleep 0.5;
    input tap 400 600
done
let waitSecs=3*60-25-$num-1
sleep $waitSecs;
for i in `seq 1 $num`; do
    input tap ${x11[$i-1]} ${y11[$i-1]}
    sleep 0.5;
    input tap 400 1300
    sleep 0.5;
    input tap ${x11[$i-1]} ${y11[$i-1]};
    sleep 1;
done
