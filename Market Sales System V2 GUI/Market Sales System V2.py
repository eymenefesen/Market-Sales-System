import tkinter as tk
import sys
import os
import dill as pickle
from tkinter import messagebox
global listebasi
listebasi = "İsimi      Adet      Fiyat"
satilacaklarlistesi = {}
global toplamkar
toplamkar=0
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
                if urun.stok >= adet:
                        print(f"{urun.isim} ürününden {adet} {urun.birim} Tutar: {urun.fiyat*adet} TL")
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


#Def ler  **********************************

def dosya_klasoru():
    if getattr(sys, 'frozen', False):  # exe ise
        return os.path.dirname(sys.executable)
    else:  # python dosyası ise
        return os.path.dirname(os.path.abspath(__file__))

def kayit():
    klasor = dosya_klasoru()
    dosya_yolu = os.path.join(klasor, "save.pkl")
    with open(dosya_yolu, "wb") as f:
        pickle.dump(urun.Urunler, f)
    print(f"Veriler kaydedildi: {dosya_yolu}")

    klasor = dosya_klasoru()
    dosya_yolu = os.path.join(klasor, "kar_save.pkl")
    with open(dosya_yolu, "wb") as f:
        pickle.dump(urun.kar, f)
    print(f"kar kaydedildi: {dosya_yolu}")
    
def kayit_oku():
    klasor = dosya_klasoru()
    dosya_yolu = os.path.join(klasor, "save.pkl")
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, "rb") as f:
            urun.Urunler = pickle.load(f)
        print(f"Veriler yüklendi: {dosya_yolu}")
    else:
        print("Kayıt dosyası bulunamadı.")
        messagebox.showwarning("Uyarı", "Kayıt Dosyası Bulunamadı. Uygulamaya İlk kez giriş yapıyorsanız Dikkate almayınız")

    klasor = dosya_klasoru()
    dosya_yolu = os.path.join(klasor, "kar_save.pkl")
    if os.path.exists(dosya_yolu):
        with open(dosya_yolu, "rb") as f:
            urun.kar = pickle.load(f)
        print(f"kar yüklendi: {dosya_yolu}")

kayit_oku()
def satisaekle():
    global adet,urun
    barkod_str = barkod.get().strip()  # Başındaki ve sonundaki boşlukları sil
    girilenadet= adet_entry.get()

    if barkod_str != "":
        try:
            adetint= float(girilenadet)
            barkod_int = int(barkod_str)  # Sayıya çevirmeyi burada deneriz
        except ValueError:
            barkod.delete(0, tk.END)
            print("Geçersiz barkod, sayı değil.")
            return
        
        for i in urun.Urunler:
            if barkod_int == i.barkod:
                if satilacaklarlistesi != {}:
                    urun_var = False
                    for u,a in list(satilacaklarlistesi.items()):
                        if u.isim == i.isim:
                            urun_var = True
                            if (adetint+a) > i.stok:
                                messagebox.showerror("Hata", f"stoklarımız yetersizdir {i.isim} ürünümüzden {i.stok} {i.birim} kalmıştır")
                            else:
                                barkod.delete(0, tk.END)
                                satilacaklarlistesi[i] = a + adetint
                            break
                    if not urun_var:
                        if adetint > i.stok:
                            messagebox.showerror("Hata", f"stoklarımız yetersizdir {i.isim} ürünümüzden {i.stok} {i.birim} kalmıştır")
                        else:
                            barkod.delete(0, tk.END)
                            satilacaklarlistesi[i] = adetint
                else:
                    # Liste boşsa direk ekle
                    if adetint > i.stok:
                        messagebox.showerror("Hata", f"stoklarımız yetersizdir {i.isim} ürünümüzden {i.stok} {i.birim} kalmıştır")
                    else:
                        barkod.delete(0, tk.END)
                        satilacaklarlistesi[i] = adetint
                break

                        
         

        satilacaklar.config(state="normal")
        satilacaklar.delete("0", tk.END)
        satilacaklar.insert(tk.END, listebasi)
        global toplamfiyat
        toplamfiyat=0
        for urunnn,adet in satilacaklarlistesi.items():
            satilacaklar.config(state="normal")
            satilacaklar.insert(tk.END, f"{urunnn.isim}      {adet}        {urunnn.fiyat*adet}")
            satilacaklar.config(state="disable")
            fiyat_=urunnn.fiyat*adet
            toplamfiyat=fiyat_+toplamfiyat
            fiyat.config(text=toplamfiyat)

    else:
        print("Barkod boş girildi.")
        messagebox.showerror("Hata", "Barkod Numarası Giriniz")
            
