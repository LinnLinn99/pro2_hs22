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



def erfassen_speichern(name_neues_mitglied,geschlecht,notgood,erstellt):
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

def finanz_eintrag_speichern(nebenkosten,wocheneinkauf,kueche,bad,divers,bezeichnung,betrag,date_gekauft):
    finanzeintrag = finanzeintrag_daten_oeffnen()
    finanzeintrag[date_gekauft] = {
        "kategorie": nebenkosten, #wocheneinkauf, kueche, bad, divers,
         # ich habe die Kategorie niergends definiert aber eigentlich sind die obrigen die unterschiedlichen Kategorien
        "bezeichnung": bezeichnung,
        "betrag": betrag
    }
    # erfassen_speichern wieder an datenbank_finanzeintragdaten_oeffnen zurückgeben
    with open("datenbank_finazeintragdaten.json", "w") as open_file:
        open_file.wirte(finanzeintrag)

