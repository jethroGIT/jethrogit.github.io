---
layout: post
title: Mengenal Dasar Jaringan Komputer dengan Cisco Packet Tracer
category: Cyber-Security
lang: IN
description: Konsep Dasar Jaringan
---

## **Pengantar**
Pada artikel kali ini, saya akan membahas dasar-dasar jaringan komputer dan praktik penggunaannya menggunakan simulator jaringan, yaitu Cisco Packet Tracer. Artikel ini cocok bagi pemula yang ingin memahami konsep jaringan sekaligus mempraktikkannya secara langsung.

## 📌 Daftar Isi

1. [Dasar-Dasar Jaringan Komputer](#dasar-dasar-jaringan-komputer)
   - [1. Jenis-Jenis Jaringan](#1-jenis-jenis-jaringan)
2. [Memahami IP Address dan Subnetting](#2-memahami-ip-address-dan-subnetting)
   - [1. Apa Itu IP Address?](#apa-itu-ip-address)
   - [2. Jenis-Jenis IP Address](#jenis-jenis-ip-address)
   - [3. Subnetting: Memecah Jaringan Jadi Lebih Kecil](#subnetting-memecah-jaringan-jadi-lebih-kecil)
   - [4. Tipe-Tipe Alamat dalam Subnet](#tipe-tipe-alamat-dalam-subnet)
3. [Mengenal DNS: "Penerjemah Nama" di Internet](#3-mengenal-dns-penerjemah-nama-di-internet)
   - [1. Apa itu DNS?](#apa-itu-dns)
   - [2. Cara Kerja DNS (Simpelnya)](#cara-kerja-dns-simpelnya)
   - [3. Kenapa DNS Penting?](#kenapa-dns-penting)
4. [Praktik: Setting IP Address, Subnet Mask, dan Gateway](#4-praktik-setting-ip-address-subnet-mask-dan-gateway)
   - [Unduh File Latihan](#-unduh-file-latihan)
   - [1. Setting IP di PC](#1-setting-ip-di-pc)
   - [2. Setting IP di Laptop](#2-setting-ip-di-laptop)
   - [3. Setting IP Router](#3-setting-ip-router)
   - [4. Menguji Koneksi](#4-menguji-koneksi)
5. [Penutup](#penutup)


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

Setelah tahu jenis-jenis jaringan, sekarang kita bahas gimana caranya komputer bisa saling “bertemu” satu sama lain dalam jaringan. Di sinilah **IP Address** berperan penting.

### Apa Itu IP Address?
Bayangin kamu lagi kirim surat ke teman. Tentu kamu butuh **alamat tujuan**, kan? Nah, dalam jaringan **IP Address** (Internet Protocol Address) adalah **alamat unik** yang diberikan ke setiap perangkat entah itu komputer, printer, router, atau bahkan HP supaya bisa dikenali dan dihubungi.

Contoh IP Address versi IPv4:

    192.168.1.10

IP Address terdiri dari dua bagian utama:
- **Network ID:** Menunjukkan alamat jaringan.
- **Host ID:** Menunjukkan perangkat tertentu dalam jaringan tersebut.

Contoh:

    IP Address : 192.168.1.10
    Subnet mask: 255.255.255.0

Di sini, `192.168.1` adalah Network ID, dan `10` adalah Host ID.


### Jenis-Jenis IP Address

Secara umum, IP Address terbagi jadi dua jenis:

- **IP Publik:** Bisa diakses dari internet langsung. Biasanya digunakan oleh server, website, atau perangkat yang harus diakses dari luar jaringan lokal.
- **IP Private:** Hanya digunakan dalam jaringan lokal (LAN/WAN). Biasanya digunakan oleh komputer rumah, printer kantor, atau router Wi-Fi.

### Subnetting: Memecah Jaringan Jadi Lebih Kecil

Subnetting adalah teknik untuk **membagi satu jaringan besar jadi beberapa sub-jaringan (subnet) yang lebih kecil**, supaya lalu lintas data lebih efisien dan lebih mudah dikelola. Setiap subnet punya jatah IP sendiri.

#### Contoh Subneting Sederhana

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

### Kenapa Subnetting Penting?

Bayangkan kamu sedang mengatur sekolah besar dengan 1.000 siswa, tapi semuanya hanya punya satu ruang kelas. Bisa dibayangkan betapa berisik dan kacau suasananya:
- Semua murid bicara sekaligus.
- Guru sulit fokus karena semua siswa saling bersahut-sahutan.
- Kalau ada informasi penting, bisa tidak terdengar atau tertukar.
- Mengelola dan mengawasi mereka jadi sangat sulit.

Sekarang, bandingkan jika kamu membagi siswa ke dalam 20 kelas kecil, masing-masing dengan 50 orang:
- Komunikasi jadi lebih terarah.
- Informasi bisa disampaikan lebih efisien.
- Masing-masing kelas bisa dikelola secara terpisah.
- Kalau ada masalah di satu kelas, tidak mengganggu yang lain.


Nah, subnetting di jaringan itu persis seperti membagi siswa ke dalam kelas-kelas kecil.
<br>
Dengan subnetting:
- Lalu lintas data (traffic) di jaringan tidak saling tabrakan.
- Broadcast (pengumuman dalam jaringan) tidak membanjiri semua perangkat.
- Keamanan dan kontrol jadi lebih mudah.
- IP Address bisa digunakan lebih hemat dan efisien.

Dengan subnetting, kamu bisa memecah jaringan jadi lebih kecil. Misalnya dari:

    Network: 192.168.1.0/24

menjadi:
- `192.168.1.0/26` → 64 alamat (62 usable)
- `192.168.1.64/26` → 64 alamat lagi
- dan seterusnya…

---

## 3. Mengenal DNS: "Penerjemah Nama" di Internet

Setelah kamu paham soal IP Address dan Subnetting, sekarang muncul satu pertanyaan:
<i>"Kalau setiap perangkat punya alamat IP, kenapa kita jarang banget mengetik angka-angka itu waktu browsing?"</i>
Jawabannya adalah: karena kita punya **DNS**!

### Apa itu DNS?

Bayangin kamu mau ngunjungin rumah teman, tapi kamu cuma inget nama panggilannya, bukan alamat rumahnya. Di dunia internet, nama itu seperti youtube.com, sedangkan alamat rumahnya adalah alamat IP seperti `142.250.190.46`. 

DNS (Domain Name System) adalah sistem yang bertugas menerjemahkan nama domain (seperti youtube.com) menjadi IP address (seperti `142.250.190.46`). 

### Cara Kerja DNS (Simpelnya):
1. Kamu mengetik www.google.com di browser.
2. Komputer akan bertanya ke DNS: 
>"IP Address dari www.google.com itu berapa ya?"
3. DNS menjawab: 
>"Ini alamatnya: `142.250.190.78`"
4. Browser kemudian membuka koneksi ke alamat IP tersebut dan menampilkan halaman Google.

DNS ini bekerja lewat server-server yang tersebar di seluruh dunia dan terstruktur secara hirarki, mulai dari **root DNS**, **TLD (Top-Level Domain) DNS**, hingga **authoritative DNS** yang menyimpan jawaban akhirnya.


### Kenapa DNS Penting?
- **Mudah Diingat** 
<br>
Tentu lebih mudah mengingat youtube.com dibanding `142.250.190.46`, kan ? 

- **Fleksibel:** 
<br>
Kalau sebuah situs pindah server (ganti IP Address), kamu **tidak perlu tahu perubahan itu**. DNS yang akan mengarahkannya ke alamat baru, tetap lewat nama yang sama.

- **Efisien:**
<br>
DNS juga menyimpan cache dari permintaan sebelumnya, jadi akses ke situs jadi **lebih cepat** setelah pertama kali dibuka.

DNS adalah jembatan antara manusia dan mesin di dunia internet. DNS memungkinkan kita menggunakan nama-nama yang ramah di mata manusia, dan membiarkan komputer mengurus alamat IP-nya di balik layar.

Setelah tahu dasar DNS, barulah kita bisa lanjut ke bagian praktik: ngatur IP Address, subnet mask, dan DNS di simulator jaringan.

---

## 4. Praktik: Setting IP Address, Subnet Mask, dan Gateway

Setelah paham teori IP Address, subnetting, dan DNS, sekarang waktunya praktek! Kita akan setting konfigurasi IP pada masing-masing perangkat di topologi berikut:

[![img1]({{ site.baseurl }}/assets/images/topologi-dasar-jaringan.png){:class="img-responsive" style="max-width: 400px; height: auto; display: block; margin: 0 auto;"}]({{ site.baseurl }}/assets/images/topologi-dasar-jaringan.png)
*<center>$\pmb{\text{Gambar 1}}$: Topologi dasar jaringan yang menunjukkan koneksi antara DNS Server, Router, Switch, PC, dan Laptop. Topologi dibuat menggunakan <a href="https://www.netacad.com/cisco-packet-tracer"><b>Cisco Packet Tracer</b></a> untuk keperluan edukasi.</center>*


### 📁 Unduh File Latihan

Sebelum masuk ke sesi praktik, silakan unduh terlebih dahulu file latihan topologi jaringan yang akan kita gunakan: 👉 [Unduh file latihan: jaringan-dasar.pkt](/assets/file/jaringan-dasar/jaringan-dasar.pkt)

### 1. Setting IP di PC
1. Klik PC (PC-PT).
2. Buka tab **Desktop** -> pilih **IP Configuration**.
3. Isi sebagai berikut:
- IP Address: `192.168.0.10`
- Subnet Mask: `255.255.255.0` (otomatis terisi)
- Default Gateway: `192.168.0.1` (alamat router Fa0/1)
- DNS Server: `10.10.10.10` (alamat server DNS)

[![img1]({{ site.baseurl }}/assets/images/PC-PT.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/PC-PT.png)
*<center>$\pmb{\text{Gambar 2}}$: Konfigurasi IP statis pada PC-PT di Cisco Packet Tracer. Perangkat ini diberi alamat IP 192.168.0.10 secara manual, dengan subnet mask 255.255.255.0, default gateway 192.168.0.1, dan DNS server 10.10.10.10. Dengan pengaturan ini, PC dapat mengakses jaringan eksternal dan melakukan resolusi nama domain melalui DNS server.</center>*

### 2. Setting IP di Laptop
1. Klik Laptop (Laptop-PT).
2. Buka tab **Desktop** -> pilih **IP Configuration**.
3. Isi sebagai berikut:
- IP Address: `192.168.0.20`
- Subnet Mask: `255.255.255.0` (otomatis terisi)
- Default Gateway: `192.168.0.1` (alamat router Fa0/1)
- DNS Server: `10.10.10.10` (alamat server DNS)

[![img1]({{ site.baseurl }}/assets/images/Laptop-PT.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/Laptop-PT.png)
*<center>$\pmb{\text{Gambar 3}}$: Konfigurasi IP statis pada Laptop-PT di Cisco Packet Tracer. Perangkat ini diberi alamat IP 192.168.0.20 secara manual, dengan subnet mask 255.255.255.0, default gateway 192.168.0.1, dan DNS server 10.10.10.10. Dengan pengaturan ini, laptop dapat mengakses jaringan eksternal dan melakukan resolusi nama domain melalui DNS server.</center>*


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
    [![img1]({{ site.baseurl }}/assets/images/tes-koneksi-ping.png){:class="img-responsive" style="max-width: 400px; height: auto; display: block; margin: 0 auto;"}]({{ site.baseurl }}/assets/images/tes-koneksi-ping.png)
    *<center>$\pmb{\text{Gambar 4}}$: Hasil pengujian koneksi menggunakan perintah ping dari PC-PT ke DNS Server (IP: 10.10.10.10). Keempat paket berhasil dikirim dan diterima tanpa kehilangan paket (0% loss), yang menunjukkan koneksi jaringan antara PC dan server berjalan dengan baik.</center>*


    


2. Akses alamat URL

    Masih dari PC atau Laptop, buka browser dan akses:
    ```bash
    http://mangaden.com
    ```

    Jika website terbuka, berarti konfigurasi DNS juga sudah berhasil.
    [![img1]({{ site.baseurl }}/assets/images/tes-koneksi-url.png){:class="img-responsive" style="max-width: 400px; height: auto; display: block; margin: 0 auto;"}]({{ site.baseurl }}/assets/images/tes-koneksi-url.png)
    *<center>$\pmb{\text{Gambar 5}}$: PC-PT berhasil mengakses domain <code>mangaden.com</code> melalui web browser. Hal ini menunjukkan bahwa DNS Server (10.10.10.10) berhasil melakukan resolusi nama domain ke alamat IP yang sesuai, sehingga PC dapat mengakses website yang dihosting di server.</center>*

---

### Penutup
Dengan memahami konsep dan praktik ini, teman teman telah menguasai fondasi penting dalam dunia jaringan komputer yang akan menjadi bekal kuat untuk belajar konfigurasi lanjutan di masa depan.

#IDNBootcampCyber


