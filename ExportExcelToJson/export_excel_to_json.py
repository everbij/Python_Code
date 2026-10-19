import pandas as pd
import json
import meetdata
import matplotlib.pyplot as plt
from collections import Counter

xValueList =[0]
yValueList =[0]

# Write excel file to Json
def excel_to_json(): 
    #    df = pd.read_excel("C:\\...directory path...\\SolarPanelDataPerDay.xlsx")
    #    df.to_json("C:\\...directory path...\\data_zonnepanelen.json", orient="records", indent=4)

    df = pd.read_excel("C:\\Python_Code\\Python_Code\\ExportExcelToJson\\SolarPanelDataPerDay.xlsx")
    df.to_json("C:\\Python_Code\\Python_Code\\ExportExcelToJson\\data_zonnepanelen.json", orient="records", indent=4)
 
# Import Json file, zet data in intern data-variabele;
def import_json():
    #    with open("C:\\...directory path...\\data_zonnepanelen.json", "r") as file:

    with open("C:\\Python_Code\\Python_Code\\ExportExcelToJson\\data_zonnepanelen.json", "r") as file:
        data = json.load(file)

    import_json_by_object(data) # Roept methode import_json_by_object aan.

# Import in Object, aangeroepen van import_json en leest het interne data-variabele in.
# Json bestand bevat de volgende elementen: Datum, ProductieCumm, ProductieDag en strDatum
# Hiervan zijn alleen de strDatum en ProductieCumm nodig voor het maken van een grafiek
# De waarden worden in een xValueList en yValueList geplaatst
def import_json_by_object(data):
    for meetdata in data:
        xValueList.append(meetdata["strDatum"])
        yValueList.append((meetdata["ProductieCumm"]))
    xValueList.remove(0)    # eerste waarde bevat getal 0 ipv reeele waarde vandaar verwijderd
    yValueList.remove(0)

    make_graph(xValueList,yValueList)   # Roept methode aan om grafiek te tonen

# Grafiek met resultaten tonen
def make_graph(xValueList,yValueList):
    # Aantal waarden in de list bepalen me behulp van Counter om de einddatum in het label te tonen
    # Counter maakt gebruik van de collections die geïmporteerd moet worden
    # from collections import Counter
    number_of_values = len(Counter(xValueList)) - 1 # hoogste index is 1 kleiner dan de lengte

    plt.plot(xValueList,yValueList)
    plt.xticks(xValueList[::365])   # door de grote hoeveelheid aan data wordt er slecht iedere 365 dagen een label
    
    plt.xlabel
    plt.xlabel("Datum")
    plt.ylabel("Produktie in KWh")
    plt.title("Cumulatieve produktie zonnepanelen")
    subtitle = "Periode van " + xValueList[0] + " tot en met " + xValueList[number_of_values]
    plt.suptitle(subtitle)
    plt.show()
	

if __name__ == "__main__":
    excel_to_json()
    import_json()