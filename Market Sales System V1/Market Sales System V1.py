

class urun:
    Urunler=[]
    kar=0.0
    def __init__(self,isim,barkod,fiyat,alisfiyati,birim,stok=1):
        self.isim=isim
        self.barkod=barkod
        self.fiyat=fiyat
        self.alisfiyati=alisfiyati
        self.stok=stok
        self.birim=birim
    @classmethod
    def urun_ekle(cls,isim,barkod,fiyat,alisfiyati,birim,stok=1):
        
        yeni_urun=cls(isim,barkod,fiyat,alisfiyati,birim,stok)
        cls.Urunler.append(yeni_urun)
        print(f"{isim} ürünü eklendi")
        return yeni_urun
    
    @classmethod
    def satis(cls, barkod,adet):
        for urun in cls.Urunler:
            if urun.barkod == barkod:
                if urun.birim == "adet":
                    if urun.stok >= adet:
                        print(f"{urun.isim} ürününden {adet} tane Tutar: {urun.fiyat*adet} TL")
                        urun.stok = urun.stok-adet 
                        cls.kar = cls.kar+((urun.fiyat*adet) - (urun.alisfiyati*adet))
                        return
                    else:
                        print(f"ürün stoklarımız yetersizdir. Bu üründen elimizde {urun.stok} adet var ")
                        return
                elif urun.birim == "kg":
                    if urun.stok >= adet:
                        print(f"{urun.isim} ürününden {adet} kg satış yapılıyor Tutar: {urun.fiyat*adet} TL")
                        urun.stok = urun.stok-adet 
                        cls.kar = cls.kar+((urun.fiyat*adet) - (urun.alisfiyati*adet))
                        return
                    else:
                        print(f"ürün stoklarımız yetersizdir. Bu üründen elimizde {urun.stok} adet var ")
                        return
            
        print("Ürün bulunamadı.")

    @classmethod
    def stok_takip(cls):
        toplam_stok=0
        for urun in cls.Urunler:
            toplam_stok=urun.stok+toplam_stok
        print("-ürün listesi-")
        for urun in cls.Urunler:
            if urun.stok != 0:
                if urun.birim =="adet":
                    print(f"{urun.isim} - {urun.stok} Adet")
                else:
                    print(f"{urun.isim} - {urun.stok} Kg")
        print(f"toplam stok - {toplam_stok}")

    @classmethod
    def urun_arama(cls,barkod):
        for urun in cls.Urunler:
            if urun.barkod==barkod:
                print(f"{urun.isim} | fiyat - {urun.fiyat} | stok - {urun.stok}")
                return
            
        print("Ürün Bulunamadı")

    @classmethod
    def Stok_ekle(cls,barkod,eklenen_stok):
        for urun in cls.Urunler:
            if urun.barkod == barkod:
                urun.stok = urun.stok+eklenen_stok
                print(f"Stok yenilendi. {urun.isim} için Yeni stok {urun.stok}")

    @classmethod
    def fiyat_degisiklik(cls,barkod,yeni_fiyat,y_alis_fiyat):
        for urun in cls.Urunler:
            if urun.barkod == barkod:
                urun.fiyat = yeni_fiyat
                urun.alisfiyati = y_alis_fiyat
                print(f"{urun.isim} ürünü'nün yeni satış fiyatı {urun.fiyat} | Alış fiyatı ise {urun.alisfiyati} | kar = {urun.fiyat - urun.alisfiyati}")
    @classmethod
    def kar_gosterimi(cls):
        print(f"Şuana kadar yaptığınız satışlardan toplam karınız {cls.kar}")

    @classmethod
    def urunlistesi(cls):
        print("                         --Ürünler--")
        print("-------------------------------------------------------------------------------")
        for i in cls.Urunler:
            if i.birim == "adet":
                print(f"ürün - {i.isim} | fiyat - {i.fiyat} | alış fiyatı - {i.alisfiyati} | stok - {i.stok} | barkod - {i.barkod} | kar - {i.fiyat-i.alisfiyati}₺")
                print("-------------------------------------------------------------------------------")
            else:
                print(f"ürün - {i.isim} | fiyat - {i.fiyat} | alış fiyatı - {i.alisfiyati} | stok - {i.stok} Kg | barkod - {i.barkod} | kar - {i.fiyat-i.alisfiyati}₺")
                print("-------------------------------------------------------------------------------")                




print("Market Satış Sistemine Hoşgeldiniz")
print("--------------------------------------")

while True:
    print("--------------------------------------")
    secenek=int(input("satış için- 1\nürün eklemek için- 2\nStok takibi için- 3\nürün arama için- 4\nstok eklemek için- 5\nfiyat değişkiliği için- 6\ntoplam karı görmek için- 7\nürünlerin listesini görmek için- 8\nyazınız: "))

    if secenek ==1:
        barkod=int(input("Satış yapmak istediğiniz ürünün barkodunu giriniz: "))
        for i in urun.Urunler:
            if i.barkod == barkod:
                adet=float(input(f"{i.isim} ürününden kaç adet/kg almak isteniyor: "))
                urun.satis(barkod,adet)

    elif secenek == 2:
        isim=input("sisteme eklemek istediğiniz ürünün ismi/markası nedir: ")
        barkod=int(input(f"{isim} ürünü'nün barkodu nedir: "))
        birim=input(f"{isim} ürünü'nün birimi nedir(adet/kg)")
        if birim== "adet":
            fiyat=float(input(f"{isim} ürünü'nün satış fiyatı nedir: "))
            alisfiyati=int(input(f"{isim} ürünü'nün alış fiyatı nedir: "))
            stok=int(input(f"{isim} ürünü'nün stoğu nedir: "))
            urun.urun_ekle(isim,barkod,fiyat,alisfiyati,birim,stok)
        elif birim == "kg":
            fiyat=float(input(f"{isim} ürünü'nün 1 kg lik fiyaı nedir : "))
            alisfiyati=int(input(f"{isim} ürünü'nün 1 kg lik alış fiyatı nedir: "))
            stok=float(input(f"{isim} ürünü'nün stoğu kaç kg : "))
            urun.urun_ekle(isim,barkod,fiyat,alisfiyati,birim,stok)
        else:
            print("birimi yalış giriniz")    

    elif secenek == 3:
        urun.stok_takip()

    elif secenek == 4:
        barkod=int(input("bulmak istediğiniz ürünün barkodunu giriniz: "))
        urun.urun_arama(barkod)

    elif secenek == 5:
        barkod=int(input("stok eklemek istediğiniz ürünün barkodunu giriniz: "))
        for i in urun.Urunler:
            if i.barkod == barkod:
                eklenen_stok=int(input(f"{i.isim} ürünü'nüne eklemek isteeiğiniz stok sayısını giriniz: "))
                urun.Stok_ekle(barkod,eklenen_stok)

    elif secenek == 6:
        barkod=int(input("fiyat güncellemesi yapmak istediğiniz ürünün barkodunu giriniz: "))
        for i in urun.Urunler:
            if i.barkod == barkod:
                y_satis_f=int(input(f"{i.isim} ürünü'nün yeni satış fiyatını giriniz: "))
                y_alis_f=int(input(f"{i.isim} ürünü'nün yeni alış fiyatını giriniz: "))
                urun.fiyat_degisiklik(barkod,y_satis_f,y_alis_f)

    elif secenek == 7:
        urun.kar_gosterimi()

    elif secenek == 8:
        urun.urunlistesi()
        

