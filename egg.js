// set oneplus screen metrics
setScreenMetrics(1080, 2340);

while (true) {
    // apply income bonus (900, 550) triple times, takes 6 sec
    for (var i = 0; i < 3; i++) {
        press(900, 550, 500);
        sleep(500);
        press(666, 888, 500);
        sleep(500);
    }

    // apply all bonus (900, 1700) twice, takes 4 secs
    for (var i = 0; i < 2; i++) {
        press(900, 1700, 500);
        sleep(500);
        press(666, 888, 500);
        sleep(500);
    }

    // magic 2 sec to make the touch happen
    press(550, 2200, 1000);
    sleep(1000);

    // takes 8 secs to long press the red button
    press(550, 2200, 7000);
    sleep(1000);

    // for the rest 10 mins
    for (var i = 0; i < (10 * 60 / 5); i++) {
        press(550, 2200, 2500);
        sleep(2500);
    }
}