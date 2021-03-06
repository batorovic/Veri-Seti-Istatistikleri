r"""
Python 3.9.0 versiyonu kullanilmistir.

Excelden veri okumak icin pandas,
Sqrt fonksiyonunu kullanabilmek serbest oldugun icin math,
Boxplot cizdirmek icin matploblib
kütüphaneleri kullanilmistir.

Kodun calismasi icin asagidaki kutuphaneleri pip ile yuklemeniz gerekmektedir.

pip install pandas
pip install openpyxl
pip install numpy
pip install matplotlib

Eger pip hata verirse:

Ortam degiskenleri -> Sistem Degiskenleri -> Path

Path kismina: C: \Users\{kullaniciAdiniz}\AppData\Local\Programs\Python\Python39\Scripts ekleyiniz.

Scripti cmd uzerinden calistirmak icin: 

Dosyayi cikardiginiz yerde cmd aciniz. Ve asagidaki satiri yaziniz.

~ python hesaplamalar.py
"""

import matplotlib.pyplot as plt
import math
import pandas as pd


def readDataFromExcel():
    df = pd.read_excel(r'veriSeti.xlsx', keep_default_na=False)
    # Excel dosyasini scriptin oldugu yerden direkt okumaktadir.
    return df


def listeninUzunlugu(data):
    length = 0

    for item in data:
        length += 1
    return length


def convertToList(data):
    liste = []

    for item in data:
        if item == "":
            break
        else:
            liste.append(item)
    return liste


def aritmetikOrtalama(data):
    toplam = 0
    for item in data:
        toplam += item
    return float("{:.2f}".format(toplam / listeninUzunlugu(data)))


def ortanca(data):
    listeBoyutu = listeninUzunlugu(data)
    data = sorted(data)
    if listeBoyutu % 2 == 0:
        medyan = (int)(listeBoyutu / 2) - 1

        return (data[medyan] + data[medyan + 1]) / 2

    else:
        medyan = (int)(listeBoyutu/2)
        return data[medyan]


def tepeDeger(testList):
    dataSozluk = {}
    durum = True
    for item in testList:
        try:
            dataSozluk[item] += 1
        except:
            dataSozluk[item] = 1

    sortedDataSozluk = dict(
        sorted(dataSozluk.items(), key=lambda item: item[1], reverse=True))

    tekrarEdenler = []
    onceki = 0

    if list(sortedDataSozluk.values())[0] == 1:
        return "Tepe degeri yok"
    else:
        for item in sortedDataSozluk:
            if(sortedDataSozluk[item] >= onceki):
                onceki = sortedDataSozluk[item]
                tekrarEdenler.append(item)

    tekrarEdenler = sorted(tekrarEdenler)

    return ", ".join(str(item) for item in tekrarEdenler)


def degisimAraligi(data):
    maximum = 0
    minimum = data[0]

    for item in data:
        if maximum < item:
            maximum = item
        elif minimum > item:
            minimum = item

    return maximum - minimum


def ortalamaMutlakSapma(data):

    dataAritmetikOrtalama = aritmetikOrtalama(data)
    toplam = 0

    for item in data:
        if item > dataAritmetikOrtalama:
            toplam += (item - dataAritmetikOrtalama)
        else:
            toplam += (dataAritmetikOrtalama - item)

    return float("{:.3f}".format(toplam / listeninUzunlugu(data)))


def varyans(data):
    dataAritmetikOrtalama = aritmetikOrtalama(data)
    toplam = 0
    for item in data:
        toplam = toplam + (item - dataAritmetikOrtalama) ** 2

    return float("{:.4f}".format((toplam) / (listeninUzunlugu(data) - 1)))


def standartSapma(data):
    return float("{:.2f}".format(math.sqrt(varyans(data))))


def degisimKatSayisi(data):
    return float('{:.4f}'.format(standartSapma(data) / aritmetikOrtalama(data)))


def ceyreklerAcikligi(data):
    data = sorted(data)
    elemanSayisi = listeninUzunlugu(data)

    q1Terim = (elemanSayisi + 1) / 4
    q3Terim = 3 * (elemanSayisi + 1) / 4
    q1 = 0
    q3 = 0

    if q1Terim % 1 != 0:
        n = int(q1Terim)
        q1 = (data[n] + data[n - 1]) / 2
    else:
        q1 = data[int(q1Terim) - 1]

    if q3Terim % 1 != 0:
        n = int(q3Terim)
        q3 = (data[n] + data[n - 1]) / 2
    else:
        q3 = data[int(q3Terim) - 1]

    return q3 - q1


def boxPlot(sutunAdlari):
    df = readDataFromExcel()
    for item in sutunAdlari:
        plt.figure(item)

        plt.boxplot(convertToList(df[item]))

        titleText = item + " BOXPLOT ÇİZİMİ"
        titleObj = plt.title(titleText)

        plt.setp(titleObj, color='r')
        plt.savefig(item)
    plt.show()


def getParaDegeriVerileri(data, gelenDataAdi, tarihler):

    return '{}{} {} {} {} {} {} {} {}  {} {}  {} {} {} {}  {} {}  {} {}  {} {} {} {} '.format(
        "\n", tarihler, "tarihleri arasinda Euro'nun", gelenDataAdi, "karsiliginda degerine gore oranlar hesaplanmistir.",
        '\nOrtalama : ', aritmetikOrtalama(data),
        "\nOrtanca : ", ortanca(data),
        "\nTepe Degeri : ", tepeDeger(data),
        "\nDegisim Araligi : ", degisimAraligi(
            data),
        "\nOrtalama Mutlak Sapma : ",
        ortalamaMutlakSapma(data),
        "\nVaryans : ", varyans(
            data),
        "\nStandart sapma : ", standartSapma(
            data),
        "\nDegisim Kat sayisi : ", degisimKatSayisi(
            data),
        "\nCeyrekler Arasi acikligi : ", ceyreklerAcikligi(data))


def writeToTxt(f, data, gelenDataAdi, tarihler):

    f.write(getParaDegeriVerileri(data, gelenDataAdi, tarihler))
    f.write("\n")


def getIlkVeSonTarihler(dataPeriod):

    dataPeriod = dataPeriod.dt.strftime("%d/%m/%y")

    return " - ".join(str(item) for item in (dataPeriod.iloc[0], dataPeriod.iloc[-1]))


def main():
    data = readDataFromExcel()

    dataLira = convertToList(data["Turkish lira"])
    dataUSD = convertToList(data["US dollar"])
    dataRuble = convertToList(data["Russian Rouble"])

    f = open("Hesaplanan Veriler.txt", "w")

    tarihler = getIlkVeSonTarihler(data['Period - Unit'])

    writeToTxt(f, dataLira, "Turk Lirasi", tarihler)
    writeToTxt(f, dataUSD, "USD", tarihler)
    writeToTxt(f, dataRuble, "Rus Rublesi", tarihler)

    f.close()

    boxPlot(["Turkish lira", "US dollar", "Russian Rouble"])

    print("Hesaplamalar txt olarak scriptin calistirildigi yere kaydedilmistir.")


if __name__ == "__main__":
    main()
