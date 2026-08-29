## 31. What is the hashing algorithm used to hash user account passwords on both Linux servers?

SHA-256

| __SHA-512__

MD5

MD4


```bash
# cat /etc/shadow 
root:$6$v8b2/P8T26uEUwvM$TBiao8o1dfqQrGPPcebRj6A6cNiixcy6/r/AFtN5Swk7N1kpg/8UyQK0pXFwdLfy5Ed/71VN91nJ6.3JyAN/00:18998:0:99999:7:::
daemon:*:18960:0:99999:7:::
bin:*:18960:0:99999:7:::
sys:*:18960:0:99999:7:::
sync:*:18960:0:99999:7:::
games:*:18960:0:99999:7:::
man:*:18960:0:99999:7:::
lp:*:18960:0:99999:7:::
mail:*:18960:0:99999:7:::
news:*:18960:0:99999:7:::
uucp:*:18960:0:99999:7:::
proxy:*:18960:0:99999:7:::
www-data:*:18960:0:99999:7:::
backup:*:18960:0:99999:7:::
list:*:18960:0:99999:7:::
irc:*:18960:0:99999:7:::
gnats:*:18960:0:99999:7:::
nobody:*:18960:0:99999:7:::
systemd-network:*:18960:0:99999:7:::
systemd-resolve:*:18960:0:99999:7:::
systemd-timesync:*:18960:0:99999:7:::
messagebus:*:18960:0:99999:7:::
syslog:*:18960:0:99999:7:::
_apt:*:18960:0:99999:7:::
tss:*:18960:0:99999:7:::
uuidd:*:18960:0:99999:7:::
tcpdump:*:18960:0:99999:7:::
sshd:*:18960:0:99999:7:::
landscape:*:18960:0:99999:7:::
pollinate:*:18960:0:99999:7:::
ec2-instance-connect:!:18960:0:99999:7:::
systemd-coredump:!!:18998::::::
ubuntu:!:18998:0:99999:7:::
lxd:!:18998::::::
rtkit:*:18998:0:99999:7:::
xrdp:!:18998:0:99999:7:::
dnsmasq:*:18998:0:99999:7:::
usbmux:*:18998:0:99999:7:::
avahi:*:18998:0:99999:7:::
cups-pk-helper:*:18998:0:99999:7:::
pulse:*:18998:0:99999:7:::
geoclue:*:18998:0:99999:7:::
saned:*:18998:0:99999:7:::
colord:*:18998:0:99999:7:::
sddm:*:18998:0:99999:7:::
gdm:*:18998:0:99999:7:::
auditor:$6$RNJCCrE9ok/yCMqD$7uPoYFsrnR3wPnSwPeLuBEiXgAzlOzGW6uZSyX.IjNNVcR5.bDBhb.dlZTN37JJR4yZXXQTetuUhOOX9ZNov6/:19099:0:99999:7:::
dbadmin:$6$1HAbXNNxXVVNCcoi$6Zy2gjvyZZYHTwSyxSLsdv0LA.5hA7EeD1WhUFzHg9SOSXrz7DxX7iG0mCQbmEBSo.yjB1c80iIujSM6Fjbpo/:19099:0:99999:7:::
mysql:!:19099:0:99999:7:::
ftp:*:19100:0:99999:7:::
```