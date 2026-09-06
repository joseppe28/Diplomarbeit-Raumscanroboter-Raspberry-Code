# Diplomarbeit Raumscanroboter: Raspberry und Mikrocontroller Code

In diesem Repository werden alle Code files die auch auf dem Raspberry oder anderen Mikrocontrollern liegen geteilt. 

## PC Setup

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
da dieser Code am Raspberry getestet wird und diese Packages / Libraries nur für die Ausführung und nicht Syntax,... wichtig sind werden sie hier weggelassen

## Raspberry Setup
Auf dem Rasperry läuft Ubuntu Server 24.04 ARM64

Für das Projekt wird ROS 2 Jazzy verwendet 

Als Lidar verwenden wir den RPLIDAR A1M8

```
# ============================================================
# 1. GENERELLES SETUP
# ============================================================

sudo apt update
sudo apt upgrade -y

sudo apt install -y \
    curl \
    git \
    software-properties-common \
    python3-serial \
    openssh-server


# ============================================================
# 2. ROS 2 JAZZY
# ============================================================

# Ubuntu Universe Repository aktivieren
sudo add-apt-repository universe -y

# ROS Repository hinzufügen
ROS_APT_SOURCE_VERSION=$(curl -s https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest | grep -F "tag_name" | awk -F'"' '{print $4}')

curl -L -o /tmp/ros2-apt-source.deb \
"https://github.com/ros-infrastructure/ros-apt-source/releases/download/${ROS_APT_SOURCE_VERSION}/ros2-apt-source_${ROS_APT_SOURCE_VERSION}.$(. /etc/os-release && echo ${UBUNTU_CODENAME})_all.deb"

sudo dpkg -i /tmp/ros2-apt-source.deb
sudo apt update

# ROS ohne grafische Programme installieren
sudo apt install -y \
    ros-jazzy-ros-base \
    ros-dev-tools

# ROS automatisch in neuen Terminals laden
echo 'source /opt/ros/jazzy/setup.bash' >> ~/.bashrc

# ROS für dieses Terminal laden
source /opt/ros/jazzy/setup.bash


# ============================================================
# 3. RPLIDAR
# ============================================================

# ROS Workspace erstellen
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# RPLIDAR ROS 2 Driver herunterladen
git clone https://github.com/Slamtec/sllidar_ros2.git

# Workspace bauen
cd ~/ros2_ws
colcon build --symlink-install

# Workspace automatisch in neuen Terminals laden
echo 'source ~/ros2_ws/install/setup.bash' >> ~/.bashrc

# Workspace für dieses Terminal laden
source ~/ros2_ws/install/setup.bash

# Zugriff auf USB/UART Geräte erlauben
sudo usermod -aG dialout $USER

# RPLIDAR USB-Regel installieren
sudo cp ~/ros2_ws/src/sllidar_ros2/scripts/rplidar.rules /etc/udev/rules.d/

sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Verbindung zum Raspberry
Die Verbindung zum Raspberry läuft über SSH und WLAN / Ethernet 
```
ssh user@hostname.local
# oder
ssh user@ipaddress
```

Nach der erfolgreichen Verbindung muss nur noch der verbundene Lidar gestartet werden: 
```
ros2 launch sllidar_ros2 sllidar_a1_launch.py serial_port:=/dev/ttyUSB0
```

Potenziell muss man den USB eingang oder das Lidar Model ändern 

Falls alles ohne fehler abgeschlossen hat sollte man zum testen ein zweites terminal mit ssh verbindung öffnen und in diesem: 
```
ros2 topic list
```
ausführen

Wenn alles richtig läuft sollte man dort auch ein /scan topic sehen.
