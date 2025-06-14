---
layout: post
title: Brute Force File ZIP
category: Cyber-Security
lang: IN
description: Simple Brute Force
---

## Pengantar

Kalau denger kata “brute force,” mungkin yang kebayang langsung: hacker, kode rumit, dan film aksi. Padahal, prinsipnya sederhana banget. Brute force itu cuma teknik coba-coba tebak password satu per satu sampai dapet yang benar.

Di tutorial ini, kita akan belajar bikin tools brute force sendiri buat nyoba ngebuka file ZIP yang dikunci password. Tapi penting ya: ini bukan buat iseng buka file orang. Ini semata-mata buat belajar, biar kita makin paham gimana keamanan digital itu bekerja dari dalam.

## 📌 Daftar Isi
1. [Persiapan](#persiapan)
2. [Kode Program](#kode-program)
   - [Script Brute Force](#script-brute-force)
3. [Cara Menjalankan Script](#cara-menjalankan-script)
4. [Kesimpulan](#kesimpulan)

---

Jadi, kenapa kita belajar ini? Karena kadang, biar paham cara ngelindungi sesuatu, kita juga harus ngerti cara nyerangnya. Brute force adalah salah satu serangan paling basic dalam dunia keamanan siber. Meskipun kelihatan simpel, teknik ini bisa jadi ancaman kalau sistem gak dilindungi dengan baik—contohnya kalau password-nya gampang ditebak.

Dalam kasus kita, kita akan coba buka file ZIP yang dilindungi password. File ZIP ini biasa banget dipake buat kompres data atau kirim file lewat email. Dan percaya deh, banyak orang masih suka pake password kayak “123456” atau “admin”. Nah, di situlah brute force bisa jadi efektif.

## Persiapan

Sebelum mulai ngoding, ada beberapa hal yang perlu disiapkan. Gak ribet kok:
1. File ZIP yang dikunci password.

    [Unduh file zip: protected.zip](/assets/file/brute-force-zip/protected.zip)

2. File wordlist. Isinya daftar password yang mau kita coba satu-satu.

    [Unduh file wordlist: rockyou.txt](/assets/file/brute-force-zip/rockyou.txt)

3. Python 3. Gak perlu install library aneh-aneh, karena kita pakai modul bawaan.
4. Text editor buat nulis script-nya. Mau pakai VSCode, Nano, atau Notepad juga boleh.

Anggap aja ini kayak nyiapin bahan masakan sebelum mulai masak, biar gak ribet di tengah jalan.

--- 

## Kode Program

Nah, ini bagian utamanya. Kita akan bikin script Python yang bisa coba password satu per satu dari wordlist ke file ZIP. Gak perlu tqdm, gak perlu GUI, cukup pakai logika dasar dan zipfile dari Python.

Simpelnya, ini kayak kamu nyoba kombinasi gembok satu-satu sampai kebuka. Bedanya, komputer yang nyoba. Dan pastinya, lebih cepet daripada tangan manusia.

Kodenya nanti akan ngebaca file ZIP, buka wordlist, terus nyobain semua password sampai nemu yang cocok. Kalau cocok, tadaa! Password ketemu. Kalau gak? Ya kita tau bahwa wordlist-nya belum cukup kuat.

### Script Brute Force:
```bash
import zipfile

def brute_force_zip(zip_path, wordlist_path):
    try:
        zip_file = zipfile.ZipFile(zip_path)
    except FileNotFoundError:
        print(f"[!] File ZIP tidak ditemukan: {zip_path}")
        return
    except zipfile.BadZipFile:
        print(f"[!] File ZIP rusak atau tidak valid: {zip_path}")
        return

    try:
        with open(wordlist_path, 'r', encoding='utf-8') as wordlist:
            for line in wordlist:
                password = line.strip()
                try:
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    print(f"[+] Password ditemukan: '{password}'")
                    return
                except RuntimeError:
                    print(f"[-] Gagal dengan password: '{password}'")
                except Exception as e:
                    print(f"[!] Error tak terduga: {e}")
    except FileNotFoundError:
        print(f"[!] Wordlist tidak ditemukan: {wordlist_path}")

    print("[-] Password tidak ditemukan dalam wordlist.")

def main():
	zip_path = str(input("Masukan Path File: "))
	wordlist_path = str(input("Masukan Path WordList: "))
	brute_force_zip(zip_path, wordlist_path)
if __name__ == "__main__":
    main()
```

## Cara Menjalankan Script

Setelah semua disiapin dan script-nya udah ditulis, cara makainya juga simpel banget.
1. Simpan script Python-nya, misalnya dengan nama brute_force_zip.py.
2. Pastikan file ZIP dan wordlist ada di folder yang sama.
3. Jalankan lewat terminal:

    ```bash
    python3 brute_force_zip.py
    ```

Nanti akan muncul di layar password apa aja yang dicoba, dan bakal ada notifikasi begitu password-nya berhasil.

Ini kayak main tebak-tebakan yang dicatat langsung sama komputer.

Output dari script-nya mirip kayak ini:
```bash
Masukan Path File: protected.zip
Masukan Path WordList: rockyou.txt
[-] Gagal dengan password: '123456'
[-] Gagal dengan password: 'password'
[-] Gagal dengan password: 'admin'
[-] Gagal dengan password: 'letmein'
[+] Password ditemukan: 'qwerty'
```

Setiap kali gagal, dia bakal kasih info password mana yang dicoba. Begitu nemu yang pas, dia langsung berhenti. Praktis dan to the point.

---

## Kesimpulan

Dari sini, kita belajar bahwa ngejalanin brute force itu bukan hal rumit, yang penting tahu tujuannya dan batasnya. Dengan modal Python dan logika sederhana, kita udah bisa bikin tool sendiri buat nyoba password file ZIP.

Semoga setelah ini kamu bisa lebih ngeh: kenapa pakai password yang kuat itu penting, dan kenapa enkripsi itu bukan cuma aksesoris. Karena kalau bisa dibobol pakai wordlist seadanya, artinya ada yang perlu dibenerin dari sisi keamanan.

#IDNBootcampCyber