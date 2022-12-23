from flask import Flask
from flask import render_template, redirect
from flask import request
import plotly.express as px
from plotly import plot

from wg_spliter.funktionen import mitbewohnerdaten_oeffnen, finanz_eintrag_speichern, \
    finanz_eintragege_sortieren, auslesen_select, eintrag_changed, eintrag_delet
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
        for person in mitbewohner:
            finanz_eintrag_speichern(
                kategorien,
                bezeichnung,
                betrag_pro_person,
                date_gekauft,
                person
            )
        return render_template("finanz_eintrag.html",
                               finanzen_gespeichert=finanz_eintrag_speichern)  # was gebe ich hier weiter?


@app.route("/uebersicht", methods=["GET", "POST"])
def uebersicht():
    # uebersicht.html wird generiert und die Variable finanzen_gespeichert werden mitgegeben
    # finanzen_gespeichert = datenbank_finanzeintragdaten_oeffnen()
    if request.method == "GET":
        return render_template("uebersicht.html", seitentitel="uebersicht")
    if request.method == "POST":
        # die daten aus dem form werden in das dic werte hinzugefügt
        werte = request.form.to_dict()
        ergebnis = finanz_eintragege_sortieren(werte)
        return render_template("uebersicht.html", ergebnis=ergebnis)


# Route um Einträge verändern - um dann löschen zu können
@app.route("/change/<eintrag_id>", methods=["GET", "POST"])
def eintragchange(eintrag_id):
    if request.method == "GET":
        eintrag = auslesen_select(int(eintrag_id))
        return render_template("bearbeiten.html", eintrag=eintrag)
    if request.method == "POST":
        eintrag_changed(int(eintrag_id), request.form.to_dict())
        return redirect("/archiv")


# Route Einträge löschen
@app.route("/delet/<eintrag_id>", methods=["GET", "POST"])
def eintragdelet(eintrag_id):
    eintrag_delet(int(eintrag_id))
    return redirect("/archiv")


def grafik():
    mitbewohner = mitbewohnerdaten_oeffnen()
    schulden = {}
    for person in mitbewohner:
        if person["betrag_pro_person"] not in schulden:
            schulden[person["betrag_pro_person"]] = 1
        else:
            schulden[person["betrag_pro_person"]] += 1

    x = schulden.keys()
    y = schulden.values()
    fig = px.bar(x=x, y=y)
    div = plot(fig, output_type="div")
    if request.method == "GET":
     return render_template("uebersicht.html", barchart=div, seitentitel="Piechart")


@app.route("/archiv")
def archiv():
    return render_template("archiv.html")


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
