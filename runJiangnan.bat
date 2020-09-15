adb start-server
adb tcpip 5792
adb connect 192.168.199.202:5792
activate auto
python jiangnan.py
