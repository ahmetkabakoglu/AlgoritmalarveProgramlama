class Costumer:
    def __init__(self, isim: str, soyisim: str, yas: int, il: str, ilce: str, adres: str, idno: str, parola: str):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.parola = parola
        self.idno = idno
        self.il = il
        self.ilce = ilce
        self.adres = adres

    def getIsim(self):
        return self.isim

    def getsoyIsim(self):
        return self.soyisim

    def getIdNo(self):
        return self.idno

    def getParola(self):
        return self.parola

    def getYas(self):
        return self.yas


class Store:
    def __init__(self, isim: str):
        self.__isim = isim
        self.__musteriler = list()

    def musteriVarMi(self, idno: str, parola: str):
        for i in self.__musteriler:
            if i.getIdNo() == idno and i.getParola() == parola:
                return i
        return False
    def musteriOl(self, isim: str, soyisim: str, yas: int, il: str, ilce: str, adres: str, idno: str, parola: str):
        self.__musteriler.append(Costumer(isim, soyisim, yas, il, ilce, adres, idno, parola))



shop = []


class Product:
    def __init__(self, marka, model, fiyat, numara):
        self.marka = marka
        self.model = model
        self.fiyat = fiyat
        self.numara = numara

    def sepet(self):
        shop.append(f"{self.marka} {self.model} ----------- {self.fiyat}₺")


class Processor(Product):
    def __init__(self, marka, seri, model, guc, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.seri = seri
        self.guc = guc

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.seri} {self.model} {self.guc}GHz {self.fiyat}₺")
        return self.fiyat


class Motherboard(Product):
    def __init__(self, marka, model, seri, guc, tip, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.seri = seri
        self.guc = guc
        self.tip = tip

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.seri} {self.model} {self.guc}MHz {self.tip} {self.fiyat}₺")


class Memory(Product):
    def __init__(self, marka, model, hiz, kapasite, tip, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.tip = tip
        self.kapasite = kapasite
        self.hiz = hiz

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.model} {self.hiz}MHz {self.kapasite}GB {self.tip} {self.fiyat}₺")


class ComputerCase(Product):
    def __init__(self, marka, model, psu, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.PSU = psu

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.model} {self.PSU}W {self.fiyat}₺")


class GraphicCard(Product):
    def __init__(self, marka, model, kapasite, tip, gpu, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.tip = tip
        self.kapasite = kapasite
        self.GPU = gpu

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.model} {self.kapasite}GB {self.tip} {self.GPU}Bit {self.fiyat}₺")


class HDD(Product):
    def __init__(self, marka, model, kapasite, onbellek, hiz, boyut, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.kapasite = kapasite
        self.onbellek = onbellek
        self.hiz = hiz
        self.boyut = boyut

    def yazdir(self):
        print(
            f"[{self.numara}] {self.marka} {self.model} {self.kapasite}TB  {self.hiz}RPM {self.onbellek}MB {self.boyut}inch  {self.fiyat}₺")


class SSD(Product):
    def __init__(self, marka, model, kapasite, okuma, yazma, boyut, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.kapasite = kapasite
        self.okuma = okuma
        self.yazma = yazma
        self.boyut = boyut

    def yazdir(self):
        print(
            f"[{self.numara}] {self.marka} {self.model} {self.kapasite}GB  {self.boyut} (Okuma:{self.okuma}MB, Yazma:{self.yazma}MB) {self.fiyat}₺")


class Monitor(Product):
    def __init__(self, marka, model, boy, tazeleme, tepki, cozunurluk, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.boy = boy
        self.tazeleme = tazeleme
        self.tepki = tepki
        self.cozunurluk = cozunurluk

    def yazdir(self):
        print(
            f"[{self.numara}] {self.marka} {self.model} {self.boy} inch  {self.tazeleme}Hz {self.tepki}ms {self.cozunurluk} {self.fiyat}₺")


class Keyboard(Product):
    def __init__(self, marka, model, ozellik, switch, dil, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.ozellik = ozellik
        self.switch = switch
        self.dil = dil

    def yazdir(self):
        print(
            f"[{self.numara}] {self.marka} {self.model} {self.switch} Switch {self.dil} {self.ozellik} Gaming Klavye {self.fiyat}₺")


class Mouse(Product):
    def __init__(self, marka, model, ozellik, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.ozellik = ozellik

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.model} {self.ozellik} Gaming Mouse {self.fiyat}₺")
        return self.fiyat

    def yaz(self):
        print(f"[{self.numara}] {self.marka} {self.model} {self.ozellik} Gaming Mouse {self.fiyat}₺")

note = []
class Notebook:
    def __init__(self, marka, seri, model, islemci, ekrankarti, boy, cozunurluk, tazeleme, bellek, depolama, isletim,
                 fiyat, numara):
        self.marka = marka
        self.seri = seri
        self.model = model
        self.islemci = islemci
        self.ekrankarti = ekrankarti
        self.boy = boy
        self.cozunurluk = cozunurluk
        self.tazeleme = tazeleme
        self.bellek = bellek
        self.depolama = depolama
        self.isletim = isletim
        self.numara = numara
        self.fiyat = fiyat

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.seri} {self.model} {self.islemci} {self.ekrankarti}\n"
              f"    {self.boy} {self.cozunurluk} {self.tazeleme} {self.bellek} {self.depolama} {self.isletim} {self.fiyat}₺")
    def hediyeEt(self):
        print(f'''    {self.boy}" Notebok Çantası (Ücretsiz)''')
    def sepet(self):
        note.append(f"{self.marka} {self.model} ----------- {self.fiyat}₺")