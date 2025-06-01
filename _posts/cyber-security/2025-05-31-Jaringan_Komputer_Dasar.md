---
layout: post
title: Mengenal Dasar Jaringan Komputer dengan Cisco Packet Tracer
category: Cyber-Security
lang: IN
description: Konsep Dasar Jaringan
---

## **Pengantar**
Pada artikel kali ini, saya akan membahas dasar-dasar jaringan komputer dan praktik penggunaannya menggunakan simulator jaringan, yaitu Cisco Packet Tracer. Artikel ini cocok bagi pemula yang ingin memahami konsep jaringan sekaligus mempraktikkannya secara langsung.

## **Dasar-Dasar Jaringan Komputer**
Sebelum masuk ke simulasi dan praktik menggunakan aplikasi seperti Cisco Packet Tracer, penting banget untuk memahami dulu dasar-dasar jaringan komputer. Jadi gini, ketika dua komputer atau lebih ingin “ngobrol” alias bertukar data, mereka butuh jalan atau media untuk mengirim dan menerima informasi. Nah, jaringan komputer inilah yang menjadi perantara komunikasi itu.

Komputer bisa saling terhubung melalui kabel, gelombang radio (Wi-Fi), atau serat optik. Tapi komunikasi antar komputer itu nggak sembarangan—ada aturan atau protokol yang mengatur bagaimana data dikirim dari satu titik ke titik lainnya, supaya nggak nyasar. Data yang dikirim juga dipaket-paketkan (makanya disebut packet), lalu dikirim lewat jalur yang paling efisien.

Sekarang, mari kita bahas jenis-jenis jaringan berdasarkan cakupan areanya:

---

## 1. Jenis-Jenis Jaringan

**🏠 LAN (Local Area Network)** 

LAN adalah jaringan kecil yang biasanya hanya mencakup satu lokasi, misalnya di rumah, kantor, atau laboratorium komputer. Dalam LAN, perangkat-perangkat seperti komputer, printer, atau router saling terhubung secara langsung dan bisa bertukar data dengan cepat. Contoh sederhana: komputer di lab kampus yang saling terkoneksi dan bisa saling sharing file atau printer.

**🏢 MAN (Metropolitan Area Network)**

MAN mencakup area yang lebih luas dibanding LAN, biasanya mencakup satu kota atau kawasan kampus yang terdiri dari banyak gedung. Jaringan ini sering digunakan oleh institusi besar, misalnya kampus atau pemerintahan kota, untuk menghubungkan beberapa lokasi yang berjauhan tapi masih dalam satu wilayah metropolitan.


**🌍 WAN (Wide Area Network)**

WAN adalah jaringan paling luas, bahkan bisa menghubungkan komputer di seluruh dunia. Internet adalah contoh nyata dari WAN. Karena jarak yang jauh, WAN sering menggunakan teknologi komunikasi seperti satelit atau jaringan fiber optik jarak jauh.

---

## 2. Memahami IP Address dan Subnetting

Setelah tahu jenis-jenis jaringan, sekarang kita bahas gimana caranya komputer bisa saling “nemu” satu sama lain dalam jaringan. Di sinilah **IP Address** berperan penting.

### Apa Itu IP Address?
Bayangin kamu lagi kirim surat ke teman—tentu kamu butuh alamat tujuan, kan? Nah, IP Address itu ibarat alamat rumah bagi perangkat di jaringan. Setiap komputer, printer, bahkan HP kamu di jaringan punya IP unik, supaya bisa dikenali dan dihubungi.

Contoh IP Address versi IPv4:

    192.168.1.10

IP Address terdiri dari dua bagian utama:
- **Network ID:** Menunjukkan alamat jaringan.
- **Host ID:** Menunjukkan perangkat tertentu dalam jaringan tersebut.

### Jenis-Jenis IP Address
- **IP Publik:**Bisa diakses dari internet langsung. Biasanya digunakan oleh server.
- **IP Private:** Hanya digunakan dalam jaringan lokal (misal LAN). Contoh: `192.168.x.x`, `10.x.x.x.`

### Subnetting: Memecah Jaringan Jadi Lebih Kecil

Subnetting adalah teknik untuk **membagi satu jaringan besar jadi beberapa jaringan kecil**, supaya lalu lintas data lebih efisien dan lebih mudah dikelola. Setiap subnet punya jatah IP sendiri.

Contoh:

    Network: 192.168.1.0/24

Artinya:
- `192.168.1.0` = Network address
- `/24` = Netmask (255.255.255.0), artinya ada 256 alamat (0–255)
- Tapi... alamat pertama (0) adalah network address dan terakhir (255) adalah broadcast address, jadi yang bisa dipakai: 192.168.1.1 sampai 192.168.1.254

#### Tipe-Tipe Alamat dalam Subnet