def satisbuton():
    global toplamkar
    kisakar=0
    if satilacaklarlistesi == {}:
        print("satışa ürün ekleyin")
        messagebox.showerror("Hata", "Satış İçin Ürün Ekleyin")
    else:
        for urunn,adett in satilacaklarlistesi.items():
            kisakar= (urunn.fiyat*adett) - (urunn.alisfiyati*adett)
            urun.kar = urun.kar + kisakar
            urunn.stok = urunn.stok - adett

        satilacaklar.config(state="normal")
        satilacaklar.delete("0", tk.END)
        satilacaklar.insert(tk.END, listebasi)
        fiyat.config(text=0.0)
        satilacaklarlistesi.clear()
        kayit()
        print("satış yapıldı")

def sifir():
    fiyat.config(text=0.0)
    satilacaklarlistesi.clear()
    satilacaklar.config(state="normal")
    satilacaklar.delete("0", tk.END)
    satilacaklar.insert(tk.END, listebasi)
    satilacaklar.config(state="disable")

def urunekletus():
    barkod_int = int(barkod.get())  
    barkod_var = False  

    for i in urun.Urunler:
        if i.barkod == barkod_int:
            barkod_var = True
            break 

    if barkod_var:
        messagebox.showerror("Hata", "Aynı Barkod Numarasına Ait Farklı Bir Ürün Var")
        barkod.delete(0, tk.END)
    else:
        urun.urun_ekle(isim.get(), barkod_int, float(fiyatentry.get()), float(alisfiyat.get()), birim_.get(), int(stok.get()))
        
     
        isim.delete(0, tk.END)
        barkod.delete(0, tk.END)
        fiyatentry.delete(0, tk.END)
        alisfiyat.delete(0, tk.END)
        stok.delete(0, tk.END)

        kayit()  
        messagebox.showinfo("Bilgi", "İşlem başarıyla tamamlandı. (Veriler Kaydedildi)")

def urunaraa():
    for i in urun.Urunler:
        if i.barkod == int(barkod2.get()):
            urunadi.config(text=i.isim)
            fiyat2.config(text=f"{i.fiyat*float(adet_entry2.get())} TL")
            barkod2.delete(0,tk.END)
            break


def stokekletusu():
    if stok_ekle_barkod.get() =="" or stoksayisi.get()=="":
        print("Boş Bırakmayınız")
        messagebox.showerror("Hata", "Lütfen Kutucukları Boş Bırakmayınız")

    else:
        
        for i in urun.Urunler:
            if i.barkod == int(stok_ekle_barkod.get()):
                stokekletext.config(text=f"{i.isim}")
                urun.Stok_ekle(int(stok_ekle_barkod.get()),float(stoksayisi.get()))

                if i.stok < 0:
                    i.stok = 0
                    print("ürün stoğu sıfırdan küçük olamamalıdır")
                messagebox.showinfo("Stok Güncellendi", f"{i.isim} ürünü'nün Güncel Stoğu {i.stok}")
                stok_ekle_barkod.delete(0,tk.END)
                stoksayisi.delete(0,tk.END)
                
                kayit()

def fiyatguncelle():

    if fiyat_degisiklik_barkod.get() =="" or satisfiyati.get()=="" or alisfiyati.get()=="":
        print("Boş Bırakmayınız")
        messagebox.showerror("Hata", "Lütfen Kutucukları Boş Bırakmayınız")

    else:
        
        for i in urun.Urunler:
            if i.barkod == int(fiyat_degisiklik_barkod.get()):
                stokekletext.config(text=f"{i.isim}")
                urun.fiyat_degisiklik(int(fiyat_degisiklik_barkod.get()),float(satisfiyati.get()),float(alisfiyati.get()))

                if i.fiyat  < 0:
                    i.fiyat = 0
                    print("ürün fiyatı sıfırdan küçük olamamalıdır")

                if i.alisfiyati  < 0:
                    i.alisfiyati = 0
                    print("ürün alış fiyatı sıfırdan küçük olamamalıdır")

                messagebox.showinfo("fiyat Güncellendi", f"{i.isim} ürünü'nün Güncel fiyatı {i.fiyat} alış fiyatı ise {i.alisfiyati}")
                fiyat_degisiklik_barkod.delete(0,tk.END)
                satisfiyati.delete(0,tk.END)
                alisfiyati.delete(0,tk.END)
                kayit()


