#!/usr/bin/env python3
import subprocess
import ipaddress
from multiprocessing import Pool


def ping_ip(ip):
    result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        return str(ip)
    return None


def scan_network(network="10.11.14.0/24"):
    print("Starting scan...")
    net = ipaddress.ip_network(network)
    ip_list = list(net.hosts())

    # Use half of available CPU cores for parallel processing
    with Pool(processes=8) as pool:
        results = pool.map(ping_ip, ip_list)

    # Filter out None values (non-responding hosts)
    active_hosts = [ip for ip in results if ip is not None]
    return active_hosts


def main():
    active_hosts = scan_network()
    print("\nActive hosts:")
    for host in sorted(active_hosts):  # Sort IPs for cleaner output
        print(f"- {host}")
    print(f"\nTotal hosts found: {len(active_hosts)}")


if __name__ == "__main__":
    main()