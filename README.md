# Satiscalculator

Satiscalculator ist ein Hilfsprogramm um Produktionslinien für das Spiel [Satisfactory](https://www.satisfactorygame.com) zu planen.

## Ausführung

python3 main.py \<Pfad der Rezeptdatei> \<Endprodukt> [-f=\<Produktionsrate>]

Beispiel: python3 main.py recipe/update4.recipes Computer -f=0.1

## Rezeptdateien

* Jede Zeile repräsentiert ein Rezept:
  * \<Liste von Eingabeprodukten> - \<Produktionszeit> \<Maschine> \> \<Anzahl> \<Produkt>
  * Liste von Eingabeprodukten:
    * Durch Komma separierte Einträge
    * Eintrag: \<Anzahl> \<Produkt>

Beispiel für ein Rezept:
10 Platine, 9 Kabel, 18 Kunststoff, 52 Schraube - 24 Manufaktor > 1 Computer

## Ausgabe

* Auflistung aller benötigten Rezepte mit zusätzlicher Information wie viele Maschinen für die gegebene Produktionsrate benötigt werden
* Auflistung aller benötigten Rohstoffe, welche pro Sekunde benötigt werden
* Kompletter Produktionsbaum, welcher visualisiert wie die Maschinen mit Förderbändern verbunden werden müssen, wie viele Maschinen jeweils benötigt werden und mit welcher Effizienz die Maschinen arbeiten werden