#Pencereler____________________


def satis_islemleri():
    
    for widget in ana_menu.winfo_children():
        widget.destroy()

    global barkod
    global adet_entry

    barkod = tk.Entry(ana_menu, width=40,bd=4)
    barkod.pack(pady=10)
    barkod.place(x=600,y=150)

    barkodtext=tk.Label(ana_menu, text="Barkod:",font=("arial",15))
    barkodtext.pack(pady=10)
    barkodtext.place(x=500,y=150)


    adet_entry = tk.Entry(ana_menu, width=40,bd=4)
    adet_entry.pack(pady=10)
    adet_entry.place(x=600,y=240)
    adet_entry.insert(0, "1") 

    adettext=tk.Label(ana_menu, text="Adet/Kg :",font=("arial",15))
    adettext.pack(pady=10)
    adettext.place(x=500,y=240)

    global fiyat
    fiyat=tk.Label(ana_menu, text="0.0",font=("Arial", 40),bg="yellow")
    fiyat.pack(pady=10)
    fiyat.place(x=140,y=40)

    ekletusu=tk.Button(ana_menu,text="ekle",bg=color,width=10,height=2,command=satisaekle)
    ekletusu.place(x=500,y=300)

    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)

    sat=tk.Button(ana_menu,text="satış",bg=color,width=10,height=2,command=satisbuton)
    sat.place(x=625,y=300)

    sıfırla=tk.Button(ana_menu,text="iptal",bg=color,width=10,height=2,command=sifir)
    sıfırla.place(x=750,y=300)

    global satilacaklar
    satilacaklar = tk.Listbox(ana_menu, font=("Arial", 15), width=30, height=15)
    satilacaklar.place(x=50,y=150)
    satilacaklar.config(state="normal")
    satilacaklar.font=("Arial", 30,)
    satilacaklar.insert(tk.END, listebasi)


def urun_tanımlama():
    global isim , barkod , fiyatentry , alisfiyat , stok , birim_
    for widget in ana_menu.winfo_children():
        widget.destroy()

    isim = tk.Entry(ana_menu, width=40,bd=4)
    isim.pack(pady=10)
    isim.place(x=325,y=100)

    isimtext=tk.Label(ana_menu, text="Ürün İsimi :",font=("arial",15))
    isimtext.pack(pady=10)
    isimtext.place(x=200,y=100)

    barkod = tk.Entry(ana_menu, width=40,bd=4)
    barkod.pack(pady=10)
    barkod.place(x=325,y=150)

    barkodtext=tk.Label(ana_menu, text="Barkod :",font=("arial",15))
    barkodtext.pack(pady=10)
    barkodtext.place(x=200,y=150)

    fiyatentry = tk.Entry(ana_menu, width=40,bd=4)
    fiyatentry.pack(pady=10)
    fiyatentry.place(x=325,y=200)

    fiyattext=tk.Label(ana_menu, text="Fiyat :",font=("arial",15))
    fiyattext.pack(pady=10)
    fiyattext.place(x=200,y=200)

    alisfiyat = tk.Entry(ana_menu, width=40,bd=4)
    alisfiyat.pack(pady=10)
    alisfiyat.place(x=325,y=250)

    alisfiyattext=tk.Label(ana_menu, text="Alış Fiyatı :",font=("arial",15))
    alisfiyattext.pack(pady=10)
    alisfiyattext.place(x=200,y=250)

    
    stok = tk.Entry(ana_menu, width=40,bd=4)
    stok.pack(pady=10)
    stok.place(x=325,y=300)
    stok.insert(0, "1") 

    stoktext=tk.Label(ana_menu, text="Stok :",font=("arial",15))
    stoktext.pack(pady=10)
    stoktext.place(x=200,y=300)

    birim_ = tk.StringVar(value="adet")  # Varsayılan değer
    birimler = ["kg", "adet"]

    birimmenu = tk.OptionMenu(ana_menu, birim_, *birimler,)
    birimmenu.place(x=325,y=350)
    birimmenu.config(width=34)

    birimtext=tk.Label(ana_menu, text="birim :",font=("arial",15))
    birimtext.pack(pady=10)
    birimtext.place(x=200,y=350)

    urunekle=tk.Button(ana_menu,text="Ürünü Ekle",bg=color,width=10,height=2,command=urunekletus)
    urunekle.place(x=700,y=200)

    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=50,y=25)


