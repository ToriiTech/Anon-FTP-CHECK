import ftplib
import sys
import signal
import time
import os

# Función para imprimir en color
def print_color(message, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "purple": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m"
    }
    reset_color = "\033[0m"
    print(f"{colors[color]}{message}{reset_color}")

# Función para manejar la interrupción de Ctrl+C
def signal_handler(sig, frame):
    print_color("\n¡Interrupción de teclado detectada! Saliendo...", "yellow")
    sys.exit(0)

# Verificamos que se haya proporcionado un archivo de IPs
if len(sys.argv) < 2:
    print_color("Por favor proporcione el nombre del archivo de IPs como argumento", "red")
    print_color("Ejemplo: python3 anonftp.py ips.txt", "red")
    sys.exit(1)

# Abrimos el archivo de IPs y lo leemos línea por línea
with open(sys.argv[1]) as file:
    ips = file.readlines()

# Eliminamos los saltos de línea de cada dirección IP
ips = [ip.strip() for ip in ips]

# Establecemos el tiempo de espera para cada intento de conexión
timeout = 5

# Realizamos la conexión a cada dirección IP y verificamos si el servicio FTP acepta conexiones anónimas
for ip in ips:
    try:
        ftp = ftplib.FTP(ip, timeout=timeout)
        ftp.login('anonymous', '')
        print_color(f"[-] FTP anónimo activo en {ip}", "red")
        ftp.quit()
    except ftplib.all_errors:
        print_color(f"[+] No se pudo establecer conexión FTP anónima en {ip}", "green")

    # Añadimos una pausa de medio segundo para no saturar las conexiones
    time.sleep(0.5)
    
# Establecemos el manejador de señales para detectar la interrupción de Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Mantenemos el script en ejecución para poder detectar la interrupción de teclado
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
