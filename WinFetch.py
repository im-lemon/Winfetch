import platform
import socket
import colorama
import wmi
import argparse
import time
import getpass

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
    username = getpass.getuser()
    print(color(f"OS: {os_name} {os_release} {os_version}", Fore.BLUE))
    print(color(f"Hostname: {hostname}", Fore.BLUE))
    print(color(f"USERNAME: {username}:", Fore.BLUE))
    print()

def ram_cpu_gpu():
    cpu = platform.processor()
    ram_bytes = psutil.virtual_memory().total
    ram_gb = round(ram_bytes / (1024*1024*1024), 1)
    gpu = wmi.WMI()
    c = gpu.Win32_VideoController()
    all_partitions = psutil.disk_partitions()
    for partition in all_partitions:
        if "C:" in partition.device or "c:" in partition.device:
            mountpoint = partition.device
        else:
            print(color(f"Disk: Unknown", Fore.LIGHTYELLOW_EX))
            break
        disk_usage = psutil.disk_usage(partition.mountpoint)
        total_gb = disk_usage.total / (1024**3)
        total_gb = round(total_gb, 1)
        used_gb = disk_usage.used / (1024**3)
        used_gb = round(used_gb, 1)
        percent = disk_usage.percent

        boot_time = psutil.boot_time()
        current_time = time.time()

        uptime_seconds = int(current_time - boot_time)
        uptime_days = uptime_seconds // 86400
        uptime_hours = (uptime_seconds % 86400) // 3600
        uptime_minutes = (uptime_seconds % 3600) // 60
        uptime_seconds = uptime_seconds % 60


    gpu_name = c[0].Name if c else "Unknown"
    cpu_usage = round(psutil.cpu_percent(), 1)
    print(color(f"RAM: {ram_gb} GB", Fore.LIGHTYELLOW_EX))
    print(color(f"CPU: {cpu}", Fore.LIGHTYELLOW_EX))
    print(color(f"CPU Usage: {cpu_usage}%", Fore.LIGHTYELLOW_EX))
    print()
    print(color(f"GPU: {gpu_name}", Fore.LIGHTYELLOW_EX))
    print(color(f"Disk: {mountpoint} (total: {total_gb}) (used: {used_gb}) (percent: {percent})", Fore.LIGHTYELLOW_EX))
    print()
    print(color(f"Uptime: {uptime_days}d, {uptime_hours}h, {uptime_minutes}m, {uptime_seconds}s", Fore.LIGHTRED_EX))

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