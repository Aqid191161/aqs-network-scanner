</h1>

<h4 align="center">Network Scanner </h4>

<p align="center">

  <a href="http://python.org">
    <img src="https://img.shields.io/badge/python-v3-blue">
  </a>
  <a href="https://en.wikipedia.org/wiki/Linux">
    <img src="https://img.shields.io/badge/Platform-Linux-red">
  </a>

</p>

## 🚀 Fitur
- **Deteksi subnet otomatis** (tanpa konfigurasi manual)  
- **ICMP Ping Sweep** - Menemukan perangkat yang merespons ping  
- **ARP Scanning** - Mengambil MAC Address dari perangkat aktif  
- **Identifikasi Vendor** berdasarkan MAC Address  
- **Tampilan tabel rapi** menggunakan `tabulate`  
- **Dapat digunakan di jaringan WiFi & LAN**  
- **Ringan, cepat, dan mudah digunakan**  
---
## 🔥Next Features
- **Logging**  File CSV
- **Monitoring** Real-Time
- **Notifikasi** Telegram untuk Perangkat Baru
- **Web Dashboard** Flask/FastAPI
- **Auto-Block Perangkat Tak Dikenal** Firewall

## 📦 Teknologi yang Digunakan
- **Python 3** - Bahasa utama  
- **Scapy** - Untuk ARP scanning  
- **Netifaces** - Untuk mendeteksi subnet otomatis  
- **Requests** - Untuk mengambil data vendor dari MacVendors API  
- **Subprocess** - Untuk menjalankan ping secara sistem  
- **Tabulate** - Untuk menampilkan hasil dalam format tabel yang rapi  



<br>

## 🔧 Instalasi dan Penggunaan
### perbarui paket  
``` 
sudo apt update  
``` 

### install git:  
```  
sudo apt install git 
```

### install python
``` 
sudo apt install python3 
``` 
### install pip
``` 
sudo apt install python3-pip
``` 

### clone repository
``` 
git clone https://github.com/Aqid191161/aqs-network-scanner.git
``` 
### masuk folder
``` 
cd aqs-network-scanner
``` 
### buat virtual environment (venv)
```
python3 -m venv aqs
source aqs/bin/activate
```

### install pustaka
```
pip3 install scapy netifaces requests tabulate
``` 


### Jalankan Program
```
sudo python3 scan.py
``` 

### 📜 Contoh Output
```
🔍 Melakukan Ping Sweep di subnet 192.168.1.x, mohon tunggu...

+---------------+-------------------+-------------------------------------+
| IP Address    | MAC Address       | Vendor                             |
+---------------+-------------------+-------------------------------------+
| 192.168.1.1   | 00:1A:2B:3C:4D:5E | TP-Link Technologies Co., Ltd.     |
| 192.168.1.10  | 34:AB:CD:12:34:56 | Apple Inc.                         |
| 192.168.1.25  | B8:27:EB:11:22:33 | Raspberry Pi Foundation            |
| 192.168.1.100 | 00:11:22:33:44:55 | Dell Inc.                          |
+---------------+-------------------+-------------------------------------+

``` 


<br>

---
 
#  Kredit

**Proyek Network Scanner**
  
- **Scapy Community** - Library untuk ARP scanning  
- **MacVendors API** - Database vendor berdasarkan MAC Address  
- **Python Open-Source Community** - Untuk pustaka tambahan seperti `netifaces`, `requests`, dan `tabulate`  

## 🔗 Sumber & Referensi
- [Scapy Documentation](https://scapy.readthedocs.io/)
- [MacVendors API](https://macvendors.com/)
- [Python Networking Guide](https://docs.python.org/3/library/)

Terima kasih kepada komunitas open-source yang telah berkontribusi dalam pengembangan alat ini! 🚀  





