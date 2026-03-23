import platform
import socket
import colorama
import wmi
import argparse

import psutil
import ctypes
import random
colorama.init(autoreset=True)
from colorama import Fore, Style
import os

parser = argparse.ArgumentParser(description="Winfetch CLI tool")
parser.add_argument("--nocolor", "--nocolour", action="store_true", dest="nocolor", help="Disable all colours")
args = parser.parse_args()

def color(text, color_code):
    if args.nocolor:
        return text
    return color_code + text + Style.RESET_ALL

print()
ascii_art = (
    color(" ▄▄▄▄ ", Fore.BLUE) + color(" ▄▄▄▄\n", Fore.CYAN) +
    color("▄▀  ▀▄", Fore.BLUE) + color("▄▀  ▀▄\n", Fore.CYAN) +
    color("▄▀▄▄▄▀", Fore.YELLOW) + color("▄▀▄▄▄▀", Fore.GREEN)
)
print(ascii_art)
print()
message = ["HE HAS RAM GET HIM",
           "Nice specs dewd!",
           "Winfetch; Windows for Neofetch.. No wait it's the other way around!",
           "aujdhdlrjrklr",
           "Holy moly look at those specs!",
           "mmm... memory chips...",
           "I use Windows btw"]

msg =random.choice(message)
print(color(msg, Fore.YELLOW))

print()
def names():
    os_name = platform.system()
    os_release = platform.release()
    os_version = platform.version()
    hostname = socket.gethostname()
    print(color(f"OS: {os_name} {os_release} {os_version}", Fore.BLUE))
    print(color(f"Hostname: {hostname}", Fore.BLUE))
    print()

def ram_cpu_gpu():
    cpu = platform.processor()
    ram_bytes = psutil.virtual_memory().total
    ram_gb = round(ram_bytes / (1024*1024*1024), 1)
    gpu = wmi.WMI()
    c = gpu.Win32_VideoController()
    disk_part = psutil.disk_partitions()

    gpu_name = c[0].Name if c else "Unknown"
    cpu_usage = round(psutil.cpu_percent(), 1)
    print(color(f"RAM: {ram_gb} GB", Fore.LIGHTYELLOW_EX))
    print(color(f"CPU: {cpu}", Fore.LIGHTYELLOW_EX))
    print(color(f"CPU Usage: {cpu_usage}%", Fore.LIGHTYELLOW_EX))
    print()
    print(color(f"GPU: {gpu_name}", Fore.LIGHTYELLOW_EX))
    print(color(f"DISK PARTITIONS: {disk_part}", Fore.LIGHTYELLOW_EX))
    print()

def resolution():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)
    print(color(f"Resolution: {width}x{height}", Fore.YELLOW))
    print()

def shell():
    shell_path = os.environ.get("COMSPEC", "cmd.exe")
    shell_name = os.path.basename(shell_path)
    print(color(f"Shell: {shell_name}", Fore.LIGHTMAGENTA_EX))





names()
ram_cpu_gpu()
resolution()
shell()