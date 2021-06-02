import sqlite3 as sql
import datetime
import classes as cls
import products as pro
import functions as fun
from time import sleep
from os import system


def main():
    vt = sql.connect('musteriler.sqlite')
    im = vt.cursor()
    im.execute("CREATE TABLE IF NOT EXISTS musteri (isim, soyisim,yas,il,ilce,adres,idno,parola)")
    store = cls.Store("Drakkar Computer")
    while True:
        system("cls")
        print("""
        1)Müşteri Ol
        2)Giriş Yap
                """)
        secim1 = input("Seçim : ")
        if secim1 == "1":
            system("cls")
            isim = input("İsim :")
            soyisim = input("Soyisim :")
            yas = int(input("Yaş :"))
            il = input("İl :")
            ilce = input("İlçe :")
            adres = input("Adres :")
            idno = input("ID :")
            parola = input("Parola :")
            store.musteriOl(isim, soyisim, yas, il, ilce, adres, idno, parola)
            kayitol = f"""INSERT INTO musteri VALUES ('{isim}', '{soyisim}', '{yas}','{il}', '{ilce}', '{adres}','{idno}', '{parola}')"""
            im.execute(kayitol)
            vt.commit()
        elif secim1 == "2":
            system("cls")
            idno = input("ID :")
            parola = input("Parola :")


            if im.execute(f"select * from musteri where idno='{idno}' and parola='{parola}'"):
                a = im.fetchone()
                musteri = cls.Costumer(str(a[0]), str(a[1]), a[2], str(a[3]), str(a[4]), str(a[5]), str(a[6]),
                                       str(a[7]))
                while True:
                    system("cls")
                    print("""
                [1] Bilgisayar Topla       [2] Notebook Satın Al
                                [0] Çıkış
                                        """)
                    secim2 = input("İşleminiz :")
                    if secim2 == "1":  # Bilgisayar Topla
                        system("cls")
                        tutar = 0
                        print("İşlemci Seçimi Yapınız \n\n")
                        fun.islemciListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.islemci in pro.islemciler:
                            if choice == pro.islemci.numara:
                                pro.islemci.sepet()
                                tutar += pro.islemci.fiyat
                            else:
                                continue
                        print("Anakart Seçimi Yapınız \n\n")
                        fun.anakartListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.anakart in pro.anakartlar:
                            if choice == pro.anakart.numara:
                                pro.anakart.sepet()
                                tutar += pro.anakart.fiyat
                            else:
                                continue
                        print("Bellek Seçimi Yapınız \n\n")
                        fun.bellekListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.ram in pro.rams:
                            if choice == pro.ram.numara:
                                pro.ram.sepet()
                                tutar += pro.ram.fiyat
                            else:
                                continue
                        print("Bilgisayar Kasası Seçimi Yapınız \n\n")
                        fun.kasaListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.kasa in pro.kasalar:
                            if choice == pro.kasa.numara:
                                pro.kasa.sepet()
                                tutar += pro.kasa.fiyat
                            else:
                                continue
                        print("Ekran Kartı Seçimi Yapınız \n\n")
                        fun.ekrankartiListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.ekrankarti in pro.ekrankartlari:
                            if choice == pro.ekrankarti.numara:
                                pro.ekrankarti.sepet()
                                tutar += pro.ekrankarti.fiyat
                            else:
                                continue
                        print("HDD Seçimi Yapınız \n\n")
                        fun.HDDListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.HDD in pro.HDDs:
                            if choice == pro.HDD.numara:
                                pro.HDD.sepet()
                                tutar += pro.HDD.fiyat
                            else:
                                continue
                        print("SSD Seçimi Yapınız \n\n")
                        fun.SSDListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.SSD in pro.SSDs:
                            if choice == pro.SSD.numara:
                                pro.SSD.sepet()
                                tutar += pro.SSD.fiyat
                            else:
                                continue
                        print("Monitor Seçimi Yapınız \n\n")
                        fun.monitorListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.monitor in pro.monitors:
                            if choice == pro.monitor.numara:
                                pro.monitor.sepet()
                                tutar += pro.monitor.fiyat
                            else:
                                continue
                        print("Klavye Seçimi Yapınız \n\n")
                        fun.klavyeListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.keyboard in pro.keyboards:
                            if choice == pro.keyboard.numara:
                                pro.keyboard.sepet()
                                tutar += pro.keyboard.fiyat
                            else:
                                continue
                        print("Mouse Seçimi Yapınız \n\n")
                        fun.mouseListele()
                        choice = int(input('Ürün Numarası :\t'))
                        system("cls")
                        for pro.mouse in pro.mouses:
                            if choice == pro.mouse.numara:
                                pro.mouse.sepet()
                                tutar += pro.mouse.fiyat
                            else:
                                continue
                        def siparisYaz():
                            for x in cls.shop:
                                print(x)
                            print(f"Toplam Tutar : {tutar}₺")

                        siparisYaz()
                        an = datetime.datetime.now()
                        with open(f"siparisler/[D] {musteri.isim} {musteri.soyisim} {datetime.date.today()} {an.hour}.{an.minute}.{an.second}.txt", "w",
                                  encoding="utf-8") as f:
                            f.write(musteri.isim + " " + musteri.soyisim)
                            f.write("\n\n")
                            for item in cls.shop:
                                f.write(f"{item}\n")
                            f.write("\n\n")
                            f.write(musteri.adres + " " + musteri.ilce + "/" + musteri.il)
                            f.write("\n\n")
                            f.write(f"Toplam Tutar : {tutar}₺")

                        print("Siparişiniz Kaydedildi")
                        input("Önceki menüye dönmek için Enter")
                    elif secim2 == "2":  # Notebook
                        system("cls")
                        tutar = 0
                        print("Notebook Seçimi Yapınız \n\n")
                        fun.notebookListele()
                        choice = int(input('Ürün Numarası :\t'))
                        for pro.notebook in pro.notebooks:
                            if choice == pro.notebook.numara:
                                pro.notebook.yazdir()
                                tutar += pro.notebook.fiyat
                                if tutar > 10000:
                                    pro.notebook.hediyeEt()
                                    cls.note.append(f'''Notebok Çantası (Ücretsiz)''')
                                else:
                                    continue
                                if int(musteri.yas) < 25:
                                    tutar = tutar*0.95
                                else:
                                    continue
                                pro.notebook.sepet()
                                print(tutar)

                            else:
                                continue

                        def siparisYaz():
                            for x in cls.note:
                                print(x)
                            print(f"Toplam Tutar : {tutar}₺")

                        siparisYaz()
                        an = datetime.datetime.now()
                        with open(
                                f"siparisler/[N] {musteri.isim} {musteri.soyisim} {datetime.date.today()} {an.hour}.{an.minute}.{an.second}.txt",
                                "w",
                                encoding="utf-8") as f:
                            f.write(musteri.isim + " " + musteri.soyisim)
                            f.write("\n\n")
                            for item in cls.note:
                                f.write(f"{item}\n")
                            f.write("\n\n")
                            f.write(musteri.adres + " " + musteri.ilce + "/" + musteri.il)
                            f.write("\n\n")
                            f.write(f"Toplam Tutar : {tutar}₺")

                        print("Siparişiniz Kaydedildi")
                        input("Önceki menüye dönmek için Enter")

                    elif secim2 == "0":
                        print("Ana menüye yönlendiririliyorsunuz")
                        sleep(1.5)
                        break
                    else:
                        print("Hatalı Giriş")
                        input("Ana menüye dönmek için Enter")
            else:
                print("Hatalı Giriş")
        else:
            print("Hatalı Giriş")


if __name__ == "__main__":
    main()
