import pandas as pd
import math
import matplotlib.pyplot as plt


def readDataFromExcel():
    df = pd.read_excel(
        r'C:\Users\BATUHAN\Desktop\İstatistikOdevi\veriSeti.xlsx', keep_default_na=False)
    return df


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
    return float("{:.2f}".format(toplam / len(data)))


def ortanca(data):
    listeBoyutu = len(data)
    # ???? sorted olcak mı bilmiyorum
    data = sorted(data)
    if listeBoyutu % 2 == 0:
        medyan = (int)(listeBoyutu / 2) - 1
        print("2 ye bolunuyor")
        print((data[medyan], data[medyan + 1]))
        return (data[medyan] + data[medyan + 1]) / 2

    else:
        print("2 ye bolunmez")
        medyan = (int)(listeBoyutu/2)
        return data[medyan]


def tepeDeger(testList):
    dataSozluk = {}
    durum = True
    # sozluk olarak sekil verme.
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
        return "Tepe deger yok"
    else:
        for item in sortedDataSozluk:
            if(sortedDataSozluk[item] >= onceki):
                onceki = sortedDataSozluk[item]
                tekrarEdenler.append(item)
    return tekrarEdenler


def degisimAraligi(data):
    maximum = 0
    minimum = data[0]

    for item in data:
        if maximum < item:
            maximum = item
        elif minimum > item:
            minimum = item

    print(maximum, minimum, ' max ve min', max(data), min(data))
    # return max(data) - min(data)
    return maximum - minimum


def ortalamaMutlakSapma(data):

    dataAritmetikOrtalama = aritmetikOrtalama(data)
    toplam = 0

    for item in data:
        if item > dataAritmetikOrtalama:
            toplam += (item - dataAritmetikOrtalama)
        else:
            toplam += (dataAritmetikOrtalama - item)

    return float("{:.3f}".format(toplam / len(data)))


def varyans(data):
    dataAritmetikOrtalama = aritmetikOrtalama(data)
    toplam = 0
    for item in data:
        toplam = toplam + (item - dataAritmetikOrtalama) ** 2

    return float("{:.4f}".format((toplam) / (len(data) - 1)))


def standartSapma(data):
    # sqrt kullanilamayabilir !
    return float("{:.2f}".format(math.sqrt(varyans(data))))


def degisimKatSayisi(data):
    return float('{:.4f}'.format(standartSapma(data) / aritmetikOrtalama(data)))


def ceyreklerAcikligi(data):
    data = sorted(data)
    elemanSayisi = len(data)

    q1Terim = (elemanSayisi + 1) / 4
    q3Terim = 3 * (elemanSayisi + 1) / 4
    q1 = 0
    q3 = 0

    if q1Terim.is_integer() == False:
        n = int(q1Terim)
        q1 = (data[n] + data[n - 1]) / 2
    else:
        q1 = data[int(q1Terim) - 1]

    if q3Terim.is_integer() == False:
        n = int(q3Terim)
        q3 = (data[n] + data[n - 1]) / 2
    else:
        q3 = data[int(q3Terim) - 1]

    return q3 - q1


def boxPlot():
    df = readDataFromExcel()
    df.boxplot(column=["Turkish lira", "US dollar", "Russian Rouble"])

    plt.show()


def getTurkishLiraVerileri(turkishLiraData):
    # print(aritmetikOrtalama(turkishLiraData))
    # print(ortanca(turkishLiraData))
    # print(tepeDeger(turkishLiraData))
    pass


def main():
    data = readDataFromExcel()

    dataLira = convertToList(data["Turkish lira"])
    dataUSD = convertToList(data["US dollar"])
    dataRuble = convertToList(data["Russian Rouble"])

    deneme = convertToList(data["ornek3"])

    boxPlot()

    # getTurkishLiraVerileri(dataLira)


if __name__ == "__main__":
    main()
