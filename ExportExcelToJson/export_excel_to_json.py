import pandas as pd
import json
import meetdata
import matplotlib.pyplot as plt

xValueList =[0]
yValueList =[0]

# Write excel file to Json
def excel_to_json(): 
    df = pd.read_excel("C:\\Python_Code\\Python_Code\\ExportExcelToJson\\SolarPanelDataPerDay_2023.xlsx")
    df.to_json("C:\\Python_Code\\Python_Code\\ExportExcelToJson\\data_zonnepanelen.json", orient="records", indent=4)
    print(df)

# Import Json file, zet data in Excel bestand in intern data-variabele;
def import_json():
    with open("C:\\Python_Code\\Python_Code\\ExportExcelToJson\\data_zonnepanelen.json", "r") as file:
        data = json.load(file)

# Test of de attributen van de CLASS meetdata gelezen kunnen worden
#     for meetdata in data:
#         print(meetdata["strDatum"], '->', meetdata["ProductieCumm"])

    import_json_by_object(data) # Roept methode import_json_by_object aan.
#    print(dataImported)

# Import in Object, aangeroepen van import_json en leest het interne data-variabele in.
def import_json_by_object(data):
    for meetdata in data:
        xValueList.append(meetdata["strDatum"])
        yValueList.append((meetdata["ProductieCumm"]))
    xValueList.remove(0)    # eerste waarde bevat getal 0 ipv reeele waarde vandaar verwijderd
    yValueList.remove(0)
    make_graph(xValueList,yValueList)   # Roept methode aan om grafiek te tonen

# Grafiek met resultaten tonen
# De opbouw van de grafiek neemt enige tijd in beslag door de grote hoeveelheod aan data
def make_graph(xValueList,yValueList):
    plt.plot(xValueList,yValueList)
    plt.xticks(xValueList[::365])   # door de grote hoeveelheid aan data wordt er slecht iedere 365 dagen een label

    plt.xlabel
    plt.xlabel("Datum")
    plt.ylabel("Produktie in KWh")
    plt.title("Cumulatieve produktie zonnepanelen")
    subtitle = "Periode van " + xValueList[0] + " tot en met " + xValueList[4754]
    plt.suptitle(subtitle)
    plt.show()
	

if __name__ == "__main__":
#    excel_to_json()
    import_json()