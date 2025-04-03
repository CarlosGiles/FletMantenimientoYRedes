# src/mantenimiento.py

import os
import shutil
import subprocess

def borrar_temp_windows():
    """
    Elimina archivos temporales en C:\\Windows\\Temp
    y recrea la carpeta para evitar errores.
    """
    temp_path = r"C:\Windows\Temp"
    shutil.rmtree(temp_path, ignore_errors=True)
    os.makedirs(temp_path, exist_ok=True)
    return "Archivos temporales de Windows eliminados."

def borrar_temp_local():
    """
    Elimina archivos temporales de %LOCALAPPDATA%\\Temp.
    """
    temp_path = os.path.join(os.environ["LOCALAPPDATA"], "Temp")
    shutil.rmtree(temp_path, ignore_errors=True)
    os.makedirs(temp_path, exist_ok=True)
    return "Archivos temporales locales eliminados."

def configurar_dhcp(interface="Wi-Fi"):
    """
    Configura la interfaz indicada para recibir IP dinámica
    y usa netsh para asignar DNS.
    """
    # Ajusta los nombres de interfaz si no son Wi-Fi o Ethernet
    subprocess.run(["netsh", "interface", "ip", "set", "address", f"name={interface}", "source=dhcp"])
    subprocess.run(["netsh", "interface", "ip", "set", "dns", f"name={interface}", "source=dhcp"])
    # Liberar y renovar la IP
    subprocess.run(["ipconfig", "/release"])
    subprocess.run(["ipconfig", "/renew"])
    # Mostrar config (opcional)
    subprocess.run(["ipconfig", "/all"])
    # Configurar DNS adicional (ej. 192.168.1.250) 
    subprocess.run(["netsh", "interface", "ip", "set", "dns", f"name={interface}", "static", "192.168.1.250"])
    return f"IP dinámica configurada correctamente en la interfaz '{interface}'."

def configurar_ip_estatica(interface, ip, mask, gateway, dns):
    """
    Configura la interfaz de red con IP estática.
    """
    subprocess.run(["netsh", "interface", "ip", "set", "address", f"name={interface}",
                    "static", ip, mask, gateway])
    subprocess.run(["netsh", "interface", "ip", "set", "dns", f"name={interface}",
                    "static", dns])
    return f"IP estática {ip} configurada correctamente en '{interface}'."

def vaciar_papelera():
    """
    Vacía la papelera de reciclaje usando PowerShell.
    """
    subprocess.run(["powershell", "-command", "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"])
    return "Papelera de reciclaje vaciada."
