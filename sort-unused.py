import os
import time

def dosyalari_tara(dizin, max_derinlik=0, mevcut_derinlik=0):
    # Mevcut zamanı al
    suanki_zaman = time.time()
    dosyalar_ve_klasorler = []

    try:
        # Dizindeki dosya ve klasörleri yürü
        with os.scandir(dizin) as it:
            for giris in it:
                if giris.is_file():
                    # Son değiştirilme zamanını al ve güne çevir
                    son_degistirme = os.path.getmtime(giris.path)
                    gun_farki = (suanki_zaman - son_degistirme) / 86400
                    if gun_farki > esik_gun:
                        dosyalar_ve_klasorler.append(giris.path)
                elif giris.is_dir():
                    # Klasörler için ayrı bir kontrol
                    dosyalar_ve_klasorler.append(giris.path)
                    # Eğer derinlik sınırlaması varsa ve mevcut derinlik max'e ulaşmamışsa, klasör içine dal
                    if max_derinlik == 0 or mevcut_derinlik < max_derinlik:
                        dosyalar_ve_klasorler.extend(dosyalari_tara(giris.path, max_derinlik, mevcut_derinlik + 1))
    except PermissionError:
        # Yetki hatası durumunda bu dizini atla
        pass

    return dosyalar_ve_klasorler

# Tarama ilerlemesini göster
def tarama_ilerlemesi(dosyalar, toplam_dosya):
    for i, dosya in enumerate(dosyalar, start=1):
        print(f"Tarama ilerlemesi: {i}/{toplam_dosya} | {dosya}")
        time.sleep(0.1)  # İlerlemeyi gözlemlemek için küçük bir gecikme

if __name__ == "__main__":
    dizin = input("Lütfen taramak istediğiniz dizini girin: ")
    esik_gun = float(input("Kaç günden eski dosyaları listelemek istiyorsunuz? "))
    
    # Ana dizin kontrolü ve derinlik sınırlaması
    max_derinlik = 0
    if dizin == "/":
        max_derinlik = 3

    if os.path.isdir(dizin):
        bulunan_dosyalar = dosyalari_tara(dizin, max_derinlik)
        if bulunan_dosyalar:
            tarama_ilerlemesi(bulunan_dosyalar, len(bulunan_dosyalar))
        else:
            print("Belirtilen kriterlere uygun dosya veya klasör bulunamadı.")
    else:
        print("Girilen dizin mevcut değil.")
