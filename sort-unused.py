import os
import time

def eski_dosyalari_listele(dizin):
    # Mevcut zamanı al
    suanki_zaman = time.time()

    # Dizindeki dosya ve klasörleri yürü
    dosyalar = [os.path.join(dizin, f) for f in os.listdir(dizin)]
    
    # Toplam dosya sayısı
    toplam_dosya = len(dosyalar)
    print(f"{toplam_dosya} dosya bulundu. Tarama başlıyor...")

    # Taranan dosya sayısı
    taranan_dosya = 0

    # Dosyaları listele
    for dosya in dosyalar:
        try:
            # Son değiştirilme zamanını al
            son_degistirme = os.path.getmtime(dosya)
            gun_farki = (suanki_zaman - son_degistirme) / 86400  # saniyeyi güne çevir

            # Eğer dosya 1 haftadan (yaklaşık 7 günden) eskiyse yazdır
            if gun_farki > 7:
                print(f"{dosya} en son {int(gun_farki)} gün önce değiştirilmiş.")
        except OSError as e:
            print(f"Hata: {e}")

        taranan_dosya += 1
        print(f"Tarama ilerlemesi: {taranan_dosya}/{toplam_dosya} dosya tarandı.", end='\r')

    print("\nTarama tamamlandı.")

if __name__ == "__main__":
    dizin = input("Lütfen taramak istediğiniz dizini girin: ")
    if os.path.isdir(dizin):
        eski_dosyalari_listele(dizin)
    else:
        print("Girilen dizin mevcut değil.")