<table class="table-terminal">
  <thead>
    <tr>
      <th>Tipe Alamat</th>
      <th>Contoh</th>
      <th>Fungsi</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Network Address</td>
      <td>192.168.1.0</td>
      <td>Menandai alamat utama jaringan</td>
    </tr>
    <tr>
      <td>Broadcast Address</td>
      <td>192.168.1.255</td>
      <td>Digunakan untuk mengirim ke semua host</td>
    </tr>
    <tr>
      <td>Host Address</td>
      <td>192.168.1.1 – 192.168.1.254</td>
      <td>Digunakan oleh perangkat di jaringan</td>
    </tr>
  </tbody>
</table>

---

## 3. Mengenal DNS: "Penerjemah Nama" di Internet

Setelah kamu paham soal IP Address dan Subnetting, sekarang muncul satu pertanyaan:
"Kalau setiap perangkat punya alamat IP, kenapa kita jarang banget mengetik angka-angka itu waktu browsing?"
Nah, di sinilah DNS (Domain Name System) ambil peran.

### Apa itu DNS?

Bayangin kamu mau ngunjungin rumah teman, tapi kamu cuma inget nama panggilannya, bukan alamat rumahnya. Di dunia internet, nama itu seperti youtube.com, sedangkan alamat rumahnya adalah alamat IP seperti `142.250.190.46`. 

DNS (Domain Name System) adalah sistem yang bertugas menerjemahkan nama domain (seperti youtube.com) menjadi IP address (seperti `142.250.190.46`). DNS bekerja menggunakan server yang tersebar di internet dan bekerja secara hirarki.

### Cara Kerja DNS (Simpelnya):
1. Kamu mengetik www.google.com di browser.
2. Komputer akan bertanya ke DNS: "IP Address dari www.google.com itu berapa ya?"
3. DNS menjawab: "Ini alamatnya: `142.250.190.78`"
4. Browser kemudian membuka koneksi ke alamat IP tersebut.

### Kenapa DNS Penting?
- **Mudah diingat:** Lebih gampang ketik youtube.com daripada `142.250.190.46`
- **Fleksibel:** Kalau Google ganti server, cukup ubah IP-nya di DNS tanpa mengubah nama domainnya


Dengan penjelasan DNS ini, pembaca akan lebih paham ketika nanti diminta mengatur DNS server di simulator seperti Cisco Packet Tracer atau GNS3. DNS bukan cuma teori, tapi bagian nyata dari praktik jaringan komputer.

Setelah tahu dasar DNS, barulah kita bisa lanjut ke bagian praktik: ngatur IP Address, subnet mask, dan DNS di simulator jaringan.

---

## 4. Praktik: Setting IP Address, Subnet Mask, dan Gateway

Setelah paham teori IP Address, subnetting, dan DNS, sekarang waktunya praktek! Kita akan setting konfigurasi IP pada masing-masing perangkat di topologi berikut:

[![img1]({{ site.baseurl }}/assets/images/topologi-dasar-jaringan.png){:class="img-responsive" style="max-width: 400px; height: auto; display: block; margin: 0 auto;"}]({{ site.baseurl }}/assets/images/topologi-dasar-jaringan.png)

### 1. Setting IP di PC
1. Klik PC (PC-PT).
2. Buka tab **Desktop** -> pilih **IP Configuration**.
3. Isi sebagai berikut:
- IP Address: `192.168.0.10`
- Subnet Mask: `255.255.255.0` (otomatis terisi)
- Default Gateway: `192.168.0.1` (alamat router Fa0/1)
- DNS Server: `10.10.10.10` (alamat server DNS)

### 2. Setting IP di Laptop
1. Klik Laptop (Laptop-PT).
2. Buka tab **Desktop** -> pilih **IP Configuration**.
3. Isi sebagai berikut:
- IP Address: `192.168.0.10`
- Subnet Mask: `255.255.255.0` (otomatis terisi)
- Default Gateway: `192.168.0.1` (alamat router Fa0/1)
- DNS Server: `10.10.10.10` (alamat server DNS)

### 3. Setting IP Router

1. Klik Router > pilih tab CLI.
2. Masukkan konfigurasi berikut:

    ```bash
    Router> enable
    Router# configure terminal
    Router(config)# interface fastEthernet 0/0
    Router(config-if)# ip address 10.10.10.1 255.255.255.0
    Router(config-if)# no shutdown
    Router(config-if)# exit
    Router(config)# interface fastEthernet 0/1
    Router(config-if)# ip address 192.168.0.1 255.255.255.0
    Router(config-if)# no shutdown
    Router(config-if)# exit
    Router(config)# exit
    Router#
    ```

### 4. Menguji Koneksi

Setelah semua IP, Gateway, dan DNS dikonfigurasi, sekarang **saatnya menguji apakah jaringan berfungsi dengan baik**.

Ada dua cara sederhana untuk melakukannya:
1. Ping alamat IP DNS Server

    Buka Command Prompt pada PC atau Laptop, lalu ketik:
    ```bash
    ping 10.10.10.10
    ```
    Jika muncul balasan (Reply from...), berarti koneksi ke server DNS berhasil.

2. Akses alamat URL

    Masih dari PC atau Laptop, buka browser dan akses:
    ```bash
    http://mangaden.com
    ```
    Jika website terbuka, berarti konfigurasi DNS juga sudah berhasil.

#IDNBootcampCyber


