## Tutoriels:


### Installation et premiers tests

Voir https://www.esa.int/Education/AstroPI/Getting_started_with_Astro_Pi_-_teach_with_space_T05.1

* Guide en français (enseignants): https://eserobelgium.be/wp-content/uploads/2018/07/T05.1b_Getting-started-with-astro-pi_teqcher-guide_FR.pdf
* Guide en français (élèves): https://eserobelgium.be/wp-content/uploads/2018/07/T05.1b_Getting-started-with-astro-pi_student-activities_FR.pdf

Aussi

* https://projects.raspberrypi.org/fr-FR/projects/raspberry-pi-getting-started - Raspberry 3 ?

### Mission 0 

* En français, pour dernier AstroPi https://projects.raspberrypi.org/fr-FR/projects/astro-pi-mission-zero
* https://astro-pi.org/mission-zero/resources

### Mission space

* https://astro-pi.org/mission-space-lab/resources

### Autres ressources

* En anglais(ou français une fois sur chaque page): https://astro-pi.org/mission-space-lab/resources
* Camera: https://projects.raspberrypi.org/fr-FR/projects/getting-started-with-picamera


## Connection SSH

Voir: https://www.raspberrypi.org/documentation/computers/remote-access.html

* login: pi
* password: raspberry
* 169.254.221.154

```
Utiliser -Y pour exporter le serveur graphique
ssh -Y pi@169.254.221.154
```

## Setup wifi

```
sudo raspi-config

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB

network={
 ssid="sciento_2.4Ghz"
 scan_ssid=1
 psk="sciento0!"
 key_mgmt=WPA-PSK
}

```


## Version

Raspberry Pi 3, Model B. Raspbian release 1.3, may 2017

```
PRETTY_NAME="Raspbian GNU/Linux 8 (jessie)"
NAME="Raspbian GNU/Linux"
VERSION_ID="8"
VERSION="8 (jessie)"
ID=raspbian
ID_LIKE=debian
HOME_URL="http://www.raspbian.org/"
SUPPORT_URL="http://www.raspbian.org/RaspbianForums"
BUG_REPORT_URL="http://www.raspbian.org/RaspbianBugs"
```

Notes:

* Seulement Scratch1 et Scratch2 dispo. 

## Jupyter notebook

https://www.instructables.com/Jupyter-Notebook-on-Raspberry-Pi/


## Minecraft

* En anglais: https://projects.raspberrypi.org/en/projects/minecraft-photobooth/2
