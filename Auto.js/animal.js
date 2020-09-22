// set oneplus screen pixel
setScreenMetrics(1080, 2340);

// create new ra for touch system
var ra = new RootAutomator();
events.on('exit', function () {
    ra.exit();
});


while(true) {
    // click random times of button bottom right corner
    var clickNum = Math.round(Math.random() * 25) + 25;
    for (var i = 0; i < clickNum; i++) {
        var coorX = Math.round(Math.random() * 150) + 870;
        var coorY = Math.round(Math.random() * 150) + 2100;
        ra.tap(coorX, coorY);
        var sleepTime = Math.round(Math.random() * 10) + 5;
        sleep(sleepTime);
    }

    // tricky way to exploit one-hour bot check
    coorX = Math.round(Math.random() * 270) + 400;
    coorY = Math.round(Math.random() * 100) + 1410;
    ra.tap(coorX, coorY);
    sleep(10);
}