import os
import time

def dosyalari_tara(dizin, kullanilmayan_sure=30):
    if not os.path.isdir(dizin):
        return []

    dosyalar_ve_klasorler = []
    simdiki_zaman = time.time()
    kullanilmayan_zaman = kullanilmayan_sure * 86400

    for root, _, files in os.walk(dizin):
        for name in files:
            dosya_yolu = os.path.join(root, name)
            try:
                if (simdiki_zaman - os.stat(dosya_yolu).st_atime) > kullanilmayan_zaman:
                    dosyalar_ve_klasorler.append(dosya_yolu)
            except FileNotFoundError:
                pass

    return dosyalar_ve_klasorler

def dosya_boyutunu_al(dosya_yolu):
    try:
        return os.path.getsize(dosya_yolu)
    except FileNotFoundError:
        return 0

if __name__ == "__main__":
    dizin = input("Lütfen taranacak dizini girin: ")
    kullanilmayan_sure = int(input("Kaç günden beri kullanılmayan dosyalar listelensin? (gün cinsinden): "))
    
    print("Tarama başladı...")
    bulunan_dosyalar = dosyalari_tara(dizin, kullanilmayan_sure)
    print("Tarama tamamlandı.")

    bulunan_dosyalar = sorted(
        bulunan_dosyalar,
        key=dosya_boyutunu_al,
        reverse=input("Dosyaları artan boyuta göre sıralamak için 'a', azalan boyuta göre için 'z' girin: ").lower() == 'z'
    )

    if bulunan_dosyalar:
        print("Kullanılmayan dosyaların listesi:")
        for dosya in bulunan_dosyalar:
            print(dosya)
    else:
        print("Kriterlere uyan dosya bulunamadı.")
