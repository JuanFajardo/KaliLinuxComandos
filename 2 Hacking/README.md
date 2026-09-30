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