# Verify-FTP_Anonymous

Este script de Python  verificar de forma automatizada la existencia de servidores FTP que permiten la conexión anónima (anonymous) sin necesidad de ingresar credenciales de autenticación.

El script utiliza una lista de direcciones IP como entrada y realiza la verificación de manera secuencial, generando una salida en la terminal que indica si el servidor FTP en cada dirección IP especificada tiene activada la opción de conexión anónima.

## **Uso:**

Para ejecutar el script, es necesario tener instalado Python 3 en el equipo. Una vez instalado, se puede ejecutar el script mediante el comando:

[+] python3 anonftp.py <archivo_de_ips.txt>
