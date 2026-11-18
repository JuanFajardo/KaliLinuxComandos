# Análisis Forense: Descompilación e Ingeniería Inversa

La descompilación y la ingeniería inversa son técnicas utilizadas durante el análisis forense para comprender el funcionamiento de una aplicación o ejecutable.

Su objetivo es identificar posibles mecanismos de comunicación, conexiones realizadas, funciones ejecutadas y acciones que pudo llevar a cabo un atacante mediante la aplicación. También permiten analizar posibles modificaciones, comportamientos sospechosos y mecanismos de persistencia.

## 🧩🔍 Descompiladores y frameworks de ingeniería inversa

**Ghidra**  
https://github.com/NationalSecurityAgency/ghidra

Framework de ingeniería inversa desarrollado por la NSA. Permite realizar desensamblado, descompilación y análisis estático de ejecutables. Es una alternativa gratuita a IDA Pro y admite extensiones mediante scripts y complementos.

**JADX**  
https://github.com/skylot/jadx

Herramienta con interfaz gráfica y línea de comandos que permite recuperar código Java legible a partir de archivos Android `.dex` y `.apk`. Muy útil para analizar aplicaciones Android.

**JavaDecompiler**  
https://java-decompiler.github.io/

Conjunto de herramientas que permite descompilar bytecode Java y recuperar código fuente legible a partir de archivos `.class` y aplicaciones Java.

**ILSpy**  
https://github.com/icsharpcode/ILSpy

Descompilador y explorador de assemblies .NET (C# / VB.NET). Permite inspeccionar ejecutables, recuperar código fuente y explorar metadatos.

**Delphi Decompiler**  
https://mega.nz/file/lUljQJhJ#HUsTyhf1YFMuGpJP4wWDtGU_-itQSTAu8KaRZPsztI0

Herramientas orientadas a recuperar código y procedimientos de ejecutables desarrollados en Delphi. El enlace compartido corresponde a una versión antigua que utilicé en proyectos anteriores; no he encontrado una fuente actualizada.

## 🐞🛠️ Depuradores (Debuggers)

**x64dbg**  
https://x64dbg.com/

Depurador de código abierto para Windows (x86/x64). Permite analizar la ejecución de programas, inspeccionar registros, memoria, instrucciones y establecer puntos de interrupción (*breakpoints*).

**WinDbg**  
https://learn.microsoft.com/en-us/windows-hardware/drivers/debuggercmds/windbg-overview

Depurador oficial de Microsoft para analizar aplicaciones y sistemas Windows, tanto en modo usuario (*user-mode*) como en modo kernel.

**GDB**  
https://www.sourceware.org/gdb/

Depurador de consola ampliamente utilizado en Linux y Unix. Permite analizar la ejecución de programas, inspeccionar memoria, registros y controlar procesos.

**EDB Debugger**  
https://github.com/eteran/edb-debugger

Depurador gráfico para Linux que permite inspeccionar instrucciones de ensamblador, memoria y registros, además de gestionar puntos de interrupción.

## 🗂️🔬 Análisis de binarios y formatos de archivos (PE / ELF / Firmware)

**PE.Tools**  
https://github.com/petoolse/petools

Conjunto de herramientas para inspeccionar y analizar archivos ejecutables de Windows en formato PE (*Portable Executable*).

**PEAnatomist**  
https://rammerlabs.alidml.ru/ru/

Herramienta para explorar la estructura interna de archivos PE, incluyendo encabezados, secciones, tablas de importación y exportación, y firmas.

**The elfutils project**  
https://sourceware.org/elfutils/

Conjunto de utilidades para analizar archivos ELF en Linux, incluyendo símbolos, información DWARF y estructuras internas de los binarios.

**Binwalk**  
https://github.com/ReFirmLabs/binwalk

Herramienta para analizar imágenes de firmware, identificar firmas, localizar sistemas de archivos y extraer datos embebidos. Es ampliamente utilizada en análisis de firmware y competiciones CTF.

## 📦🔓 Empaquetadores y herramientas de desempaquetado (Packers / Unpackers)

**UPX**  
https://upx.github.io/

Herramienta multiplataforma para comprimir y empaquetar ejecutables. También permite desempaquetarlos mediante el comando `upx -d`. Es útil durante el análisis de ejecutables comprimidos.

## 🕵️‍♂️🚫 Herramientas para análisis de técnicas Anti-Debugging

**ScyllaHide**  
https://github.com/x64dbg/ScyllaHide

Complemento para x64dbg que permite identificar y contrarrestar técnicas anti-debugging utilizadas por determinados programas para detectar la presencia de un depurador.

**HyperHide**  
https://github.com/Air14/HyperHide

Herramienta orientada a ocultar la presencia de determinados mecanismos de depuración y analizar técnicas de detección de depuradores.

**TitanHide**  
https://github.com/mrexodia/TitanHide

Herramienta para Windows que permite ocultar determinados indicadores de depuración frente a mecanismos anti-debugging.

## 🪟🧰 Suite de utilidades y herramientas para Windows

**Sysinternals Suite**  
https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite

Conjunto de utilidades oficiales de Microsoft para diagnóstico, monitoreo y análisis de sistemas Windows. Incluye herramientas como Process Explorer, ProcDump, Autoruns y Handle, muy útiles durante las primeras etapas de análisis forense (*triage*).