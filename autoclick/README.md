# autoclick

Simple wrapper of [adbutils](https://github.com/openatx/adbutils), make it quicker and easier to develop code to perform some automatic actions on the phone.
Due to the limit of adbutils, only support Python3.6+.

## Requirements

- Android Debug Bridge (adb) tools. Download from [here](https://developer.android.com/studio/releases/platform-tools).
- Python dependencies
    `pip3 install -r reqirements.txt`

## Preparation

Specify the IP address and port number in `config.json` file.
You can set your port number with the command `adb tcpip <port_number>`.
You can find your device IP address with the command `adb shell ip addr show wlan0 | grep inet`.

## Usage

### screenshot

```python
import autoclick
autoclick.screenshot(device)
```

### tap and swipe

```python
import autoclick
autoclick.tap(device, coordinates:(int, int))
autoclick.swipe(devices, start_coordinate:(int, int), changes_coordinate:(int, int), time:float)
```

## Examples

See [jiangnan.py](https://github.com/Fingalzzz/scripts/blob/master/autoclick/jiangnan.py) as an expamle
It's a simple scripts use autoclick to cheat [江南百景图](https://jiangnan.coconut.is/), make money in the game using wells.

## Thanks

[adbutils](https://github.com/openatx/adbutils)

## LICENSE

[MIT](https://github.com/Fingalzzz/scripts/blob/master/LICENSE)

