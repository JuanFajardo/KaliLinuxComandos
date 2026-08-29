## 16. What host can be used to pivot into the internal network?

WINSERVER-01

| __WINSERVER-03__

WINSERVER-02

WEBSERVER-01


```bash
C:\Users\Administrator>hostname
WINSERVER-03
WINSERVER-03

C:\Users\Administrator>ipconfig
Windows IP Configuration
Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : us-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::5ca1:c373:8cd0:5e48%8
   IPv4 Address. . . . . . . . . . . : 192.168.100.55
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.100.1

Ethernet adapter Ethernet 4:

   Connection-specific DNS Suffix  . : us-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::c08c:cf2b:4bd2:40c6%27
   IPv4 Address. . . . . . . . . . . : 192.168.0.50
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1

```



```bash
WINSERVER-01
WINSERVER-01
Windows IP Configuration
Ethernet adapter Ethernet 2:
   Connection-specific DNS Suffix  . : us-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::e09a:d08e:b7aa:df97%12
   IPv4 Address. . . . . . . . . . . : 192.168.100.50
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.100.1

Tunnel adapter isatap.us-west-1.compute.internal:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : us-west-1.compute.internal
   Connection-specific DNS Suffix  . : us-west-1.compute.internal

```

```bash
WINSERVER-02
WINSERVER-02
Windows IP Configuration
Ethernet adapter Ethernet 2:
   Connection-specific DNS Suffix  . : us-west-1.compute.internal
   Link-local IPv6 Address . . . . . : fe80::914:f336:1cb9:b0c8%12
   IPv4 Address. . . . . . . . . . . : 192.168.100.51
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.100.1

Tunnel adapter isatap.us-west-1.compute.internal:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . : us-west-1.compute.internal
```


```bash
# ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    inet 192.168.100.52/24 brd 192.168.100.255 scope global dynamic eth0
       valid_lft 1921sec preferred_lft 1921sec
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
       valid_lft forever preferred_lft forever
4: br-c9cc91cc3452: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    inet 172.18.0.1/16 brd 172.18.255.255 scope global br-c9cc91cc3452
       valid_lft forever preferred_lft forever
5: br-decc664e2ae4: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    inet 172.19.0.1/16 brd 172.19.255.255 scope global br-decc664e2ae4
       valid_lft forever preferred_lft forever
```


