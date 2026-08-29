
## 1. What is the IP address of the host running SAMBA?

192.168.100.51
192.168.100.50
192.168.100.54
| __192.168.100.52__

```bash
root@kali:~# nmap -sS -sV -Pn -n  192.168.100.50,51,52
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
```