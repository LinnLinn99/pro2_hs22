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
def finanz_eintrag_speichern(kategorien, bezeichnung, betrag, date_gekauft,
                             mitbewohner):
    finanzeintrag = datenbank_finanzeintragdaten_oeffnen()
    finanzeintrag_neu = {
        "kategorien": kategorien,
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
# in der liste_final werden die gewünschten Ausgaben ausgegeben
def finanz_eintragege_sortieren(werte):
    liste_namen = []
    liste_final = []
    for eintrag in datenbank_finanzeintragdaten_oeffnen():
        if werte["inputarchiv_name"] != "alle_mitbewohner":
            if werte["inputarchiv_name"] == eintrag["mitbewohner"]:
                liste_namen.append(eintrag)
        else:
            liste_namen == datenbank_finanzeintragdaten_oeffnen()
    for eintrag in liste_namen:
        if werte["inputarchiv_kategorie"] != 'alle_einkaeufe':
            if werte["inputarchiv_kategorie"] in eintrag['kategorien']:
                liste_final.append(eintrag)
        else:
            liste_final = liste_namen
    return liste_final


# auswahl von den selektierten von der Übersicht auslesen und zusammenfassen in neue liste
def auslesen_select(eintrag_id):
    for eintrag in auslesen():
        if eintrag["id"] == eintrag_id:
            return eintrag
        return


# einträge die verändert werden
def eintrag_changed(eintrag_id, daten):
    platz = 0
    eintraege = auslesen()
    eintrag_changed = {
        "id": eintrag_id,
        "kategorien": daten["kategorien"],
        "bezeichnung": daten["bezeichnung"],
        "betrag": daten["betrag"],
        "date_gekauft": daten["date_gekauft"],
        "mitbewohner": daten["mitbewohner"]
    }


# id's für Einträge erstellen
    for eintrag in eintraege:
        if eintrag["id"] == eintrag_id:
            print(eintrag["id"])
            print(platz)
            eintraege[platz] = eintrag_changed
        else:
            platz = platz + 1

# Aud Daten in json zugreifen // dumps heisst stores
    eintraege_json = json.dumps(eintraege, indent=4)
    file = open("datenbank_finazeintragdaten.json", "w")
    file.write(eintraege_json)
    file.close()
    return auslesen_select()

# Auf Daten in json zugreifen um zu löschen
def eintrag_delet(eintrag_id):
    eintraege = auslesen()
    eintraege_neu = []
    for eintrag in eintraege:
        if eintrag["id"] != eintrag_id:
            eintraege_neu.append(eintrag)
    eintraege_json = json.dumps(eintraege_neu, indent=4)
    file = open("datenbank_finazeintragdaten.json", "w")
    file.write(eintraege_json)
    file.close()
    return






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