def stoktakip():
    stoklistebasi="Barkod                         İsim                         Stok" #25 boşluk
    for widget in ana_menu.winfo_children():
        widget.destroy()
    urunler = tk.Listbox(ana_menu, font=("Arial", 20), width=40, height=25)
    urunler.place(x=270,y=20)
    urunler.insert(tk.END, stoklistebasi)
    for i in urun.Urunler:
        urunler.insert(tk.END, f"{i.barkod}      {i.isim}     {i.stok}  {i.birim}")
    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)

def urunarama():
    for widget in ana_menu.winfo_children():
        widget.destroy()
    global barkod2
    barkod2 = tk.Entry(ana_menu, width=40,bd=4)
    barkod2.pack(pady=10)
    barkod2.place(x=600,y=150)

    barkodtext2=tk.Label(ana_menu, text="Barkod:",font=("arial",15))
    barkodtext2.pack(pady=10)
    barkodtext2.place(x=500,y=150)

    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)

    global adet_entry2
    adet_entry2 = tk.Entry(ana_menu, width=40,bd=4)
    adet_entry2.pack(pady=10)
    adet_entry2.place(x=600,y=240)
    adet_entry2.insert(0, "1") 

    adettext2=tk.Label(ana_menu, text="Adet/Kg :",font=("arial",15))
    adettext2.pack(pady=10)
    adettext2.place(x=500,y=240)

    global fiyat2
    fiyat2=tk.Label(ana_menu, text="0.0",font=("Arial", 50),bg="yellow")
    fiyat2.pack(pady=10)
    fiyat2.place(x=250,y=100)
    global urunadi
    urunadi=tk.Label(ana_menu,font=("arial",25))
    urunadi.pack(pady=10)
    urunadi.place(x=210,y=225)

    urunara=tk.Button(ana_menu,text="Ürün Ara",bg=color,width=10,height=2,command=urunaraa)
    urunara.place(x=675,y=300)

def stokekle2():
    for widget in ana_menu.winfo_children():
        widget.destroy()        

    global stok_ekle_barkod
    stok_ekle_barkod = tk.Entry(ana_menu, width=40,bd=4)
    stok_ekle_barkod.pack(pady=10)
    stok_ekle_barkod.place(x=600,y=150)

    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)

    barkodtext2=tk.Label(ana_menu, text="Barkod:",font=("arial",15))
    barkodtext2.pack(pady=10)
    barkodtext2.place(x=500,y=150)

    global stokekletext
    stokekletext=tk.Label(ana_menu, text="--",font=("arial",25))
    stokekletext.pack(pady=10)
    stokekletext.place(x=200,y=150)

    global stoksayisi
    stoksayisi = tk.Entry(ana_menu, width=40,bd=4)
    stoksayisi.pack(pady=10)
    stoksayisi.place(x=600,y=250)

    stoksayisitext=tk.Label(ana_menu, text="Eklenecek Stok:",font=("arial",15))
    stoksayisitext.pack(pady=10)
    stoksayisitext.place(x=430,y=250)

    stoklarıekle=tk.Button(ana_menu,text="Stok Ekle",bg=color,width=10,height=2,command=stokekletusu)
    stoklarıekle.place(x=675,y=300)

def fiyatdegisiklik():

    for widget in ana_menu.winfo_children():
        widget.destroy()        

    global fiyat_degisiklik_barkod
    fiyat_degisiklik_barkod = tk.Entry(ana_menu, width=40,bd=4)
    fiyat_degisiklik_barkod.pack(pady=10)
    fiyat_degisiklik_barkod.place(x=600,y=150)

    barkodtext2=tk.Label(ana_menu, text="Barkod:",font=("arial",15))
    barkodtext2.pack(pady=10)
    barkodtext2.place(x=500,y=150)

    alisfiyattext=tk.Label(ana_menu, text="Yeni Satış Fiyatı:",font=("arial",15))
    alisfiyattext.pack(pady=10)
    alisfiyattext.place(x=425,y=350)

    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)

    global stokekletext
    stokekletext=tk.Label(ana_menu, text="--",font=("arial",25))
    stokekletext.pack(pady=10)
    stokekletext.place(x=200,y=150)

    global satisfiyati
    satisfiyati = tk.Entry(ana_menu, width=40,bd=4)
    satisfiyati.pack(pady=10)
    satisfiyati.place(x=600,y=250)

    global alisfiyati
    alisfiyati = tk.Entry(ana_menu, width=40,bd=4)
    alisfiyati.pack(pady=10)
    alisfiyati.place(x=600,y=350)

    stoksayisitext=tk.Label(ana_menu, text="Yeni Satış Fiyatı:",font=("arial",15))
    stoksayisitext.pack(pady=10)
    stoksayisitext.place(x=430,y=250)

    stoklarıekle=tk.Button(ana_menu,text="Fiyat Güncelle",bg=color,width=10,height=2,command=fiyatguncelle)
    stoklarıekle.place(x=675,y=400)

