---
layout: post
title: Analisis Malware Win32/Koi Stealer pada Jaringan PT. ABC
category: Cyber-Security
lang: IN
description: Security Report
---

## **Pengantar** 

Pada artikel kali ini, saya akan membahas sebuah studi kasus nyata mengenai insiden keamanan jaringan berdasarkan hasil analisis log lalu lintas jaringan. Studi kasus ini merupakan bagian dari tugas yang diberikan dalam bootcamp Cybersecurity yang diselenggarakan oleh ID-Networkers.

Peserta bootcamp diminta untuk menganalisis file log jaringan yang mencatat aktivitas mencurigakan, yang ternyata merupakan bagian dari serangan malware. Dari analisis tersebut, ditemukan bahwa salah satu host di jaringan internal PT. ABC telah terinfeksi oleh malware bernama Win32/Koi Stealer, yang aktif melakukan komunikasi ke server eksternal berbahaya.

## 📌 Daftar Isi

1. [Executive Summary](#executive-summary)
2. [Indicator of Compromise (IOC)](#indicator-of-compromise-ioc)
3. [Proof of Concept (POC)](#proof-of-concept-poc)
    - [HTTP POST Request](#http-post-request)
    - [User-Agent String](#user-agent-string)
    - [Indikasi Win32/Koi Stealer](#indikasi-win32koi-stealer)
    - [Analisa VirusTotal](#analisa-virustotal)
    - [Affected Host](#affected-host)
    - [Security Alert](#security-alert)
4. [URL Generating the Alert Traffic](#url-generating-the-alert-traffic)
5. [Risk Assessment](#risk-assesment)
6. [Mitigation](#mitigation)
7. [References](#references)
8. [Conclusion](#conclusion)


## **EXECUTIVE SUMMARY**

<table class="table-terminal">
  <thead>
    <tr>
      <th>Field</th>
      <th>Detail</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Host Name</td>
      <td>DESKTOP-RNV09AT</td>
    </tr>
    <tr>
      <td>Client MAC Address</td>
      <td>18:3d:a2:b6:8d:c4</td>
    </tr>
    <tr>
      <td>Date/Time Detected</td>
      <td>2024-09-04 17:35 UTC</td>
    </tr>
    <tr>
      <td>Internal IP Address</td>
      <td>172.17.0.99</td>
    </tr>
    <tr>
      <td>External IP Address </td>
      <td>79.124.78.197</td>
    </tr>
    <tr>
      <td>Malware</td>
      <td>Win32/Koi Stealer</td>
    </tr>
  </tbody>
</table>

Pada tanggal **4 September 2024**, beberapa host internal di jaringan PT. ABC menunjukkan aktivitas yang mencurigakan dalam lalu lintas jaringan, berdasarkan file PCAP yang dianalisis. Salah satu host dengan IP `172.17.0.99` terlihat cukup aktif melakukan komunikasi, baik dengan IP eksternal maupun internal, dan aktivitasnya terpantau cukup intensif.

Dari hasil analisis lebih lanjut, host ini secara terus-menerus mengirimkan **HTTP POST request** ke **file foots.php** yang berada di IP eksternal `79.124.78.197`. Setelah dicek melalui layanan VirusTotal, IP tersebut dikategorikan sebagai berbahaya (malicious). Aktivitas ini mengindikasikan bahwa host `172.17.0.99` kemungkinan besar telah terinfeksi **malware**, dan sedang menjalankan operasi **Command-and-Control (C2)**.

---

## **INDICATOR OF COMPROMISE (IOC)**

<table class="table-terminal">
  <thead>
    <tr>
      <th>Type</th>
      <th>Value</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Internal IP</strong></td>
      <td>172.17.0.99</td>
      <td>Host yang terinfeksi dan menjadi sumber komunikasi mencurigakan dalam jaringan.</td>
    </tr>
    <tr>
      <td><strong>External IP</strong></td>
      <td>79.124.78.197</td>
      <td>Alamat IP tujuan dari aktivitas HTTP POST; dikategorikan sebagai malicious oleh VirusTotal.</td>
    </tr>
    <tr>
      <td><strong>URL</strong></td>
      <td>http://79.124.78.197/foots.php</td>
      <td>Endpoint command-and-control (C2) yang menerima request dari host terinfeksi.</td>
    </tr>
    <tr>
      <td><strong>URL</strong></td>
      <td>http://79.124.78.197/index.php</td>
      <td>Berisi token beacon C2 dari malware Win32/Koi Stealer.</td>
    </tr>
    <tr>
      <td><strong>Malware</strong></td>
      <td>Win32/Koi Stealer</td>
      <td>Jenis malware yang terindikasi dari pola komunikasi dan token dalam traffic.</td>
    </tr>
    <tr>
      <td><strong>HTTP Method</strong></td>
      <td>POST</td>
      <td>Metode permintaan yang digunakan malware untuk komunikasi dengan server eksternal.</td>
    </tr>
    <tr>
      <td><strong>Content-Type</strong></td>
      <td>application/octet-stream</td>
      <td>Format data biner yang digunakan untuk mengirim command atau data curian.</td>
    </tr>
    <tr>
      <td><strong>Content-Encoding</strong></td>
      <td>binary</td>
      <td>Encoding data POST—umum digunakan dalam komunikasi malware.</td>
    </tr>
    <tr>
      <td><strong>User-Agent</strong></td>
      <td>Mozilla/4.0 (MSIE 7.0; Windows NT 10.0; WOW64...)</td>
      <td>String agen pengguna palsu dan usang, sering digunakan malware untuk menghindari deteksi.</td>
    </tr>
    <tr>
      <td><strong>Token</strong></td>
      <td>HckDcK0czXjqa48jVHNm|qIOuKk7U|http://79.124.78.197/index.php</td>
      <td>Beacon C2 khas milik Koi Stealer, menunjukkan komunikasi awal antara malware dan server.</td>
    </tr>
    <tr>
      <td><strong>MAC Address</strong></td>
      <td>18:3d:a2:b6:8d:c4</td>
      <td>Alamat fisik perangkat yang terinfeksi di jaringan PT. ABC.</td>
    </tr>
  </tbody>
</table>

---

## **PROOF OF CONCEPT (POC)**

### HTTP POST Request

Pada file 2024-09-04-traffic-analysis-exercise.pcap, terdeteksi permintaan **HTTP POST** dalam jumlah banyak dari host internal `172.17.0.99` ke IP eksternal `79.124.78.197` menuju endpoint **/foots.php**.

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/HTTP-POST:79.124.78.197.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/HTTP-POST:79.124.78.197.png)
*<center>$\pmb{\text{Gambar 1}}$: Contoh HTTP POST request yang dikirim oleh host <code>172.17.0.99</code> ke server berbahaya <code>79.124.78.197</code>. Aktivitas ini terlihat jelas di file <code>2024-09-04-traffic-analysis-exercise.pcap</code> dan merupakan bagian dari komunikasi C2 yang dilakukan malware Win32/Koi Stealer.</center>*

Permintaan yang dikirimkan oleh host `172.17.0.99` ke server eksternal menggunakan **HTTP POST** dengan header **Content-Type: application/octet-stream** dan **Content-Encoding: binary**. Format seperti ini umum digunakan dalam komunikasi **Command-and-Control (C2)** oleh malware, karena memungkinkan **pengiriman data biner yang bisa berisi perintah dari server penyerang** ataupun data yang dicuri dari sistem korban.

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/HTTP-POST-Header.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/HTTP-POST-Header.png)
*<center>$\pmb{\text{Gambar 2}}$: Header dari HTTP POST request yang digunakan malware. Terlihat <code>Content-Type: application/octet-stream</code> dan <code>Content-Encoding: binary</code>, format yang umum dipakai malware untuk mengirim data biner atau menerima perintah dari server C2.</center>*

Menariknya, permintaan ini ditujukan ke endpoint **foots.php**, yang ditulis menggunakan PHP. Penggunaan PHP sebagai endpoint merupakan taktik yang cukup umum dalam komunikasi malware atau web shell, karena PHP dapat dengan mudah menangani permintaan dan respons secara dinamis, baik untuk menerima perintah maupun mengirimkan hasil curian ke attacker.

---

### User-Agent String

Salah satu hal yang mencolok dari komunikasi mencurigakan ini adalah **User-Agent string** yang digunakan, yaitu:
> `Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729)`

User-Agent ini tergolong usang dan tidak lazim ditemukan di lingkungan modern, terutama pada sistem dengan Windows 10. Hal ini menjadi indikator tambahan bahwa traffic tersebut kemungkinan berasal dari aplikasi yang dipalsukan atau digunakan oleh malware untuk menyamarkan diri agar terlihat seperti aplikasi lama dan sah.

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/String-Agent.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/String-Agent.png)
*<center>$\pmb{\text{Gambar 3}}$: User-Agent string yang digunakan oleh malware di dalam request. String ini usang dan tidak wajar (<code>Mozilla/4.0 (MSIE 7.0; Windows NT 10.0; WOW64...)</code>), salah satu trik agar traffic malware terlihat seperti traffic normal dari aplikasi lama.</center>*

#### Detail User-String Agen
<table class="table-terminal">
  <thead>
    <tr>
      <th>Type</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>MSIE 7.0</td>
      <td>Menunjukkan penggunaan Internet Explorer 7, yang dirilis pada tahun 2006.</td>
    </tr>
    <tr>
      <td>.NET CLR 2.0.50727</td>
      <td>Menunjukan penggunaan .NET Framework 2.0, rilis tahun 2005.</td>
    </tr>
    <tr>
      <td>Windows NT 10.0; WOW64</td>
      <td>Mengindikasikan OS Windows 10 versi 64-bit.</td>
    </tr>
  </tbody>
</table>

Jika dilihat secara keseluruhan, kombinasi string ini tidak masuk akal secara teknis. Internet Explorer 7 dan .NET versi lama tidak wajar digunakan bersamaan dengan Windows 10, kecuali memang sengaja disusun untuk menyamarkan aktivitas malware. Ini adalah taktik umum malware, yaitu berpura-pura menjadi aplikasi atau browser lama agar lalu lintasnya tidak terlalu mencolok dalam sistem monitoring yang fokus pada signature modern. Selain itu, string seperti ini kadang digunakan untuk mengeksploitasi kerentanan lama pada server target yang masih rentan terhadap user-agent lawas.

---

### Indikasi Win32/Koi Stealer

Pada log jaringan, terlihat adanya akses ke URL berikut:

    http://79.124.78.197/index.php

Ketika dianalisis lebih lanjut, file index.php mengandung sebuah token:

    HckDcK0czXjqa48jVHNm|qIOuKk7U|http://79.124.78.197/index.php

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Indikasi-Win32.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Indikasi-Win32.png)
*<center>$\pmb{\text{Gambar 4}}$: Token yang ditemukan dalam komunikasi ke <code>http://79.124.78.197/index.php</code>. Pola token ini sangat mirip dengan beacon C2 yang digunakan oleh Win32/Koi Stealer saat pertama kali melakukan handshake dengan server C2.</center>*

Token ini sangat mirip dengan pola **C2 beacon** (penanda komunikasi Command-and-Control) yang biasa digunakan oleh **malware Koi Stealer**. Beacon seperti ini biasanya digunakan untuk melakukan **handshake** awal antara malware yang sudah terpasang di host korban dengan server pengendali (attacker).

Struktur token yang terdiri dari beberapa bagian dipisahkan oleh tanda `|` menunjukkan bahwa ada parameter identifikasi atau autentikasi yang dikirimkan oleh malware untuk memberitahu server bahwa infeksi berhasil. Biasanya, string seperti ini memuat ID unik, status sistem korban, atau URL callback yang akan digunakan untuk komunikasi selanjutnya.

Fakta bahwa token ini muncul dalam komunikasi HTTP ke IP yang sudah dikonfirmasi berbahaya semakin memperkuat dugaan bahwa sistem telah terinfeksi Koi Stealer dan aktif menjalin koneksi dengan server penyerang untuk menerima perintah lanjutan atau mengirimkan data yang dicuri.

---

### Analisa VirusTotal

Untuk memperkuat analisis dan validasi terhadap aktivitas mencurigakan dari host `172.17.0.99`, dilakukan pengecekan reputasi terhadap IP tujuan utama `79.124.78.197` menggunakan layanan **VirusTotal** (<a href="www.virustotal.com">www.virustotal.com</a>).

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Analisa-VirusTotal.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Analisa-VirusTotal.png)
*<center>$\pmb{\text{Gambar 5}}$: Hasil pengecekan reputasi IP <code>79.124.78.197</code> di VirusTotal. IP ini sudah ditandai sebagai malicious oleh beberapa vendor keamanan, yang semakin memperkuat dugaan bahwa IP ini memang dipakai untuk aktivitas C2 dan distribusi malware.</center>*

Hasil pencarian menunjukkan bahwa IP tersebut telah ditandai sebagai **malicious** oleh sejumlah vendor keamanan yang kredibel seperti **BitDefender**, **G-Data**, **CyRadar**, dan **alphaMountain.ai** . Banyaknya deteksi positif dari berbagai engine keamanan menunjukkan bahwa IP ini memang telah terlibat dalam berbagai aktivitas berbahaya, seperti **penyebaran malware**, **command-and-control server**, hingga **phishing**.

Berdasarkan hasil analisis teknis dan korelasi dengan reputasi IP, 79.124.78.197 kemungkinan besar berperan dalam satu atau lebih dari fungsi berikut dalam infrastruktur serangan:

#### 1. Server Command-and-Control (C2)

IP ini sangat mungkin digunakan oleh penyerang sebagai server Command-and-Control, yaitu pusat kendali yang digunakan untuk mengirim perintah ke sistem yang sudah terinfeksi—dalam hal ini, host 172.17.0.99. Komunikasi dilakukan melalui permintaan HTTP POST secara berulang ke endpoint /foots.php, yang merupakan pola umum dalam skenario C2. Server ini dapat menginstruksikan malware untuk melakukan berbagai aksi seperti mencuri kredensial, mengambil screenshot, hingga mengunduh file berbahaya lainnya.

#### 2. Titik Distribusi Malware

Walaupun tidak langsung terlihat pada log (PCAP) yang dianalisis, IP berbahaya seperti ini sering juga berfungsi sebagai host untuk menyebarkan payload malware. Dengan kata lain, selain mengontrol sistem yang terinfeksi, server ini bisa saja digunakan untuk menyebarkan file berbahaya yang dikamuflase sebagai installer, dokumen, atau aplikasi palsu kepada korban lain dalam kampanye serangan yang sama.

#### 3. Endpoint Eksfiltrasi Data

IP ini juga sangat mungkin digunakan sebagai endpoint eksfiltrasi data. Malware yang aktif di host korban dapat mengumpulkan data sensitif seperti username/password, file penting, history browser, atau bahkan clipboard, lalu mengirimkannya dalam format binary menggunakan Content-Type: application/octet-stream. Fakta bahwa komunikasi ini terjadi secara terus-menerus (bukan hanya satu kali) menunjukkan bahwa infeksi bersifat persisten dan sedang dikendalikan secara aktif dari jarak jauh.

---

### Affected Host

Host ini merupakan perangkat internal dalam jaringan PT. ABC yang terdeteksi melakukan aktivitas mencurigakan berdasarkan hasil analisis file log 2024-09-04-traffic-analysis-exercise.pcap.

<table class="table-terminal">
  <thead>
    <tr>
      <th>Type</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>IP Address</strong></td>
      <td>172.17.0.99</td>
    </tr>
    <tr>
      <td><strong>MAC Address</strong></td>
      <td>18:3d:a2:b6:8d:c4</td>
    </tr>
  </tbody>
</table>

Perangkat ini secara aktif melakukan komunikasi ke IP eksternal yang telah terverifikasi sebagai **malicious**, yaitu `79.124.78.197`. Komunikasi tersebut berupa **HTTP POST** dalam jumlah besar dengan pola yang khas digunakan oleh malware, yang mengindikasikan bahwa host ini telah terinfeksi dan kemungkinan menjadi bagian dari operasi **Command-and-Control (C2)**.

MAC address 18:3d:a2:b6:8d:c4 mengidentifikasi secara unik perangkat ini di dalam jaringan lokal.

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Affected-Host.png){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Affected-Host.png)
*<center>$\pmb{\text{Gambar 6}}$: Informasi host yang terinfeksi. Host <code>172.17.0.99</code> dengan MAC address <code>18:3d:a2:b6:8d:c4</code> teridentifikasi sebagai sumber utama aktivitas komunikasi mencurigakan di jaringan PT. ABC.</center>*

---

### Security Alert 

Alert ini berasal dari file 2024-09-04-traffic-analysis-exercise-alerts.txt, yang berisi hasil pemantauan lalu lintas jaringan oleh sistem deteksi intrusi (IDS). Alert ini mengindikasikan adanya aktivitas berbahaya dari host internal 172.17.0.99 yang mencoba melakukan komunikasi Command-and-Control (C2) dengan IP eksternal 79.124.78.197.

```bash
------------------------------------------------------------------------
Count:48 Event#3.1504 First seen: 2024-09-04 17:35 UTC
ETPRO TROJAN Win32/Koi Stealer CnC Checkin (POST) M2
172.17.0.99 -> 79.124.78.197
IPVer=4 hlen=5 tos=0 dlen=429 ID=0 flags=0 offset=0 ttl=0 chksum=28310
Protocol: 6 sport=49813 -> dport=80

Seq=0 Ack=0 Off=5 Res=0 Flags=******** Win=0 urp=36144 chksum=0
```

[![img1]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Security-Alert.jpg){:class="img-responsive"}]({{ site.baseurl }}/assets/images/log-analisis:PT_ABC/Security-Alert.jpg)
*<center>$\pmb{\text{Gambar 7}}$: Salah satu alert yang muncul di IDS berdasarkan file <code>2024-09-04-traffic-analysis-exercise-alerts.txt</code>. Alert ini mengonfirmasi adanya komunikasi C2 yang dilakukan oleh malware Win32/Koi Stealer dari host <code>172.17.0.99</code> ke server berbahaya.</center>*

Signature alert:
> **ETPRO TROJAN Win32/Koi Stealer CnC Checkin (POST) M2**

Menunjukkan bahwa pola komunikasi yang terdeteksi sangat cocok dengan ciri khas malware Koi Stealer saat melakukan proses check-in ke server pengendali. Ini merupakan fase awal dari serangan, di mana malware memberitahukan kehadirannya ke attacker dan siap menerima instruksi lanjutan.

---

## **URL GENERATING THE ALERT TRAFFIC**

Daftar URL berikut merupakan endpoint yang digunakan oleh malware untuk berkomunikasi dengan server eksternal. Ketiga URL ini terekam dalam log dan alert keamanan, dan semuanya mengarah ke IP yang telah dikonfirmasi sebagai malicious (`79.124.78.197`):

- http://79.124.78.197/index.php?id&subid=qIOuKk7U
- http://79.124.78.197/index.php
- http://79.124.78.197/foots.php

---

## **RISK ASSESMENT**

<table class="table-terminal">
  <thead>
    <tr>
      <th>Kategori</th>
      <th>Penilaian</th>
      <th>Keterangan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Kemungkinan Infeksi</strong></td>
      <td>Dikonfirmasi</td>
      <td>Host `172.17.0.99` mengirim HTTP POST ke IP eksternal berbahaya dan terdeteksi oleh signature malware Koi Stealer.</td>
    </tr>
    <tr>
      <td><strong>Potensi Dampak</strong></td>
      <td>Tinggi</td>
      <td>Aktivitas C2 berpotensi menyebabkan pencurian data, kontrol penuh atas host, dan penyebaran ke sistem lain.</td>
    </tr>
    <tr>
      <td><strong>Potensi Penyebaran</strong></td>
      <td>Sedang</td>
      <td>Ditemukan aktivitas SMB internal; potensi penyebaran tergantung hak akses dan konfigurasi sistem lain.</td>
    </tr>
    <tr>
      <td><strong>Stealth Level</strong></td>
      <td>Sedang</td>
      <td>Koneksi menggunakan HTTP biasa dengan payload kecil dan endpoint generik (foots.php), tanpa enkripsi.</td>
    </tr>
  </tbody>
</table>

---

## **MITIGATION**

Host Terinfeksi (172.17.0.99):
- Melakukan isolasi dari jaringan (untuk mencegah penyebaran malwere).
- Melakukan pemindaian malware secara menyeluruh menggunakan antivirus (misalnya Windows Defender, Malwarebytes, atau toolkit forensik).
- Membersihkan atau melakukan install ulang (re-image).

Keamanan Jaringan:
- Memblokir seluruh lalu lintas ke/dari IP `79.124.78.197`.
- Mencari di log apakah ada mesin internal lain yang juga berkomunikasi dengan IP `79.124.78.197`.
- Membatasi akses keluar (outbound traffic) dari jaringan hanya ke layanan atau domain yang sah.

---

## **REFERENCES**
- File PCAP: [2024-09-04-traffic-analysis-exercise.pcap](/assets/file/log-serangan/PT-ABC/2024-09-04-traffic-analysis-exercise.pcap)
- IDS Alert Log: [2024-09-04-traffic-analysis-exercise-alerts.tx](/assets/file/log-serangan/PT-ABC/2024-09-04-traffic-analysis-exercise-alerts.txt)
- VirusTotal IP Reputation: <a href="https://www.virustotal.com/gui/ip-address/79.124.78.197">https://www.virustotal.com/gui/ip-address/79.124.78.197</a>

---

## **CONCLUSION**

Berdasarkan analisis terhadap file PCAP dan alert IDS, dapat disimpulkan bahwa
host 172.17.0.99 telah terinfeksi malware jenis Win32/Koi Stealer. Malware ini aktif melakukan komunikasi ke C2 server, menyalahgunakan protokol internal, serta menyusun domain palsu untuk aktivitas AD spoofing. Semua aktivitas telah tervalidasi melalui traffic analysis dan threat intelligence eksternal

#IDNBootcampCyber