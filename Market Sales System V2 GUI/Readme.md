🛒 Market Satış Sistemi

Market Satış Sistemi, Python ve Tkinter kullanılarak geliştirilmiş, küçük ve orta ölçekli marketler için tasarlanmış bir satış ve stok yönetim uygulamasıdır. Kullanıcı dostu arayüzü ile ürün ekleme, stok takibi, satış işlemleri ve fiyat yönetimini kolayca yapabilirsiniz.

🚀 Özellikler
1. Ürün Yönetimi

Yeni ürün ekleme (İsim, Barkod, Satış Fiyatı, Alış Fiyatı, Stok, Birim)

Mevcut ürünleri listeleme ve detaylarını görüntüleme

Ürün arama ve fiyat gösterimi

Barkod bazlı eşsiz ürün yönetimi

2. Satış İşlemleri

Barkod ile hızlı satış ekleme

Adet veya kilogram bazlı satış

Toplam fiyat hesaplama

Satış iptali (Sıfırlama) özelliği

Satış sonrası stok ve kar güncelleme

3. Stok Yönetimi

Mevcut ürünlerin stok takibi

Stok ekleme ve güncelleme

Stok yetersiz olduğunda uyarı gösterme

4. Fiyat Güncelleme

Ürün fiyat ve alış fiyatı güncelleme

Barkod ile hızlı erişim

Güncel kar bilgisi gösterme

5. Kar Takibi

Tüm satışlardan elde edilen toplam karın görüntülenmesi

Kar kaydı ve geri yükleme

6. Veri Kaydetme ve Yükleme

Satış ve ürün bilgileri otomatik kaydedilir

Uygulama tekrar açıldığında kayıtlı veriler yüklenir

.pkl formatında güvenli ve hızlı veri saklama

💻 Teknolojiler

Python 3

Tkinter: Kullanıcı arayüzü

Dill: Veri kaydetme ve yükleme (pickle alternatifi)

📦 Kurulum ve Çalıştırma

Python 3 yüklü olmalı.

Gerekli paketleri yükle:

pip install dill


Kodu çalıştır:

python market_satis_sistemi.py


Ana menü üzerinden işlemlere başlayabilirsin.

🎨 Arayüz

Basit ve anlaşılır menüler

Satış işlemleri için renkli ve büyük fiyat göstergesi

Listeleme ve giriş alanları kolay erişim için optimize edilmiş

Geri butonları ile tüm ekranlarda hızlı geçiş

🔧 Kullanım Örnekleri
Ürün Ekleme

“Ürün Tanımlama” menüsünü aç.

Ürün bilgilerini gir (isim, barkod, fiyat, alış fiyatı, stok, birim).

“Ürünü Ekle” butonuna bas ve kaydı tamamla.

Satış Yapma

“Satış İşlemleri” menüsünü aç.

Barkod ve adet gir.

“Ekle” ile satış listesine ekle.

Toplam fiyat otomatik hesaplanır.

“Satış” ile işlemi tamamla ve stok güncellensin.

Stok Güncelleme

“Stok Eklemek” menüsünü aç.

Barkod ve eklemek istediğin miktarı gir.

“Stok Ekle” butonuna bas, stok güncellenecektir.

⚡ İpuçları

Barkod ile ürün eklerken benzersiz olmasına dikkat et.

Satış listesi sıfırlandığında ürünler stoktan düşer ve toplam kar güncellenir.

Fiyat değişikliği ve stok güncellemelerinde negatif değer girilmemeli.

📂 Dosya Yapısı
market_satis_sistemi/
│
├─ market_satis_sistemi.py    # Ana Python dosyası
├─ save.pkl                    # Ürün verileri (otomatik kaydedilir)
├─ kar_save.pkl                # Kar bilgisi (otomatik kaydedilir)
└─ ikon.png                    # Uygulama ikonu

🎯 Gelecek Geliştirmeler

Barkod okuyucu desteği ile hızlı satış

Raporlama ve grafiksel kar-gelir analizleri

Kullanıcı yetkilendirme sistemi

Mobil ve web entegrasyonu