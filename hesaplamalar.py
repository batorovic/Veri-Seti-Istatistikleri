import pandas as pd


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
    if listeBoyutu % 2 == 0:
        medyan = (int)(listeBoyutu/2) - 1
        print("2 ye bolunuyor")
        return (data[medyan] + data[medyan+1]) / 2

    else:
        print("2 ye bolunmez")
        medyan = (int)(listeBoyutu/2)
        return data[medyan]


def getTurkishLiraVerileri(turkishLiraData):
    # print(aritmetikOrtalama(turkishLiraData))
    # print(ortanca(turkishLiraData))
    print(tepeDeger(turkishLiraData))


def tepeDeger(testList):
    dataSozluk = {}
    durum = True
    # sozluk olarak sekil verme.
    for item in testList:
        try:
            dataSozluk[item] += 1
        except:
            dataSozluk[item] = 1

    sortedDataSozluk = dict(sorted(dataSozluk.items(),
                                   key=lambda item: item[1], reverse=True))

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


def main():
    data = readDataFromExcel()

    dataLira = convertToList(data["Turkish lira"])
    dataUSD = convertToList(data["US dollar"])
    dataRuble = convertToList(data["Russian Rouble"])

    deneme = convertToList(data["ornek3"])

    # getTurkishLiraVerileri(dataLira)


if __name__ == "__main__":
    main()
