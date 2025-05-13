Demo Trojan Uygulaması

trojan/dist/trojan_cmd.exe adlı dosyayı çalıştırınca cmd ekranı açılıp ekranda "kriptoloji" yazan ve 3 saniye sonra kapanan uygulama
Nasıl Yapıldı?
main.py dosyasını açtıktan sonra terminale: pyinstaller --onefile trojan_cmd.py komutunu vererek derlemesini sağladık.
eğer pyinstaller yüklü değilse terminale: pip install pyinstaller komutunu vererek yüklüyoruz.
