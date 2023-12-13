import os

def dosyalari_tara(dizin, max_derinlik, mevcut_derinlik=0):
    # Eğer maksimum derinliğe ulaşıldıysa, daha fazla tarama yapma
    if mevcut_derinlik > max_derinlik:
        return []

    # Taranan dizin bir dizin olmalıdır, değilse boş liste dön
    if not os.path.isdir(dizin):
        print(f"Hata: '{dizin}' bir dizin değil.")
        return []

    dosyalar_ve_klasorler = []
    try:
        with os.scandir(dizin) as it:
            for giris in it:
                if giris.is_dir(follow_symlinks=False):
                    # Özyinelemeli olarak alt klasörleri tara
                    dosyalar_ve_klasorler.extend(dosyalari_tara(giris.path, max_derinlik, mevcut_derinlik + 1))
                else:
                    dosyalar_ve_klasorler.append(giris.path)
    except NotADirectoryError as e:
        print(f"Hata: {e}")
    except PermissionError as e:
        print(f"Erişim reddedildi: {e}")
    return dosyalar_ve_klasorler

# Örnek kullanım:
if __name__ == "__main__":
    dizin = "/Users/berkegulacar/Downloads"
    max_derinlik = 2
    bulunan_dosyalar = dosyalari_tara(dizin, max_derinlik)
    print(bulunan_dosyalar)
