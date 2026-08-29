## 22. What web server contains a file called "todo.txt"?

| __WINSERVER-03__

WEBSERVER-01

WINSERVER-01

WINSERVER-02

```bash
root@kali:~# nbtscan 192.168.100.55
Doing NBT name scan for addresses from 192.168.100.55
IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
192.168.100.55   WINSERVER-03     <server>  <unknown>        06:ea:bd:7d:6a:a7
Administrator" user on WINSERVER-03?
What is the password of the user account "mary" on WINSERVER-03?
What is the value of the flag C:\Users\Administrator\flag.txt on WINSERVER-03?
```

http://192.168.100.55/todo.txt

```txt
Greetings gents!

I have setup this server to host our production services.
I will be sharing changelogs and updates on the HTTP File Server.

So far this server does not have any running services, as a result, you must login via RDP or SMB.

- Administrator
```


![[Pasted image 20251213194217.png]]