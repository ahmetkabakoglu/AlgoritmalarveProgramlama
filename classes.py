class Product:
    def __init__(self, marka, model, fiyat, numara):
        self.marka = marka
        self.model = model
        self.fiyat = fiyat
        self.numara = numara

    def sepet(self):
        print(f"{self.marka} {self.model} ----------- {self.fiyat}₺")


class Costumer:
    def __init__(self, isim, soyisim, musterino, adres):
        self.isim = isim
        self.soyisim = soyisim
        self.musterino = musterino
        self.adres = adres


class Processor(Product):
    def __init__(self, marka, seri, model, guc, fiyat, numara):
        Product.__init__(self, marka, model, fiyat, numara)
        self.seri = seri
        self.guc = guc

    def yazdir(self):
        print(f"[{self.numara}] {self.marka} {self.seri} {self.model} {self.guc}GHz {self.fiyat}₺")


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
