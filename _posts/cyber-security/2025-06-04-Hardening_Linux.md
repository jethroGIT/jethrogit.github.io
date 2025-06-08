---
layout: post
title: Hardening SSH Service Ubuntu Server 20.04 LTS
category: Cyber-Security
lang: IN
description: Hardening Linux Security
---

## **Pengantar** 

Pada artikel kali ini, saya akan membahas secara rinci tentang hardening SSH (Secure Shell) di sistem operasi Linux, mulai dari pengertian SSH, peran pentingnya dalam pengelolaan server jarak jauh, hingga berbagai teknik dan konfigurasi yang dapat diterapkan untuk memperkuat keamanannya. Selain itu, saya juga akan mengulas beberapa contoh praktik terbaik (best practice) serta potensi risiko keamanan jika konfigurasi SSH dibiarkan dalam kondisi default.


## 📌 Daftar Isi

1. [Apa itu SSH?](#apa-itu-ssh)
2. [Kenapa SSH Penting?](#kenapa-ssh-penting)
3. [Ancaman Umum terhadap SSH](#ancaman-umum-terhadap-ssh)
   - [1. Brute-force Attack](#1-brute-force-attack)
   - [2. Credential Stuffing](#2-credential-stuffing)
   - [3. Man-in-the-Middle (MitM) Attack](#3-man-in-the-middle-mitm-attack)
   - [4. Penyalahgunaan oleh Akun Internal](#4-penyalahgunaan-oleh-akun-internal)
4. [Persiapan Awal](#persiapan-awal)
   - [Update Sistem](#update-sistem)
   - [Backup Konfigurasi](#backup-konfigurasi)
   - [Tools yang Digunakan](#tools-yang-digunakan)
5. [Konfigurasi Hardening SSH](#konfigurasi-hardening-ssh)
   - [Nonaktifkan Login Root](#nonaktifkan-login-root)
   - [Gunakan SSH Key, Nonaktifkan Password Login](#gunakan-ssh-key-nonaktifkan-password-login)
   - [Ganti Port Default SSH](#ganti-port-default-ssh)
   - [Batasi Akses User dan IP](batasi-akses-user-dan-ip)
   - [Konfigurasi Timeout & Connection Settings](#konfigurasi-timeout--connection-settings)
   - [Logging SSH](#logging-ssh)
   - [Implementasi Fail2Ban](#implementasi-fail2ban)
6. [Uji Konfigurasi SSH](#uji-konfigurasi-ssh)
   - [Cek Syntax Config](#cek-syntax-config)
   - [Restart SSH Service](#restart-ssh-service)
   - [Tes Login dengan SSH Key](#tes-login-dengan-ssh-key)
7. [Kesimpulan](#kesimpulan)
   - [Pentingnya Hardening SSH Sebagai Bagian dari Hardening Sistem Linux Secara Umum](#pentingnya-hardening-ssh-sebagai-bagian-dari-hardening-sistem-linux-secara-umum)
   - [Langkah-Langkah Praktis yang Sudah Dibahas](#langkah-langkah-praktis-yang-sudah-dibahas)

## Apa itu SSH?

SSH (Secure Shell) adalah protokol jaringan yang digunakan untuk mengakses dan mengelola sistem komputer secara remote melalui jaringan yang tidak aman, seperti internet. SSH memungkinkan pengguna untuk melakukan login ke server jarak jauh dan menjalankan perintah-perintah secara aman, berkat penggunaan enkripsi yang melindungi data yang ditransfer.

Secara umum, SSH menggantikan protokol lama seperti Telnet atau rlogin, yang mentransmisikan data dalam bentuk *plain text* tanpa enkripsi. Dengan SSH, seluruh komunikasi (termasuk username, password, dan perintah yang dijalankan) dienkripsi sehingga jauh lebih aman.

## Kenapa SSH Penting?

SSH sangat penting karena merupakan salah satu jalur utama yang digunakan untuk mengelola server Linux, baik di lingkungan pengembangan, staging, maupun produksi. Melalui SSH, administrator dapat melakukan berbagai tugas, seperti:

- Memantau performa server
- Mengelola file dan konfigurasi
- Memasang atau memperbarui perangkat lunak
- Menangani troubleshooting

Karena fungsinya yang krusial ini, SSH hampir selalu dibuka di server yang dikelola jarak jauh, menjadikannya target utama bagi para penyerang. Oleh sebab itu, memastikan konfigurasi SSH aman (atau *di-hardening*) adalah langkah yang sangat penting dalam menjaga keamanan seluruh sistem.

## Ancaman Umum terhadap SSH

Meskipun SSH menggunakan enkripsi yang kuat, tetap ada sejumlah ancaman keamanan yang sering menyerang service SSH. Berikut beberapa ancaman yang umum:

### 1. Brute-force Attack

Serangan ini mencoba menebak username dan password SSH dengan mengirimkan ribuan (bahkan jutaan) kombinasi secara otomatis. Jika server SSH mengizinkan login password tanpa pembatasan, serangan ini dapat berhasil membuka akses.

### 2. Credential Stuffing

Jika attacker memiliki daftar username dan password hasil kebocoran data di situs lain, mereka dapat mencoba kombinasi tersebut pada server SSH. Teknik ini sering lebih efektif daripada brute-force karena menggunakan kredensial yang memang pernah valid.

### 3. Man-in-the-Middle (MitM) Attack

Dalam serangan ini, attacker mencegat lalu lintas SSH antara client dan server, berusaha untuk menyadap atau bahkan memanipulasi komunikasi. Walaupun SSH memiliki mekanisme perlindungan terhadap MitM (dengan verifikasi *host key*), serangan ini masih mungkin terjadi jika pengguna mengabaikan peringatan saat koneksi awal ke server.

### 4. Penyalahgunaan oleh Akun Internal

Kadang, ancaman datang dari dalam: akun SSH yang tidak digunakan atau yang memiliki hak akses berlebihan dapat dimanfaatkan untuk serangan jika tidak dikelola dengan baik.

## Persiapan Awal

Sebelum melakukan hardening SSH, ada beberapa langkah persiapan yang penting dilakukan. Langkah-langkah ini akan membantu memastikan proses hardening berjalan aman, serta memudahkan pemulihan jika terjadi kesalahan konfigurasi.

### Update Sistem

Langkah pertama sebelum melakukan *hardening* adalah memastikan sistem operasi dan semua paket perangkat lunak berada dalam versi terbaru. Hal ini penting karena setiap update biasanya membawa perbaikan terhadap celah keamanan yang sudah diketahui.

Khusus untuk service SSH, pembaruan OpenSSH sering mencakup patch terhadap kerentanan yang bisa dieksploitasi oleh penyerang.

**Perintah untuk update sistem:**

```bash
sudo apt update && sudo apt upgrade -y
```

### Backup Konfigurasi

Sebelum melakukan perubahan pada konfigurasi SSH, sangat disarankan untuk membuat backup file konfigurasi utama, yaitu /etc/ssh/sshd_config. Backup ini akan sangat berguna apabila terjadi kesalahan konfigurasi yang menyebabkan service SSH tidak dapat diakses.

Dengan memiliki salinan konfigurasi awal, kita dapat dengan mudah mengembalikan pengaturan SSH ke kondisi semula, sehingga proses troubleshooting menjadi lebih cepat dan aman.

**Contoh perintah untuk membuat backup:**

```bash
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup
```

### Tools yang Digunakan

Untuk membantu proses hardening SSH dan meningkatkan perlindungan server, ada beberapa tools tambahan yang bisa kita manfaatkan. Beberapa di antaranya:

- #### Fail2Ban

    Tools ini berfungsi untuk memantau log SSH dan secara otomatis memblokir IP yang melakukan upaya login berulang (brute-force attack). Dengan Fail2Ban, kita dapat secara proaktif melindungi server dari serangan login yang tidak sah.

- #### UFW (Uncomplicated Firewall)

    UFW adalah firewall yang mudah dikonfigurasi dan dapat digunakan untuk mengatur akses jaringan ke server. Dengan UFW, kita bisa membatasi akses ke port SSH hanya untuk IP tertentu atau subnet yang dipercaya.

- #### iptables/nftables

    Untuk kebutuhan konfigurasi firewall yang lebih kompleks, kita dapat menggunakan iptables atau nftables. Tools ini memungkinkan kita membuat aturan yang lebih detail dalam mengontrol lalu lintas jaringan, termasuk untuk proteksi SSH.

Dengan mempersiapkan langkah-langkah awal di atas, kita akan lebih siap untuk melanjutkan ke tahap konfigurasi hardening SSH dengan aman dan terkontrol.


## Konfigurasi Hardening SSH

Setelah melakukan langkah-langkah persiapan awal, kita bisa melanjutkan ke tahap inti, yaitu konfigurasi hardening SSH. Pada bagian ini, kita akan mengubah beberapa pengaturan penting di file konfigurasi SSH untuk meningkatkan keamanannya. Setiap pengaturan yang akan kita ubah memiliki tujuan tertentu dalam memperkecil risiko serangan terhadap server.

### Nonaktifkan Login Root

Salah satu pengaturan pertama yang sangat disarankan adalah menonaktifkan kemampuan login langsung sebagai root melalui SSH. Hal ini penting karena akun root biasanya menjadi target utama dalam serangan brute-force.

Untuk menonaktifkan login root, kita bisa mengatur opsi berikut di file `/etc/ssh/sshd_config`:

```bash
PermitRootLogin no
```

Dengan pengaturan ini, hanya user non-root yang diizinkan login via SSH. Jika perlu melakukan tugas administratif, kita bisa menggunakan perintah sudo setelah login.

### Gunakan SSH Key, Nonaktifkan Password Login

Penggunaan autentikasi berbasis password lebih rentan terhadap serangan brute-force atau credential stuffing. Oleh karena itu, lebih aman menggunakan SSH key pair.

Cara membuat SSH key cukup mudah. Di sisi client, jalankan perintah:

```bash
ssh-keygen -t rsa -b 4096
```

```bash
mpls41@linuxmint:~$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mpls41/.ssh/id_rsa): 
```

```bash
mpls41@linuxmint:~$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mpls41/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
```

Contoh output kesulurahan:
```bash
mpls41@linuxmint:~$ ssh-keygen -t rsa -b 4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/mpls41/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/mpls41/.ssh/id_rsa
Your public key has been saved in /home/mpls41/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:fTtkLc1f2qZ7YDAcDS/NLUPHR61OTFxPQatF5x8zG8g mpls41@ubuntu-svr
The key's randomart image is:
+---[RSA 4096]----+
|            .+oBO|
|            o=*=B|
|           ..E*O=|
|         .  +=*oB|
|        S . =*+.o|
|           + o++.|
|            o...+|
|             . o.|
|              oo |
+----[SHA256]-----+
```

Kemudian, upload public key ke server dengan:

```bash
ssh-copy-id username@server_ip
```

Setelah SSH key sudah terpasang, kita bisa menonaktifkan autentikasi password dengan mengatur opsi berikut di file konfigurasi:

```bash
PasswordAuthentication no
```

Dengan cara ini, hanya user dengan SSH key yang valid yang dapat login ke server.

### Ganti Port Default SSH 

Secara default, SSH berjalan di port 22. Banyak bot otomatis memindai port ini untuk mencari server yang rentan. Salah satu langkah sederhana untuk mengurangi risiko serangan otomatis adalah mengganti port SSH ke port lain.

Namun, perlu diingat bahwa ini bukan solusi keamanan utama — hanya sebagai tambahan.

Kelebihannya: mengurangi jumlah serangan otomatis.
Kekurangannya: Anda perlu selalu mengingat port baru saat melakukan koneksi SSH.

Contoh konfigurasi untuk mengganti port ke 2222:

```bash
Port 2222
```

Setelah mengubah port, pastikan firewall sudah diatur untuk mengizinkan port baru ini.

### Batasi Akses User dan IP

Untuk lebih memperketat akses SSH, kita bisa membatasi hanya user atau grup tertentu yang boleh login. Ini bisa dilakukan dengan menambahkan opsi berikut:

```bash
AllowUsers user1 user2
```

Atau, jika ingin menggunakan grup:

```bash
AllowGroups sshusers
```

Selain itu, kita juga bisa memfilter berdasarkan alamat IP dengan konfigurasi Match block. Contohnya:

```bash
Match Address 192.168.1.*
    AllowUsers user1
```

Dengan konfigurasi ini, hanya user tertentu dari IP tertentu yang boleh login.

### Konfigurasi Timeout & Connection Settings

Agar koneksi SSH yang idle tidak dibiarkan terbuka terlalu lama (yang bisa meningkatkan risiko serangan), kita bisa mengatur timeout dan parameter lain yang berkaitan dengan koneksi.

Agar koneksi SSH yang idle tidak dibiarkan terbuka terlalu lama (yang bisa meningkatkan risiko serangan), kita bisa mengatur timeout dan parameter lain yang berkaitan dengan koneksi.

Beberapa pengaturan yang direkomendasikan:

```bash
ClientAliveInterval 300
```

Server akan mengirim sinyal ke client setiap 300 detik.

```bash
ClientAliveCountMax 0

```
Jika client tidak merespon, koneksi akan diputus.

```bash
LoginGraceTime 60
```

User hanya diberi waktu 60 detik untuk login, setelah itu koneksi akan ditutup.

### Logging SSH

Logging SSH sangat penting untuk memantau aktivitas login dan mendeteksi upaya serangan.

Secara default, log SSH bisa ditemukan di:

`/var/log/auth.log` (Debian/Ubuntu)

`/var/log/secure` (RHEL/CentOS/Fedora)

Kita bisa memantau log tersebut secara berkala menggunakan perintah seperti:

```bash
sudo tail -f /var/log/auth.log
```

Dengan memantau log, kita bisa segera mengetahui jika ada upaya login yang mencurigakan.

### Implementasi Fail2Ban

Selain konfigurasi manual, kita juga bisa memperkuat proteksi SSH dengan menggunakan tool tambahan seperti Fail2Ban.

Fail2Ban berfungsi memantau log SSH, dan secara otomatis memblokir IP yang mencoba melakukan brute-force attack.

Cara install Fail2Ban di Debian/Ubuntu:

```bash
sudo apt install fail2ban
```

Setelah terpasang, kita bisa mengaktifkan konfigurasi default Fail2Ban untuk SSH. Biasanya cukup dengan membuat atau menyesuaikan file jail.local:

```bash
[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 5
```

Dengan pengaturan ini, IP yang gagal login sebanyak 5 kali akan otomatis diblokir untuk sementara waktu.

---

Dengan menerapkan langkah-langkah hardening di atas, kita bisa secara signifikan meningkatkan keamanan service SSH di server Linux. Tentunya, hardening bukan proses sekali jalan — sebaiknya dilakukan review dan penyesuaian secara berkala untuk menghadapi ancaman yang terus berkembang.

## Uji Konfigurasi SSH

Setelah kita melakukan konfigurasi hardening SSH, jangan lupa untuk melakukan pengujian terlebih dahulu sebelum benar-benar memberlakukan perubahan secara permanen. Ini penting untuk memastikan bahwa semua setting berjalan sesuai harapan, dan yang paling penting — kita tidak sampai terkunci keluar dari server.

### Cek Syntax Config

Langkah pertama sebelum me-restart service SSH adalah mengecek apakah file konfigurasi SSH yang baru kita ubah tidak mengandung kesalahan sintaks.
Caranya:

```bash
sudo sshd -t
```

- Jika tidak ada output → berarti konfigurasi valid.
- Jika ada error → perbaiki terlebih dahulu sebelum melanjutkan.

Langkah ini sangat penting, karena jika konfigurasi salah, service SSH bisa gagal start, dan kamu bisa kehilangan akses ke server.

### Restart SSH Service

Setelah memastikan konfigurasi valid, lanjutkan dengan me-restart service SSH agar perubahan diterapkan:

```bash
sudo systemctl restart ssh
```

### Tes Login dengan SSH Key

Sekarang lakukan tes login dari client ke server menggunakan SSH key dan menggunakan port baru:

```bash
ssh -p 2222 username@server_ip
```

Jika proses hardening sudah benar, login akan berhasil menggunakan SSH key tanpa masalah.

## Kesimpulan

### Pentingnya Hardening SSH Sebagai Bagian dari Hardening Sistem Linux Secara Umum

SSH adalah pintu utama akses ke server Linux, terutama server yang berjalan di lingkungan cloud atau public-facing. Oleh karena itu, memperkuat keamanan SSH merupakan bagian fundamental dari strategi hardening sistem secara keseluruhan.

Tanpa hardening, service SSH bisa menjadi target empuk bagi berbagai jenis serangan seperti brute-force, credential stuffing, dan man-in-the-middle.

#### Langkah-Langkah Praktis yang Sudah Dibahas

Di artikel ini kita telah membahas langkah-langkah praktis untuk hardening SSH, mulai dari:
- Menonaktifkan login root.
- Menggunakan SSH key dan mematikan autentikasi password.
- Mengganti port default SSH.
- Membatasi user dan IP yang dapat login.
- Mengatur timeout dan parameter koneksi.
- Mengaktifkan logging.
- Mengimplementasikan proteksi tambahan menggunakan Fail2Ban.

Konfigurasi hardening bukan langkah sekali selesai. Ancaman keamanan terus berkembang, sehingga penting bagi kita untuk:
- Selalu memperbarui sistem & service SSH.
- Secara berkala meninjau konfigurasi keamanan.
- Memantau log aktivitas SSH.
- Menerapkan prinsip least privilege — hanya memberikan akses SSH kepada user yang benar-benar membutuhkan.

#IDNBootcampCyber