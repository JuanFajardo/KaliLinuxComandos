## 18. What is the password for the user "mike" on WINSERVER-01?

superman

greenday

bonita

|__diamond__


```bash
root@kali:~# smbmap -H 192.168.100.50 -u mike -p diamond
[+] IP: 192.168.100.50:445      Name: wordpress.local                                   
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        print$                                                  READ ONLY       Printer Drivers
root@kali:~# 
```


