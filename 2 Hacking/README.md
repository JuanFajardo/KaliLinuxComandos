## Tema 1 
```bash
 site:bo filetype:sql
 
 http://181.188.137.135/caub/publico/buscar_consultora.php
```

- Seguridad ofensiva.
- Metodologias
    - [OWASP](https://owasp.org/www-project-top-ten/)
    - [MITRE ATT&CK ](https://attack.mitre.org/)
    - [ISECOM–OSSTMM](https://www.isecom.org/OSSTMM.3.pdf).
- Certificaciones de ciberseguridad.
- CEH y Ethical Hacking.
- Proceso de Pentesting.
- Análisis de vulnerabilidades, 
    - [CVE](https://nvd.nist.gov/vuln/search?resultType=records) 
    - [CWE](https://cwe.mitre.org/)
    - [CVSS](https://chandanbn.github.io/cvss/)
- Documentación y evidencias.
- Informes técnicos y ejecutivos.




## Tema 2
- [Footprinting](https://elhacker.info/manuales/Auditorias%20Web/La_Biblia_del_Footprinting.pdf)
- https://shorturl.at/8Qjby


## Tema 3
- https://nmap.org/book/
- https://ffuf.me/

__Testeo:__
- scanme.nmap.com
- nmap insecure.org
- zonetransfer.me


## Tema 4

Zona de transferencia en DNS

https://shorturl.at/seAMJ

https://digi.ninja/projects/zonetransferme.php


__Testeo:__
- scanme.nmap.com
- nmap insecure.org
- zonetransfer.me


## Tema 5

Fuerza Bruta
https://drive.google.com/file/d/1V5DqnANstfQpTV1gYZcJ0ZJw39KKoqM5/view
https://www.kali.org/tools/medusa/
https://github-com.translate.goog/danielmiessler/seclists?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

```python
import itertools
import string
letras = string.ascii_lowercase
combinaciones = itertools.product(letras, repeat=3)
diccionario_3_letras = { "".join(comb): 0 for comb in combinaciones }
print(f"Total de claves generadas: {len(diccionario_3_letras)}")
print("Ejemplo de las primeras claves:")
for k in list(diccionario_3_letras.keys())[:10]:
    print(k)
```
https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm

__Testeo:__
- ssh
- ftp
- diccioanrios
- medusa



## Tema 5

https://drive.google.com/drive/folders/1Z8HqFSIjrxVBJdZL2yZ1OtDkVScr-WrW?usp=drive_link


## Critpgrafia
Morse
....- -../..... .-/..... --.../....- --.../....- ...--/..... .-/...-- ...--/...-- ...--/....- ----./..... .-/..... .----/..... --.../....- --.../...-- ...../....- -.-./....- -../....- ..-./..... ..---/..... .----/..... --.../....- ----./..... ---../...-- ..---/....- -./....- ./..... .-/..... ....-/..... --.../....- -.../...-- ...--/..... ....-/....- -./....- -../..... -..../..... .-/....- ..-./...-- ..---/..... ----./....- -.../...-- --.../....- -.../..... ..---/..... ...--/..... --.../....- --.../...-- ...--/..... ....-/..... -----/....- ./..... ..---/..... ---../..... --.../..... -----/...-- ...--/....- -.-./....- ..---/....- -.-./...-- ...../....- -.../..... ...../....- ...--/..... ...../....- ....-/...-- ...../....- ...../....- .----/...-- -../...-- -../...-- -../...-- -../...-- -../...-- -..

bcrypt
$2a$04$2b44V2F3.A244V2F3.A24u3Kk3d6I5L1k3N5O7P9Q1R3S5T7U9V1W
SHA-512
$6$saltejemplo$9K3Xj5vQ0L1mN2oP3qR4sT5uV6wX7yZ8aB9cC0dE1fG2hI3jK4lM5nO6pQ7rS8tU9vW0xY1z2A3B4C5D6E7F8

Vim
VmltQ3J5cHR+MDMhtRLEsyMCOq24rFaFJoCNPgDslSjPlsR2f2WLboitnlzdmWCEzLcddQ==

RaR
UmFyIRoHAQAzkrXlCgEFBgAFAQGAgAAtDY/nWAIDPKAABJAAIJW/ENeAAwALY2lmcmFkby50eHQwAQADD1iXbc8JAml1zTmNZzLNv9mbCE34cDIBbXEVXekgA8X7uY1eJtbT6Q7MNjsDCgMC990PT/hU3QGWLTAiJrYqR8utAUXlwOyBJw1qz6mxnW6Y7l4+Ys6Nqh13VlEDBQQA

Red
iVBORw0KGgoAAAANSUhEUgAAAFkAAAAXCAYAAABgWeOzAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAIqSURBVGhD7ZSBjeIwEEXTC8VQC6VQCYVQB7Vw+oiH3vnGZMMmXmkvX5qFdcb2/DcTpvuuzbVDHqAd8gD9BXmapldcLpf78Xh8fD8cDs+M36t4xPv5fH5Evp9Op2fG53pB5gJiFGTuWMPMpzLgRAB77Z3CaS7v8eR6vb4SswltDZlpyedP6Xa7vby7jmqSnWvBL7wqPbLdjWxAW0OOgZzvxo5Wb8AqAT5hAb/HacJoG9lYQfZrRLgxkQtPuInVm+I18jxBVR2sOXyOgXgCE0yscxypv72z8s2z3oSjxZDbPALQBlpFBdlNIm8OcmU6wfk9gETy1oIcsVbp2z8XXM50uBjkRhoyuWkoIm8Ocity2GeA1BaxlvwoflmrBsB3+sxWlRe0GDJrbWCO/23MrxNGekWRNwfZjXMArweEfZy1FuSo6yl/vgrZxlpYSyFH7LXIewfZZrmHnJ+CTP63J5n/MWZ4QAGci6uaE3Ge76z2s5c1znMjyMmZkYFwZ1Xvp5D/mdbneqVFkA2LAApFu5AqKiNeq+4gqKO6gzoqyFUAaQlkc/IzN6/SIsgReeRizlPVGrSR6nybiziTZ1UdvZx8Rq6hheMpXAI58hDw7EuQt5ZNGjIF29xaMuT21V5bQG4bglaHHGCG5i63RQA/QNbWSMi8DX6brU0gY64NTzFimnsFfqpRkPHbm+Jodcj+jSPeFbCVRk7ynIb8Jv/v2iEP0A55gHbIm+t+/wPfLjX2DYJL3wAAAABJRU5ErkJggg==


# Práctica: Identificación y recuperación de contraseña de un archivo ZIP

## Objetivo

Convertir un archivo de texto codificado en **Base64** a un archivo `.zip`, verificar que la conversión sea correcta, identificar el tipo de cifrado utilizado y recuperar la contraseña mediante **John the Ripper**.

---

## 1. Convertir el archivo Base64 a ZIP

Descargue el archivo **`[CI].zip.txt`** y colóquelo dentro del directorio `zip/`.

Convierta el contenido codificado en Base64 en un archivo `.zip`:

```bash
echo "TEXTO" | base64 -d > [CI].zip
```

> Reemplace `TEXTO` por el contenido correspondiente del archivo.

---

## 2. Verificar el tipo de archivo

Utilice el comando `file` para comprobar que la conversión se realizó correctamente:

```bash
file [CI].zip
```

El comando debe identificar el archivo como un archivo ZIP.

Si el resultado muestra únicamente **`data`**, significa que la conversión no se realizó correctamente y debe revisarse el proceso de decodificación.

---

## 3. Generar el diccionario de contraseñas

La contraseña del archivo ZIP es numérica y se encuentra dentro del rango de **1000 a 10000**.

Genere un diccionario denominado:

```text
numeros.txt
```

Este archivo debe contener los posibles valores numéricos que serán utilizados para realizar la recuperación de la contraseña.

---

## 4. Extraer el hash del archivo ZIP

Utilice la herramienta correspondiente de **John the Ripper** para extraer la información necesaria del archivo comprimido.

> Si se utilizara `rar2john` para archivos `.RAR`, para un archivo `.ZIP` debe utilizarse la herramienta correspondiente para ZIP.

El resultado deberá guardarse en:

```text
zip.txt
```

Por ejemplo, el archivo `zip.txt` contendrá la información extraída necesaria para que John the Ripper pueda realizar el ataque de diccionario.

---

## 5. Identificar el tipo de cifrado

Una vez obtenido el hash, consulte el identificador de hashes:

[https://hashes.com/en/tools/hash_identifier](https://hashes.com/en/tools/hash_identifier)

Utilice esta herramienta para determinar qué tipo de cifrado o formato corresponde al hash obtenido del archivo ZIP.

---

## 6. Consultar los formatos disponibles en John the Ripper

Consulte los formatos soportados por John the Ripper:

```bash
john --list=formats
```

Identifique el formato correspondiente al hash del archivo ZIP.

---

## 7. Recuperar la contraseña

Utilice John the Ripper con el diccionario `numeros.txt`:

```bash
john --format=????? --wordlist=numeros.txt zip.txt
```

Reemplace `?????` por el formato identificado en el paso anterior.

### Archivos utilizados

| Archivo        | Descripción                                                               |
| -------------- | ------------------------------------------------------------------------- |
| `[CI].zip.txt` | Archivo original con el contenido codificado en Base64.                   |
| `[CI].zip`     | Archivo ZIP obtenido después de la decodificación.                        |
| `numeros.txt`  | Diccionario con las posibles contraseñas numéricas.                       |
| `zip.txt`      | Información extraída del archivo ZIP para utilizarla con John the Ripper. |

---

## 8. Verificar la contraseña

Una vez recuperada la contraseña, utilícela para abrir el archivo `[CI].zip` y comprobar que permite acceder correctamente a su contenido.

---

## 9. Entrega

Una vez completada la práctica, **envíe el contenido del archivo comprimido al grupo de WhatsApp**, según las indicaciones del docente.
