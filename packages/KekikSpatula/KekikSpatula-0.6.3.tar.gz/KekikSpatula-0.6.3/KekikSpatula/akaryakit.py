# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from requests     import get
from bs4          import BeautifulSoup

from KekikSpatula import KekikSpatula

class Akaryakit(KekikSpatula):
    """
    Akaryakit : haberler.com adresinden akaryakıt verilerini hazır formatlarda elinize verir.

    Methodlar
    ----------
        .veri:
            json verisi döndürür.

        .gorsel():
            oluşan json verisini insanın okuyabileceği formatta döndürür.

        .tablo():
            tabulate verisi döndürür.

        .anahtarlar:
            kullanılan anahtar listesini döndürür.

        .nesne:
            json verisini python nesnesine dönüştürür.
    """
    def __repr__(self) -> str:
        return f"{__class__.__name__} Sınıfı -- {self.kaynak}'dan akaryakıt verileri döndürmesi için yazılmıştır.."

    def __init__(self) -> None:
        """akaryakıt verilerini haberler.com'dan alarak bs4'ile ayrıştırır."""

        self.kaynak = "haberler.com"
        istek       = get(f"https://{self.kaynak}/finans/akaryakit/", headers=self.kimlik)

        corba       = BeautifulSoup(istek.content, "lxml")

        son_guncellenme = corba.select("div.hbTableContent.piyasa > table > tbody > tr:nth-child(1) > td:nth-child(2)")[0].text
        cerceve         = corba.find("div", class_="hbTableContent piyasa")

        kekik_json = {"kaynak": self.kaynak, "son_guncellenme": son_guncellenme, "veri" : []}

        for tablo in cerceve.findAll("tr")[1:]:
            cinsi  = tablo.find("td", {"width" : "50%"}).text.replace(" TL"," -- ₺")
            fiyati = tablo.find("td", {"width" : "16%"}).text

            kekik_json["veri"].append({
                "cinsi"     : cinsi,
                "fiyati"    : fiyati
            })

        self.kekik_json = kekik_json if kekik_json["veri"] != [] else None