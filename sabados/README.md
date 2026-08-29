
## 1. What is the IP address of the host running SAMBA?

192.168.100.51 

192.168.100.50

192.168.100.54

| __192.168.100.52__


## 2. How many hosts on the DMZ network are running Windows?

2

3

| __4__

5


## 3. What version of MySQL is running on the system hosting a Drupal site?

| __MySQL 5.5.5__

MySQL 5.5.10

MySQL 5.5.0

MySQL 5.5.3


## 4. How many hosts on the DMZ network are running a web server on port 80?

2

| __4__

5

6


## 5. What version of Windows is running on the host running WordPress?

Windows 10

Windows 7 SP3

| __Windows Server 2012 R2__

Windows Server 2016


## 6. What services does Syntex provide to companies?

Software Development

Financial Services

| __Workflow Development__

Cloud Hosting


![[Captura de pantalla 2025-12-13 122216.png]](ejpt/imagenes/Captura%20de%20pantalla%202025-12-13%20122216.png)


## 7. What is the email of the admin user on the Drupal site?

admin@syntexd.com

admin-user@syntex.com

administrator@syntex.com

| __admin@syntex.com__


## 8. What is the name of the active theme on the WordPress site?

| __Spintech__

BizPress

TwentyNineteen

Burgertheme


## 9. How many systems on the target network have FTP servers with anonymous access enabled?

1

| __2__

3

4

## 10. How many user accounts can be enumerated from the SAMBA server running on the system hosting Drupal?

1

2

| __3__

5

## 11. What type of vulnerability can be exploited to elevate your privileges on the Linux host running Drupal?

| __Misconfigured SUDO Permissions__

Cron Job

Vulnerable Service

Locally Stored Credentials


## 12. What type of vulnerability can be exploited to gain access to WINSERVER-03?

SMB Brute Force

Buffer Overflow

Command Injection

| EternalBlue


## 13 What type of vulnerability can be exploited on the WordPress site to obtain a reverse shell?

Command Injection

SQL Injection

| __Arbitrary File Upload__

RCE


## 15 How many hosts exist within the internal network that cannot be accessed through the DMZ network?

| __2__

3

4

5


## 16. What host can be used to pivot into the internal network?

WINSERVER-01

| __WINSERVER-03__

WINSERVER-02

WEBSERVER-01


## 17. What is the password of the "Administrator" user on WINSERVER-03?

Submit answer

Case-sensitive answer. Please enter text as displayed.

```bash
[3389][rdp] host: 192.168.100.55   login: administrator   password: swordfish
```


## 18. What is the password for the user "mike" on WINSERVER-01?

superman

greenday

bonita

|__diamond__


## 19. What is the password of the user account "mary" on WINSERVER-03?

Submit answer

Case-sensitive answer. Please enter text as displayed.

| __hotmama__

```bash
root@kali:~# hydra -l mary -P /usr/share/wordlists/rockyou.txt rdp://192.168.100.55
```

## 20. What is the CVSS V3.x rating for the Drupalgeddon2 vulnerability?

7.7

8.1

8.5

| __9.8__

https://www.cvedetails.com/cve/CVE-2018-7600/

## 21. What host within the DMZ network can be exploited via command injection.

WEBSERVER-02

WINSERVER-03

|__WINSERVER-02__

WINSERVER-01

http://192.168.100.51/aspnet_client/cmdasp.aspx


## 22. What web server contains a file called "todo.txt"?

| __WINSERVER-03__

WEBSERVER-01

WINSERVER-01

WINSERVER-02

;) X) X) X)


## 23. How many Drupal accounts exist on the Drupal site?

1

2

3

| __4__


## 24. What WordPress file stores the database configuration?

config.php

phpconfig.php

wp-admin.php

| __wp-config.php__


## 25. How many plugins are installed on the WordPress site?

2

| __3__

4

5


## 26. What host on the DMZ network is running a database server on port 3307?

192.168.100.52

192.168.0.100

| __192.168.100.50__

192.168.100.51


## 27. What is the root password of the MySQL database on the server running Drupal?

Submit answer

Case-sensitive answer. Please enter text as displayed.


```bash
root@kali:~# mysql -h 192.168.100.52 -u root -psyntex0421
```


## 28. What is the version of the Linux kernel running on the system hosting the Drupal site?

5.4.2

5.12.1

| __5.13.0__

5.5.1

```bash
# uname -a
```


## 29. What is the total number of open TCP ports running on WINSERVER-02?

8

| __11__

14

15


## 30. What user account is a member of the local administrators group on WINSERVER-03?

mike

mary

lawrence

| __admin__


## 31. What is the hashing algorithm used to hash user account passwords on both Linux servers?

SHA-256

| __SHA-512__

MD5

MD4


```bash
# cat /etc/shadow 
root:$6$v8b2/P8T26uEUwvM$TBiao8o1dfqQrGPPcebRj6A6cNiixcy6/r/
```


## 33. A system contains the file C:\Users\mike\Documents\flag.txt; what is the value of the flag?

I understand that I only have one attempt at this answer. After clicking _Submit answer_, I will not be able to make edits. Your answer will be graded based on the state of the lab environment at the time it is submitted.

Submit answer


## 34. What is the value of the flag /root/flag.txt on the host running Drupal?

I understand that I only have one attempt at this answer. After clicking _Submit answer_, I will not be able to make edits. Your answer will be graded based on the state of the lab environment at the time it is submitted.

Submit answer


## 35. What is the value of the flag C:\Users\Administrator\flag.txt on WINSERVER-03?

I understand that I only have one attempt at this answer. After clicking _Submit answer_, I will not be able to make edits. Your answer will be graded based on the state of the lab environment at the time it is submitted.

Submit answer

3a7b20642b5e46bab2a08602e21403b1