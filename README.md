# Repositorio de Comandos Básicos para Kali Linux

## Índice

1. [Idioma](#1-idioma)

   * [Cambiar el idioma del teclado a español](#cambiar-el-idioma-del-teclado-a-español)
2. [Comandos de navegación](#2-comandos-de-navegación)

   * [Mostrar el directorio actual](#mostrar-el-directorio-actual)
   * [Crear archivos](#crear-archivos)
   * [Crear archivos con contenido](#crear-archivos-con-contenido)
   * [Visualizar archivos](#visualizar-archivos)
   * [Visualizar usuarios de Linux](#visualizar-usuarios-de-linux)
   * [Identificar el tipo de archivo](#identificar-el-tipo-de-archivo)
   * [Listar directorios](#listar-directorios)
   * [Listar directorios en formato detallado](#listar-directorios-en-formato-detallado)
   * [Crear carpetas](#crear-carpetas)
   * [Ingresar a una carpeta](#ingresar-a-una-carpeta)
   * [Salir de una carpeta](#salir-de-una-carpeta)
   * [Ir a la raíz](#ir-a-la-raíz)
   * [Ir al directorio principal](#ir-al-directorio-principal)
   * [Ejercicio](#ejercicio-de-comandos-de-navegación)
3. [Comandos de red](#3-comandos-de-red)

   * [Visualizar la IP con ifconfig](#visualizar-la-ip-con-ifconfig)
   * [Visualizar la IP con ip](#visualizar-la-ip-con-ip)
   * [Visualizar servidores DNS](#visualizar-servidores-dns)
   * [Asignar servidores DNS](#asignar-servidores-dns)
   * [Visualizar configuración de red](#visualizar-configuración-de-red)
   * [Asignar una IP estática](#asignar-una-ip-estática)
4. [Instalación de paquetes](#4-instalación-de-paquetes)

   * [Actualizar repositorios](#actualizar-repositorios)
   * [Buscar paquetes](#buscar-paquetes)
   * [Buscar paquetes por palabra inicial](#buscar-paquetes-por-palabra-inicial)
   * [Instalar paquetes](#instalar-paquetes)
   * [Desinstalar paquetes](#desinstalar-paquetes)
   * [Ejercicio: buscar e instalar SuperTux](#ejercicio-buscar-e-instalar-supertux)
5. [Administración de servicios](#5-administración-de-servicios)
---

# 1. Idioma

## Cambiar el idioma del teclado a español

Para configurar el teclado en español:

```bash
setxkbmap es
```

### Resultado esperado

```text
$ setxkbmap es
```

El comando normalmente no muestra ningún mensaje si se ejecuta correctamente.

Para comprobar la configuración:

```bash
setxkbmap -query
```

### Resultado esperado

```text
rules:      evdev
model:      pc105
layout:     es
```

---

# 2. Comandos de navegación

## Mostrar el directorio actual

El comando `pwd` permite conocer la ubicación actual dentro del sistema de archivos.

```bash
pwd
```

### Resultado de ejemplo

```text
/home/kali
```

---

## Crear archivos

El comando `touch` permite crear un archivo vacío.

```bash
touch archivo.txt
```

### Resultado

El archivo será creado:

```text
archivo.txt
```

Podemos comprobarlo con:

```bash
ls
```

### Resultado de ejemplo

```text
archivo.txt
```

---

## Crear archivos con contenido

Podemos utilizar `echo` para mostrar texto:

```bash
echo "Hola mundo"
```

### Resultado

```text
Hola mundo
```

También podemos guardar el contenido en un archivo:

```bash
echo "Hola mundo" > archivo.txt
```

Visualizamos el contenido:

```bash
cat archivo.txt
```

### Resultado

```text
Hola mundo
```

> El operador `>` crea el archivo si no existe y reemplaza su contenido si ya existe.

---

## Visualizar archivos

El comando `cat` permite visualizar el contenido de un archivo.

```bash
cat archivo.txt
```

### Resultado

```text
Hola mundo
```

---

## Visualizar usuarios de Linux

Los usuarios registrados en Linux pueden consultarse en `/etc/passwd`.

```bash
cat /etc/passwd
```

### Resultado de ejemplo

```text
root:x:0:0:root:/root:/usr/bin/zsh
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
kali:x:1000:1000:Kali,,,:/home/kali:/usr/bin/zsh
```

Cada línea corresponde a un usuario o cuenta del sistema.

---

## Identificar el tipo de archivo

El comando `file` permite identificar qué tipo de archivo tenemos.

```bash
file archivo.txt
```

### Resultado

```text
archivo.txt: ASCII text
```

---

## Listar directorios

El comando `ls` permite visualizar los archivos y carpetas del directorio actual.

```bash
ls
```

### Resultado de ejemplo

```text
archivo.txt
Documentos
Descargas
Imágenes
```

---

## Listar directorios en formato detallado

La opción `-l` muestra información adicional:

```bash
ls -l
```

### Resultado de ejemplo

```text
total 8
-rw-r--r-- 1 kali kali   11 Aug  9 22:30 archivo.txt
drwxr-xr-x 2 kali kali 4096 Aug  9 22:30 Documentos
drwxr-xr-x 2 kali kali 4096 Aug  9 22:30 Descargas
```

La información incluye permisos, propietario, grupo, tamaño y fecha de modificación.

---

## Crear carpetas

El comando `mkdir` permite crear directorios.

```bash
mkdir practica
```

### Resultado

Normalmente no se muestra ningún mensaje.

Podemos comprobar que se creó:

```bash
ls
```

### Resultado de ejemplo

```text
archivo.txt
Documentos
Descargas
practica
```

---

## Ingresar a una carpeta

Utilizamos `cd` para cambiar de directorio.

```bash
cd practica
```

Podemos comprobar nuestra ubicación:

```bash
pwd
```

### Resultado

```text
/home/kali/practica
```

---

## Salir de una carpeta

Para regresar al directorio anterior:

```bash
cd ..
```

### Resultado

```text
/home/kali
```

---

## Ir a la raíz

El directorio raíz de Linux se representa mediante `/`.

```bash
cd /
```

Comprobamos:

```bash
pwd
```

### Resultado

```text
/
```

---

## Ir al directorio principal

Para ir directamente al directorio personal del usuario:

```bash
cd ~
```

También podemos utilizar:

```bash
cd
```

### Resultado de ejemplo

```text
/home/kali
```

---

# Ejercicio de comandos de navegación

### Objetivo

Practicar los comandos básicos de navegación y manipulación de archivos.

### Actividades

1. Crear una carpeta llamada `practica`.
2. Ingresar a la carpeta.
3. Crear un archivo llamado `datos.txt`.
4. Escribir `Hola Kali Linux` dentro del archivo.
5. Visualizar el contenido del archivo.
6. Mostrar el tipo de archivo.
7. Mostrar el directorio actual.
8. Regresar al directorio anterior.
9. Listar el contenido utilizando `ls -l`.

### Comandos esperados

```bash
mkdir practica
cd practica
echo "Hola Kali Linux" > datos.txt
cat datos.txt
file datos.txt
pwd
cd ..
ls -l
```

---

# 3. Comandos de red

## Visualizar la IP con ifconfig

`ifconfig` es una herramienta tradicional para visualizar la configuración de las interfaces de red.

```bash
ifconfig
```

### Resultado de ejemplo

```text
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>
        inet 192.168.1.10
        netmask 255.255.255.0
        broadcast 192.168.1.255
```

> En sistemas modernos se recomienda utilizar `ip`, ya que `ifconfig` pertenece a herramientas consideradas tradicionales.

---

## Visualizar la IP con ip

Para visualizar las direcciones IPv4:

```bash
ip -4 addr
```

También puede utilizarse:

```bash
ip -4 a
```

### Resultado de ejemplo

```text
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP>
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
```

---

## Visualizar servidores DNS

Los servidores DNS configurados pueden consultarse mediante:

```bash
cat /etc/resolv.conf
```

### Resultado de ejemplo

```text
nameserver 192.168.1.1
```

En algunos sistemas puede aparecer:

```text
nameserver 1.1.1.1
nameserver 8.8.8.8
```

---

## Asignar servidores DNS

En determinados entornos puede editarse el archivo:

```bash
sudo mousepad /etc/resolv.conf
```

Por ejemplo:

```text
nameserver 1.1.1.1
nameserver 8.8.8.8
```

También se puede consultar el archivo con:

```bash
cat /etc/resolv.conf
```

### Resultado

```text
nameserver 1.1.1.1
nameserver 8.8.8.8
```

> En Kali Linux moderno, `/etc/resolv.conf` puede ser administrado automáticamente por NetworkManager o systemd-resolved. Por ello, los cambios manuales pueden no permanecer después de reiniciar o cambiar de red.

---

## Visualizar configuración de red

El archivo tradicional de configuración de interfaces es:

```bash
cat /etc/network/interfaces
```

### Resultado de ejemplo

```text
auto lo
iface lo inet loopback
```

> En instalaciones modernas de Kali Linux, NetworkManager suele encargarse de la configuración de red, por lo que este archivo puede no contener la configuración de las interfaces.

---

## Asignar una IP estática

Una configuración tradicional podría tener la siguiente estructura:

```text
auto eth0
iface eth0 inet static
    address 192.168.1.10
    netmask 255.255.255.0
    gateway 192.168.1.1
```

El archivo podría editarse mediante:

```bash
sudo mousepad /etc/network/interfaces
```

Después de realizar cambios, la forma de aplicar la configuración dependerá del sistema de administración de red utilizado.

### Comprobar la configuración

```bash
ip -4 addr
```

### Resultado de ejemplo

```text
inet 192.168.1.10/24
```

---

# 4. Instalación de paquetes

Kali Linux utiliza `apt` para administrar paquetes.

## Actualizar repositorios

Para actualizar la información de los paquetes disponibles:

```bash
sudo apt update
```

### Resultado de ejemplo

```text
Hit:1 http://http.kali.org/kali kali-rolling InRelease
Reading package lists... Done
```

---

## Buscar paquetes

Para buscar un paquete:

```bash
apt search nombre
```

Por ejemplo:

```bash
apt search supertux
```

### Resultado de ejemplo

```text
Sorting... Done
Full Text Search... Done
supertux/kali-rolling 0.6.x amd64
  Classic 2D jump'n run game
```

---

## Buscar paquetes por palabra inicial

El símbolo `^` permite buscar paquetes cuyo nombre comienza con un determinado texto.

Por ejemplo:

```bash
apt search ^super
```

Esto permite encontrar paquetes cuyo nombre comienza con `super`.

### Resultado de ejemplo

```text
supertux/kali-rolling ...
supertuxkart/kali-rolling ...
```

---

## Instalar paquetes

Para instalar un paquete:

```bash
sudo apt install nombre-del-paquete
```

Ejemplo:

```bash
sudo apt install supertux
```

Durante la instalación, `apt` mostrará los paquetes que serán instalados y solicitará confirmación.

### Resultado de ejemplo

```text
Do you want to continue? [Y/n]
```

Introducir:

```text
Y
```

---

## Desinstalar paquetes

Para eliminar un paquete:

```bash
sudo apt remove nombre-del-paquete
```

Ejemplo:

```bash
sudo apt remove supertux
```

### Resultado de ejemplo

```text
The following packages will be REMOVED:
  supertux

Do you want to continue? [Y/n]
```

---

# Ejercicio: buscar e instalar SuperTux

### Objetivo

Utilizar `apt` para buscar e instalar un programa.

### Actividades

1. Actualizar la información de los repositorios.
2. Buscar el paquete `supertux`.
3. Buscar paquetes cuyo nombre comience con `super`.
4. Instalar `supertux`.
4. Instalar `terminator`.


### Comandos

```bash
sudo apt update

apt search supertux

apt search ^super

sudo apt install supertux

supertux

sudo apt remove supertux
```

# 5. Administración de servicios

Los servicios son programas que se ejecutan en segundo plano y proporcionan diferentes funciones al sistema. En Kali Linux, muchos servicios pueden administrarse mediante `systemctl`, que forma parte de `systemd`.

---

## 5.1 Ver el estado de un servicio

Para consultar el estado de un servicio:

```bash
systemctl status nombre-servicio
```

Por ejemplo:

```bash
systemctl status ssh
```

### Resultado de ejemplo

```text
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded
     Active: active (running)
```

Los estados más importantes son:

* `active (running)` → el servicio está ejecutándose.
* `inactive (dead)` → el servicio está detenido.
* `failed` → el servicio intentó iniciar pero ocurrió un error.
* `enabled` → está configurado para iniciar automáticamente.

---

## 5.2 Iniciar un servicio

El comando `start` inicia un servicio inmediatamente.

```bash
sudo systemctl start nombre-servicio
```

Ejemplo:

```bash
sudo systemctl start ssh
```

### Comprobar

```bash
systemctl status ssh
```

---

## 5.3 Detener un servicio

El comando `stop` detiene un servicio que está ejecutándose.

```bash
sudo systemctl stop nombre-servicio
```

Ejemplo:

```bash
sudo systemctl stop ssh
```

### Comprobar

```bash
systemctl status ssh
```

---

## 5.4 Reiniciar un servicio

El comando `restart` detiene y vuelve a iniciar el servicio.

```bash
sudo systemctl restart nombre-servicio
```

Ejemplo:

```bash
sudo systemctl restart ssh
```

Es especialmente útil después de modificar la configuración de un servicio.

---

## 5.5 Habilitar un servicio al iniciar Kali

El comando `enable` configura el servicio para que se inicie automáticamente durante el arranque del sistema.

```bash
sudo systemctl enable nombre-servicio
```

Ejemplo:

```bash
sudo systemctl enable ssh
```

### Importante

`enable` **no necesariamente inicia el servicio inmediatamente**.

Si queremos habilitarlo y además iniciarlo ahora:

```bash
sudo systemctl enable --now ssh
```

---

## 5.6 Deshabilitar un servicio

Para evitar que un servicio se inicie automáticamente:

```bash
sudo systemctl disable nombre-servicio
```

Ejemplo:

```bash
sudo systemctl disable ssh
```

---

## 5.7 Ver todos los servicios

Para mostrar los servicios conocidos por `systemd`:

```bash
systemctl list-unit-files --type=service
```

Para mostrar solamente los servicios que están ejecutándose:

```bash
systemctl list-units --type=service --state=running
```

---

## 5.8 Buscar un servicio

Podemos utilizar `grep` para buscar un servicio específico.

Por ejemplo:

```bash
systemctl list-unit-files --type=service | grep ssh
```

Resultado de ejemplo:

```text
ssh.service    enabled
```

---

# 5.9 Lista de servicios que podemos encontrar en Kali Linux

La lista exacta depende de los paquetes instalados. Algunos servicios comunes o que pueden instalarse en Kali Linux son:

| Servicio       | Unidad                   | Función                                |
| -------------- | ------------------------ | -------------------------------------- |
| OpenSSH        | `ssh.service`            | Acceso remoto mediante SSH             |
| Apache         | `apache2.service`        | Servidor web                           |
| MariaDB        | `mariadb.service`        | Servidor de base de datos              |
| PostgreSQL     | `postgresql.service`     | Servidor de base de datos              |
| NetworkManager | `NetworkManager.service` | Administración de conexiones de red    |
| Tor            | `tor.service`            | Servicio de red Tor, si está instalado |


> **Nota:** algunos de estos servicios no vienen instalados por defecto en Kali Linux. Aparecerán después de instalar el paquete correspondiente.

---

# 5.10 Ejemplo completo con SSH

Podemos practicar las operaciones básicas utilizando `ssh`.

### Verificar si está instalado

```bash
systemctl status ssh
```

### Iniciar

```bash
sudo systemctl start ssh
```

### Detener

```bash
sudo systemctl stop ssh
```

### Reiniciar

```bash
sudo systemctl restart ssh
```

### Habilitar al iniciar el sistema

```bash
sudo systemctl enable ssh
```

### Habilitar e iniciar inmediatamente

```bash
sudo systemctl enable --now ssh
```

### Deshabilitar el inicio automático

```bash
sudo systemctl disable ssh
```

---

# 5.11 Comandos principales de `systemctl`

| Comando                                               | Función                            |
| ----------------------------------------------------- | ---------------------------------- |
| `systemctl status servicio`                           | Consultar estado                   |
| `systemctl start servicio`                            | Iniciar                            |
| `systemctl stop servicio`                             | Detener                            |
| `systemctl restart servicio`                          | Reiniciar                          |
| `systemctl enable servicio`                           | Activar inicio automático          |
| `systemctl disable servicio`                          | Desactivar inicio automático       |
---

# Ejercicio: Administración de servicios

### Objetivo

Aprender a consultar, iniciar, detener, reiniciar y habilitar servicios en Kali Linux.

### Actividades

1. Mostrar los servicios disponibles.
2. Buscar el servicio `apache2`.
3. Consultar su estado.
4. Iniciar el servicio.
5. Comprobar que está ejecutándose.
6. Reiniciar el servicio.
7. Habilitarlo para que inicie automáticamente.
8. Comprobar si está habilitado.
9. Detener el servicio.
10. Volver a iniciarlo.

### Comandos

```bash
systemctl status apache2

sudo systemctl start apache2

systemctl status apache2

sudo systemctl restart apache2

firefox http://127.0.0.1

```

---

## Nota para estudiantes

Los resultados mostrados en este documento son **ejemplos**. La salida real puede variar dependiendo de la versión de Kali Linux, el usuario, las interfaces de red, la dirección IP y los paquetes instalados en cada equipo.
