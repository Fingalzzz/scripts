# confirm pos 400 600
# finish pos  400 1300

x11=(50 150 260 600 200 500 800 600 800 950 1050)
y11=(1500 1400 1500 1400 1800 1700 1500 1800 1700 1750 1680)
num=${#x11[*]}
while true; do
    for i in `seq 1 $num`;do
        let x=${x11[$i-1]}+$RANDOM%20-10
        let y=${y11[$i-1]}+$RANDOM%20-10
        input tap $x $y
        let r=$RANDOM%20/100
        sleep 0.5;
        let x=400+$RANDOM%10-5
        let y=600+$RANDOM%10-5
        input tap $x $y
        sleep 0.4;
        input tap $x $y
        #input tap 400 600
    done
    sleep 190;
done

