#!/usr/bin/env python3
import subprocess

def scan_network():
    active_hosts = []
    # Explicitly scan from .1 to .254 in the VLAN
    print("Starting scan...")
    for last_octet in range(1, 255):
        ip = f"10.11.14.{last_octet}"
        result = subprocess.run(['ping', '-c', '1', '-W', '1', ip],
                              stdout=subprocess.DEVNULL,
                              stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            print(f"Host found: {ip}")
            active_hosts.append(ip)
    return active_hosts


def main():
    print("In main")
    active_hosts = scan_network()
    print("\nActive hosts:")
    for host in active_hosts:
        print(f"- {host}")
    print(f"\nTotal hosts found: {len(active_hosts)}")


if __name__ == "__main__":
    main()