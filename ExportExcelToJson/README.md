# Opdracht om Excel bestand met waarden van zonnepanelen te verwerken

Bij deze opdracht worden de Excel gegevens omgezet naar een Json bestand.  
Vervolgens wordt het Json bestand in een loop omgezet tot instanties van de klasse meetdata.  
Daarna worden de attributen strDatum en productieCumm van de meetdata overgezet naar x- en y waarden om een grafiek te maken.  
Als laatste moet de grafiek nog vorm gegeven worden.

**Stap 1**
- Importeer pandas en json
- Lees het meegeleverde Excel bestand (`SolarPanelDataPerDay.xlsx`) in en zet dit om in een Json-bestand met de naam `data_zonnepanelen.json`

**Stap 2**
- Maak een CLASS aan met de naam meetdata welke bestaat uit de volgende attributen:
    -   datum
    -   productiecumm
    -   productieDag
    -   strDatum

**Stap 3**
- Importeer het zojuist gemaakte Json-bestand in een interne `data` variabele

**Stap 4**
- Verwerk de interne data variabele door de waarden om te zetten naar de meetdata class.
- Voeg het attribuut strDatum toe aan een `xValueList`
- Voeg het attribuur ProductieCumm toe aan een `yValueList`

**Stap 5**
- Importeer matplotlib
- Maak een grafiek van de zojuist aangemaakte xValueList en yValueList
- Maak een label voor de x- en y-as (`Datum`, `Produktie in KWh`)
- Door de grote aantal waarden in de xValueList worden de x-labels niet goed getoond.
- Zorg ervoor dat er om de 365 dagen een x-label getoond wordt.
- Geef de grafiek de titel `Cumulatieve produktie zonnepanelen`
- Geef in de sub-titel aan over welke periode de gegevens getoond worden:
  -  `Periode van ` + xValueList[0] + ` tot en met ` + xValueList[xxx]
