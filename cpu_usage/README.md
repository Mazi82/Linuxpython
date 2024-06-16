# CPU Usage Monitoring Service

## Installation

1. Placera `cpu_usage.py` i en katalog, till exempel `/usr/local/bin/`.
2. Skapa en systemd-tjänstfil `cpu_usage.service` i `/etc/systemd/system/`.

## Instruktioner

### Kopiera filerna:

```bash
sudo cp /path/to/cpu_usage.py /usr/local/bin/cpu_usage.py
sudo cp /path/to/cpu_usage.service /etc/systemd/system/cpu_usage.service



#### Starta tjänsten
sudo systemctl daemon-reload
sudo systemctl enable cpu_usage.service
sudo systemctl start cpu_usage.service

##### Stoppa tjänsten
sudo systemctl stop cpu_usage.service
sudo systemctl disable cpu_usage.service

###### Test av tjänst
sudo systemctl start cpu_usage.service



Kolla om /tmp/cpu_usage_rapport.txt skapas
