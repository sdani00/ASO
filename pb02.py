#!/usr/bin/env python3
import subprocess
import ipaddress


def scan_network(network="10.11.14.0/24"):
    active_hosts = []
    net = ipaddress.ip_network(network)
    print("Starting scan...")
    total_ips = len(list(net.hosts()))
    current = 0

    for ip in net.hosts():
        current += 1
        print(f"Scanning {ip} ({current}/{total_ips})")  # Debug line
        result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"Host found: {ip}")
            active_hosts.append(str(ip))
    print("Scan completed")  # Debug line
    return active_hosts


def main():
    print("Starting main")  # Debug line
    active_hosts = scan_network()
    print("\nActive hosts:")
    for host in active_hosts:
        print(f"- {host}")
    print(f"\nTotal hosts found: {len(active_hosts)}")
    print("Main completed")  # Debug line


if __name__ == "__main__":
    main()