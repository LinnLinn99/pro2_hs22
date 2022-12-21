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


def erfassen_speichern(name_neues_mitglied, geschlecht, alter, notgood, erstellt):
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
        finanzeintrag = []

    return finanzeintrag


# Daten welche vom Input kommen werden in der "datenbank_finanzeintragdaten.json" nach der unteren Dic-Vorlage gespeichert
def finanz_eintrag_speichern(nebenkosten, wocheneinkauf, kueche, bad, divers, bezeichnung, betrag, date_gekauft,
                             mitbewohner):
    finanzeintrag = datenbank_finanzeintragdaten_oeffnen()
    finanzeintrag_neu = {
        "nebenkosten": nebenkosten,
        "wocheneinkauf": wocheneinkauf,
        "kueche": kueche,
        "bad": bad,
        "divers": divers,
        "bezeichnung": bezeichnung,
        "betrag": betrag,
        "date_gekauft": date_gekauft,
        "mitbewohner": mitbewohner
    }
    finanzeintrag.append(finanzeintrag_neu)

    # erfassen_speichern wieder an datenbank_finanzeintragdaten_oeffnen zurückgeben
    with open("datenbank_finazeintragdaten.json", "w") as open_file:
        json.dump(finanzeintrag, open_file, indent=4)


# Um Finanzeinträge nach Kategorien zu Filtern braucht es eine neue Liste
def finanz_eintragege_sortieren(alle, nebenkosten, wocheneinkauf, kueche, bad, divers, mitbewohner,
                                inputarchiv_kategorie, inputarchiv_name):
    finanzeintraege = datenbank_finanzeintragdaten_oeffnen()
    finanzeintrag_gefiltert = []
    if nebenkosten:
        ausgabe_type = "nebenkosten"
    elif wocheneinkauf:
        ausgabe_type = "wocheneinkauf"
    elif kueche:
        ausgabe_type = "kueche"
    elif bad:
        ausgabe_type = "bad"
    elif divers:
        ausgabe_type = "divers"
    for finanzeintrag in finanzeintraege:
        if ausgabe_type in finanzeintrag:
            finanzeintrag[inputarchiv_kategorie] = {
                "nebenkosten": nebenkosten,
                "wocheneinkauf": wocheneinkauf,
                "kueche": kueche,
                "bad": bad,
                "divers": divers,
            }
    for finanzeintrag in finanzeintraege:
        if ausgabe_type in finanzeintrag:
            finanzeintrag[inputarchiv_name] = {
                "mitbewohner": mitbewohner
            }

    if all(datenbank_finanzeintragdaten_oeffnen()):
        finanzeintrag_gefiltert.append(finanzeintrag)
    return finanzeintrag_gefiltert


# eintraege_gefiltert, inputarchiv_kategorie = funktion()


# auslesen definiert für die Filterfunktion für die Einträge der Finanzen
def auslesen():
    file = open("datenbank_finazeintragdaten.json")
    eintraege = json.load(file)
    return eintraege

    # Filterfunktion für die Einträge der Finanzen


def finanzen_gespeichert(merkmale):
    eintraege_finanz = auslesen()
    eintraege_finanz_gefiltert = []
    for eintrag in eintraege_finanz:
        finanzcheck = (
            merkmale["nebenkosten"] == "" or eintrag["nebenkosten"] == merkmale["nebenkosten"],
            merkmale["wocheneinkauf"] == "" or eintrag["wocheneinkauf"] == merkmale["wocheneinkauf"],
            merkmale["kueche"] == "" or eintrag["kueche"] == merkmale["kueche"],
            merkmale["bad"] == "" or eintrag["bad"] == merkmale["bad"],
            merkmale["divers"] == "" or eintrag["divers"] == merkmale["divers"]
        )
        if all(finanzcheck):
            eintraege_finanz_gefiltert.append(eintrag)
        return eintraege_finanz_gefiltert
