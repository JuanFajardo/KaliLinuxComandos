
## 4. How many hosts on the DMZ network are running a web server on port 80?

2

| __4__

5

6


```bash
$ cat nmapCompeto.txt | grep "80/tcp"
80/tcp    open  http               Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
80/tcp    open  http               Microsoft IIS httpd 8.5
80/tcp   open  http          Apache httpd 2.4.41
80/tcp   open  http          Microsoft IIS httpd 10.0
```