import json


# Funktion zum Öffnen der datenbank_mitbewohnerdaten
def mitbewohnerdaten_oeffnen():
    try:
        with open('datenbank_mitbewohnerdaten.json', 'r', encoding='utf-8') as datenbank_mitbewohnerdaten:
            # Inhalt der Datenbank wird als Dictionary mitbewohner gespeichert.
            mitbewohner = json.load(datenbank_mitbewohnerdaten)
    except:
        mitbewohner = {}

    return mitbewohner



def erfassen_speichern(name_neues_mitglied,geschlecht,alter,notgood,erstellt):
    mitbewohner = mitbewohnerdaten_oeffnen()
    mitbewohner[name_neues_mitglied] = {
        "geschlecht": geschlecht,
        "alter": alter,
        "notgood": notgood,
        "erstellt": erstellt
    }
    # erfassen_speichern wieder an mitbewohner_oeffnen zurückgeben
    with open("datenbank_mitbewohnerdaten.json", "w") as open_file:
        open_file.wirte(mitbewohner)




# Funktion zum Öffnen der datenbank_finanzeintragdaten
def datenbank_finanzeintragdaten_oeffnen():
    try:
        with open('datenbank_finazeintragdaten.json', 'r', encoding='utf-8') as datenbank_finanzeintragdaten:
            # Inhalt der Datenbank wird als Dictionary Finanzeintrag gespeichert.
            finanzeintrag = json.load(datenbank_finanzeintragdaten)
    except:
        finanzeintrag = {}

    return finanzeintrag


def finanzeintrag_daten_oeffnen():
    pass


def finanz_eintrag_speichern(person, nebenkosten,wocheneinkauf,kueche,bad,divers,bezeichnung,betrag,date_gekauft):
    finanzeintrag = finanzeintrag_daten_oeffnen()
    finanzeintrag[date_gekauft] = {
        "person": person,
        "nebenkosten": nebenkosten,
        "wocheneinkauf": wocheneinkauf,
        "kueche": kueche,
        "bad": bad,
        "divers": divers,
        "bezeichnung": bezeichnung,
        "betrag": betrag,
        "date_gekauft": date_gekauft
    }
    # erfassen_speichern wieder an datenbank_finanzeintragdaten_oeffnen zurückgeben
    with open("datenbank_finazeintragdaten.json", "w") as open_file:
        open_file.wirte(finanzeintrag)


# auslesen definiert für die Filterfunktion für die Einträge der Finanzen

def auslesen():
    file = open("datenbank_finazeintragdaten.json")
    eintraege = json.load(file)
    return eintraege
# Filterfunktion für die Einträge der Finanzen
def sortieren_eintrag_finanz(merkmale):
    eintraege_finanz = auslesen()
    eintraege_finanz_gefiltert = []
    for eintrag in eintraege_finanz:
        finanzcheck = (
            merkmale["nebenkosten"] == "" or eintrag["nebenkosten"] == merkmale["nebenkosten"]
        )
        if all (finanzcheck):
            eintraege_finanz_gefiltert.append(eintrag)
        return eintraege_finanz_gefiltert

