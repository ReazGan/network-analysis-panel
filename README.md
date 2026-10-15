# network-analysis-panel

A live network analysis dashboard. It sniffs traffic on the host and visualizes
connections in real time on a world map and interactive panels, with a protocol
breakdown you can filter by.

For each connection it resolves the IP, port, geolocation, hostname and
organization, and flags addresses that belong to known hosting or proxy
services. A built-in console shows activity, and the live feed can be paused or
cleared from the interface.

It is built with Python (Flask, Flask-SocketIO, Scapy) and a Leaflet and
Chart.js front end.

![network-analysis-panel](https://github.com/user-attachments/assets/ba7cae06-1df7-4223-a738-59b92de41171)

## Requirements

Python 3.8+ and, on Windows, Npcap (installed with "WinPcap API-compatible
mode" enabled) so Scapy can capture.

```
pip install flask flask-socketio scapy requests eventlet
```

## Usage

```
python app.py
```

On Windows, `run_as_admin.bat` requests the privileges needed to capture. The
dashboard opens at http://127.0.0.1:5000.

## Notice

For education and authorized testing only. Monitor only networks you own or are
authorized to.

## License

MIT
