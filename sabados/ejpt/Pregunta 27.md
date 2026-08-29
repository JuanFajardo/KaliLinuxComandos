## 27. What is the root password of the MySQL database on the server running Drupal?

Submit answer

Case-sensitive answer. Please enter text as displayed.


```bash
root@kali:~# mysql -h 192.168.100.52 -u root -psyntex0421
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1785
Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| drupal             |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
4 rows in set (0.001 sec)

MariaDB [(none)]> 
```



```php
* @endcode
 */
$databases = array (
  'default' => 
  array (
    'default' => 
    array (
      'database' => 'drupal',
      'username' => 'drupal',
      'password' => 'syntex0421',
      'host' => 'localhost',
      'port' => '3306',
      'driver' => 'mysql',
      'prefix' => '',
    ),
  ),
);
```

```bash
# mysql -u root -p
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 1783
Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1 Ubuntu 20.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> use mysql;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
MariaDB [mysql]> select host, user, password from user;
+-----------+--------+-------------------------------------------+
| host      | user   | password                                  |
+-----------+--------+-------------------------------------------+
| localhost | root   | *7C695400AEECFFAD9251CB1CF2DC6CE8A143FCE9 |
| %         | root   | *7C695400AEECFFAD9251CB1CF2DC6CE8A143FCE9 |
| localhost | drupal | *7C695400AEECFFAD9251CB1CF2DC6CE8A143FCE9 |
+-----------+--------+-------------------------------------------+
3 rows in set (0.000 sec)
```