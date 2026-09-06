# Diplomarbeit Raumscanroboter: Raspberry und Mikrocontroller Code

In diesem Repository werden alle Code files die auch auf dem Raspberry oder anderen Mikrocontrollern liegen geteilt. 

## Setup

Das Projekt ist ein Python 3.12 Projekt: 
``` 
python3 -m venv .venv
source .venv/bin/activate
```

mit folgendem Packages(die lokal installiert werden können): 
```
pip install numpy
pip install pyserial 
pip install scipy
```

### Achtung: 
Damit das Projekt funktioniert bräuchte man noch mehr Packages und Libraries wie ROS und RPLIDAR 
da dieser Code am Raspberry getestet wird und diese Packages / Libraries nur für die Ausführung und nicht Syntax,... wichtig werden sie hier weggelassen

## Raspberry Setup
Auf dem Rasperry läuft Ubuntu Server 24.04 ARM64
Für das Projekt wird ROS 2 Jazzy verwendet 
Als Lidar verwenden wir den RPLIDAR A1M8

