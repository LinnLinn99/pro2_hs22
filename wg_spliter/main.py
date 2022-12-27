from flask import Flask
from flask import render_template, redirect
from flask import request
import uuid

from wg_spliter.funktionen import mitbewohnerdaten_oeffnen, finanz_eintrag_speichern, \
    finanz_eintragege_sortieren, auslesen_select, eintrag_delet, grafik
from wg_spliter.funktionen import erfassen_speichern

app = Flask("wg_spliter")


@app.route("/")
def startseite():
    return render_template("index.html")


@app.route("/eintrag", methods=["GET", "POST"])
def finanz_eintrag():
    if request.method == "GET":
        mitbewohner = mitbewohnerdaten_oeffnen()
        mitbewohner = mitbewohner.keys()
        return render_template("finanz_eintrag.html", mitbewohner_gespeichert=mitbewohner)  # Verknüpfung zum html

    if request.method == "POST":
        daten = request.form.to_dict()
        kategorien = []
        if 'Nebenkosten' in daten:
            kategorien.append('Nebenkosten')
        if 'Wocheneinkauf' in daten:
            kategorien.append('Wocheneinkauf')
        if 'Kueche' in daten:
            kategorien.append('Kueche')
        if 'Bad' in daten:
            kategorien.append('Bad')
        if 'Divers' in daten:
            kategorien.append('Divers')

        betrag = float(
            request.form.get('betrag'))
        bezeichnung = request.form.get('bezeichnung')
        date_gekauft = request.form.get('date_gekauft')
        mitbewohner = request.form.getlist("mitbewohner")
        betrag_pro_person = betrag / len(mitbewohner)  # Betrag / anzahl Mitbewohner
        id = str(uuid.uuid4())
        for person in mitbewohner:
            finanz_eintrag_speichern(
                kategorien,
                bezeichnung,
                betrag_pro_person,
                date_gekauft,
                person,
                id
            )
        return render_template('erfassen_bestaetigen.html', finanzen_gespeichert=finanz_eintrag_speichern)

@app.route("/uebersicht", methods=["GET", "POST"])
def uebersicht():
    div = grafik()
    # uebersicht.html wird generiert und die Variable finanzen_gespeichert werden mitgegeben
    # finanzen_gespeichert = datenbank_finanzeintragdaten_oeffnen()
    if request.method == "GET":
        return render_template("uebersicht.html", seitentitel="uebersicht", barchart=div)
    if request.method == "POST":
        # die daten aus dem form werden in das dic werte hinzugefügt
        werte = request.form.to_dict()
        ergebnis = finanz_eintragege_sortieren(werte)
        return render_template("uebersicht.html", ergebnis=ergebnis, barchart=div)


# Route Einträge löschen
@app.route("/delet/<eintrag_id>", methods=["GET", "POST"])
def eintragdelet(eintrag_id):
    eintrag_delet(str(eintrag_id))
    return render_template('delet_bestaetigen.html')


@app.route("/mitglied", methods=["GET", "POST"])
def neuer_eintrag_mitglied():
    if request.method == "GET":
        return render_template("neuer_eintrag_mitglied.html")
    # Die Verknüpfung zum html

    if request.method == "POST":
        notgood = request.form['notgood']
        geschlecht = request.form['gender']
        erstellt = request.form['erstellt']
        alter = request.form['alter']
        erfassen_speichern(notgood, geschlecht, erstellt, alter)
        return "yes es funktioniert dein Eintrag wurde hinzugefügt"


if __name__ == "__main__":
    app.run(debug=True, port=5001)
