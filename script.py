import argparse
import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor
import dns.resolver
from colorama import Fore, Style, init

# Inicializa o Colorama para garantir compatibilidade em diferentes plataformas
init(autoreset=True)

def ping(host):
    """Executa o comando ping no sistema operacional para testar a conectividade."""
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

def smtp_check(ip):
    """Tenta abrir um socket no endereço IP no port 25 para testar a resposta SMTP."""
    try:
        server = socket.create_connection((ip, 25), timeout=10)
        server.close()
        return True
    except socket.error:
        return False

def test_mx_records(domain):
    """Testa os registros MX de um domínio."""
    results = []
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        with ThreadPoolExecutor(max_workers=4) as executor:
            futures = [executor.submit(test_single_mx_record, mx_record.exchange.to_text()) for mx_record in mx_records]
            results.extend(future.result() for future in futures)
    except Exception as e:
        print(Fore.RED + f"Error resolving MX records for {domain}: {str(e)}")
    return results

def test_single_mx_record(mx_record):
    """Testa um único registro MX (ping e SMTP)."""
    ip = socket.gethostbyname(mx_record)
    ping_result = ping(ip)
    smtp_result = smtp_check(ip)
    return (mx_record, ip, ping_result, smtp_result)

def print_results(results):
    """Imprime os resultados do teste de registros MX e DNS."""
    for mx_record, ip, ping_result, smtp_result in results:
        print(Fore.YELLOW + f"MX Record: {mx_record} ({ip})")
        if ping_result:
            print(Fore.GREEN + "✓ Ping: Successful")
        else:
            print(Fore.RED + "✗ Ping: Failed")
        
        if smtp_result:
            print(Fore.GREEN + "✓ SMTP check: Successful")
        else:
            print(Fore.RED + "✗ SMTP check: Failed")

def test_dns_records(domain):
    """Testa e exibe os registros DNS A e AAAA para o domínio."""
    try:
        a_records = dns.resolver.resolve(domain, 'A')
        for record in a_records:
            print(Fore.CYAN + f"A record: {record.to_text()}")
    except Exception as e:
        print(Fore.RED + f"Error resolving A records: {str(e)}")

    try:
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        for record in aaaa_records:
            print(Fore.CYAN + f"AAAA record: {record.to_text()}")
    except Exception as e:
        print(Fore.RED + f"Error resolving AAAA records: {str(e)}")

def main(args):
    if args.MX or args.ALL:
        print(Fore.CYAN + f"Testing MX Records for {args.domain}")
        mx_results = test_mx_records(args.domain)
        print_results(mx_results)

    if args.DNS or args.ALL:
        print(Fore.CYAN + f"Testing DNS Records for {args.domain}")
        test_dns_records(args.domain)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test DNS configurations for a domain")
    parser.add_argument('domain', type=str, help="The domain to test")
    parser.add_argument('-MX', action='store_true', help="Test only MX records")
    parser.add_argument('-DNS', action='store_true', help="Test only DNS records")
    parser.add_argument('-ALL', action='store_true', help="Test both MX and DNS records")
    args = parser.parse_args()

    main(args)
