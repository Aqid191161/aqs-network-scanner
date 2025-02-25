import os

# Clear terminal sebelum menjalankan program
os.system('cls' if os.name == 'nt' else 'clear')


import subprocess
import scapy.all as scapy
import netifaces
import requests
import time
from tabulate import tabulate

def get_local_subnet():
    """Mendeteksi subnet jaringan secara otomatis"""
    interfaces = netifaces.interfaces()
    for iface in interfaces:
        try:
            addr = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
            if addr.startswith(("192.168.", "10.", "172.")):
                return ".".join(addr.split(".")[:3])  # Contoh: '192.168.1'
        except (KeyError, IndexError):
            continue
    return None

def ping_sweep(subnet):
    """Melakukan Ping Sweep untuk menemukan perangkat yang aktif"""
    active_hosts = []
    for i in range(1, 255):  # Scan IP .1 sampai .254
        ip = f"{subnet}.{i}"
        result = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            active_hosts.append(ip)
    return active_hosts

def get_mac(ip):
    """Mendapatkan MAC Address dari IP menggunakan ARP"""
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    answered, _ = scapy.srp(broadcast / arp_request, timeout=1, verbose=False)
    return answered[0][1].hwsrc if answered else "Unknown MAC"

def get_vendor(mac_address):
    """Mencari vendor berdasarkan MAC Address"""
    try:
        url = f"https://api.macvendors.com/{mac_address}"
        response = requests.get(url, timeout=5)
        return response.text if response.status_code == 200 else "Unknown Vendor"
    except requests.exceptions.RequestException:
        return "Unknown Vendor"

def main():
    subnet = get_local_subnet()
    if not subnet:
        print("Gagal mendeteksi jaringan. Pastikan Anda terhubung ke WiFi atau LAN.")
        return
    
    print(f"\n🔍 Melakukan Ping Sweep di subnet {subnet}.x, mohon tunggu...\n")

    active_ips = ping_sweep(subnet)

    if not active_ips:
        print("🚫 Tidak ada perangkat yang terdeteksi. Periksa koneksi jaringan Anda.")
        return

    data = []
    for ip in active_ips:
        mac = get_mac(ip)
        vendor = get_vendor(mac) if mac != "Unknown MAC" else "Unknown Vendor"
        data.append([ip, mac, vendor])
        time.sleep(0.5)  # Hindari terlalu banyak request API sekaligus

    # Menampilkan hasil dalam tabel rapi
    print(tabulate(data, headers=["IP Address", "MAC Address", "Vendor"], tablefmt="grid"))

if __name__ == "__main__":
    main()
