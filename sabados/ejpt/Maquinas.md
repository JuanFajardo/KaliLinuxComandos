	# Kali 

oot@kali:~# df -h
Filesystem      Size  Used Avail Use% Mounted on
udev            3.9G     0  3.9G   0% /dev
tmpfs           796M  1.1M  795M   1% /run
/dev/xvda1       40G   13G   25G  35% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
/dev/xvda15     124M  278K  124M   1% /boot/efi
root@kali:~# free -h
               total        used        free      shared  buff/cache   available
Mem:           7.8Gi       590Mi       6.5Gi        32Mi       666Mi       6.9Gi
Swap:             0B          0B          0B
root@kali:~# fdisk -l
Disk /dev/xvda: 40 GiB, 42949672960 bytes, 83886080 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 4F297594-2921-7243-945F-0F7B0BEF560A

Device       Start      End  Sectors  Size Type
/dev/xvda1  262144 83886046 83623903 39.9G Linux filesystem
/dev/xvda14   2048     8191     6144    3M BIOS boot
/dev/xvda15   8192   262143   253952  124M EFI System

Partition table entries are not in disk order.



## IP
root@kali:~# ip -4 a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9001 qdisc mq state UP group default qlen 1000
    inet 192.168.100.5/24 brd 192.168.100.255 scope global dynamic eth0
       valid_lft 3407sec preferred_lft 3407sec
root@kali:~# 


## ARPSCAN
oot@kali:~# arp-scan -I eth0 --localnet
Interface: eth0, type: EN10MB, MAC: 06:c1:60:76:09:a5, IPv4: 192.168.100.5
Starting arp-scan 1.9.7 with 256 hosts (https://github.com/royhills/arp-scan)
192.168.100.1   06:3e:cc:b3:a9:8b       (Unknown: locally administered)
192.168.100.50  06:35:24:ae:0f:7d       (Unknown: locally administered)
192.168.100.51  06:4d:b8:4a:0c:e5       (Unknown: locally administered)
192.168.100.52  06:c6:16:9c:4e:29       (Unknown: locally administered)
192.168.100.55  06:ea:bd:7d:6a:a7       (Unknown: locally administered)
192.168.100.63  06:44:df:e3:ef:05       (Unknown: locally administered)
192.168.100.67  06:0e:6c:5d:f0:0b       (Unknown: locally administered)

9 packets received by filter, 0 packets dropped by kernel
Ending arp-scan 1.9.7: 256 hosts scanned in 1.966 seconds (130.21 hosts/sec). 7 responded

## NMAP


# ---------------------------------------------------

cat nmapscan_sn.txt | grep "192.168.100" | cut -d "(" -f 2 | cut -d ")" -f 1
192.168.100.1
192.168.100.50
192.168.100.51
192.168.100.52
192.168.100.55
192.168.100.63
192.168.100.67
192.168.100.5


192.168.100.1

192.168.100.50
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
192.168.100.51
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
192.168.100.55
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows
192.168.100.63
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

192.168.100.52
cpe:/o:linux:linux_kernel
192.168.100.67
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
192.168.100.5
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel