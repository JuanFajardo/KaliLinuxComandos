## 12. What type of vulnerability can be exploited to gain access to WINSERVER-03?

SMB Brute Force

Buffer Overflow

Command Injection

EternalBlue


```bash
root@kali:~# nbtscan 192.168.100.55
Doing NBT name scan for addresses from 192.168.100.55

IP address       NetBIOS Name     Server    User             MAC address      
------------------------------------------------------------------------------
192.168.100.55   WINSERVER-03     <server>  <unknown>        06:ea:bd:7d:6a:a7

# nmap -p 3389 --script rdp-ntlm-info 192.168.100.55
Starting Nmap 7.92 ( https://nmap.org ) at 2025-12-14 02:19 IST
Nmap scan report for ip-192-168-100-55.us-west-1.compute.internal (192.168.100.55)
Host is up (0.00019s latency).

PORT     STATE SERVICE
3389/tcp open  ms-wbt-server
| rdp-ntlm-info: 
|   Target_Name: WINSERVER-03
|   NetBIOS_Domain_Name: WINSERVER-03
|   NetBIOS_Computer_Name: WINSERVER-03
|   DNS_Domain_Name: WINSERVER-03
|   DNS_Computer_Name: WINSERVER-03
|   Product_Version: 10.0.17763
|_  System_Time: 2025-12-13T20:49:57+00:00
MAC Address: 06:EA:BD:7D:6A:A7 (Unknown)




root@kali:~# ffuf -u http://192.168.100.55/FUZZ -w /usr/share/wordlists/dirb/small.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.3.1 Kali Exclusive <3
________________________________________________

 :: Method           : GET
 :: URL              : http://192.168.100.55/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405
________________________________________________

webdav                  [Status: 301, Size: 152, Words: 9, Lines: 2]



[!] Valid Combinations Found:
 | Username: admin, Password: estrella

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Dec 14 03:10:30 2025
[+] Requests Done: 272
[+] Cached Requests: 4
[+] Data Sent: 104.097 KB
[+] Data Received: 304.827 KB
[+] Memory used: 209.473 MB
[+] Elapsed time: 00:00:12
root@kali:~# wpscan --url http://192.168.100.50/wordpress --rua --passwords /usr/share/wordlists/rockyou.txt --usernames admin

```
