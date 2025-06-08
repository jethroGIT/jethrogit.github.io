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
