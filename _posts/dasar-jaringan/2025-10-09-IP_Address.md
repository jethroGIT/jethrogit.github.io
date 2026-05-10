---
layout: post
title: Dasar IP Address
category: Dasar-Jaringan
lang: IN
description: Pengenalan IP Address
---

## Pengantar

Pernah nggak sih, kamu nyambung ke Wi-Fi tapi nggak bisa internetan? Nah, sering kali masalahnya bukan di koneksinya, tapi di pengaturan **IP address**.  
IP address itu ibaratkan “alamat rumah” di dunia digital. Kalau alamatnya ga benar, perangkat kamu nggak bisa ngobrol sama perangkat lain di jaringan.

Makanya, kalau kamu tertarik sama jaringan komputer atau lagi belajar dasar-dasar networking, paham konsep IP address itu **wajib hukumnya**. 

## 📌 Daftar Isi  

1. [Apa itu IP Address?](#apa-itu-ip-address)  
2. [Struktur IP Address](#struktur-ip-address)  
3. [Versi IP Address: IPv4 dan IPv6](#versi-ip-address-ipv4-dan-ipv6)  
   - [IPv4](#ipv4)  
   - [IPv6](#ipv6)  
4. [Kelas-Kelas IP Address](#kelas-kelas-ip-address)  
   - [Kelas A](#kelas-a)  
   - [Kelas B](#kelas-b)  
   - [Kelas C](#kelas-c)  
   - [Kelas D dan E](#kelas-d-dan-e)  
5. [Range & Contoh IP Tiap Kelas](#range--contoh-ip-tiap-kelas)  
6. [Private dan Public IP Address](#private-dan-public-ip-address)  
7. [Subnet Mask dan Pembagian Jaringan](#subnet-mask-dan-pembagian-jaringan)  
8. [Kesimpulan](#kesimpulan)

---

## Apa itu IP Address?

Gampangnya, **IP Address (Internet Protocol Address)** adalah identitas unik yang diberikan ke setiap perangkat yang terhubung ke jaringan, supaya bisa saling berkomunikasi.

Bayangin aja kayak sistem pengantaran paket. Supaya paket bisa sampai ke tujuan, pengirim dan penerima harus punya alamat. Nah, sama halnya dengan komputer dan server di internet itu butuh IP buat kirim dan nerima data.

Fungsi IP meliputi:
* **Identifikasi perangkat:** Setiap perangkat di jaringan punya IP yang beda.  
* **Komunikasi antar perangkat:** IP jadi rute perjalanan buat ngirim data.  
* **Lokasi jaringan:** IP bisa menunjukkan dari jaringan mana perangkat berasal.  

---

## Struktur IP Address

Perlu teman teman ketahui kalau IP address itu terdiri dari dua bagian utama:  
1. **Network ID** - bagian ini menunjukkan jaringan tempat perangkat berada.  
2. **Host ID** - bagian ini menunjukkan perangkat spesifik di dalam jaringan itu.  

Contoh:  

> 192.168.1.10 → [Network ID: 192.168.1] [Host ID: 10 ]

Dengan struktur ini komputer jadi tahu “kamu dari jaringan mana” dan “perangkat mana yang mau diajak komunikasi”.

---

## Versi IP Address: IPv4 dan IPv6

Ada dua versi IP yang umum dipakai:

### IPv4

Format klasik yang terdiri dari **32 bit** (4 oktet) dan biasanya ditulis seperti ini:

> 192.168.0.1

Totalnya ada sekitar 4 miliar alamat, tapi sekarang udah hampir habis.

### IPv6

Karna jumlah IPv4 hampir habis, dibuatlah penggantinya **IPv6** yang punya **128 bit**. Contohnya:

> 2001:0db8:85a3:0000:0000:8a2e:0370:7334

Nah, dengan jumlah alamat yang hampir nggak terbatas, IPv6 dibuat supaya semua perangkat dimasa depan termasuk IoT pun kebagian alamat!

---

## Kelas-Kelas IP Address

Alamat IPv4 dibagi jadi beberapa **kelas** berdasarkan kapasitas jaringan dan kebutuhan pengguna. Ini dikenal dengan istilah **Classful IP Addressing**.

### Kelas A

* **Rentang:** 1.0.0.0 – 126.255.255.255  
* **Bit network:** 8 bit  
* **Bit host:** 24 bit  
* **Jumlah host:** ±16 juta per jaringan  
* **Awalan biner:** 0  
Kelas ini cocok buat **organisasi besar** yang butuh banyak alamat IP.

### Kelas B

* **Rentang:** 128.0.0.0 – 191.255.255.255  
* **Bit network:** 16 bit  
* **Bit host:** 16 bit  
* **Jumlah host:** ±65 ribu per jaringan  
Biasanya dipakai untuk jaringan menengah kayak **universitas atau perusahaan menengah**.

### Kelas C

* **Rentang:** 192.0.0.0 – 223.255.255.255  
* **Bit network:** 24 bit  
* **Bit host:** 8 bit  
* **Jumlah host:** 254 per jaringan  
Paling sering dipakai buat **jaringan kecil** kayak kantor atau rumah.

### Kelas D dan E

* **Kelas D (224.0.0.0 – 239.255.255.255):** digunakan untuk **multicast** (ngirim data ke banyak perangkat sekaligus).  
* **Kelas E (240.0.0.0 – 255.255.255.255):** dicadangkan untuk **eksperimen atau riset**.

---

## Range & Contoh IP Tiap Kelas

<table class="table-terminal">
  <thead>

    <tr>
      <th>Kelas</th>
      <th>Rentang IP</th>
      <th>Jumlah Jaringan</th>
      <th>Jumlah Host per Jaringan</th>
      <th>Contoh</th>
    </tr>

  </thead>
  <tbody>

    <tr>
      <td>A</td>
      <td>1.0.0.0 – 126.255.255.255</td>
      <td>128</td>
      <td>±16.777.214</td>
      <td>10.0.0.1</td>
    </tr>
    <tr>
      <td>B</td>
      <td>128.0.0.0 – 191.255.255.255</td>
      <td>16.384</td>
      <td>±65.534</td>
      <td>172.16.0.1</td>
    </tr>
    <tr>
      <td>C</td>
      <td>192.0.0.0 – 223.255.255.255</td>
      <td>2.097.152</td>
      <td>254</td>
      <td>192.168.1.1</td>
    </tr>
    <tr>
      <td>D</td>
      <td>224.0.0.0 – 239.255.255.255</td>
      <td>Multicast</td>
      <td>-</td>
      <td>224.0.0.1</td>
    </tr>
    <tr>
      <td>E</td>
      <td>240.0.0.0 – 255.255.255.255</td>
      <td>Eksperimen</td>
      <td>-</td>
      <td>-</td>
    </tr>

  </tbody>
</table>

---

## Private dan Public IP Address

Nggak semua IP bisa diakses dari internet. Ada dua jenis utama:

* **Public IP:** dipakai buat perangkat yang terhubung langsung ke internet (contohnya server web).  
* **Private IP:** dipakai di jaringan lokal (LAN) dan nggak bisa diakses dari luar.

Contoh **Private IP Address**:  
* Kelas A: 10.0.0.0 – 10.255.255.255  
* Kelas B: 172.16.0.0 – 172.31.255.255  
* Kelas C: 192.168.0.0 – 192.168.255.255  

Kalau kamu lihat IP seperti 192.168.x.x itu tandanya kamu lagi di jaringan lokal, bukan langsung ke internet.

---

## Subnet Mask dan Pembagian Jaringan

Supaya IP bisa lebih efisien, dibuatlah konsep **subnetting**.  
Subnetting membagi jaringan besar jadi beberapa jaringan kecil (subnetwork) biar lebih hemat dan teratur.

Contoh subnet mask:
- **Kelas A:** 255.0.0.0  
- **Kelas B:** 255.255.0.0  
- **Kelas C:** 255.255.255.0  

Dengan subnet mask, router jadi tahu bagian mana dari IP address yang menunjukkan **network ID** dan mana yang menunjukkan **host ID**.

Setiap jaringan memiliki dua alamat khusus, yaitu **Network Address** dan **Broadcast Address**. 
- Network Address adalah IP Address yang digunakan untuk menandai area sebuah jaringan, 
- Broadcast Address adalah IP Address digunakan untuk mengirim pesan/data secara broadcast ke semua host yang berada dalam satu jaringan yang sama. 

Penjelasan lebih detail mengenai cara menghitung keduanya akan dibahas pada artikel berikutnya tentang Subnetting dan VLSM (Variable Length Subnet Masking).

---

## Kesimpulan

IP address bukan cuma angka acak yang muncul di pengaturan jaringan, tapi sebagai identitas di dunia digital.  
Dengan paham konsep **kelas IP, private/public IP**, dan **subnet mask**, kamu udah selangkah lebih dekat buat ngerti gimana internet dan jaringan bekerja di balik layar.

Next step-nya? Kamu bisa lanjut ke topik **subnetting dan VLSM**, biar makin jago ngatur jaringan sendiri.  
