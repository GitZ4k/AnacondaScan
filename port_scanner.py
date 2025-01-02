import socket
import concurrent.futures as con
import colorama
import os
import platform
from colorama import Fore, Style
import time
import datetime
colorama.init(autoreset=True)

def anaconda():
    from rich import print
    banner = '\n\n' + fr'''[#01F9C6]                               /^\/^\
                             _|__|  O|
                    \/     /~     \_/ \
                     \____|__________/  \
                            \_______      \
                                    `\     \                 \
                                      |     |                  \
                                     /      /                    \
                                    /     /                       \\
                                  /      /                         \ \
                                 /     /                            \  \
                               /     /             _----_            \   \
                              /     /           _-~      ~-_         |   |
                             (      (        _-~    _--_    ~-_     _/   |
                              \      ~-____-~    _-~    ~-_    ~-_-~    /
                                ~-_           _-~          ~-_       _-~
                                   ~--______-~                ~-___-~
    ''' + '\n\n'
    delay = 0.035
    lines = banner.split('\n')
    for line in lines:
        print(f'[#01F9C6]{line}')
        time.sleep(delay)
def current_time():
    date = datetime.datetime.now().strftime('%H:%M:%S')
    return date

command = 'cls' if platform.system() == 'Windows' else 'clear'
os.system(command)
anaconda()

# COLORS

RED=Fore.RED
GREEN=Fore.GREEN
YELLOW=Fore.YELLOW
BLUE=Fore.BLUE
MAGENTA=Fore.MAGENTA
CYAN=Fore.CYAN
WHITE=Fore.WHITE
GREY=Fore.LIGHTBLACK_EX 

ip = input(f'{Style.BRIGHT}{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}>{MAGENTA}] | Ip {WHITE}-> ')
print(f'{Style.BRIGHT}{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}~{MAGENTA}] | Scanning...{CYAN} ')
def get_port_service(port):
    try:
        service = socket.getservbyport(port)
    except:
        service = 'Unknown'
    return service

def port_scanner(ip):
    open_ports = 0
    start = time.perf_counter()
    def main(ip, port):
        nonlocal open_ports
        sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sender.settimeout(1)
        try:
            result = sender.connect_ex((ip, port))
            if result == 0:
                open_ports += 1
                return f'{Style.BRIGHT}{MAGENTA}Port: {WHITE}{port} {MAGENTA}Status: {WHITE}Open {MAGENTA}Service: {WHITE}{get_port_service(port)}'
            return None
        except Exception as error:
            return f'{Style.BRIGHT}{RED}[{WHITE}{current_time()}{RED}] [{WHITE}>{RED}] | Error -> {error}'
    with con.ThreadPoolExecutor(max_workers=20) as exe:
        tasks = []
        for port in range(0,  65535):
            tasks.append(exe.submit(main, ip, port))
        for task in con.as_completed(tasks):
            if task.result():
                current_time()
                print(f'{Style.BRIGHT}{MAGENTA}[{WHITE}{current_time()}{MAGENTA}] [{WHITE}+{MAGENTA}] | {MAGENTA}{task.result()}')
    print(f'\n{Style.BRIGHT}{YELLOW}[{WHITE}{current_time()}{YELLOW}] [{WHITE}>{YELLOW}] | FINISHED -> {YELLOW}{f'Discovered {open_ports} ports!' if open_ports > 0 else 'No Ports Found'} finished scanning in {round(time.perf_counter()-start, 2)} seconds')
port_scanner(ip)