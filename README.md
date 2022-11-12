# Semesterarbeit - Abrechnen in der WG

## 1. Ausgangslage
Aktuell werden die Einkäufe in der Wohngemeinschaft (nachfolgend mit WG abgekürzt) manuel und sporadisch untereinander verrechnet.

## 2. Projektidee
Mit der Webapplikation soll es für die Mitglieder aus der WG die Fananzübersicht erleichtern, indem getätigte Einkäufe direkt auf die Mitbewohner/ beteiligten verteilt.
## 3. Ablauf Diagramm
![img_1.png](img_1.png)
    
### 3.1 Installation / Benutzung
Damit die Applikation funktioniern kann, müssen folgende Einbindungen gemacht werden:
- Flask (Flask, render_template, request, redirect, url_for)

#### Startseite
- Der User kann direkt über die Startseite einen Finanzeintrag tätigen. Folgende Daten müssen dafür eingegeben werden:
  - Beschreibung
  - Preis von dem Einkauf
  - Mitglieder, die zu schuldner werden anwählen
  - Falls Besuch involviert ist, diesen anwählen
  - Falls Notwendig, Foto vom Beleg hochladen
  - Datum des Einkaufs anwählen
#### Einkaufsliste
- Unter Einkaufliste, kann eine Einkaufliste erstellt oder bearbeitet werden.
  - Artikel mittels Tags neu erfassen
  - Tags die angewählt werden, kommen in die Einkaufsliste
  - Tags die entfernt werden, gehen aus der Einkaufsliste raus
#### Statistik
- Unter Statistik wird aufgezeigt, welches Mitglied wie viel Geld an einem Schuldet. 
- Der Rechner im Hintergrund rechnet die Einkäufe mit den angewählten Mitgliedern aus.
- Zudem kann ein neues Mitglied erfasst werden, indem es ganz unten über die Eingabe eingegeben wird. 

#### Navigation 
Der User gelangt über den Header auf die Seiten "Eintrag erfassen", "Statistik" und "Einkaufsliste" 
### 3.2 Vorhandene Funktionen
- Dateneingabe: Neue Mitglieder, Einkaufliste, Einkaufsschulden der Einkäufe
- Datensicherung: Mitglieder werden in einem JSON-Datei gespeichert
- Datenverarbeitung: Mittels For-Schleife wird eine Datenbank Abfrage gemacht, wie viel die einzelnen Mitglieder schulden
- Datenausgabe: Ausgabe der Schulden von den Mitgliedern.
### 3.3 Zutaten

## FAQ`s (Fazit)
###### Was funktioniert noch nicht - und warum nicht
###### wie ist es mir dabei gelaufen