def toplamkargosterim():
    for widget in ana_menu.winfo_children():
        widget.destroy()  
    kargosterimi=tk.Label(ana_menu,font=("arial",50))
    kargosterimi.pack(pady=10)

    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)

    kargosterimi.place(x=500,y=200)
    kargosterimi.config( text=urun.kar)
    kartext=tk.Label(ana_menu, text="Toplam Karınız",font=("arial",30))
    kartext.pack(pady=10)
    kartext.place(x=415,y=280)

def tum_urunler():
    stoklistebasi="Barkod         İsim            Stok       Satış Fiyatı         Alış Fiyatı" 
    for widget in ana_menu.winfo_children():
        widget.destroy()
    urunler = tk.Listbox(ana_menu, font=("Arial", 20), width=40, height=25)
    urunler.place(x=270,y=20)
    urunler.insert(tk.END, stoklistebasi)
    for i in urun.Urunler:
        urunler.insert(tk.END, f"{i.barkod}      {i.isim}     {i.stok} {i.birim}      {i.fiyat}           {i.alisfiyati}")
    geri=tk.Button(ana_menu,text="<<",bg=color,width=10,height=2,command=anasayfa)
    geri.place(x=10,y=20)





print("Market Satış Sistemine Hoşgeldiniz")
print("--------------------------------------")
xb=200
color="gray"
ana_menu = tk.Tk()
icon = tk.PhotoImage(file="ikon.png")
ana_menu.geometry("1100x700")
ana_menu.resizable(False, False)
ana_menu.title("Market Sales System")
ana_menu.iconphoto(False,icon)
def anasayfa(event=None):
    ana_menu.bind("<Escape>", anasayfa)
    satilacaklarlistesi.clear()
    for widget in ana_menu.winfo_children():
        widget.destroy()

    satis_buton=tk.Button(ana_menu,text="Satış İşlemleri",bg=color,width=100,height=2,command=satis_islemleri)
    satis_buton.place(x=xb,y=40)

    urun_ekleme=tk.Button(ana_menu,text="Ürün Tanımlama",bg=color,width=100,height=2,command=urun_tanımlama)
    urun_ekleme.place(x=xb,y=120)

    stok_takip=tk.Button(ana_menu,text="Stok Takip",bg=color,width=100,height=2,command=stoktakip)
    stok_takip.place(x=xb,y=200)

    urun_arama=tk.Button(ana_menu,text="Ürün Arama/Fiyat Görme",bg=color,width=100,height=2,command=urunarama)
    urun_arama.place(x=xb,y=280)

    stok_ekle=tk.Button(ana_menu,text="Stok Eklemek",bg=color,width=100,height=2,command=stokekle2)
    stok_ekle.place(x=xb,y=360)

    fiyat_degistirme=tk.Button(ana_menu,text="Fiyat Değişikliği",bg=color,width=100,height=2,command=fiyatdegisiklik)
    fiyat_degistirme.place(x=xb,y=430)

    toplam_kar=tk.Button(ana_menu,text="Toplam Kar",bg=color,width=100,height=2,command=toplamkargosterim)
    toplam_kar.place(x=xb,y=510)

    urun_listesi=tk.Button(ana_menu,text="Tüm Ürünler",bg=color,width=100,height=2,command=tum_urunler)
    urun_listesi.place(x=xb,y=590)

    kayit_tusu=tk.Button(ana_menu,text="Kaydetme",bg=color,width=20,height=2,command=kayit)
    kayit_tusu.place(x=20,y=530)

    kayitokuma_tusu=tk.Button(ana_menu,text="Kayıt okuma",bg=color,width=20,height=2,command=kayit_oku)
    kayitokuma_tusu.place(x=20,y=590)

anasayfa()
ana_menu.mainloop()
