menu = 0
class urun():
        satis = 0
        stok = 0
        fiyat = 0
urun = urun()
while True:
    print ("""
                       MENÜ
               [1]: Satış Sayfası
               [2]: Stok Sayfası
               [3]: Fiyat Sayfası
               [4]: Sistemden Çıkış
        
    """)
               
    menu = int(input("Lütfen bir seçim yapınız: "))
        
    match menu:
        case 1:
            print("""
                      
                       SATIŞ SAYFASI
                  [A]: Satış Bilgisi Görüntüle
                  [B]: Satış Verisi Ekle
                  [C]: Satış Verisi Çıkar
                  [D]: Satış Bilgilerini Temizle
        
            """)
            satisbilgisi = str(input("Lütfen bir seçim yapınız: "))
            satisbilgisi = satisbilgisi.upper()
            match satisbilgisi:
                case "A":
                    print("Satış miktarı: ",urun.satis)
                    print("Menüye geri dönülüyor...")
                case "B":
                    veri = int(input("Lütfen bir satış verisi giriniz: "))
                    while veri>urun.satis:
                        urun.satis = urun.satis+1
                        if (veri==urun.satis):
                            break
                    print("Mevcut ürün satış miktarı: ",urun.satis)
                    print("Menüye geri dönülüyor...")
                case "C":
                    #Satış bilgisinin eksiltilme sebebi iadelerdir. İADE
                    veri = int(input("Lütfen eksiltilecek satış verisini giriniz: "))
                    urun.satis = urun.satis - veri
                    print("Mevcut ürün satış miktarı: ",urun.satis)
                    print("Menüye geri dönülüyor...")
                case "D":
                    urun.satis = 0
                    print("Mevcut ürün satış miktarı: ",urun.satis)
                    print("Menüye geri dönülüyor...")
        case 2:
            print("""
                      
                               STOK DURUMU
                       [A]: Stok Bilgisi Görüntüle
                       [B]: Stok Verisi Ekle
                       [C]: Stok Verisi Çıkar
                       [D]: Stok Bilgilerini Temizle
        
            """)
            stokbilgisi = str(input("Lütfen bir seçim yapınız: "))
            stokbilgisi = stokbilgisi.upper()
            match stokbilgisi:
                case "A":
                    print("Mevcut ürün stok miktarı: ",urun.stok)
                    print("Menüye geri dönülüyor...")
                case "B":
                    veri = int(input("Lütfen bir stok verisi giriniz: "))
                    urun.stok = urun.stok + veri
                    print("Mevcut ürün stok miktarı: ",urun.stok)
                    print("Menüye geri dönülüyor...")
                case "C":
                    veri = int(input("Lütfen eksiltilecek stok verisini giriniz: "))
                    urun.stok = urun.stok - veri
                    print("Mevcut ürün stok miktarı: ",urun.stok)
                    print("Menüye geri dönülüyor...")
                case "D":
                    urun.stok = 0
                    print("Mevcut ürün stok miktarı: ",urun.stok)
                    print("Menüye geri dönülüyor...")
        case 3:
            print("""
                      
                         FİYAT SAYFASI
                    [A]: Fiyat Bilgisi Görüntüle
                    [B]: Fiyat Verisi Ekle
                    [C]: Fiyat Verisi Çıkar
                    [D]: Fiyat Bilgilerini Temizle
        
            """)
            fiyatbilgisi = str(input("Lütfen bir seçim yapınız: "))
            fiyatbilgisi = fiyatbilgisi.upper()
            match fiyatbilgisi:
                case "A":
                    print("Mevcut ürün fiyatı: ",urun.fiyat,"Tl")
                    print("Menüye geri dönülüyor...")
                case "B":
                    veri = int(input("Lütfen bir stok verisi giriniz: "))
                    urun.fiyat = urun.fiyat + veri
                    print("Mevcut ürün fiyatı: ",urun.fiyat,"Tl")
                    print("Menüye geri dönülüyor...")
                case "C":
                    veri = int(input("Lütfen azaltılacak fiyat miktarı giriniz: "))
                    urun.fiyat = urun.fiyat - veri
                    print("Mevcut ürün fiyatı: ",urun.fiyat,"Tl")
                    print("Menüye geri dönülüyor...")
                case "D":
                    urun.fiyat = 0
                    print("Mevcut ürün fiyatı: ",urun.fiyat,"Tl")
                    print("Menüye geri dönülüyor...")
        case 4:
            print()
        case _:
            print("Yanlış tuşlama yapıldı! Lütfen tekrar deneyiniz.")
    if menu == 4:
        break

__author__ = "Hüdayi Emre Sarıça"
__copyright__ ="Copyright (C) 2024 Hüdayi Emre Sarıça"
__license__ = "Private"
__version__ = "1.0"