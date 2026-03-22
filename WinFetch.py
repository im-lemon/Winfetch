import platform
import socket
import colorama
import wmi

import psutil
import ctypes
import random
colorama.init()
from colorama import Fore, Style
import os



print(
    Fore.BLUE + " ▄▄▄▄ " + Style.RESET_ALL + Fore.CYAN + " ▄▄▄▄ " + Style.RESET_ALL + "\n" +
    Fore.BLUE + "▄▀  ▀▄" + Style.RESET_ALL + Fore.CYAN + "▄▀  ▀▄" + Style.RESET_ALL + "\n" +
    Fore.YELLOW + "▄▀▄▄▄▀" + Style.RESET_ALL + Fore.GREEN + "▄▀▄▄▄▀" + Style.RESET_ALL
)

print()
def names():
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    hostname = socket.gethostname()
    print(Fore.BLUE + f"OS: {os_name} {os_release} {os_version}" + Style.RESET_ALL)
    print(Fore.BLUE + f"Hostname: {hostname}" + Style.RESET_ALL)
    print()

def ram_cpu_gpu():
    cpu = platform.processor()
    ram_bytes = psutil.virtual_memory().total
    ram_gb = round(ram_bytes / (1024*1024*1024), 1)
    gpu = wmi.WMI()
    c = gpu.Win32_VideoController()

    for g in c:
        gpu_name = g.Name
    cpu_usage = round(psutil.cpu_percent(), 1)
    print(Fore.LIGHTYELLOW_EX + f"RAM: {ram_gb} GB" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + f"CPU: {cpu}" + Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + f"CPU Usage: {cpu_usage}%" + Style.RESET_ALL)
    print()
    print(Fore.LIGHTYELLOW_EX + f"GPU: {gpu_name}" + Style.RESET_ALL)
    print()

def resolution():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    print(Fore.YELLOW + f"Resolution: {width}x{height}" + Style.RESET_ALL)
    print()

def shell():
    shell_path = os.environ.get("COMSPEC", "cmd.exe")
    shell_name = os.path.basename(shell_path)
    print(Fore.LIGHTMAGENTA_EX + f"Shell: {shell_name}" + Style.RESET_ALL)
message = ["HE HAS RAM GET HIM",
           "Nice specs dewd!",
           "Winfetch; Windows for Neofetch.. No wait it is the other way around!",
           "aujdhdlrjrklr",
           "Holy moly look at those specs!"
           "mmm... memory chips..."]
msg =random.choice(message)
print(Fore.YELLOW + f"{msg}" + Style.RESET_ALL)
print()



names()
ram_cpu_gpu()
resolution()
shell()