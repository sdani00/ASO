#!/usr/bin/env python3
import subprocess
import ipaddress


def scan_network(network="10.11.14.0/24"):
    active_hosts = []

    net = ipaddress.ip_network(network)

    print("Starting scan...")
    for ip in net.hosts():
        result = subprocess.run(['ping', '-c', '1', '-W', '1', str(ip)],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)

        if result.returncode == 0:
            print(f"Host found: {ip}")
            active_hosts.append(str(ip))

    return active_hosts


if __name__ == "__main__":
    active_hosts = scan_network()
    print("\nScan complete!")
    print("\nActive hosts:")
    for host in active_hosts:
        print(f"- {host}")
    print(f"\nTotal hosts found: {len(active_hosts)}")